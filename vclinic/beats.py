"""Beats of a 12-lead ECG: R peaks, the median beat, the J point, the ST
deviation and the QT interval.

These are the tools of Week 5. They work on the 10-second recordings of
PTB-XL at 100 Hz and on the synthetic ECGs of the virtual clinic. An ECG is
an array of 12 leads × samples in mV, in the order of LEADS.

The ST deviation follows the fourth universal definition of myocardial
infarction [Thygesen et al., Circulation 138:e618-e651, 2018]: It is measured
at the J point, the end of the QRS complex, against the level of the PR
segment, and new ST elevation counts when it reaches the cut-point of its
lead in at least two contiguous leads.
"""
import numpy as np
from scipy.signal import find_peaks

from .measure import bandpass, pan_tompkins_signal, global_slope, t_end_tangent

LEADS = ("I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6")
GROUPS = {"anterior": ("V1", "V2", "V3", "V4", "V5", "V6"),
          "inferior": ("II", "III", "aVF"),
          "lateral": ("I", "aVL")}
BEFORE_S, AFTER_S = 0.30, 0.55


def _as_leads(x):
    x = np.asarray(x, dtype=float)
    if x.ndim == 1:
        return x[None, :]
    return x if x.shape[0] <= x.shape[1] else x.T


def r_peaks(x, fs=100, threshold=0.3, refractory_s=0.25):
    """Indices of the R peaks of an ECG of one or more leads.

    The Pan-Tompkins signal of every lead is divided by its own 99th
    percentile and the leads are added, so that a lead with a small QRS
    complex counts as much as a lead with a large one. The peaks of the sum
    that are higher than threshold times its 99th percentile and at least
    refractory_s apart are the QRS complexes. Each is then placed at the
    largest absolute value, within 75 ms, of the band-passed leads added in
    the same way, so that the beats of a recording line up on one point.
    """
    x = _as_leads(x)
    m = np.zeros(x.shape[1])
    y = np.zeros(x.shape[1])
    for lead in x:
        if np.ptp(lead) < 1e-6:
            continue
        p = pan_tompkins_signal(lead, fs)
        m += p / (np.percentile(p, 99) + 1e-12)
        b = np.abs(bandpass(lead, fs, 1.0, min(40.0, 0.45 * fs)))
        y += b / (np.percentile(b, 99) + 1e-12)
    if not m.any():
        return np.array([], dtype=int)
    peaks, _ = find_peaks(m, height=threshold * np.percentile(m, 99), distance=int(round(refractory_s * fs)))
    half = int(round(0.075 * fs))
    out = [max(0, p - half) + int(np.argmax(y[max(0, p - half):p + half + 1])) for p in peaks]
    return np.unique(np.array(out, dtype=int))


def r_peaks_many(X, fs=100, threshold=0.3, refractory_s=0.25):
    """R peaks of many recordings at once: X is recordings × leads × samples.

    The same method as r_peaks, with the filters applied to all recordings
    together, which is much faster. Returns a list with the array of R
    peaks of each recording.
    """
    from scipy.signal import butter, filtfilt
    X = np.asarray(X, dtype=np.float32)
    b, a = butter(2, [5.0 / (fs / 2), 15.0 / (fs / 2)], btype="band")
    m = filtfilt(b, a, X, axis=-1)
    m = (np.gradient(m, axis=-1) * fs) ** 2
    w = max(1, int(round(0.150 * fs)))
    kernel = np.ones(w) / w
    m = np.apply_along_axis(lambda v: np.convolve(v, kernel, mode="same"), -1, m)
    b2, a2 = butter(2, [1.0 / (fs / 2), min(40.0, 0.45 * fs) / (fs / 2)], btype="band")
    y = np.abs(filtfilt(b2, a2, X, axis=-1))
    flat = np.ptp(X, axis=-1) < 1e-6
    m = np.where(flat[..., None], 0.0, m / (np.percentile(m, 99, axis=-1, keepdims=True) + 1e-12)).sum(axis=1)
    y = np.where(flat[..., None], 0.0, y / (np.percentile(y, 99, axis=-1, keepdims=True) + 1e-12)).sum(axis=1)
    half = int(round(0.075 * fs))
    out = []
    for mi, yi in zip(m, y):
        if not mi.any():
            out.append(np.array([], dtype=int))
            continue
        peaks, _ = find_peaks(mi, height=threshold * np.percentile(mi, 99), distance=int(round(refractory_s * fs)))
        out.append(np.unique(np.array([max(0, p - half) + int(np.argmax(yi[max(0, p - half):p + half + 1])) for p in peaks], dtype=int)))
    return out


def rr_intervals(x, fs=100):
    """RR intervals (s) of an ECG, from the R peaks of all its leads."""
    return np.diff(r_peaks(x, fs)) / fs


def median_beat(x, fs=100, peaks=None, before_s=BEFORE_S, after_s=AFTER_S):
    """The median beat of a recording: leads × samples, with the R peak at
    index round(before_s × fs).

    Every beat whose window from before_s before to after_s after its R
    peak fits into the recording is cut out, and the median of these beats
    is taken sample by sample. Returns (beat, number of beats used); the
    beat is None when no beat fits.
    """
    x = _as_leads(x)
    peaks = r_peaks(x, fs) if peaks is None else np.asarray(peaks, dtype=int)
    b, a = int(round(before_s * fs)), int(round(after_s * fs))
    use = [p for p in peaks if p - b >= 0 and p + a < x.shape[1]]
    if not use:
        return None, 0
    stack = np.stack([x[:, p - b:p + a + 1] for p in use])
    return np.median(stack, axis=0), len(use)


def qrs_onset_offset(beat, fs=100, r_index=None, frac=0.08):
    """QRS onset and offset (sample indices) of a median beat.

    The global slope of the leads, the sum of their absolute slopes, is
    compared with frac times its largest value around the R peak. The search
    starts at the steepest slope before and after the R peak: The onset is
    the last sample below this level before the R peak, and the offset, the
    J point, the first sample below it after the R peak.
    """
    beat = _as_leads(beat)
    r = int(round(BEFORE_S * fs)) if r_index is None else int(r_index)
    g = global_slope(beat.T, fs)
    lo, hi = max(0, r - int(0.12 * fs)), min(len(g) - 1, r + int(0.14 * fs))
    level = frac * g[lo:hi + 1].max()
    on = lo + int(np.argmax(g[lo:r + 1]))
    off = r + int(np.argmax(g[r:min(hi, r + int(0.08 * fs)) + 1]))
    while on > lo and g[on] > level:
        on -= 1
    while off < hi and g[off] > level:
        off += 1
    return on, off


def st_deviation(beat, fs=100, r_index=None):
    """ST deviation at the J point of every lead of a median beat (mV).

    The reference level of each lead is the mean of the 40 ms of the PR
    segment that end 20 ms before the QRS onset. Returns a dictionary with
    the ST deviation of each lead, the QRS onset and the J point (sample
    indices of the beat) and the reference levels.
    """
    beat = _as_leads(beat)
    on, j = qrs_onset_offset(beat, fs, r_index)
    a, b = max(0, on - int(round(0.06 * fs))), max(1, on - int(round(0.02 * fs)))
    level = beat[:, a:b].mean(axis=1)
    st = beat[:, j] - level
    return {"st_mv": dict(zip(LEADS, np.round(st, 3))), "onset": on, "j": j, "level": level}


def cut_point(lead, sex, age):
    """The cut-point of new ST elevation at the J point (mV) of the fourth
    universal definition: 0.2 mV in V2 and V3 for men of 40 years or older,
    0.25 mV for men under 40, 0.15 mV for women, and 0.1 mV in all other
    leads. sex is "M" or "F"."""
    if lead in ("V2", "V3"):
        if sex == "F":
            return 0.15
        return 0.2 if age >= 40 else 0.25
    return 0.1


def stemi_criteria(st_mv, sex, age):
    """The ST criteria of the fourth universal definition for one recording.

    st_mv: dictionary of the ST deviation of each lead (mV). A lead meets
    the criterion when its ST elevation reaches its cut-point, and the alarm
    fires when at least two leads of one group of contiguous leads meet it
    (anterior V1 to V6, inferior II, III and aVF, lateral I and aVL).
    Returns (alarm, the leads that meet the criterion, the groups that meet it).
    aVR is not part of a group.
    """
    meet = [lead for lead in LEADS if lead in st_mv and st_mv[lead] >= cut_point(lead, sex, age) - 1e-9]
    groups = [g for g, names in GROUPS.items() if sum(n in meet for n in names) >= 2]
    return bool(groups), meet, groups


def qt_interval(beat, fs=100, rr_s=None, lead="V5", r_index=None):
    """QT interval of a median beat (ms), from the QRS onset of all leads to
    the end of the T wave in one lead by the tangent method.

    rr_s is the mean RR interval of the recording (s); the search for the T
    wave ends at 70 percent of the way to the next R peak. Returns the QT
    interval in ms, or nan when no T wave end is found.
    """
    beat = _as_leads(beat)
    r = int(round(BEFORE_S * fs)) if r_index is None else int(r_index)
    on, off = qrs_onset_offset(beat, fs, r)
    k = LEADS.index(lead)
    a, b = max(0, on - int(round(0.06 * fs))), max(1, on - int(round(0.02 * fs)))
    level = float(beat[k, a:b].mean())
    next_r = r + int(round((rr_s if rr_s and np.isfinite(rr_s) else 1.0) * fs))
    last = beat.shape[1] - 1 - int(round(0.05 * fs))
    next_r = min(next_r, off + int((last - off) / 0.7))
    try:
        end = t_end_tangent(beat[k], fs, off, next_r, baseline=level)
    except ValueError:
        return float("nan")
    if not np.isfinite(end) or end <= off or end >= beat.shape[1]:
        return float("nan")
    return float((end - on) / fs * 1000)


def qtc(qt_ms, rr_s, formula="Bazett"):
    """Corrected QT interval (ms): Bazett QT/RR^(1/2) or Fridericia QT/RR^(1/3), RR in s."""
    power = 0.5 if formula == "Bazett" else 1.0 / 3.0
    return qt_ms / rr_s ** power
