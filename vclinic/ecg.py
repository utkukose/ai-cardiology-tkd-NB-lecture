"""Synthetic 12-lead electrocardiogram (ECG) from a moving heart vector.

The model follows the dipole hypothesis of electrocardiography. The electrical
activity of the heart is summarised by one vector H(t) in three dimensions,
and every lead records the projection of H(t) on its lead vector L:

    V_L(t) = L . H(t) = Lx*Hx(t) + Ly*Hy(t) + Lz*Hz(t)

H(t) is built from Gaussian-shaped components (P, QRS and T waves), each with
its own direction in space, in the spirit of the dynamical ECG models of
McSharry et al. (2003) and their three-dimensional extension by Sameni et al.
(2007). Patient parameters set the timing (PR, QRS and QT intervals), the
heart rate, the electrical axis, the rhythm (sinus or atrial fibrillation),
the conduction (normal or left bundle branch block) and an optional ST injury
vector. Because the parameters are known, every measurement made on the
signal can be compared with its true value.

Coordinates: x points to the patient's left, y points down (toward the feet)
and z points forward (anterior). Amplitudes are in millivolts (mV) and times
in seconds (s), unless a name ends in _ms.

The signals are synthetic teaching material and are not for clinical use.
"""

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

LEADS = ("I", "II", "III", "aVR", "aVL", "aVF",
         "V1", "V2", "V3", "V4", "V5", "V6")

# Frontal-plane angles of the six limb leads (hexaxial reference system).
LIMB_ANGLES = {"I": 0, "II": 60, "III": 120, "aVR": -150, "aVL": -30,
               "aVF": 90}

# Chest leads: horizontal angle (degrees from the left toward the front),
# downward tilt (degrees) and strength. The electrodes lie close to the
# heart, so their lead vectors are longer than those of the limb leads, and
# V3 to V6 sit slightly below the centre of the heart. The values are
# idealised; real lead vectors differ from person to person.
CHEST_LEADS = {"V1": (115, 0, 1.2), "V2": (95, 0, 1.8), "V3": (75, 10, 1.9),
               "V4": (55, 20, 1.9), "V5": (30, 20, 1.6), "V6": (5, 15, 1.2)}

TERRITORY_ANGLES = {
    # (frontal angle, anterior angle) of the ST injury vector
    "anterior": (-40, 55),   # left anterior descending artery (LAD)
    "inferior": (100, -10),  # right coronary artery (RCA)
    "lateral": (-10, -40),   # left circumflex artery (LCx)
    # diffuse subendocardial ischaemia: with a negative st_mv the ST segment is
    # depressed in the leads that face the apex and raised in aVR
    "subendocardial": (45, 20),
}


def direction(frontal_deg, anterior_deg=0.0):
    """Unit vector from a frontal-plane angle and an anterior tilt.

    frontal_deg: angle in the frontal plane, 0 = toward the left arm,
        +90 = toward the feet (the hexaxial convention).
    anterior_deg: tilt toward the front of the chest (negative = back).
    """
    f = np.deg2rad(frontal_deg)
    a = np.deg2rad(anterior_deg)
    return np.array([np.cos(a) * np.cos(f), np.cos(a) * np.sin(f), np.sin(a)])


def _lead_vectors():
    vectors = {}
    for name, angle in LIMB_ANGLES.items():
        # Goldberger's augmented leads are sqrt(3)/2 as long as the
        # bipolar limb leads in the ideal Einthoven triangle.
        strength = np.sqrt(3) / 2 if name.startswith("aV") else 1.0
        vectors[name] = strength * direction(angle, 0.0)
    for name, (angle, tilt, strength) in CHEST_LEADS.items():
        a = np.deg2rad(angle)
        e = np.deg2rad(tilt)
        vectors[name] = strength * np.array([np.cos(e) * np.cos(a), np.sin(e),
                                             np.cos(e) * np.sin(a)])
    return vectors


LEAD_VECTORS = _lead_vectors()
LEAD_MATRIX = np.vstack([LEAD_VECTORS[name] for name in LEADS])  # 12 x 3


def project(heart_vector):
    """Voltages of the 12 leads for one heart vector (or an n x 3 array)."""
    h = np.asarray(heart_vector, dtype=float)
    return h @ LEAD_MATRIX.T


def frontal_axis(v_lead_i, v_lead_avf):
    """Frontal QRS axis (degrees) from the net voltages of leads I and aVF."""
    hy = v_lead_avf / (np.sqrt(3) / 2)
    return float(np.degrees(np.arctan2(hy, v_lead_i)))


# --------------------------------------------------------------------------
# One heart beat as a list of components
# --------------------------------------------------------------------------

@dataclass
class Component:
    """One Gaussian-shaped wave component of the heart vector.

    centre: time of the peak, relative to the QRS onset (s)
    sigma_rise, sigma_fall: widths before and after the peak (s)
    amplitude: peak length of the vector (mV)
    direction: unit vector of the component
    wave: "P", "QRS" or "T"
    """
    centre: float
    sigma_rise: float
    sigma_fall: float
    amplitude: float
    direction: np.ndarray
    wave: str


def beat_components(p):
    """Components of one beat from a parameter dictionary.

    Keys used: rhythm, conduction, pr_ms, p_ms, qrs_ms, qt_ms, axis_deg,
    r_amp, t_amp.
    Interval definitions used for the true values:
    P onset and QRS onset/offset lie 2.5 sigma from the nearest component
    centre (about 4 percent of its peak). The T end lies where the tangent
    at the steepest point of the falling T wave meets the baseline, which
    for a Gaussian falling side is 2 sigma after the T peak.
    """
    qrs = p["qrs_ms"] / 1000.0
    qt = p["qt_ms"] / 1000.0
    axis = p["axis_deg"]
    comps = []

    if p["rhythm"] == "sinus":
        pr = p["pr_ms"] / 1000.0
        pdur = p.get("p_ms", 100) / 1000.0
        sp = 0.14 * pdur
        onset = -pr
        comps.append(Component(onset + 2.5 * sp, sp, sp, 0.11,
                               direction(75, 30), "P"))      # right atrium
        comps.append(Component(onset + 0.65 * pdur, sp, sp, 0.10,
                               direction(30, -35), "P"))     # left atrium

    if p["conduction"] == "LBBB":
        sq, s1, s2 = 0.07 * qrs, 0.12 * qrs, 0.12 * qrs
        comps.append(Component(2.5 * sq, sq, sq, 0.12,
                               direction(15, -20), "QRS"))
        comps.append(Component(0.36 * qrs, s1, s1, 0.95 * p["r_amp"],
                               direction(axis, -38), "QRS"))
        comps.append(Component(qrs - 2.5 * s2, s2, s2, 1.05 * p["r_amp"],
                               direction(axis - 10, -45), "QRS"))
        t_dir = direction(axis + 180, 35)
    else:
        sq, sr, ss = 0.08 * qrs, 0.11 * qrs, 0.085 * qrs
        comps.append(Component(2.5 * sq, sq, sq, 0.16,
                               direction(200, 45), "QRS"))   # septum
        comps.append(Component(0.47 * qrs, sr, sr, p["r_amp"],
                               direction(axis, -15), "QRS"))  # free walls
        comps.append(Component(qrs - 2.5 * ss, ss, ss, 0.25,
                               direction(250, -30), "QRS"))  # base
        t_dir = direction(axis - 5, 30)

    s_fall = 0.095 * qt
    s_rise = 1.6 * s_fall
    t_peak = qt - 2.0 * s_fall
    comps.append(Component(t_peak, s_rise, s_fall, p["t_amp"], t_dir, "T"))
    return comps


def _gauss(t, c):
    sig = np.where(t < c.centre, c.sigma_rise, c.sigma_fall)
    return np.exp(-0.5 * ((t - c.centre) / sig) ** 2)


def _plateau(t, start, end, edge=0.008):
    """Smooth step up at start and down at end (for the ST segment)."""
    up = 1.0 / (1.0 + np.exp(-(t - start) / edge))
    down = 1.0 / (1.0 + np.exp((t - end) / edge))
    return up * down


# --------------------------------------------------------------------------
# Rhythm: the times of the beats
# --------------------------------------------------------------------------

def rr_intervals(n_beats, hr_bpm, rhythm, rng, hrv=1.0, resp_hz=0.25):
    """RR intervals (s) for n_beats beats.

    Sinus rhythm: a mean interval modulated by breathing (respiratory sinus
    arrhythmia), a slow 0.1 Hz wave and a little random variation; hrv
    scales the size of this variability.
    Atrial fibrillation: irregularly irregular intervals from a gamma
    distribution with a coefficient of variation of about 0.2.
    """
    rr0 = 60.0 / hr_bpm
    if rhythm == "AF":
        shape = 1.0 / 0.2 ** 2
        rr = rng.gamma(shape, rr0 / shape, size=n_beats)
        return np.clip(rr, 0.30, 2.0)
    phase1, phase2 = rng.uniform(0, 2 * np.pi, size=2)
    t_beat = np.arange(n_beats) * rr0
    rr = rr0 * (1.0
                + hrv * 0.030 * np.sin(2 * np.pi * resp_hz * t_beat + phase1)
                + hrv * 0.020 * np.sin(2 * np.pi * 0.10 * t_beat + phase2)
                + hrv * 0.008 * rng.standard_normal(n_beats))
    return rr


# --------------------------------------------------------------------------
# The ECG object
# --------------------------------------------------------------------------

@dataclass
class ECG:
    """A synthetic 12-lead ECG with its true values.

    fs: sampling frequency (Hz)
    leads: table of the 12 leads (mV), one column per lead; the index is
        the time in seconds
    vcg: heart vector over time, an n x 3 array (mV)
    truth: true values of the intervals, the rate and the beat times
    params: the parameters that produced the ECG
    """
    fs: int
    leads: pd.DataFrame
    vcg: np.ndarray
    truth: dict
    params: dict = field(default_factory=dict)
    patient_id: str = ""

    @property
    def time(self):
        return self.leads.index.to_numpy()

    def lead(self, name):
        return self.leads[name].to_numpy()

    def __repr__(self):
        t = self.truth
        return (f"ECG(patient={self.patient_id or '-'}, fs={self.fs} Hz, "
                f"{len(self.leads) / self.fs:.1f} s, rhythm={t['rhythm']}, "
                f"HR={t['hr_bpm']:.0f} bpm)")


DEFAULTS = dict(rhythm="sinus", conduction="normal", hr_bpm=70.0,
                pr_ms=160.0, p_ms=100.0, qrs_ms=90.0, qt_ms=390.0,
                axis_deg=50.0, r_amp=1.35, t_amp=0.38, hrv=1.0,
                st_mv=0.0, st_territory="none")


def simulate(params=None, duration_s=10.0, fs=500, noise="low", seed=0,
             patient_id=""):
    """Simulate a 12-lead ECG.

    params: dictionary of parameters (see DEFAULTS); missing keys take the
        default values. qt_ms is the QT interval at the mean heart rate.
    duration_s: length of the recording (s)
    fs: sampling frequency (Hz)
    noise: "none", "low" or "clinic" (baseline wander, muscle noise and
        50 Hz mains interference of increasing size)
    seed: seed of the random numbers, so that the same call returns the
        same signal
    """
    p = dict(DEFAULTS)
    p.update(params or {})
    rng = np.random.default_rng(seed)
    n = int(round(duration_s * fs))
    t = np.arange(n) / fs

    comps = beat_components(p)
    rr_mean = 60.0 / p["hr_bpm"]
    n_beats = int(duration_s / rr_mean * 1.6) + 6
    rr = rr_intervals(n_beats, p["hr_bpm"], p["rhythm"], rng, hrv=p["hrv"])
    first = -rng.uniform(0.3, 0.9) * rr_mean
    onsets = first + np.concatenate([[0.0], np.cumsum(rr[:-1])])
    onsets = onsets[onsets < duration_s + 0.5]

    vcg = np.zeros((n, 3))
    for t0 in onsets:
        for c in comps:
            lo = int(max(0, np.floor((t0 + c.centre - 5 * c.sigma_rise) * fs)))
            hi = int(min(n, np.ceil((t0 + c.centre + 5 * c.sigma_fall) * fs)
                         + 1))
            if hi <= lo:
                continue
            seg = t[lo:hi] - t0
            vcg[lo:hi] += c.amplitude * _gauss(seg, c)[:, None] * c.direction
        if p["st_mv"] and p["st_territory"] in TERRITORY_ANGLES:
            d = direction(*TERRITORY_ANGLES[p["st_territory"]])
            j_point = p["qrs_ms"] / 1000.0
            t_end = p["qt_ms"] / 1000.0
            lo = int(max(0, np.floor((t0 + j_point - 0.05) * fs)))
            hi = int(min(n, np.ceil((t0 + t_end + 0.05) * fs) + 1))
            if hi > lo:
                seg = t[lo:hi] - t0
                vcg[lo:hi] += (p["st_mv"] * _plateau(seg, j_point, t_end)
                               )[:, None] * d

    if p["rhythm"] == "AF":
        f0 = rng.uniform(5.0, 7.0)
        wave = np.zeros(n)
        for k, a in ((1, 1.0), (2, 0.35), (3, 0.15)):
            ph = rng.uniform(0, 2 * np.pi)
            wob = rng.uniform(0, 2 * np.pi)
            wave += a * np.sin(2 * np.pi * k * f0 * t + ph
                               + 0.8 * np.sin(2 * np.pi * 0.37 * t + wob))
        vcg += 0.045 * wave[:, None] * direction(160, 50)

    signals = vcg @ LEAD_MATRIX.T
    signals = signals + _noise(n, fs, noise, rng)
    # Like an electrocardiograph, record I and II and compute III and the
    # augmented leads from them (Einthoven's and Goldberger's relations).
    lead_i, lead_ii = signals[:, 0], signals[:, 1]
    signals[:, 2] = lead_ii - lead_i              # III
    signals[:, 3] = -(lead_i + lead_ii) / 2       # aVR
    signals[:, 4] = lead_i - lead_ii / 2          # aVL
    signals[:, 5] = lead_ii - lead_i / 2          # aVF
    leads = pd.DataFrame(signals, columns=list(LEADS))
    leads.index = pd.Index(np.round(t, 6), name="time_s")

    inside = (onsets - p["pr_ms"] / 1000.0 >= 0) & \
             (onsets + p["qt_ms"] / 1000.0 <= duration_s)
    if p["rhythm"] == "AF":
        inside = (onsets >= 0) & (onsets + p["qt_ms"] / 1000.0 <= duration_s)
    full = onsets[inside]
    r_centre = 0.47 if p["conduction"] != "LBBB" else 0.5
    rr_strip = np.diff(onsets[(onsets >= 0) & (onsets <= duration_s)])
    rr_true = float(np.mean(rr_strip)) if len(rr_strip) else rr_mean
    qt_s = p["qt_ms"] / 1000.0
    truth = dict(
        rhythm=p["rhythm"], conduction=p["conduction"],
        hr_bpm=60.0 / rr_true, rr_mean_s=rr_true,
        pr_ms=p["pr_ms"] if p["rhythm"] == "sinus" else float("nan"),
        qrs_ms=p["qrs_ms"], qt_ms=p["qt_ms"],
        qtc_bazett_ms=p["qt_ms"] / np.sqrt(rr_true),
        qtc_fridericia_ms=p["qt_ms"] / np.cbrt(rr_true),
        axis_deg=p["axis_deg"],
        qrs_onsets_s=full,
        r_times_s=full + r_centre * p["qrs_ms"] / 1000.0,
        qrs_offsets_s=full + p["qrs_ms"] / 1000.0,
        t_ends_s=full + qt_s,
        p_onsets_s=(full - p["pr_ms"] / 1000.0) if p["rhythm"] == "sinus"
        else np.array([]),
        all_beats_s=onsets[(onsets >= 0) & (onsets < duration_s)]
        + r_centre * p["qrs_ms"] / 1000.0,
    )
    return ECG(fs=fs, leads=leads, vcg=vcg, truth=truth, params=p,
               patient_id=patient_id)


def _noise(n, fs, level, rng):
    if level == "none":
        return np.zeros((n, 12))
    sizes = {"low": (0.006, 0.03, 0.0), "clinic": (0.02, 0.10, 0.015)}
    emg, wander, mains = sizes.get(level, sizes["low"])
    t = np.arange(n) / fs
    out = emg * rng.standard_normal((n, 12))
    for j in range(12):
        f = rng.uniform(0.15, 0.35)
        out[:, j] += wander * np.sin(2 * np.pi * f * t + rng.uniform(0, 6.3))
        if mains:
            out[:, j] += mains * np.sin(2 * np.pi * 50.0 * t
                                        + rng.uniform(0, 6.3))
    return out


def lead_ii_long(params=None, duration_s=300.0, fs=250, noise="low", seed=0):
    """Long single-lead (II) recording for heart rate variability.

    Returns (time, signal, truth) without building all 12 leads.
    """
    ecg = simulate(params, duration_s=duration_s, fs=fs, noise="none",
                   seed=seed)
    sig = ecg.lead("II")
    rng = np.random.default_rng(seed + 1)
    if noise != "none":
        sig = sig + _noise(len(sig), fs, noise, rng)[:, 1]
    return ecg.time, sig, ecg.truth
