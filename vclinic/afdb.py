"""The MIT-BIH Atrial Fibrillation Database (AFDB), the Holter recordings of Week 10.

The AFDB holds 25 long-term ECG recordings of people with atrial fibrillation
(AF), mostly paroxysmal, made at Beth Israel Hospital in Boston. Each record
lasts about 10 hours and has two ECG signals at 250 samples per second with a
resolution of 12 bits over +-10 mV; records 00735 and 03665 have no signals,
only their annotations. The rhythm annotations (.atr) were prepared by hand and
mark (AFIB atrial fibrillation, (AFL atrial flutter, (J AV junctional rhythm
and (N all other rhythms. The beat annotations (.qrs) come from an automatic
detector and were not checked by hand [Moody and Mark, Computers in Cardiology
10:227-230, 1983].

download() fetches the 75 header and annotation files of the 25 records, about
2.7 MB, and the signal files of the records named in `signals` (27.6 MB each)
from PhysioNet, and checks every file against the SHA-256 sums that PhysioNet
publishes with the database. The AFDB is published under the Open Data Commons
Attribution License v1.0 (ODC-By 1.0). The files are not part of the course
repository: every participant downloads them from PhysioNet.

The readers below need no extra package: beats() and rhythm() read the MIT
format of the annotation files, and strip() reads a few seconds of the signals
(format 212) without loading the whole file.
"""

import concurrent.futures
import hashlib
import pathlib
import time
import urllib.request

import numpy as np

BASE = "https://physionet.org/files/afdb/1.0.0/"
CITATION = ("G. B. Moody, R. G. Mark. A new method for detecting atrial fibrillation using R-R intervals. "
            "Computers in Cardiology 10:227-230, 1983. PhysioNet, doi:10.13026/C2MW2D")
LICENSE = "Open Data Commons Attribution License v1.0 (ODC-By 1.0)"
FS = 250
RECORDS = ("00735", "03665", "04015", "04043", "04048", "04126", "04746", "04908", "04936", "05091",
           "05121", "05261", "06426", "06453", "06995", "07162", "07859", "07879", "07910", "08215",
           "08219", "08378", "08405", "08434", "08455")
NO_SIGNALS = ("00735", "03665")
# The records whose signals the course uses for the strips of the prototype
SIGNALS = ("04936", "06426", "08219")
DAT_BYTES = 27_617_280
# The split of the course, by record
SPLITS = {"training": ("00735", "03665", "04048", "04126", "04746", "05091", "05261", "06453", "07162",
                       "07859", "07879", "08215", "08405", "08434", "08455"),
          "validation": ("04043", "04908", "06995", "08219", "08378"),
          "test": ("04015", "04936", "05121", "06426", "07910")}


def default_folder():
    """The folder data/afdb of the course folder (next to the package vclinic)."""
    return pathlib.Path(__file__).resolve().parents[1] / "data" / "afdb"


def _fetch(url, target, tries=5):
    if target.exists() and target.stat().st_size > 0:
        return 0
    target.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                data = r.read()
            tmp = target.with_suffix(target.suffix + ".part")
            tmp.write_bytes(data)
            tmp.replace(target)
            return len(data)
        except Exception:
            if attempt == tries - 1:
                raise
            time.sleep(2 + 3 * attempt)
    return 0


def _sums(folder):
    path = folder / "SHA256SUMS.txt"
    out = {}
    for line in path.read_text(encoding="ascii").splitlines():
        parts = line.split()
        if len(parts) == 2:
            out[parts[1].lstrip("*")] = parts[0]
    return out


def download(signals=SIGNALS, folder=None, workers=4, verbose=True):
    """Download the annotations of the 25 records and the signals of `signals`.

    Files that are already there are skipped, so the function can be run again
    after an interruption. Every file is checked against SHA256SUMS.txt of
    PhysioNet; a file that does not match raises an error. Returns the folder.
    """
    folder = pathlib.Path(folder) if folder else default_folder()
    _fetch(BASE + "SHA256SUMS.txt", folder / "SHA256SUMS.txt")
    names = [f"{r}.{e}" for r in RECORDS for e in ("hea", "atr", "qrs")] + [f"{r}.dat" for r in signals]
    todo = [n for n in names if not (folder / n).exists()]
    if verbose:
        mb = (len(todo) - sum(n.endswith(".dat") for n in todo)) * 0.04 + sum(n.endswith(".dat") for n in todo) * DAT_BYTES / 1e6
        print(f"AFDB: {len(names)} files of 25 records, {len(names) - len(todo)} already present, "
              f"about {mb:.0f} MB to download.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        list(pool.map(lambda n: _fetch(BASE + n, folder / n), todo))
    sums = _sums(folder)
    for n in names:
        digest = hashlib.sha256((folder / n).read_bytes()).hexdigest()
        if digest != sums.get(n):
            raise IOError(f"{n}: the file does not match SHA256SUMS.txt of PhysioNet; delete it and run download() again.")
    if verbose:
        print("AFDB data in", folder, "· all files match SHA256SUMS.txt")
        print("License:", LICENSE, "· Citation:", CITATION)
    return folder


def _read_mit(path):
    """Samples, codes and auxiliary texts of an annotation file in the MIT format."""
    data = np.fromfile(path, dtype="<u2")
    samples, codes, aux = [], [], []
    t, i = 0, 0
    while i < len(data):
        word = int(data[i])
        if word == 0:
            break
        code, value = word >> 10, word & 0x3FF
        if code == 59:          # SKIP: a 32-bit interval follows
            skip = (int(data[i + 1]) << 16) | int(data[i + 2])
            t += skip - 2 ** 32 if skip >= 2 ** 31 else skip
            i += 3
            continue
        if code in (60, 61, 62):  # NUM, SUB, CHN: no change of time
            i += 1
            continue
        if code == 63:          # AUX: a text of `value` bytes for the annotation before
            n_words = (value + 1) // 2
            raw = data[i + 1:i + 1 + n_words].astype("<u2").tobytes()[:value]
            if aux:
                aux[-1] = raw.decode("latin-1").rstrip("\x00")
            i += 1 + n_words
            continue
        t += value
        samples.append(t)
        codes.append(code)
        aux.append("")
        i += 1
    return np.array(samples, dtype=np.int64), codes, aux


def beats(record, folder=None):
    """Times of the beats (s) from the unaudited beat annotations (.qrs)."""
    folder = pathlib.Path(folder) if folder else default_folder()
    samples, _, _ = _read_mit(folder / f"{record}.qrs")
    return samples / FS


def rhythm(record, folder=None):
    """Rhythm episodes from the reference annotations (.atr): a list of (start_s, end_s, rhythm).

    The last episode ends at the last beat of the record.
    """
    folder = pathlib.Path(folder) if folder else default_folder()
    samples, _, aux = _read_mit(folder / f"{record}.atr")
    end = beats(record, folder)[-1]
    starts = samples / FS
    ends = list(starts[1:]) + [end]
    return [(float(s), float(e), a) for s, e, a in zip(starts, ends, aux)]


def strip(record, start_s, seconds=10.0, folder=None):
    """Both ECG signals (mV) of a record from start_s for `seconds`; returns (time in s, signals).

    The signals are stored in format 212: two 12-bit samples in three bytes,
    with a gain of 200 units per mV and a baseline of 0.
    """
    folder = pathlib.Path(folder) if folder else default_folder()
    first = int(round(start_s * FS))
    n = int(round(seconds * FS))
    with open(folder / f"{record}.dat", "rb") as f:
        f.seek(3 * first)
        raw = np.frombuffer(f.read(3 * n), dtype=np.uint8).reshape(-1, 3).astype(np.int32)
    a = raw[:, 0] + ((raw[:, 1] & 0x0F) << 8)
    b = raw[:, 2] + ((raw[:, 1] & 0xF0) << 4)
    a[a > 2047] -= 4096
    b[b > 2047] -= 4096
    t = start_s + np.arange(len(a)) / FS
    return t, np.column_stack([a, b]) / 200.0
