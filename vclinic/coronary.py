"""Coronary anatomy and coronary angiography of the virtual clinic.

Every patient with coronary artery disease in the registry, and a sample of
patients without it, has a coronary angiography. The lesions follow the
registry: patients with coronary artery disease have at least one
significant stenosis, patients with an acute coronary syndrome have a
culprit lesion in the territory of their ST elevation, and patients without
coronary artery disease have normal arteries or plaques below 50 percent.
The same lesions are described in the angiography reports of Week 6 and
drawn in the angiograms of Week 7.

A stenosis is significant from 50 percent in the left main coronary artery
and from 70 percent elsewhere. A territory counts as diseased when it holds
a significant stenosis; the number of diseased vessels counts the three
territories LAD, LCX and RCA. Branches belong to the territory of their
parent artery: D1 and D2 to the LAD, OM1 and OM2 to the LCX, and the PDA to
the RCA, since only right-dominant systems carry a lesion of the PDA here.
"""
import hashlib

import numpy as np
import pandas as pd

VESSELS = ("LM", "LAD", "D1", "D2", "LCX", "OM1", "OM2", "RCA", "PDA")
TERRITORY = {"LM": "LM", "LAD": "LAD", "D1": "LAD", "D2": "LAD", "LCX": "LCX", "OM1": "LCX", "OM2": "LCX",
             "RCA": "RCA", "PDA": "RCA"}
TERRITORIES = ("LM", "LAD", "LCX", "RCA")
SEGMENTS = {"LM": ("ostial", "body", "distal"), "LAD": ("proximal", "mid", "distal"), "LCX": ("proximal", "mid", "distal"),
            "RCA": ("proximal", "mid", "distal"), "D1": ("ostial", "proximal"), "D2": ("ostial", "proximal"),
            "OM1": ("ostial", "proximal"), "OM2": ("ostial", "proximal"), "PDA": ("ostial", "proximal")}
BRANCHES = {"LAD": ("D1", "D2"), "LCX": ("OM1", "OM2"), "RCA": ("PDA",)}
CATEGORIES = ("<50", "50-69", "70-89", "90-99", "100")


def category(stenosis):
    """Category of a stenosis in percent: 0 below 50, 1 for 50 to 69, 2 for 70 to 89, 3 for 90 to 99, 4 for an occlusion."""
    s = float(stenosis)
    return 0 if s < 50 else (1 if s < 70 else (2 if s < 90 else (3 if s < 100 else 4)))


def significant(territory, stenosis):
    """A stenosis is significant from 50 percent in the left main coronary artery and from 70 percent elsewhere."""
    return stenosis >= (50 if territory == "LM" else 70)


class _Draw:
    """Random draws of one patient, each from its own named stream."""

    def __init__(self, seed, pid):
        self.seed, self.pid = seed, pid

    def rng(self, key):
        h = int(hashlib.md5(f"coronary:{self.seed}:{self.pid}:{key}".encode()).hexdigest()[:12], 16)
        return np.random.default_rng(h)

    def u(self, key):
        return float(self.rng(key).random())

    def pick(self, key, items, p=None):
        r = self.rng(key)
        if p is None:
            return items[int(r.integers(len(items)))]
        p = np.asarray(p, dtype=float)
        return items[int(r.choice(len(items), p=p / p.sum()))]

    def integer(self, key, lo, hi):
        return int(self.rng(key).integers(lo, hi + 1))


def _severe(d, key, low=70):
    """A significant stenosis in percent, rounded as angiographers report it."""
    v = d.pick(key, [70, 75, 80, 85, 90, 95, 99, 100], [12, 10, 16, 8, 14, 10, 6, 8])
    return max(v, low)


def _mild(d, key):
    return d.pick(key, [20, 30, 40, 50, 60], [3, 4, 4, 2, 2])


def _place(d, key, territory):
    """Vessel and segment of a lesion in a territory: the main artery in 80 percent, a branch otherwise."""
    if territory == "LM":
        return "LM", d.pick(key + "seg", SEGMENTS["LM"], [3, 3, 4])
    vessel = territory if d.u(key + "branch") < 0.8 else d.pick(key + "which", BRANCHES[territory])
    segs = SEGMENTS[vessel]
    seg = d.pick(key + "seg", segs, [4, 4, 2][:len(segs)] if len(segs) == 3 else [1, 3])
    return vessel, seg


def angiography(cohort, seed=2026, share_without_cad=0.25):
    """Coronary angiographies of the registry.

    Returns two tables. The first has one row per patient with an
    angiography: patient_id, dominance (right, left or codominant), access
    (radial or femoral), treatment (PCI, CABG or medical), the treated
    vessel and segment, and for every territory the largest stenosis
    (max_LM, max_LAD, max_LCX, max_RCA), whether it is significant
    (sig_LM ...), left_main (0 or 1) and n_vessels (0 to 3). The second has
    one row per lesion: patient_id, vessel, territory, segment, stenosis in
    percent, kind (de novo or in-stent), culprit (0 or 1) and order, the
    position of the lesion along its artery.
    """
    pats, lesions = [], []
    for _, row in cohort.iterrows():
        pid = row["patient_id"]
        d = _Draw(seed, pid)
        cad = bool(row["cad"])
        if not cad and d.u("angio") >= share_without_cad:
            continue
        dominance = d.pick("dominance", ["right", "left", "codominant"], [83, 9, 8])
        access = d.pick("access", ["radial", "femoral"], [7, 3])
        found = []  # (vessel, segment, stenosis, kind, culprit)
        if cad:
            diag = row["main_diagnosis"]
            k = {"ACS": [55, 30, 15], "CCS": [50, 30, 20], "HFrEF": [20, 35, 45], "HFpEF": [55, 30, 15]}.get(diag, [50, 30, 20])
            n_sig = d.pick("nsig", [1, 2, 3], k)
            terr = list(d.rng("territories").choice(["LAD", "RCA", "LCX"], size=3, replace=False, p=[0.45, 0.30, 0.25]))
            if diag == "ACS":
                where = row["stemi_territory"]
                if where == "anterior":
                    culprit_t = "LAD"
                elif where == "inferior":
                    culprit_t = "RCA" if d.u("inf") < 0.85 else "LCX"
                elif where == "lateral":
                    culprit_t = "LCX" if d.u("lat") < 0.7 else "LAD"
                else:
                    culprit_t = terr[0]
                terr = [culprit_t] + [t for t in terr if t != culprit_t]
            for j, t in enumerate(terr[:n_sig]):
                vessel, seg = _place(d, f"sig{j}", t)
                culprit = int(diag == "ACS" and j == 0)
                if culprit:
                    vessel = t if (row["stemi_territory"] != "lateral" or t == "LCX") else d.pick("latbranch", ["D1", "LAD"])
                    seg = d.pick("culpritseg", ["proximal", "mid"]) if vessel in ("LAD", "LCX", "RCA") else "proximal"
                    s = 100 if (row["stemi_territory"] != "none" and d.u("occl") < 0.6) else d.pick("culprits", [90, 95, 99])
                else:
                    s = _severe(d, f"sigs{j}")
                kind = "in-stent" if (not culprit and d.u(f"ist{j}") < 0.08) else "de novo"
                found.append((vessel, seg, s, kind, culprit))
            if d.u("lm") < (0.04 + 0.06 * (n_sig == 3)):
                found.append(("LM", d.pick("lmseg", SEGMENTS["LM"], [3, 3, 4]), d.pick("lms", [50, 60, 70, 80], [3, 3, 3, 1]), "de novo", 0))
            for j, t in enumerate(terr[n_sig:]):
                if d.u(f"mildt{j}") < 0.45:
                    vessel, seg = _place(d, f"mild{j}", t)
                    found.append((vessel, seg, _mild(d, f"milds{j}"), "de novo", 0))
            if d.u("extra") < 0.3:
                t = terr[0]
                vessel, seg = _place(d, "extra", t)
                if not any(f[0] == vessel and f[1] == seg for f in found):
                    found.append((vessel, seg, d.pick("extras", [30, 40, 50, 60]), "de novo", 0))
            if d.u("oldstent") < 0.12 and diag != "ACS":
                t = d.pick("oldstentt", ["LAD", "RCA", "LCX"])
                if not any(TERRITORY[f[0]] == t for f in found):
                    found.append((t, d.pick("oldstentseg", ["proximal", "mid"]), 0, "in-stent", 0))
        else:
            if d.u("plaque") < 0.4:
                for j in range(d.integer("nplaque", 1, 2)):
                    t = d.pick(f"pt{j}", ["LAD", "LCX", "RCA"], [5, 2, 3])
                    vessel, seg = _place(d, f"plaque{j}", t)
                    found.append((vessel, seg, d.pick(f"ps{j}", [20, 30, 40]), "de novo", 0))
        # PDA lesions only in right-dominant systems
        found = [(("RCA", "distal", s, k, c) if (v == "PDA" and dominance != "right") else (v, sg, s, k, c)) for v, sg, s, k, c in found]
        # one lesion per vessel and segment, the larger one kept
        best = {}
        for v, sg, s, k, c in found:
            if (v, sg) not in best or s > best[(v, sg)][0]:
                best[(v, sg)] = (s, k, c)
        order = {"ostial": 0, "proximal": 1, "body": 1, "mid": 2, "distal": 3}
        rows = []
        for (v, sg), (s, k, c) in best.items():
            rows.append(dict(patient_id=pid, vessel=v, territory=TERRITORY[v], segment=sg, stenosis=int(s), kind=k, culprit=int(c), order=order[sg]))
        rows.sort(key=lambda r: (VESSELS.index(r["vessel"]), r["order"]))
        lesions += rows
        mx = {t: max([r["stenosis"] for r in rows if r["territory"] == t], default=0) for t in TERRITORIES}
        sig = {t: int(significant(t, mx[t])) for t in TERRITORIES}
        n_vessels = sig["LAD"] + sig["LCX"] + sig["RCA"]
        if row["main_diagnosis"] == "ACS":
            treatment = "PCI"
        elif sig["LM"] or n_vessels == 3:
            treatment = "CABG"
        elif n_vessels >= 1 and d.u("pci") < 0.65:
            treatment = "PCI"
        else:
            treatment = "medical"
        target = None
        if treatment == "PCI":
            cands = [r for r in rows if r["culprit"]] or sorted([r for r in rows if significant(r["territory"], r["stenosis"]) and r["territory"] != "LM"],
                                                                key=lambda r: -r["stenosis"])
            target = (cands[0]["vessel"], cands[0]["segment"]) if cands else None
            if target is None:
                treatment = "medical"
        pats.append(dict(patient_id=pid, dominance=dominance, access=access, treatment=treatment,
                         target_vessel=target[0] if target else "", target_segment=target[1] if target else "",
                         **{f"max_{t}": mx[t] for t in TERRITORIES}, **{f"sig_{t}": sig[t] for t in TERRITORIES},
                         left_main=sig["LM"], n_vessels=n_vessels))
    return pd.DataFrame(pats), pd.DataFrame(lesions)
