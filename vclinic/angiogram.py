"""Synthetic coronary angiograms of the virtual clinic.

Every patient with an angiography (vclinic.coronary) gets two X-ray frames of
512 x 512 pixels: a view of the left coronary artery, with the left main, the
LAD, the circumflex and their branches, and a view of the right coronary
artery with its posterior descending branch. The lesions drawn are the
lesions of the registry, the same that the angiography reports of Week 6
describe. A stenosis narrows the diameter of the vessel by its percentage
over a few millimetres; an occlusion stops the contrast, and the distal
vessel fills only faintly through collaterals. The image is a model, not a
simulation of an X-ray system: vessels are tubes whose attenuation follows
the length of the chord through them, on a background of soft structures,
with noise and blur.

Each frame comes with its truth: the centre, the box, the vessel, the
segment and the percentage of every stenosis, and the mask of the vessels.
"""
import hashlib

import numpy as np

from . import coronary

SIZE = 512
MM_PER_PIXEL = 0.3
SEGMENT_RANGE = {"ostial": (0.0, 0.08), "proximal": (0.05, 0.33), "body": (0.25, 0.6), "mid": (0.33, 0.66), "distal": (0.66, 0.95)}
# control points of the centrelines in a reference frame of 512 x 512 pixels
LEFT = {"LM": [(236, 96), (252, 122), (270, 146)],
        "LAD": [(270, 146), (262, 210), (236, 290), (200, 370), (160, 440), (126, 488)],
        "LCX": [(270, 146), (330, 172), (388, 220), (424, 290), (432, 360)],
        "D1": [(250, 232), (196, 262), (150, 300)],
        "D2": [(212, 342), (166, 372), (128, 406)],
        "OM1": [(372, 206), (360, 270), (350, 330)],
        "OM2": [(414, 266), (402, 330), (392, 392)]}
RIGHT = {"RCA": [(210, 104), (176, 150), (152, 220), (156, 300), (196, 368), (262, 410), (318, 420)],
         "PDA": [(318, 420), (300, 456), (272, 492)]}
RADIUS_MM = {"LM": 2.2, "LAD": 1.75, "LCX": 1.6, "RCA": 1.8, "D1": 1.1, "D2": 1.0, "OM1": 1.1, "OM2": 1.0, "PDA": 1.0}
PARENT = {"D1": "LAD", "D2": "LAD", "OM1": "LCX", "OM2": "LCX", "PDA": "RCA"}
VIEW_OF = {v: ("left" if v in LEFT else "right") for v in list(LEFT) + list(RIGHT)}


class _Rand:
    def __init__(self, seed, pid):
        self.seed, self.pid = seed, pid

    def rng(self, key):
        h = int(hashlib.md5(f"angiogram:{self.seed}:{self.pid}:{key}".encode()).hexdigest()[:12], 16)
        return np.random.default_rng(h)


def _curve(points, step=1.0):
    """A smooth curve through the control points (Catmull-Rom), sampled every step pixels of arc length."""
    p = np.asarray(points, dtype=float)
    p = np.vstack([2 * p[0] - p[1], p, 2 * p[-1] - p[-2]])
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        for t in np.linspace(0, 1, 40, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2 + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(p[-2])
    c = np.array(out)
    seg = np.hypot(*np.diff(c, axis=0).T)
    s = np.concatenate([[0], np.cumsum(seg)])
    n = max(2, int(s[-1] / step) + 1)
    u = np.linspace(0, s[-1], n)
    return np.column_stack([np.interp(u, s, c[:, 0]), np.interp(u, s, c[:, 1])])


def _geometry(pid, view, dominance, seed):
    """Centrelines of one view, deformed for the patient: a rotation, a scale, a shift and a smooth jitter of the points."""
    r = _Rand(seed, pid)
    ref = LEFT if view == "left" else RIGHT
    g = r.rng(view + ":affine")
    ang, sc = np.deg2rad(g.uniform(-9, 9)), g.uniform(0.9, 1.08)
    shift = g.uniform(-18, 18, size=2)
    rot = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
    centre = np.array([SIZE / 2, SIZE / 2])
    lines = {}
    for v, pts in ref.items():
        if view == "right" and v == "PDA" and dominance == "left":
            continue
        j = r.rng(view + ":jitter:" + v).normal(0, 9, size=(len(pts), 2))
        j[0] = 0
        p = (np.asarray(pts, float) + j - centre) @ rot.T * sc + centre + shift
        lines[v] = p
    # branches start on their parent: move the first point of a branch onto the nearest point of the parent curve
    curves = {}
    for v in lines:
        if v in PARENT and PARENT[v] in lines:
            parent = _curve(lines[PARENT[v]])
            k = int(np.argmin(np.hypot(*(parent - lines[v][0]).T)))
            lines[v][0] = parent[k]
    from scipy.ndimage import gaussian_filter1d
    for v, p in lines.items():
        c = _curve(p)
        if len(c) > 20:
            d = np.gradient(c, axis=0)
            nrm = np.column_stack([-d[:, 1], d[:, 0]]) / (np.hypot(d[:, 0], d[:, 1])[:, None] + 1e-9)
            wander = gaussian_filter1d(r.rng(view + ":wander:" + v).normal(0, 1, len(c)), 9) * 9
            wander[:5] = 0
            c = c + nrm * wander[:, None]
        curves[v] = c
    if view == "left" and dominance == "left":     # a left-dominant circumflex runs further
        c = curves["LCX"]
        ext = c[-1] + (c[-1] - c[-12]) / 11 * np.arange(1, 60)[:, None]
        curves["LCX"] = np.vstack([c, ext])
    if view == "right" and dominance == "left":    # a small right coronary artery
        curves["RCA"] = curves["RCA"][: int(len(curves["RCA"]) * 0.6)]
    return curves


def _lesion_place(pid, vessel, segment, n, seed, k):
    """The position of a lesion along its vessel, as a fraction of the length, and its length in pixels."""
    a, b = SEGMENT_RANGE.get(segment, (0.2, 0.8))
    g = _Rand(seed, pid).rng(f"lesion:{vessel}:{segment}:{k}")
    return g.uniform(a, b), g.uniform(3.0, 8.0) / MM_PER_PIXEL / 2


def _background(pid, view, seed):
    g = _Rand(seed, pid).rng(view + ":background")
    y, x = np.mgrid[0:SIZE, 0:SIZE] / SIZE
    base = 0.78 + 0.06 * (x - 0.5) * g.uniform(-1, 1) - 0.10 * ((x - 0.5) ** 2 + (y - 0.5) ** 2)
    # spine and ribs: soft bands; diaphragm: a darker dome at the bottom
    sx = g.uniform(0.38, 0.62)
    base -= 0.08 * np.exp(-((x - sx) / 0.07) ** 2)
    phase, slope, bend = g.uniform(0, 2 * np.pi), g.uniform(0.15, 0.45), g.uniform(0.3, 0.9)
    ribs = np.sin(2 * np.pi * (y + slope * x + bend * (x - 0.5) ** 2) * 4.2 + phase)
    base -= 0.022 * np.clip(ribs, 0, None) ** 3
    dome = g.uniform(0.78, 0.92) + 0.18 * (x - g.uniform(0.3, 0.7)) ** 2
    base -= 0.12 / (1 + np.exp(-(y - dome) * 60))
    low = g.normal(0, 1, size=(16, 16))
    up = np.kron(low, np.ones((SIZE // 16, SIZE // 16)))
    from scipy.ndimage import gaussian_filter
    base += 0.025 * gaussian_filter(up, 20)
    return base


def _tube(thick, curve, radius, value=1.0):
    """Add the chord length of a tube with a radius at every point of its centreline (maximum along the tube)."""
    t = np.zeros_like(thick)
    for (cx, cy), r in zip(curve, radius):
        if r <= 0.15:
            continue
        x0, x1 = int(max(0, cx - r - 2)), int(min(SIZE, cx + r + 3))
        y0, x_ = int(max(0, cy - r - 2)), None
        y1 = int(min(SIZE, cy + r + 3))
        if x0 >= x1 or y0 >= y1:
            continue
        yy, xx = np.mgrid[y0:y1, x0:x1]
        d2 = (xx - cx) ** 2 + (yy - cy) ** 2
        chord = 2 * np.sqrt(np.clip(r * r - d2, 0, None)) * value
        t[y0:y1, x0:x1] = np.maximum(t[y0:y1, x0:x1], chord)
    return thick + t


def frame(patient, lesions, view, seed=2026):
    """One synthetic angiogram of a patient.

    patient: a row of the patient table of vclinic.coronary.angiography; lesions: its lesions.
    Returns (image as uint8 of 512 x 512, truth) where truth holds the stenoses drawn in this view
    and the mask of the vessels.
    """
    pid, dom = patient["patient_id"], patient["dominance"]
    curves = _geometry(pid, view, dom, seed)
    thick = np.zeros((SIZE, SIZE))
    faint = np.zeros((SIZE, SIZE))
    stenoses = []
    for v, c in curves.items():
        n = len(c)
        s = np.linspace(0, 1, n)
        r = RADIUS_MM[v] / MM_PER_PIXEL * (1 - 0.45 * s)
        stop = n
        mine = lesions[lesions["vessel"] == v] if len(lesions) else lesions
        for k, (_, le) in enumerate(mine.iterrows()):
            frac, half = _lesion_place(pid, v, le["segment"], n, seed, k)
            i0 = int(frac * (n - 1))
            idx = np.arange(n)
            w = np.where(np.abs(idx - i0) < half, 0.5 * (1 + np.cos(np.pi * (idx - i0) / half)), 0.0)
            p = float(le["stenosis"]) / 100
            if p >= 1.0:
                stop = min(stop, i0)
            else:
                r = r * (1 - p * w)
            cx, cy = c[i0]
            ext = half + RADIUS_MM[v] / MM_PER_PIXEL + 4
            stenoses.append(dict(vessel=v, territory=coronary.TERRITORY[v], segment=le["segment"], stenosis=int(le["stenosis"]),
                                 kind=le["kind"], x=float(cx), y=float(cy),
                                 box=[float(cx - ext), float(cy - ext), float(2 * ext), float(2 * ext)],
                                 significant=int(coronary.significant(coronary.TERRITORY[v], le["stenosis"]))))
        if stop < n:
            thick = _tube(thick, c[:stop], r[:stop])
            faint = _tube(faint, c[stop + 3:], r[stop + 3:] * 0.8)    # the distal vessel through collaterals
        else:
            thick = _tube(thick, c, r)
    # small side branches without lesions: septal and marginal branches
    g = _Rand(seed, pid).rng(view + ":side")
    for v in [x for x in curves if x in ("LAD", "LCX", "RCA")]:
        c = curves[v]
        for _ in range(int(g.integers(2, 5))):
            i0 = int(g.uniform(0.15, 0.8) * (len(c) - 1))
            d = c[min(i0 + 3, len(c) - 1)] - c[max(i0 - 3, 0)]
            d = d / (np.hypot(*d) + 1e-9)
            side = np.array([-d[1], d[0]]) * g.choice([-1, 1])
            length = g.uniform(20, 55)
            bend = g.uniform(-0.4, 0.4)
            pts = [c[i0], c[i0] + side * length * 0.5 + d * length * (0.3 + bend), c[i0] + side * length + d * length * (0.5 + bend)]
            sc_ = _curve(pts)
            rr = np.linspace(g.uniform(0.5, 0.8), 0.25, len(sc_)) / MM_PER_PIXEL
            thick = _tube(thick, sc_, rr)
    # the catheter at the ostium
    first = curves["LM" if view == "left" else "RCA"][0]
    cat = np.column_stack([np.linspace(first[0] + 40, first[0], 80), np.linspace(-10, first[1], 80)])
    thick = _tube(thick, cat, np.full(len(cat), 2.0), value=0.8)
    bg = _background(pid, view, seed)
    look = _Rand(seed, pid).rng(view + ":look")
    mu = look.uniform(0.065, 0.1)
    img = bg * np.exp(-mu * thick - 0.3 * mu * faint)
    from scipy.ndimage import gaussian_filter
    img = gaussian_filter(img, look.uniform(0.9, 1.4))
    g = _Rand(seed, pid).rng(view + ":noise")
    img = img + g.normal(0, 0.018, size=img.shape) * np.sqrt(np.clip(img, 0.05, None))
    img = np.clip(img, 0, 1)
    mask = (thick > 0.5).astype(np.uint8)
    inside = [s for s in stenoses if 0 <= s["x"] < SIZE and 0 <= s["y"] < SIZE]
    return (img * 255).astype(np.uint8), dict(patient_id=pid, view=view, stenoses=inside, mask=mask)


def frames(patient, lesions, seed=2026):
    """Both views of a patient: {"left": (image, truth), "right": (image, truth)}."""
    out = {}
    for view in ("left", "right"):
        vs = [v for v, w in VIEW_OF.items() if w == view]
        out[view] = frame(patient, lesions[lesions["vessel"].isin(vs)], view, seed)
    return out


_CACHE = {}


def registry(seed=2026):
    """The patients with an angiography and their lesions, with the sets of Week 6:
    training (patients VC-0001 to VC-1800), validation (to VC-2400), test (to VC-3000) and external (VC-3001 to VC-3600)."""
    if seed not in _CACHE:
        from .cohort import make_cohort
        pats, les = coronary.angiography(make_cohort(3600), seed=seed)
        num = pats["patient_id"].str[3:].astype(int)
        pats = pats.assign(split=np.select([num <= 1800, num <= 2400, num <= 3000], ["training", "validation", "test"], "external"))
        _CACHE[seed] = (pats.reset_index(drop=True), les.reset_index(drop=True))
    return _CACHE[seed]


def patient_frames(pid, seed=2026):
    """Both views of one patient of the registry: {"left": (image, truth), "right": (image, truth)}."""
    pats, les = registry(seed)
    p = pats[pats["patient_id"] == pid].iloc[0]
    return frames(p, les[les["patient_id"] == pid], seed)


def patches(split, size=64, n_patients=None, per_stenosis=2, neg_per_pos=3, away=48, seed=2026):
    """Patches of the synthetic angiograms of one set: positives near every significant stenosis, negatives on the
    vessels at least `away` pixels from every stenosis, significant or not. Returns (X, y, patient ids)."""
    pats, _ = registry(seed)
    pids = pats.loc[pats["split"] == split, "patient_id"].tolist()[:n_patients]
    rng = np.random.default_rng(seed)
    h = size // 2
    X, y, ids = [], [], []
    for pid in pids:
        for view, (img, truth) in patient_frames(pid, seed).items():
            g = img.astype(np.float32) / 255
            pad = np.pad(g, size, mode="reflect")
            cut = lambda r, c: pad[r + size - h:r + size + h, c + size - h:c + size + h]
            sig = [s for s in truth["stenoses"] if s["significant"]]
            for s in sig:
                for _ in range(per_stenosis):
                    dx, dy = rng.integers(-6, 7, size=2)
                    X.append(cut(int(s["y"]) + dy, int(s["x"]) + dx)); y.append(1); ids.append(pid)
            cand = np.argwhere(truth["mask"] > 0)
            cand = cand[rng.permutation(len(cand))[:300]]
            far = [c for c in cand if all(np.hypot(c[1] - s["x"], c[0] - s["y"]) > away for s in truth["stenoses"])]
            for r, c in far[:neg_per_pos * per_stenosis * max(1, len(sig))]:
                X.append(cut(int(r), int(c))); y.append(0); ids.append(pid)
    return np.stack(X).astype(np.float32), np.array(y, dtype=np.int64), np.array(ids)
