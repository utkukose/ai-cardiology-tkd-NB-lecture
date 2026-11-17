"""Reference implementations of the ECG measurements of Week 1.

The Week 1 Jupyter notebook builds these steps one by one. The functions
here are the same steps in one place, for use in later weeks.
"""

import numpy as np
from scipy.signal import butter, filtfilt, find_peaks


def bandpass(x, fs, low=5.0, high=15.0, order=2):
    """Zero-phase Butterworth band-pass filter."""
    b, a = butter(order, [low / (fs / 2), high / (fs / 2)], btype="band")
    return filtfilt(b, a, x)


def lowpass(x, fs, cutoff=20.0, order=2):
    """Zero-phase Butterworth low-pass filter."""
    b, a = butter(order, cutoff / (fs / 2), btype="low")
    return filtfilt(b, a, x)


def pan_tompkins_signal(x, fs):
    """Band-pass, derivative, squaring and moving-window integration.

    Returns the integrated signal used to find the QRS complexes.
    """
    y = bandpass(x, fs, 5.0, 15.0)
    d = np.gradient(y) * fs              # derivative (mV/s)
    z = d ** 2                           # squaring
    w = max(1, int(round(0.150 * fs)))   # 150 ms window
    return np.convolve(z, np.ones(w) / w, mode="same")


def detect_r_peaks(x, fs, threshold=0.3, refractory_s=0.25):
    """Indices of the R peaks of one lead.

    The integrated Pan-Tompkins signal is searched for peaks higher than
    threshold times its 99th percentile and at least refractory_s apart.
    Each peak is then moved to the largest absolute value of the band-passed
    lead within 75 ms.
    """
    m = pan_tompkins_signal(x, fs)
    level = threshold * np.percentile(m, 99)
    peaks, _ = find_peaks(m, height=level,
                          distance=int(round(refractory_s * fs)))
    y = bandpass(x, fs, 1.0, 40.0)
    half = int(round(0.075 * fs))
    out = []
    for p in peaks:
        lo, hi = max(0, p - half), min(len(x), p + half + 1)
        out.append(lo + int(np.argmax(np.abs(y[lo:hi]))))
    return np.unique(np.array(out, dtype=int))


def match_beats(detected_s, reference_s, window_s=0.150):
    """True positives, false positives and false negatives.

    A detected beat matches a reference beat when the two lie within
    window_s of each other (each reference beat is matched once).
    """
    det = np.sort(np.asarray(detected_s, dtype=float))
    ref = np.sort(np.asarray(reference_s, dtype=float))
    used = np.zeros(len(det), dtype=bool)
    tp = 0
    for r in ref:
        if len(det) == 0:
            break
        j = int(np.argmin(np.abs(det - r) + used * 1e9))
        if not used[j] and abs(det[j] - r) <= window_s:
            used[j] = True
            tp += 1
    fp = int((~used).sum())
    fn = len(ref) - tp
    return tp, fp, fn


def global_slope(leads, fs, smooth_s=0.010):
    """Sum over the leads of the absolute slope (mV/s).

    Each lead is first band-passed from 1 to 40 Hz so that the slope of
    the noise stays small, and the sum is smoothed over smooth_s.
    """
    arr = np.asarray(leads, dtype=float)
    if arr.ndim == 1:
        arr = arr[:, None]
    arr = np.column_stack([bandpass(arr[:, j], fs, 1.0, 40.0)
                           for j in range(arr.shape[1])])
    g = np.abs(np.gradient(arr, axis=0)).sum(axis=1) * fs
    w = max(1, int(round(smooth_s * fs)))
    return np.convolve(g, np.ones(w) / w, mode="same")


def qrs_bounds(leads, fs, r_idx, frac=0.08):
    """QRS onset and offset (sample indices) around each R peak.

    The global slope of all leads is compared with frac times its largest
    value near the R peak; the onset is the last sample below this level
    before the R peak and the offset the first sample below it after.
    """
    g = global_slope(leads, fs)
    onsets, offsets = [], []
    for r in r_idx:
        lo = max(0, r - int(0.12 * fs))
        hi = min(len(g) - 1, r + int(0.14 * fs))
        level = frac * g[lo:hi + 1].max()
        on = r
        while on > lo and g[on] > level:
            on -= 1
        off = r
        while off < hi and g[off] > level:
            off += 1
        onsets.append(on)
        offsets.append(off)
    return np.array(onsets), np.array(offsets)


def t_end_tangent(x, fs, qrs_off, next_r, baseline=0.0):
    """End of the T wave by the tangent method (sample index).

    The T peak is the largest deviation from the baseline between 80 ms
    after the QRS offset and 70 percent of the way to the next R peak.
    The tangent at the steepest point of the falling limb is extended to
    the baseline; the crossing point is the end of the T wave.
    """
    lo = qrs_off + int(0.08 * fs)
    hi = qrs_off + int(0.7 * (next_r - qrs_off))
    seg = x[lo:hi] - baseline
    if len(seg) < 5:
        return np.nan
    k = int(np.argmax(np.abs(seg)))
    peak = lo + k
    sign = np.sign(seg[k]) or 1.0
    d = np.gradient(x) * fs
    stop = min(len(x) - 1, peak + int(0.20 * fs))
    s_idx = peak + int(np.argmin(sign * d[peak:stop]))
    slope = d[s_idx]
    if slope == 0:
        return np.nan
    return s_idx + (baseline - x[s_idx]) / slope * fs


def p_onset(x, fs, qrs_on, frac=0.10, earliest=0):
    """Onset of the P wave before a QRS onset (sample index).

    The P peak is searched between 300 and 40 ms before the QRS onset,
    but not before the sample earliest (for example the end of the
    previous T wave). The baseline is the median of the first 40 ms of
    this window, which lies on the flat segment before the P wave. The
    onset is the last sample before the peak whose height above this
    baseline is below frac times the P amplitude.
    """
    lo = max(0, int(earliest), qrs_on - int(0.30 * fs))
    hi = max(lo + 1, qrs_on - int(0.04 * fs))
    seg = np.asarray(x[lo:hi], dtype=float)
    if len(seg) < int(0.08 * fs):
        return np.nan
    base = float(np.median(seg[:int(0.04 * fs)]))
    seg = seg - base
    k = int(np.argmax(seg))
    amp = seg[k]
    if amp <= 0 or k < int(0.03 * fs):
        return np.nan
    j = k
    while j > 0 and seg[j] > frac * amp:
        j -= 1
    return lo + j


def hrv_time_domain(rr_s):
    """SDNN and RMSSD (ms) of a series of RR intervals in seconds."""
    rr = np.asarray(rr_s, dtype=float) * 1000.0
    sdnn = float(np.std(rr, ddof=1))
    rmssd = float(np.sqrt(np.mean(np.diff(rr) ** 2)))
    return sdnn, rmssd


def bland_altman(a, b):
    """Bias and 95 percent limits of agreement of a - b."""
    d = np.asarray(a, dtype=float) - np.asarray(b, dtype=float)
    bias = float(np.mean(d))
    sd = float(np.std(d, ddof=1))
    return bias, bias - 1.96 * sd, bias + 1.96 * sd
