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
    return course_root().joinpath("data", *parts)


def load_cleveland(download_if_missing=True):
    """UCI Heart Disease data, Cleveland subset (303 patients, 14 columns).

    The file bundled with the course is read first; if it is missing, the
    file is downloaded from the UCI Machine Learning Repository. Missing
    values ("?") become NaN. The column disease is 1 when num > 0
    (angiographic narrowing of more than 50 percent in a major vessel).
    """
    path = data_path("uci-heart-disease", "processed.cleveland.data")
    source = str(path) if path.exists() else (UCI_URL if download_if_missing
                                              else None)
    if source is None:
        raise FileNotFoundError(path)
    df = pd.read_csv(source, header=None, names=CLEVELAND_COLUMNS,
                     na_values="?")
    df["disease"] = (df["num"] > 0).astype(int)
    return df


def read_physionet(record, folder):
    """Read a bundled PhysioNet record with wfdb, or with the small reader.

    record: record name, for example "100"
    folder: folder under data/physionet, for example "mitdb"
    Returns (signal table in mV, sampling frequency, comments).
    """
    path = str(data_path("physionet", folder, record))
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


def read_physionet_annotation(record, folder, extension="atr"):
    """Annotation samples and symbols of a bundled PhysioNet record."""
    path = str(data_path("physionet", folder, record))
    try:
        import wfdb
        ann = wfdb.rdann(path, extension)
    except ImportError:
        from .physionet import read_annotation
        ann = read_annotation(path, extension)
    return np.asarray(ann.sample), list(ann.symbol)
