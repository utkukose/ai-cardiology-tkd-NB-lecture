"""Reading PhysioNet records without extra packages.

The course uses the wfdb package to read PhysioNet records. When wfdb is
not installed, the small readers below read the two record formats of the
course records (format 212 of the MIT-BIH Arrhythmia Database and format
16 of the PTB Diagnostic ECG Database) and MIT annotation files. They are
simplified readers for these files only; wfdb remains the general tool.
"""

import os

import numpy as np


class Record:
    """Signals of a record in physical units (mV), like wfdb.Record."""

    def __init__(self, name, fs, sig_name, units, p_signal, comments):
        self.record_name = name
        self.fs = fs
        self.sig_name = sig_name
        self.units = units
        self.p_signal = p_signal
        self.sig_len = p_signal.shape[0]
        self.n_sig = p_signal.shape[1]
        self.comments = comments


class Annotation:
    """Annotation positions (samples) and symbols, like wfdb.Annotation."""

    def __init__(self, sample, symbol):
        self.sample = np.asarray(sample, dtype=int)
        self.symbol = list(symbol)


def _read_header(path):
    with open(path + ".hea", encoding="latin-1") as f:
        lines = [ln.rstrip("\n") for ln in f]
    comments = [ln[1:].strip() for ln in lines if ln.startswith("#")]
    body = [ln for ln in lines if ln.strip() and not ln.startswith("#")]
    first = body[0].split()
    n_sig = int(first[1])
    fs = float(first[2].split("/")[0])
    n_samp = int(first[3]) if len(first) > 3 else None
    sigs = []
    for ln in body[1:1 + n_sig]:
        parts = ln.split()
        fmt = parts[1].split("x")[0].split(":")[0].split("+")[0]
        gain_txt = parts[2].split("/")[0]
        baseline = 0
        if "(" in gain_txt:
            gain_txt, base_txt = gain_txt.split("(")
            baseline = int(base_txt.rstrip(")"))
        gain = float(gain_txt) if float(gain_txt) != 0 else 200.0
        units = parts[2].split("/")[1] if "/" in parts[2] else "mV"
        adc_zero = int(parts[4]) if len(parts) > 4 else 0
        if "(" not in parts[2]:
            baseline = adc_zero
        name = parts[-1] if len(parts) > 8 else f"ch{len(sigs)}"
        sigs.append(dict(file=parts[0], fmt=fmt, gain=gain,
                         baseline=baseline, units=units, name=name))
    return fs, n_samp, sigs, comments


def _read_212(path, n_ch):
    raw = np.fromfile(path, dtype=np.uint8)
    raw = raw[: (len(raw) // 3) * 3].reshape(-1, 3).astype(np.int32)
    a = raw[:, 0] + ((raw[:, 1] & 0x0F) << 8)
    b = raw[:, 2] + ((raw[:, 1] & 0xF0) << 4)
    a[a > 2047] -= 4096
    b[b > 2047] -= 4096
    flat = np.empty(2 * len(a), dtype=np.int32)
    flat[0::2] = a
    flat[1::2] = b
    n = len(flat) // n_ch
    return flat[: n * n_ch].reshape(n, n_ch)


def _read_16(path, n_ch):
    flat = np.fromfile(path, dtype="<i2").astype(np.int32)
    n = len(flat) // n_ch
    return flat[: n * n_ch].reshape(n, n_ch)


def read_record(path):
    """Read a record (path without extension) into a Record object."""
    fs, n_samp, sigs, comments = _read_header(path)
    folder = os.path.dirname(path)
    blocks = []
    files = []
    for s in sigs:
        if s["file"] not in files:
            files.append(s["file"])
    for fname in files:
        group = [s for s in sigs if s["file"] == fname]
        fmt = group[0]["fmt"]
        full = os.path.join(folder, fname)
        if fmt == "212":
            digital = _read_212(full, len(group))
        elif fmt == "16":
            digital = _read_16(full, len(group))
        else:
            raise ValueError(f"Format {fmt} is not supported here; "
                             "install wfdb to read this record.")
        for j, s in enumerate(group):
            blocks.append((digital[:, j] - s["baseline"]) / s["gain"])
    n = min(len(b) for b in blocks)
    if n_samp:
        n = min(n, n_samp)
    p_signal = np.column_stack([b[:n] for b in blocks])
    name = os.path.basename(path)
    return Record(name, fs, [s["name"] for s in sigs],
                  [s["units"] for s in sigs], p_signal, comments)


# Annotation codes of the MIT format (the subset used by the course
# records); see the WFDB documentation for the full table.
_CODES = {1: "N", 2: "L", 3: "R", 4: "a", 5: "V", 6: "F", 7: "J", 8: "A",
          9: "S", 10: "E", 11: "j", 12: "/", 13: "Q", 14: "~", 16: "|",
          18: "s", 19: "T", 20: "*", 21: "D", 22: '"', 23: "=", 24: "p",
          25: "B", 26: "^", 27: "t", 28: "+", 29: "u", 30: "?", 31: "!",
          32: "[", 33: "]", 34: "e", 35: "n", 36: "@", 37: "x", 38: "f",
          39: "(", 40: ")", 41: "r"}


def read_annotation(path, extension="atr"):
    """Read an MIT-format annotation file into an Annotation object."""
    data = np.fromfile(f"{path}.{extension}", dtype="<u2")
    samples, symbols = [], []
    t = 0
    i = 0
    while i < len(data):
        word = int(data[i])
        code = word >> 10
        value = word & 0x3FF
        if word == 0:
            break
        if code == 59:          # SKIP: a 32-bit interval follows
            hi, lo = int(data[i + 1]), int(data[i + 2])
            skip = (hi << 16) | lo
            if skip >= 2 ** 31:
                skip -= 2 ** 32
            t += skip
            i += 3
            continue
        if code in (60, 61, 62):  # NUM, SUB, CHN: no time change
            i += 1
            continue
        if code == 63:          # AUX: text follows, padded to even length
            i += 1 + (value + 1) // 2
            continue
        t += value
        samples.append(t)
        symbols.append(_CODES.get(code, "?"))
        i += 1
    return Annotation(samples, symbols)
