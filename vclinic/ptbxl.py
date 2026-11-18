"""PTB-XL, the 12-lead ECGs of Week 5.

PTB-XL holds 21,799 clinical 12-lead electrocardiograms (ECGs) of 10 seconds
from 18,869 patients, recorded with devices of Schiller AG between 1989 and
1996 and annotated by up to two cardiologists with the statements of the
SCP-ECG standard [Wagner et al., Scientific Data 7:154, 2020,
doi:10.1038/s41597-020-0495-6]. The records are split into ten folds by
patient; folds 9 and 10 hold labels of higher quality and are meant for
validation and test.

The course uses the records at 100 Hz of four folds: folds 1 and 2 for
training, fold 9 for validation and fold 10 for the test. download() fetches
them from PhysioNet, so every participant receives the same files in Google
Colab and in Jupyter. PTB-XL is published under the Creative Commons
Attribution 4.0 International License (CC BY 4.0).
"""

import ast
import concurrent.futures
import pathlib
import time
import urllib.request

import numpy as np
import pandas as pd

from .physionet import read_record

BASE = "https://physionet.org/files/ptb-xl/1.0.3/"
CITATION = ("P. Wagner, N. Strodthoff, R.-D. Bousseljot, D. Kreiseler, F. I. Lunze, W. Samek, T. Schaeffter. "
            "PTB-XL, a large publicly available electrocardiography dataset. Scientific Data 7:154, 2020. "
            "doi:10.1038/s41597-020-0495-6")
LICENSE = "CC BY 4.0"
LEADS = ("I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6")
FS = 100
SAMPLES = 1000
SPLITS = {"training": (1, 2), "validation": (9,), "test": (10,)}
TABLES = ("ptbxl_database.csv", "scp_statements.csv")
DAT_BYTES = SAMPLES * len(LEADS) * 2
ACUTE = ("Stadium I", "Stadium I-II")


def default_folder():
    """The folder data/ptbxl of the course folder (next to the package vclinic)."""
    return pathlib.Path(__file__).resolve().parents[1] / "data" / "ptbxl"


def _fetch(url, target, size=None, tries=5):
    if target.exists() and target.stat().st_size > 0 and (size is None or target.stat().st_size == size):
        return 0
    target.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                data = r.read()
            if size is not None and len(data) != size:
                raise IOError(f"{target.name}: {len(data)} of {size} bytes")
            tmp = target.with_suffix(target.suffix + ".part")
            tmp.write_bytes(data)
            tmp.replace(target)
            return len(data)
        except Exception:
            if attempt == tries - 1:
                raise
            time.sleep(2 + 3 * attempt)
    return 0


def _folds(splits):
    out = []
    for s in splits:
        out += list(SPLITS[s])
    return out


def download(splits=tuple(SPLITS), folder=None, workers=16, verbose=True):
    """Download the two tables and the 100 Hz records of the course.

    splits: the splits to download, by default training, validation and test.
    Files that are already complete are skipped, so the function can be run
    again after an interruption. Returns the folder of the data.
    """
    folder = pathlib.Path(folder) if folder else default_folder()
    for name in TABLES:
        _fetch(BASE + name, folder / name)
    db = pd.read_csv(folder / TABLES[0])
    rows = db[db["strat_fold"].isin(_folds(splits))]
    jobs = []
    for fn in rows["filename_lr"]:
        jobs.append((BASE + fn + ".hea", folder / (fn + ".hea"), None))
        jobs.append((BASE + fn + ".dat", folder / (fn + ".dat"), DAT_BYTES))
    todo = [j for j in jobs if not (j[1].exists() and j[1].stat().st_size > 0
                                    and (j[2] is None or j[1].stat().st_size == j[2]))]
    if verbose:
        print(f"PTB-XL: {len(rows)} records of folds {', '.join(map(str, _folds(splits)))}, "
              f"{len(jobs)} files, about {len(rows) * (DAT_BYTES + 700) / 1e6:.0f} MB; "
              f"{len(jobs) - len(todo)} files already present.")
    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(_fetch, *j) for j in todo]
        for k, fut in enumerate(concurrent.futures.as_completed(futures), 1):
            done += fut.result()
            if verbose and (k % max(1, len(todo) // 10) == 0 or k == len(todo)):
                print(f"  {k} of {len(todo)} files, {done / 1e6:.0f} MB")
    if verbose:
        print("PTB-XL data in", folder)
        print("License:", LICENSE, "· Citation:", CITATION)
    return folder


def statements(folder=None):
    """The table of the SCP-ECG statements: description and kind of each code."""
    folder = pathlib.Path(folder) if folder else default_folder()
    st = pd.read_csv(folder / TABLES[1], index_col=0)
    return st


def table(splits=tuple(SPLITS), folder=None):
    """One row per record of the chosen splits.

    The column codes holds the statements of each record as a dictionary
    (statement: likelihood in percent); split is training, validation or
    test; sex is "M" or "F"; acute_mi is True when the infarction stage of
    the record is Stadium I or Stadium I-II. PTB-XL stores the ages of 90
    years or more as 300; the table gives them as 90.
    """
    folder = pathlib.Path(folder) if folder else default_folder()
    db = pd.read_csv(folder / TABLES[0])
    db = db[db["strat_fold"].isin(_folds(splits))].copy()
    fold_split = {f: s for s, fs in SPLITS.items() for f in fs}
    db["split"] = db["strat_fold"].map(fold_split)
    db["codes"] = db["scp_codes"].apply(ast.literal_eval)
    db["sex"] = np.where(db["sex"] == 0, "M", "F")
    db["age"] = db["age"].where(db["age"] < 300, 90)
    stage = db["infarction_stadium1"].fillna("") + "|" + db["infarction_stadium2"].fillna("")
    db["acute_mi"] = stage.apply(lambda s: any(a in s.split("|") for a in ACUTE))
    keep = ["ecg_id", "patient_id", "age", "sex", "split", "strat_fold", "codes", "report",
            "infarction_stadium1", "infarction_stadium2", "acute_mi", "validated_by_human",
            "baseline_drift", "static_noise", "burst_noise", "electrodes_problems",
            "extra_beats", "pacemaker", "filename_lr"]
    return db[keep].reset_index(drop=True)


def has(codes, code, min_likelihood=0.0):
    """True when the statements of a record hold code with at least this likelihood."""
    return code in codes and codes[code] >= min_likelihood


def labels(tab, codes):
    """Multi-hot labels: one row per record, one column per statement (0 or 1)."""
    out = pd.DataFrame({c: tab["codes"].apply(lambda d, c=c: int(c in d)) for c in codes})
    out.index = tab["ecg_id"].to_numpy()
    out.index.name = "ecg_id"
    return out


def record(ecg_id, folder=None, tab=None):
    """The 12 leads of one record (mV) as a table, one column per lead, with
    the time in seconds as the index."""
    folder = pathlib.Path(folder) if folder else default_folder()
    if tab is None:
        tab = table(folder=folder)
    fn = tab.loc[tab["ecg_id"] == ecg_id, "filename_lr"]
    if fn.empty:
        raise KeyError(f"No record {ecg_id} in the course splits")
    rec = read_record(str(folder / fn.iloc[0]))
    names = [n.replace("AVR", "aVR").replace("AVL", "aVL").replace("AVF", "aVF") for n in rec.sig_name]
    leads = pd.DataFrame(rec.p_signal, columns=names)[list(LEADS)]
    leads.index = pd.Index(np.round(np.arange(len(leads)) / rec.fs, 6), name="time_s")
    return leads


def signals(tab, folder=None, cache=True, verbose=True):
    """An array of all records of a table: records × 12 leads × 1000 samples (mV).

    The records are read in batches of 500. The first call writes the array
    to a cache file in the data folder, and later calls read it from there.
    """
    folder = pathlib.Path(folder) if folder else default_folder()
    ids = tab["ecg_id"].to_numpy()
    key = f"{len(ids)}_{int(ids.sum()) % 1000003}_{int(ids[:50].sum())}"
    path = folder / "cache" / f"signals_{key}.npy"
    if cache and path.exists():
        return np.load(path)
    out = np.zeros((len(ids), len(LEADS), SAMPLES), dtype=np.float32)
    files = tab["filename_lr"].tolist()
    for start in range(0, len(ids), 500):
        for k in range(start, min(start + 500, len(ids))):
            rec = read_record(str(folder / files[k]))
            names = [n.upper() for n in rec.sig_name]
            order = [names.index(n.upper()) for n in LEADS]
            out[k] = rec.p_signal[:SAMPLES, order].T
        if verbose:
            print(f"  {min(start + 500, len(ids))} of {len(ids)} records read")
    if cache:
        path.parent.mkdir(parents=True, exist_ok=True)
        np.save(path, out)
    return out
