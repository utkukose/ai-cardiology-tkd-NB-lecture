"""A 24-hour Holter recording of the virtual clinic.

recording() returns the beats of a synthetic 24-hour recording: the time of
every beat, its RR interval and its kind (sinus, premature atrial beat or
atrial fibrillation). The heart rate follows the time of day, an hour of
walking raises it, premature atrial beats come and go, and episodes of
paroxysmal atrial fibrillation (AF) start and stop at known times. Because
the truth is known, an AF detector that reads the RR intervals in windows
can be judged beat by beat and minute by minute. strip() draws a short
segment of the recording as one ECG lead (lead II).

The data are synthetic teaching material and are not for clinical use.
"""

import numpy as np

from .ecg import (DEFAULTS, LEADS, LEAD_MATRIX, beat_components, direction,
                  _gauss, _noise)

# Episodes of AF: (clock time of the start in hours, duration in minutes,
# mean heart rate during the episode in beats per minute, coefficient of
# variation of the RR intervals)
EPISODES = ((2 + 10 / 60, 45, 104, 0.20), (13 + 20 / 60, 165, 118, 0.15),
            (21 + 40 / 60, 12, 126, 0.24))
# Hour of walking: (start, end) in clock hours
WALK = (9.5, 10.5)
# Premature atrial beats per hour: a low rate, and a busy hour in the evening
PAC_PER_HOUR = 6
PAC_BUSY = ((18.0, 19.0), 150)
# Periods of electrode noise (clock hours), in which the beat detector of the
# recorder misses some beats and finds some that are not there
NOISY = ((7.0, 7.4), (23.5, 23.6))
MISS, EXTRA = 0.10, 0.08

PATIENT = dict(patient_id="VC-0128", start_clock=8.0, hours=24.0)


def _clock(t_s, start_clock):
    return (start_clock + t_s / 3600.0) % 24.0


def _heart_rate(clock_h):
    """Sinus heart rate (beats per minute) at a clock time.

    About 55 per minute at 4 a.m. and about 73 at 4 p.m., with 30 more
    during the hour of walking.
    """
    hr = 64.0 + 9.0 * np.cos(2 * np.pi * (clock_h - 16.0) / 24.0)
    w0, w1 = WALK
    ramp = np.clip((clock_h - w0) * 12, 0, 1) * np.clip((w1 - clock_h) * 12, 0, 1)
    return hr + 30.0 * ramp


def _in_episode(clock_h):
    """Index of the AF episode at a clock time, or -1."""
    for k, (c0, minutes, _, _) in enumerate(EPISODES):
        c1 = c0 + minutes / 60.0
        if c0 <= clock_h < c1:
            return k
    return -1


def recording(hours=PATIENT["hours"], start_clock=PATIENT["start_clock"], seed=2026):
    """Beats of the 24-hour recording.

    Returns a dictionary:
        beat_s: time of each beat from the start of the recording (s)
        rr_s: RR interval that ends at each beat (s); the first is the
            interval before the recording started
        kind: "N" sinus beat, "A" premature atrial beat, "F" beat in AF
        episodes: list of (start_s, end_s) of the AF episodes
        detected_s: times of the beats found by the beat detector of the
            recorder, with misses and false beats in the periods of noise
        noisy: list of (start_s, end_s) of the periods of noise
        start_clock: clock time of the start (hours)
        hours: length of the recording (hours)
    """
    rng = np.random.default_rng(seed)
    total = hours * 3600.0
    t = 0.0
    beats, rrs, kinds = [], [], []
    phase1, phase2 = rng.uniform(0, 2 * np.pi, size=2)
    pending_pause = 0.0
    while t < total:
        clock = _clock(t, start_clock)
        ep = _in_episode(clock)
        if ep >= 0:
            mean_rr = 60.0 / EPISODES[ep][2]
            shape = 1.0 / EPISODES[ep][3] ** 2
            rr = float(np.clip(rng.gamma(shape, mean_rr / shape), 0.30, 1.6))
            kind = "F"
            pending_pause = 0.0
        else:
            rr0 = 60.0 / _heart_rate(clock)
            rr = rr0 * (1.0 + 0.030 * np.sin(2 * np.pi * 0.25 * t + phase1)
                        + 0.020 * np.sin(2 * np.pi * 0.10 * t + phase2)
                        + 0.008 * rng.standard_normal())
            kind = "N"
            if pending_pause:
                rr = pending_pause
                pending_pause = 0.0
            else:
                busy = PAC_BUSY[0][0] <= clock < PAC_BUSY[0][1]
                per_hour = PAC_BUSY[1] if busy else PAC_PER_HOUR
                if rng.uniform() < per_hour * rr0 / 3600.0:
                    rr = rr0 * rng.uniform(0.60, 0.75)
                    kind = "A"
                    pending_pause = rr0 * rng.uniform(1.08, 1.18)
        t += rr
        if t >= total:
            break
        beats.append(t)
        rrs.append(rr)
        kinds.append(kind)
    beat_s = np.array(beats)
    kind = np.array(kinds)
    episodes = []
    is_f = kind == "F"
    edges = np.flatnonzero(np.diff(np.r_[0, is_f.astype(int), 0]))
    rr_arr = np.array(rrs)
    for a, b in zip(edges[::2], edges[1::2]):
        episodes.append((float(beat_s[a] - rr_arr[a]), float(beat_s[b - 1])))
    noisy = []
    for c0, c1 in NOISY:
        a = ((c0 - start_clock) % 24.0) * 3600.0
        noisy.append((a, a + (c1 - c0) * 3600.0))
    in_noise = np.zeros(len(beat_s), dtype=bool)
    for a, b in noisy:
        in_noise |= (beat_s >= a) & (beat_s < b)
    keep = ~(in_noise & (rng.uniform(size=len(beat_s)) < MISS))
    extra = in_noise & (rng.uniform(size=len(beat_s)) < EXTRA)
    false_beats = beat_s[extra] - rr_arr[extra] * rng.uniform(0.3, 0.7, size=int(extra.sum()))
    detected = np.sort(np.r_[beat_s[keep], false_beats])
    return dict(beat_s=beat_s, rr_s=rr_arr, kind=kind, episodes=episodes,
                detected_s=detected, noisy=noisy,
                start_clock=start_clock, hours=hours)


def af_seconds(rec, start_s, end_s):
    """Seconds of AF between start_s and end_s (the truth)."""
    total = 0.0
    for a, b in rec["episodes"]:
        total += max(0.0, min(b, end_s) - max(a, start_s))
    return total


def burden(rec):
    """True AF burden: the share of the recording spent in AF."""
    return af_seconds(rec, 0.0, rec["hours"] * 3600.0) / (rec["hours"] * 3600.0)


def clock_text(t_s, start_clock=PATIENT["start_clock"]):
    """Clock time of a moment of the recording, as hh:mm."""
    c = _clock(t_s, start_clock)
    h = int(c)
    m = int(round((c - h) * 60))
    if m == 60:
        h, m = (h + 1) % 24, 0
    return f"{h:02d}:{m:02d}"


def strip(rec, start_s, duration_s=10.0, fs=250, noise="low", seed=0):
    """Lead II of the recording between start_s and start_s + duration_s.

    The beats are placed at the times of the recording. Sinus and premature
    beats have P waves; beats in AF have none, and fibrillatory waves are
    added during AF. In the periods of electrode noise, bursts of muscle
    noise and jumps of the baseline are added as well. Returns (time in s
    from start_s, lead II in mV).
    """
    p = dict(DEFAULTS)
    p.update(hr_bpm=75.0)
    n = int(round(duration_s * fs))
    tt = np.arange(n) / fs
    sinus = beat_components(dict(p, rhythm="sinus"))
    af = beat_components(dict(p, rhythm="AF"))
    r_centre = 0.47 * p["qrs_ms"] / 1000.0
    vcg = np.zeros((n, 3))
    sel = (rec["beat_s"] > start_s - 1.0) & (rec["beat_s"] < start_s + duration_s + 1.0)
    for t_r, kind in zip(rec["beat_s"][sel], rec["kind"][sel]):
        onset = t_r - start_s - r_centre
        comps = af if kind == "F" else sinus
        for c in comps:
            lo = int(max(0, np.floor((onset + c.centre - 5 * c.sigma_rise) * fs)))
            hi = int(min(n, np.ceil((onset + c.centre + 5 * c.sigma_fall) * fs) + 1))
            if hi <= lo:
                continue
            seg = tt[lo:hi] - onset
            vcg[lo:hi] += c.amplitude * _gauss(seg, c)[:, None] * c.direction
    rng = np.random.default_rng(seed)
    in_af = np.zeros(n, dtype=bool)
    for a, b in rec["episodes"]:
        in_af |= (tt + start_s >= a) & (tt + start_s < b)
    if in_af.any():
        f0 = rng.uniform(5.0, 7.0)
        wave = np.zeros(n)
        for k, amp in ((1, 1.0), (2, 0.35), (3, 0.15)):
            wave += amp * np.sin(2 * np.pi * k * f0 * tt + rng.uniform(0, 2 * np.pi))
        vcg += (0.045 * wave * in_af)[:, None] * direction(160, 50)
    leads = vcg @ LEAD_MATRIX.T + _noise(n, fs, noise, rng)
    lead = leads[:, LEADS.index("II")]
    for a, b in rec.get("noisy", []):
        inside = (tt + start_s >= a) & (tt + start_s < b)
        if inside.any():
            burst = np.convolve(rng.standard_normal(n), np.ones(5) / 5, mode="same") * 0.35
            steps = np.cumsum(rng.standard_normal(n) * 0.03)
            lead = lead + inside * (burst + steps - steps[inside].mean())
    return tt, lead
