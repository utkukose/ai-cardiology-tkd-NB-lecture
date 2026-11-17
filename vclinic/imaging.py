"""Images of the virtual clinic (from Week 3).

echo_images() draws one end-diastolic frame of the parasternal short-axis
view for every patient of a registry made by add_followup(). The size of the
left ventricle and the thickness of its walls come from the echocardiographic
columns of the patient, so the images agree with the table. The report of
the echo laboratory calls a frame abnormal when the left ventricle is
dilated (diameter above 58 mm) or its septum is thickened (13 mm or more).

make_cmr_set() draws short-axis slices of cine cardiac magnetic resonance
(CMR) for three groups of a cardiomyopathy clinic: normal hearts, dilated
cardiomyopathy (DCM) and hypertrophic cardiomyopathy (HCM).

Every image comes from its own stream of random numbers, indexed by the
number of the patient or of the study, so an image stays the same when the
set is filtered or made larger. The images are synthetic teaching material
and are not for clinical use.
"""

import zlib

import numpy as np
import pandas as pd

from .cohort import DEFAULT_SEED, _stream

ECHO_CLASSES = ("normal", "abnormal")
CMR_CLASSES = ("normal", "DCM", "HCM")
PIXEL_MM = 2.0          # size of one pixel in millimetres (images of 64 x 64 pixels)


def _rng(seed, name, number):
    return np.random.default_rng([seed, zlib.crc32(name.encode("utf-8")), int(number)])


def _smooth_step(x, width):
    """0 below -width, 1 above +width, smooth in between."""
    return np.clip(0.5 + x / (2 * width), 0.0, 1.0)


def _blur(img, sigma):
    """Gaussian blur with a separable kernel (NumPy only)."""
    r = max(1, int(3 * sigma))
    t = np.arange(-r, r + 1)
    k = np.exp(-t ** 2 / (2 * sigma ** 2))
    k /= k.sum()
    pad = np.pad(img, r, mode="edge")
    tmp = np.apply_along_axis(lambda v: np.convolve(v, k, mode="valid"), 0, pad)
    return np.apply_along_axis(lambda v: np.convolve(v, k, mode="valid"), 1, tmp)


def _ventricle(size, rng, lvedd_mm, septum_mm, posterior_mm, rv_scale=1.0):
    """Polar geometry of the heart: distances and masks of the walls and cavities."""
    c = (size - 1) / 2 + rng.uniform(-2.5, 2.5, 2)
    yy, xx = np.mgrid[0:size, 0:size].astype(float)
    dy, dx = yy - c[0], xx - c[1]
    rot = rng.uniform(-0.35, 0.35)
    ell = rng.uniform(0.92, 1.08)
    ang = np.arctan2(dy, dx) - rot
    xr, yr = np.cos(ang) * np.hypot(dx, dy), np.sin(ang) * np.hypot(dx, dy)
    r = np.hypot(xr * ell, yr / ell)
    th = np.arctan2(yr, xr)
    endo = lvedd_mm / 2 / PIXEL_MM
    # wall thickness depends on the angle: the septum lies toward the right ventricle (left side)
    w_sept = np.clip(np.cos(th - np.pi), 0, None) ** 2
    thick = (posterior_mm + (septum_mm - posterior_mm) * w_sept) / PIXEL_MM
    epi = endo + thick
    # right ventricle: a crescent that wraps the septum on the left side
    ep_mean = endo + (posterior_mm + septum_mm) / 2 / PIXEL_MM
    cx = -(ep_mean * 0.55) * rv_scale
    a, b = endo * 0.95 * rv_scale + 3.0, endo * 1.30 * rv_scale + 3.0
    rv_cav = (np.hypot((xr - cx) / a, yr / b) < 1.0) & (r > epi + 1.0) & (xr < endo * 0.2)
    rv_wall = (np.hypot((xr - cx) / (a + 1.3), yr / (b + 1.3)) < 1.0) & ~rv_cav & (r > epi + 0.3) & (xr < endo * 0.25)
    return dict(r=r, th=th, endo=endo, epi=epi, rv=rv_cav, rv_wall=rv_wall, xr=xr, yr=yr)


def echo_psax(lvedd_mm, septum_mm, posterior_mm, size=64, rng=None):
    """One end-diastolic parasternal short-axis frame, values from 0 to 1."""
    rng = rng or np.random.default_rng()
    g = _ventricle(size, rng, lvedd_mm, septum_mm, posterior_mm)
    r, th, endo, epi = g["r"], g["th"], g["endo"], g["epi"]
    myo = _smooth_step(r - endo, 0.6) * (1 - _smooth_step(r - epi, 0.6))
    img = 0.10 + 0.55 * myo
    # papillary muscles inside the cavity
    for a in (0.75, 2.35):
        a += rng.uniform(-0.2, 0.2)
        px, py = (endo - 2.2) * np.cos(a), (endo - 2.2) * np.sin(a)
        d = np.hypot(g["xr"] - px, g["yr"] - py)
        img += 0.35 * (1 - _smooth_step(d - rng.uniform(1.6, 2.4), 0.6)) * (r < endo)
    # right ventricle cavity (dark) and bright pericardium behind the posterior wall
    img = np.where(g["rv"], 0.06, img)
    img = np.where(g["rv_wall"], 0.45, img)
    peri = np.exp(-((r - epi - 1.6) ** 2) / 1.2) * np.clip(np.sin(th), 0, None)
    img += 0.45 * peri
    # speckle, depth gain and sector of the transducer
    yy, xx = np.mgrid[0:size, 0:size].astype(float)
    img *= rng.rayleigh(0.8, (size, size))
    img = _blur(img, rng.uniform(0.6, 0.9))
    depth = yy / size
    img *= rng.uniform(0.85, 1.15) * (1.15 - 0.45 * depth)
    apex = np.array([-size * 0.18, size / 2 + rng.uniform(-2, 2)])
    ang = np.arctan2(xx - apex[1], yy - apex[0])
    sector = (np.abs(ang) < 0.62) & (np.hypot(yy - apex[0], xx - apex[1]) < size * 1.25)
    img = np.where(sector, img, 0.0)
    img += rng.normal(0, 0.02, (size, size)) * sector
    return np.clip(img, 0, 1).astype(np.float32)


def cmr_sax(lvedd_mm, septum_mm, posterior_mm, size=64, rng=None):
    """One end-diastolic short-axis slice of cine CMR (bright blood), values from 0 to 1."""
    rng = rng or np.random.default_rng()
    g = _ventricle(size, rng, lvedd_mm, septum_mm, posterior_mm, rv_scale=rng.uniform(0.9, 1.2))
    r, th, endo, epi = g["r"], g["th"], g["endo"], g["epi"]
    blood = 1 - _smooth_step(r - endo, 0.5)
    myo = _smooth_step(r - endo, 0.5) * (1 - _smooth_step(r - epi, 0.5))
    yy, xx = np.mgrid[0:size, 0:size].astype(float)
    img = 0.36 + 0.10 * _blur(rng.normal(0, 1, (size, size)), 4.0) / 0.12      # surrounding tissue
    edge = size * rng.uniform(0.18, 0.26) + 5 * np.sin(yy / size * 3 + rng.uniform(0, 6))
    lung = _smooth_step(edge - xx, 1.5) * _smooth_step(size * 0.85 - yy, 3)
    img = img * (1 - lung) + 0.06 * lung
    img = img * (1 - blood - myo) + 0.92 * blood + 0.24 * myo
    img = np.where(g["rv"], 0.88, img)
    img = np.where(g["rv_wall"], 0.26, img)
    fat = np.exp(-((r - epi - 1.0) ** 2) / 0.8) * (np.cos(th - rng.uniform(0, 6.3)) > 0.2)
    img += 0.35 * fat
    for a in (0.8, 2.3):                                    # papillary muscles (dark in bright blood)
        a += rng.uniform(-0.25, 0.25)
        px, py = (endo - 2.0) * np.cos(a), (endo - 2.0) * np.sin(a)
        d = np.hypot(g["xr"] - px, g["yr"] - py)
        img -= 0.6 * (1 - _smooth_step(d - rng.uniform(1.3, 2.1), 0.5)) * (r < endo)
    img = _blur(np.clip(img, 0, 1), rng.uniform(0.5, 0.8))
    img *= rng.uniform(0.85, 1.15)
    noise = rng.uniform(0.02, 0.05)
    img = np.hypot(img + rng.normal(0, noise, img.shape), rng.normal(0, noise, img.shape))   # Rician noise
    return np.clip(img, 0, 1).astype(np.float32)


def echo_images(registry, size=64, seed=DEFAULT_SEED):
    """Parasternal short-axis frames of the patients of a registry made by add_followup().

    Returns (images, labels, table): images of shape (n, size, size), labels 0 for a
    normal and 1 for an abnormal report, and a table with the measurements of each frame.
    """
    num = registry["patient_id"].str.slice(3).astype(int).to_numpy()
    lvedd = registry["lvedd_mm"].to_numpy(float)
    ivs = registry["ivs_mm"].to_numpy(float)
    imgs, pws = [], []
    for k, n in enumerate(num):
        rng = _rng(seed, "echo-psax", n)
        pw = round(float(ivs[k] * rng.uniform(0.82, 1.0)), 1)
        pws.append(pw)
        imgs.append(echo_psax(lvedd[k], ivs[k], pw, size, rng))
    dilated, thick = lvedd > 58, ivs >= 13
    labels = (dilated | thick).astype(int)
    table = pd.DataFrame({"patient_id": registry["patient_id"].to_numpy(), "lvedd_mm": lvedd, "ivs_mm": ivs,
                          "pw_mm": pws, "dilated": dilated.astype(int), "thick_septum": thick.astype(int),
                          "label": labels, "report": np.array(ECHO_CLASSES)[labels]})
    return np.stack(imgs), labels, table


def make_cmr_set(n_per_class=300, size=64, seed=DEFAULT_SEED):
    """Short-axis CMR slices of a cardiomyopathy clinic: normal, DCM and HCM.

    Returns (images, labels, table): images of shape (3 * n_per_class, size, size),
    labels 0 normal, 1 DCM and 2 HCM, and a table with the study number and the
    measurements of each slice.
    """
    rows, imgs = [], []
    for k in range(3 * n_per_class):
        cls = k % 3
        rng = _rng(seed, "cmr-sax", k + 1)
        if cls == 0:
            lvedd, sept = rng.uniform(42, 57), rng.uniform(7, 11.5)
            post = sept * rng.uniform(0.85, 1.05)
        elif cls == 1:
            lvedd, sept = rng.uniform(56, 76), rng.uniform(5, 9)
            post = sept * rng.uniform(0.85, 1.05)
        else:
            lvedd, sept = rng.uniform(34, 50), rng.uniform(13, 26)
            post = rng.uniform(8, 14)
        imgs.append(cmr_sax(lvedd, sept, post, size, rng))
        rows.append(dict(study_id=f"CMR-{k + 1:04d}", lvedd_mm=round(lvedd, 1), septum_mm=round(sept, 1),
                         posterior_mm=round(post, 1), label=cls, diagnosis=CMR_CLASSES[cls]))
    table = pd.DataFrame(rows)
    return np.stack(imgs), table["label"].to_numpy(), table
