"""Paths and loaders of the real data sets bundled with the course."""

import os
from pathlib import Path

import numpy as np
import pandas as pd

CLEVELAND_COLUMNS = ["age", "sex", "cp", "trestbps", "chol", "fbs",
                     "restecg", "thalach", "exang", "oldpeak", "slope",
                     "ca", "thal", "num"]

UCI_URL = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
           "heart-disease/processed.cleveland.data")


def course_root():
    """Folder of the course repository (the one that holds vclinic)."""
    return Path(__file__).resolve().parent.parent


def data_path(*parts):
    """A data file of the course: the copy in the folder of the course, or, when it is missing there, a copy downloaded once from the GitHub repository of the course."""
    path = course_root().joinpath("data", *parts)
    if path.exists() or not Path(parts[-1]).suffix:
        return path
    import tempfile
    import urllib.request
    from .sources import COURSE_RAW
    cache = Path(tempfile.gettempdir()).joinpath("ai-cardiology-data", *parts)
    if not cache.exists():
        try:
            cache.parent.mkdir(parents=True, exist_ok=True)
            urllib.request.urlretrieve(COURSE_RAW + "data/" + "/".join(parts), cache)
        except OSError:
            return path
    return cache


def load_cleveland(download_if_missing=True, source=None):
    """UCI Heart Disease data, Cleveland subset (303 patients, 14 columns).

    Without a source, the file bundled with the course is read first; if it
    is missing, the file is downloaded from the UCI Machine Learning
    Repository. A source chooses where the data come from: "library"
    (ucimlrepo, the Python library of the UCI repository), "web" (the copy
    in the course repository) or "computer" (the file
    processed.cleveland.data in the current folder; Colab asks for it).
    Missing values ("?") become NaN. The column disease is 1 when num > 0
    (angiographic narrowing of more than 50 percent in a major vessel).
    """
    if source is None:
        path = data_path("uci-heart-disease", "processed.cleveland.data")
        where = str(path) if path.exists() else (UCI_URL if download_if_missing
                                                 else None)
        if where is None:
            raise FileNotFoundError(path)
        df = pd.read_csv(where, header=None, names=CLEVELAND_COLUMNS,
                         na_values="?")
    else:
        from .sources import source_name, install, local_file, COURSE_RAW
        kind = source_name(source)
        if kind == "library":
            install("ucimlrepo")
            from ucimlrepo import fetch_ucirepo
            uci = fetch_ucirepo(id=45)
            df = pd.concat([uci.data.features, uci.data.targets],
                           axis=1)[CLEVELAND_COLUMNS]
        else:
            where = (COURSE_RAW + "data/uci-heart-disease/processed.cleveland.data"
                     if kind == "web" else local_file("processed.cleveland.data"))
            df = pd.read_csv(where, header=None, names=CLEVELAND_COLUMNS,
                             na_values="?")
    df["disease"] = (df["num"] > 0).astype(int)
    return df


def _signal_files(header_path):
    """Names of the signal files that a WFDB header lists."""
    lines = [l for l in Path(header_path).read_text().splitlines()
             if l.strip() and not l.startswith("#")]
    n_sig = int(lines[0].split()[1])
    return sorted({l.split()[0] for l in lines[1:1 + n_sig]})


def physionet_files(record, folder, source, extensions=()):
    """Local path of a PhysioNet record (without extension), from the web copy of the course or from this computer.

    folder is the folder of the record under data/physionet, which is also
    its folder on PhysioNet (for example "mitdb"). extensions adds files
    such as "atr" (the beat labels) to the header and the signal files.
    """
    import tempfile
    from .sources import source_name, local_files, web_files, COURSE_RAW
    kind = source_name(source)
    if kind == "web":
        url = COURSE_RAW + f"data/physionet/{folder}/"
        target = Path(tempfile.gettempdir()) / "ai-cardiology-data" / folder
        header = web_files(url, [record + ".hea"], folder=target)[0]
        names = _signal_files(header) + [record + "." + e for e in extensions]
        web_files(url, names, folder=target)
        return header[:-4]
    if kind == "computer":
        header = local_files(record + ".hea")[0]
        local_files(*(_signal_files(header) + [record + "." + e for e in extensions]))
        return header[:-4]
    raise ValueError(source)


def read_physionet(record, folder, source=None):
    """Read a PhysioNet record with wfdb, or with the small reader.

    record: record name, for example "100"
    folder: folder under data/physionet, for example "mitdb"; it is also
    the folder of the record on PhysioNet
    source: None for the copy bundled with the course, or "library" (wfdb
    reads PhysioNet), "web" (the copy in the course repository) or
    "computer" (the files in the current folder; Colab asks for them)
    Returns (signal table in mV, sampling frequency, comments).
    """
    from .sources import source_name
    if source is not None and source_name(source) == "library":
        import wfdb
        rec = wfdb.rdrecord(record, pn_dir=folder)
    else:
        path = (str(data_path("physionet", folder, record)) if source is None
                else physionet_files(record, folder, source))
        try:
            import wfdb
            rec = wfdb.rdrecord(path)
        except ImportError:
            from .physionet import read_record
            rec = read_record(path)
    table = pd.DataFrame(rec.p_signal, columns=list(rec.sig_name))
    table.index = pd.Index(np.round(np.arange(len(table)) / rec.fs, 6),
                           name="time_s")
    return table, float(rec.fs), list(rec.comments)


def read_physionet_annotation(record, folder, extension="atr", source=None):
    """Annotation samples and symbols of a PhysioNet record (sources as in read_physionet)."""
    from .sources import source_name
    if source is not None and source_name(source) == "library":
        import wfdb
        ann = wfdb.rdann(record, extension, pn_dir=folder)
        return np.asarray(ann.sample), list(ann.symbol)
    path = (str(data_path("physionet", folder, record)) if source is None
            else physionet_files(record, folder, source, extensions=(extension,)))
    try:
        import wfdb
        ann = wfdb.rdann(path, extension)
    except ImportError:
        from .physionet import read_annotation
        ann = read_annotation(path, extension)
    return np.asarray(ann.sample), list(ann.symbol)
