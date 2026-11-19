"""The chest pain unit of the virtual clinic (from Week 8).

presentations() returns one row per presentation with chest pain: what the
triage team knows at arrival and what happened in the next 30 days. Each
presentation has
- the patient: age, sex, risk factors, known coronary artery disease, heart
  rate, systolic blood pressure and eGFR;
- the triage note, a few sentences in Turkish and in English on the pain;
- the 12-lead ECG at arrival, as parameters of vclinic.ecg (ecg() draws the
  signal), and its reading;
- high-sensitivity cardiac troponin at arrival and after one hour (the second
  value is missing for some patients);
- a bedside echocardiogram for some patients: the ejection fraction and
  whether a regional wall motion abnormality is seen;
- the HEART score, the true diagnosis and major adverse cardiac events (MACE)
  within 30 days: an index myocardial infarction, an urgent
  revascularisation or death.

Hospital A is the chest pain unit of the course, with the sets training,
validation and test. Hospital B is another hospital: Its patients are older and
sicker, it measures troponin I with another assay, its notes are short, and it
sends more patients with angina to an urgent revascularisation.
Every value comes from its own stream of random numbers, so a presentation
keeps its values when the table is made larger.

The data are synthetic teaching material and are not for clinical use.
"""

import numpy as np
import pandas as pd

from .cohort import DEFAULT_SEED, _ckd_epi_2021, _logistic, _stream
from .ecg import simulate

DIAGNOSES = ("non-cardiac", "stable angina", "unstable angina", "NSTEMI", "STEMI")
# upper reference limit (99th percentile) of the two troponin assays, ng/L
ASSAYS = {"A": ("hs-cTnT", 14.0), "B": ("hs-cTnI", 26.0)}
SIZES = {"A": 4000, "B": 1000}
SETS_A = (("training", 2400), ("validation", 800), ("test", 800))

# features of the history: (name, probability by diagnosis in the order of DIAGNOSES)
HISTORY = {
    "pressure":  (0.32, 0.62, 0.60, 0.62, 0.66),   # pressing, tight or heavy pain
    "radiation": (0.18, 0.35, 0.40, 0.45, 0.50),   # to the left arm, both arms or the jaw
    "exertion":  (0.15, 0.65, 0.45, 0.28, 0.22),   # started or worsens on exertion
    "sweating":  (0.10, 0.12, 0.25, 0.35, 0.50),
    "nausea":    (0.12, 0.10, 0.18, 0.25, 0.32),
    "sharp":     (0.38, 0.15, 0.14, 0.12, 0.10),   # sharp or stabbing pain
    "pleuritic": (0.20, 0.05, 0.06, 0.06, 0.05),   # worse on breathing
    "positional": (0.16, 0.05, 0.05, 0.05, 0.04),  # changes with position
    "palpation": (0.20, 0.04, 0.05, 0.05, 0.04),   # reproduced by pressing on the chest wall
}
TYPICAL = ("pressure", "radiation", "exertion", "sweating", "nausea")
ATYPICAL = ("sharp", "pleuritic", "positional", "palpation")


def _s(seed, hospital, name):
    return _stream(seed, f"triage:{hospital}:{name}")


def history_score(row):
    """The History item of HEART from the features of the pain: 2 highly suspicious, 1 moderately, 0 slightly."""
    typical = sum(int(row[f"hx_{k}"]) for k in TYPICAL)
    atypical = sum(int(row[f"hx_{k}"]) for k in ATYPICAL)
    if typical >= 3 and atypical == 0:
        return 2
    if typical <= 1 and atypical >= 1:
        return 0
    return 1


def _mentions(row, rng):
    """The features that the triage note mentions, in the order of the note: a present feature is usually written
    down, an absent one sometimes as absent."""
    parts = []
    for k in HISTORY:
        u = rng.uniform()
        if row[f"hx_{k}"]:
            if u < 0.88:
                parts.append((k, 0))
        elif u < 0.35:
            parts.append((k, 1))
    rng.shuffle(parts)
    return parts


def _note(row, parts, lang, short):
    """The triage note in one language: the same mentions in English and in Turkish."""
    h = int(row["hours"])
    if lang == "en":
        sex = "man" if row["sex"] == "M" else "woman"
        words = dict(pressure=("The pain is pressing.", "The pain is not pressing."),
                     radiation=("It radiates to the left arm.", "It does not radiate."),
                     exertion=("It started on exertion.", "It started at rest."),
                     sweating=("Sweating is present.", "No sweating."),
                     nausea=("Nausea is present.", "No nausea."),
                     sharp=("The pain is sharp.", "The pain is not sharp."),
                     pleuritic=("It worsens on breathing.", "It does not change with breathing."),
                     positional=("It changes with position.", "It does not change with position."),
                     palpation=("Pressing on the chest wall reproduces it.", "It is not reproduced on palpation."))
        article = "An" if str(row["age"]).startswith("8") or row["age"] in (11, 18) else "A"
        head = (f"Chest pain {h} h. " if short else f"{article} {row['age']}-year-old {sex} with chest pain for {h} hour{'' if h == 1 else 's'}. ")
        if short:
            words = dict(pressure=("Pressing.", "Not pressing."), radiation=("Radiation to L arm +.", "No radiation."),
                         exertion=("Onset on exertion.", "Onset at rest."), sweating=("Sweating +.", "No sweating."),
                         nausea=("Nausea +.", "No nausea."), sharp=("Sharp.", "Not sharp."),
                         pleuritic=("Worse on breathing.", "No change with breathing."), positional=("Positional.", "Not positional."),
                         palpation=("Tender on palpation.", "Not tender on palpation."))
    else:
        sex = "erkek" if row["sex"] == "M" else "kadın"
        words = dict(pressure=("Ağrı baskı tarzındadır.", "Ağrı baskı tarzında değildir."),
                     radiation=("Ağrı sol kola yayılmaktadır.", "Ağrı yayılmamaktadır."),
                     exertion=("Ağrı eforla başlamıştır.", "Ağrı istirahatte başlamıştır."),
                     sweating=("Terleme vardır.", "Terleme yoktur."),
                     nausea=("Bulantı vardır.", "Bulantı yoktur."),
                     sharp=("Ağrı batıcı niteliktedir.", "Ağrı batıcı değildir."),
                     pleuritic=("Ağrı solunumla artmaktadır.", "Ağrı solunumla değişmemektedir."),
                     positional=("Ağrı pozisyonla değişmektedir.", "Ağrı pozisyonla değişmemektedir."),
                     palpation=("Göğüs duvarına basmakla ağrı oluşmaktadır.", "Palpasyonla ağrı oluşmamaktadır."))
        head = (f"{h} saattir göğüs ağrısı. " if short else f"{row['age']} yaşında {sex} hasta, {h} saattir göğüs ağrısı tarif etmektedir. ")
        if short:
            words = dict(pressure=("Baskı tarzı.", "Baskı tarzı değil."), radiation=("Sol kola yayılım +.", "Yayılım yok."),
                         exertion=("Eforla başlamış.", "İstirahatte başlamış."), sweating=("Terleme +.", "Terleme yok."),
                         nausea=("Bulantı +.", "Bulantı yok."), sharp=("Batıcı.", "Batıcı değil."),
                         pleuritic=("Solunumla artıyor.", "Solunumla değişmiyor."), positional=("Pozisyonla değişiyor.", "Pozisyonla değişmiyor."),
                         palpation=("Palpasyonla ağrı +.", "Palpasyonla ağrı yok."))
    return head + " ".join(words[k][i] for k, i in parts)


def presentations(hospital="A", n=None, seed=DEFAULT_SEED):
    """The presentations with chest pain of hospital A (the course) or B (another hospital), one row each."""
    n = n or SIZES[hospital]
    s = lambda name: _s(seed, hospital, name)
    b = hospital == "B"
    pre = "CP" if hospital == "A" else "CPB"
    df = pd.DataFrame({"patient_id": [f"{pre}-{i:04d}" for i in range(1, n + 1)], "hospital": hospital})
    if hospital == "A":
        df["set"] = np.concatenate([[name] * k for name, k in SETS_A])[:n] if n == SIZES["A"] else \
            np.where(np.arange(n) < 0.6 * n, "training", np.where(np.arange(n) < 0.8 * n, "validation", "test"))
    else:
        df["set"] = "external"

    # the patient
    age = 25 + 65 * s("age").beta(2.4 + 0.6 * b, 2.2, size=n)
    male = s("sex").uniform(size=n) < 0.58
    a10 = (age - 60) / 10
    df["age"] = np.round(age).astype(int)
    df["sex"] = np.where(male, "M", "F")
    smoker = s("smoker").uniform(size=n) < np.where(male, 0.32, 0.18) * np.where(age > 70, 0.6, 1.0)
    diabetes = s("diabetes").uniform(size=n) < _logistic(-1.55 + 0.40 * a10 + 0.45 * b)
    htn = s("hypertension").uniform(size=n) < _logistic(0.05 + 0.60 * a10)
    lipid = s("lipid").uniform(size=n) < _logistic(-0.55 + 0.30 * a10)
    obese = s("obese").uniform(size=n) < 0.24
    fam = s("family").uniform(size=n) < 0.18
    known = s("known_cad").uniform(size=n) < _logistic(-2.25 + 0.50 * a10 + 0.60 * male + 0.50 * diabetes + 0.30 * b)
    creat = np.exp(s("creatinine").normal(np.log(np.where(male, 0.95, 0.78)) + 0.06 * np.clip(a10, 0, None)
                                          + 0.10 * diabetes + 0.12 * b, 0.20, n))
    df["egfr"] = np.round(_ckd_epi_2021(creat, df["age"].to_numpy(), ~male)).astype(int)
    for k, v in (("smoker", smoker), ("diabetes", diabetes), ("hypertension", htn), ("hyperlipidaemia", lipid),
                 ("obesity", obese), ("family_history", fam), ("known_cad", known)):
        df[k] = v.astype(int)

    # the true diagnosis
    lp = (-2.55 + 0.45 * a10 + 0.55 * male + 0.45 * smoker + 0.45 * diabetes + 0.30 * htn + 0.35 * lipid
          + 0.30 * fam + 0.85 * known + 0.25 * b)
    acs = s("acs").uniform(size=n) < _logistic(lp)
    u = s("acs_type").uniform(size=n)
    stable = (~acs) & (s("stable").uniform(size=n) < _logistic(lp - 0.6))
    diag = np.full(n, "non-cardiac", dtype=object)
    diag[stable] = "stable angina"
    diag[acs & (u < 0.25)] = "unstable angina"
    diag[acs & (u >= 0.25) & (u < 0.75)] = "NSTEMI"
    diag[acs & (u >= 0.75)] = "STEMI"
    df["diagnosis"] = diag
    k = np.array([DIAGNOSES.index(d) for d in diag])
    mi = (diag == "NSTEMI") | (diag == "STEMI")

    # the history and the note
    for name, probs in HISTORY.items():
        df[f"hx_{name}"] = (s(f"hx:{name}").uniform(size=n) < np.array(probs)[k]).astype(int)
    df["hours"] = np.clip(np.round(np.exp(s("hours").normal(np.log(3.0), 0.8, n))), 1, 24).astype(int)
    rng_note = s("note")
    rows = df.to_dict("records")
    mentions = [_mentions(r, rng_note) for r in rows]
    df["note_en"] = [_note(r, m, "en", b) for r, m in zip(rows, mentions)]
    df["note_tr"] = [_note(r, m, "tr", b) for r, m in zip(rows, mentions)]

    # heart rate and blood pressure
    df["heart_rate"] = np.round(np.clip(s("hr").normal(80, 14, n) + 8 * mi + 6 * (diag == "STEMI"), 45, 150)).astype(int)
    df["sbp"] = np.round(np.clip(s("sbp").normal(138, 20, n) + 8 * htn - 6 * (diag == "STEMI"), 85, 220)).astype(int)

    # the ECG at arrival
    lbbb = s("lbbb").uniform(size=n) < (0.02 + 0.04 * known + 0.02 * b)
    lvh = (~lbbb) & (s("lvh").uniform(size=n) < 0.03 + 0.06 * htn)
    af = s("af").uniform(size=n) < _logistic(-3.3 + 0.7 * a10)
    st_mv = np.zeros(n)
    territory = np.full(n, "none", dtype=object)
    t_amp = np.clip(s("t_amp").normal(0.36, 0.06, n), 0.2, 0.5)
    v = s("ecg_kind").uniform(size=n)
    stemi = diag == "STEMI"
    w = s("territory").uniform(size=n)
    territory[stemi & (w < 0.45)] = "anterior"
    territory[stemi & (w >= 0.45) & (w < 0.85)] = "inferior"
    territory[stemi & (w >= 0.85)] = "lateral"
    st_mv[stemi] = s("st_elev").uniform(0.15, 0.40, n)[stemi]
    p_dep = np.select([diag == "NSTEMI", diag == "unstable angina", diag == "stable angina"], [0.38, 0.22, 0.05], 0.03)
    p_tinv = np.select([diag == "NSTEMI", diag == "unstable angina", diag == "stable angina"], [0.18, 0.15, 0.10], 0.10)
    dep = (~stemi) & (~lbbb) & (v < p_dep)
    tinv = (~stemi) & (~dep) & (v >= p_dep) & (v < p_dep + p_tinv)
    territory[dep] = "subendocardial"
    st_mv[dep] = -s("st_dep").uniform(0.06, 0.20, n)[dep]
    t_amp = np.where(tinv | lvh, -np.abs(t_amp) * np.where(lvh, 0.8, 0.7), t_amp)
    reading = np.full(n, "normal", dtype=object)
    reading[lvh] = "LVH with repolarisation changes"
    reading[tinv] = "T-wave inversion"
    reading[lbbb] = "LBBB"
    reading[dep] = "ST depression"
    reading[stemi] = "ST elevation"
    df["ecg_rhythm"] = np.where(af, "AF", "sinus")
    df["ecg_conduction"] = np.where(lbbb, "LBBB", "normal")
    df["ecg_r_amp"] = np.round(np.where(lvh, 2.4, s("r_amp").normal(1.3, 0.15, n)), 2)
    df["ecg_t_amp"] = np.round(t_amp, 2)
    df["ecg_st_mv"] = np.round(st_mv, 2)
    df["ecg_st_territory"] = territory
    df["ecg_qrs"] = np.round(np.where(lbbb, s("qrs_lbbb").normal(148, 10, n), s("qrs").normal(90, 8, n))).astype(int)
    df["ecg_qt"] = np.round(np.clip(400 + s("qt").normal(0, 18, n) - 0.9 * (df["heart_rate"] - 70) + 20 * lbbb, 300, 520)).astype(int)
    df["ecg_axis"] = np.round(np.where(lbbb, s("axis_lbbb").normal(-20, 25, n), s("axis").normal(50, 22, n))).astype(int)
    df["ecg_reading"] = reading
    # the ECG item of HEART: 2 significant ST deviation, 1 non-specific repolarisation (LBBB, LVH, T inversion), 0 normal
    df["heart_e"] = np.select([stemi | dep, lbbb | lvh | tinv], [2, 1], 0)

    # troponin at arrival and after one hour
    assay, url = ASSAYS[hospital]
    base = (5.5 * np.exp(0.025 * (age - 50)) * np.where(df["egfr"] < 60, 2.0, 1.0) * np.where(known, 1.3, 1.0)
            * np.exp(s("trop_base").normal(0, 0.60, n)))
    # acute injury without a coronary event (myopericarditis, pulmonary embolism, tachyarrhythmia, sepsis)
    injury = (~mi) & (s("injury").uniform(size=n) < 0.08 + 0.06 * (age > 70))
    base = base + np.where(injury, np.exp(s("injury_size").normal(np.log(50), 0.9, n)), 0.0)
    onset = df["hours"].to_numpy() + s("onset").uniform(0, 1, n)
    size = np.exp(s("trop_size").normal(np.log(np.where(stemi, 600, 140)), 1.1, n))
    rise = lambda t: np.where(mi, size * (1 - np.exp(-t / 6.0)), 0.0)
    noise0, noise1 = np.exp(s("trop_noise0").normal(0, 0.06, n)), np.exp(s("trop_noise1").normal(0, 0.06, n))
    factor = 1.0 if hospital == "A" else url / ASSAYS["A"][1] * 1.15
    t0 = (base + rise(onset)) * noise0 * factor
    t1 = (base + rise(onset + 1)) * noise1 * factor
    missing_1h = s("trop_missing").uniform(size=n) < np.where(stemi, 0.80, 0.30)
    df["troponin_assay"] = assay
    df["troponin_url"] = url
    df["troponin_0h"] = np.round(np.clip(t0, 2, 50000), 1)
    df["troponin_1h"] = np.where(missing_1h, np.nan, np.round(np.clip(t1, 2, 50000), 1))
    df["heart_t"] = np.select([df["troponin_0h"] > 3 * url, df["troponin_0h"] > url], [2, 1], 0)

    # the bedside echocardiogram, done more often in sicker patients
    done = s("echo_done").uniform(size=n) < _logistic(-0.45 + 0.8 * (df["heart_e"] > 0) + 0.6 * known + 0.3 * a10
                                                      + 0.8 * (df["troponin_0h"] > url))
    ef = np.where(known, s("ef_known").normal(50, 9, n), s("ef").normal(60, 6, n))
    ef = np.where(stemi, ef - s("ef_stemi").uniform(5, 15, n), np.where(diag == "NSTEMI", ef - s("ef_nstemi").uniform(0, 8, n), ef))
    p_rwma = np.select([stemi, diag == "NSTEMI", diag == "unstable angina", known], [0.85, 0.60, 0.20, 0.40], np.where(diag == "stable angina", 0.10, 0.03))
    rwma = s("rwma").uniform(size=n) < p_rwma
    df["echo_done"] = done.astype(int)
    df["lvef"] = np.where(done, np.round(np.clip(ef, 15, 75)), np.nan)
    df["rwma"] = np.where(done, rwma.astype(float), np.nan)

    # the other items of HEART
    df["heart_h"] = [history_score(r) for r in df.to_dict("records")]
    df["heart_a"] = np.select([age >= 65, age >= 45], [2, 1], 0)
    count = smoker.astype(int) + diabetes + htn + lipid + obese + fam
    df["heart_r"] = np.select([known | (count >= 3), count >= 1], [2, 1], 0)
    df["heart"] = df[["heart_h", "heart_e", "heart_a", "heart_r", "heart_t"]].sum(axis=1)

    # major adverse cardiac events within 30 days
    # hospital B follows a more invasive strategy in angina
    revasc = np.select([stemi, diag == "NSTEMI", diag == "unstable angina", diag == "stable angina"],
                       [0.92, 0.65, 0.45 + 0.20 * b, 0.14 + 0.16 * b], 0.005 + 0.015 * known)
    revasc = s("revasc").uniform(size=n) < revasc
    death = s("death").uniform(size=n) < _logistic(-6.2 + 0.8 * a10 + 1.8 * mi + 0.6 * (df["egfr"] < 45) + 0.4 * known)
    df["mace30"] = (mi | revasc | death).astype(int)
    df["mace_type"] = np.select([mi, revasc, death], ["myocardial infarction", "revascularisation", "death"], "none")
    return df


def ecg(row, duration_s=10.0, fs=500, noise="low"):
    """The 12-lead ECG at arrival of one presentation (a row of presentations())."""
    params = dict(rhythm=row["ecg_rhythm"], conduction=row["ecg_conduction"], hr_bpm=float(row["heart_rate"]),
                  qrs_ms=float(row["ecg_qrs"]), qt_ms=float(row["ecg_qt"]), axis_deg=float(row["ecg_axis"]),
                  r_amp=float(row["ecg_r_amp"]), t_amp=float(row["ecg_t_amp"]), st_mv=float(row["ecg_st_mv"]),
                  st_territory=row["ecg_st_territory"])
    number = int(str(row["patient_id"]).split("-")[1]) + (100000 if row["hospital"] == "B" else 0)
    return simulate(params, duration_s=duration_s, fs=fs, noise=noise, seed=number, patient_id=row["patient_id"])


def ecg_array(table, fs=100, duration_s=10.0):
    """The ECGs of a table as an array of n x 12 x (fs x duration) samples in mV, drawn at 500 Hz and downsampled."""
    step = 500 // fs
    out = np.zeros((len(table), 12, int(fs * duration_s)), dtype=np.float32)
    for i, r in enumerate(table.to_dict("records")):
        out[i] = ecg(r, duration_s=duration_s).leads.to_numpy().T[:, ::step][:, :out.shape[2]]
    return out
