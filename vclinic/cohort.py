"""The patient registry of the virtual cardiology clinic.

make_cohort() returns a table of synthetic patients. The values of each
variable come from their own stream of random numbers, so a patient keeps
the same values when the cohort is made larger and when new variables are
added in later weeks. Every patient also carries the parameters of a 12-lead
electrocardiogram (ECG), and patient_ecg() turns them into a signal.

The relations between the variables follow broad clinical patterns (older
age, smoking or diabetes raise the chance of coronary artery disease, heart
failure raises N-terminal pro-B-type natriuretic peptide, and so on). The
exact coefficients are set by the course and are documented in TRUE_EFFECTS,
so that later weeks can compare what a model learns with the known truth.

The data are synthetic teaching material and are not for clinical use.
"""

import zlib

import numpy as np
import pandas as pd

from .ecg import simulate

DEFAULT_SEED = 2026

# True log-odds effects used to generate angiographic coronary artery
# disease (CAD). Week 2 fits a model to the data and Week 9 compares its
# explanations with these values.
TRUE_EFFECTS = {
    "intercept": -1.15,
    "age_per_10y": 0.55,
    "male": 0.90,
    "smoker": 0.60,
    "diabetes": 0.50,
    "hypertension": 0.40,
    "ldl_per_40": 0.45,
    "hdl_per_15": -0.35,
    "family_history": 0.40,
}

MAIN_DIAGNOSES = ("none", "CCS", "ACS", "HFrEF", "HFpEF")


def _stream(seed, name):
    return np.random.default_rng([seed, zlib.crc32(name.encode("utf-8"))])


def _logistic(x):
    return 1.0 / (1.0 + np.exp(-x))


def _ckd_epi_2021(creatinine, age, female):
    """Estimated glomerular filtration rate, CKD-EPI 2021 (race-free)."""
    kappa = np.where(female, 0.7, 0.9)
    alpha = np.where(female, -0.241, -0.302)
    ratio = creatinine / kappa
    egfr = (142.0 * np.minimum(ratio, 1.0) ** alpha
            * np.maximum(ratio, 1.0) ** -1.200 * 0.9938 ** age
            * np.where(female, 1.012, 1.0))
    return egfr


def make_cohort(n=500, seed=DEFAULT_SEED):
    """Synthetic patient registry with n patients (one row per patient)."""
    s = lambda name: _stream(seed, name)
    idx = np.arange(1, n + 1)
    df = pd.DataFrame({"patient_id": [f"VC-{i:04d}" for i in idx]})

    age = 30 + 60 * s("age").beta(2.6, 2.0, size=n)
    male = s("sex").uniform(size=n) < 0.56
    df["age"] = np.round(age).astype(int)
    df["sex"] = np.where(male, "M", "F")
    height = np.where(male, s("height").normal(174, 7, n),
                      s("height_f").normal(161, 6.5, n))
    bmi = np.clip(s("bmi").normal(28.0, 4.5, n), 17, 48)
    df["height_cm"] = np.round(height, 0)
    df["weight_kg"] = np.round(bmi * (height / 100) ** 2, 1)
    df["bmi"] = np.round(df["weight_kg"] / (df["height_cm"] / 100) ** 2, 1)

    a10 = (df["age"].to_numpy() - 60) / 10.0
    p_smk = np.where(male, 0.38, 0.18) * np.where(df["age"] > 70, 0.6, 1.0)
    smoker = s("smoker").uniform(size=n) < p_smk
    diabetes = s("diabetes").uniform(size=n) < _logistic(
        -1.35 + 0.35 * a10 + 0.08 * (bmi - 28))
    htn = s("hypertension").uniform(size=n) < _logistic(
        0.10 + 0.60 * a10 + 0.09 * (bmi - 28))
    fam = s("family_history").uniform(size=n) < 0.20
    df["smoker"] = smoker.astype(int)
    df["diabetes"] = diabetes.astype(int)
    df["hypertension"] = htn.astype(int)
    df["family_history"] = fam.astype(int)

    df["sbp"] = np.round(np.clip(128 + 4.5 * a10 + 14 * htn + 0.6 * (bmi - 28)
                                 + s("sbp").normal(0, 13, n), 90, 210))
    df["dbp"] = np.round(np.clip(78 + 1.5 * a10 + 6 * htn
                                 + s("dbp").normal(0, 8, n), 50, 120))

    ldl = np.clip(s("ldl").normal(128, 36, n), 40, 260)
    hdl = np.clip(np.where(male, s("hdl").normal(44, 10, n),
                           s("hdl_f").normal(53, 12, n)), 20, 100)
    tg = np.clip(np.exp(s("tg").normal(np.log(140), 0.45, n)), 40, 600)
    df["ldl"] = np.round(ldl)
    df["hdl"] = np.round(hdl)
    df["triglycerides"] = np.round(tg)
    df["total_chol"] = np.round(ldl + hdl + tg / 5.0)

    creat = np.exp(s("creatinine").normal(
        np.log(np.where(male, 0.95, 0.78)) + 0.06 * np.clip(a10, 0, None)
        + 0.10 * diabetes, 0.18, n))
    df["creatinine"] = np.round(creat, 2)
    df["egfr"] = np.round(_ckd_epi_2021(df["creatinine"].to_numpy(),
                                        df["age"].to_numpy(), ~male), 0)

    e = TRUE_EFFECTS
    lp_cad = (e["intercept"] + e["age_per_10y"] * a10 + e["male"] * male
              + e["smoker"] * smoker + e["diabetes"] * diabetes
              + e["hypertension"] * htn + e["ldl_per_40"] * (ldl - 130) / 40
              + e["hdl_per_15"] * (hdl - 50) / 15
              + e["family_history"] * fam)
    cad = s("cad").uniform(size=n) < _logistic(lp_cad)
    acs = cad & (s("acs").uniform(size=n) < 0.12)
    hfref = s("hfref").uniform(size=n) < _logistic(
        -3.6 + 1.5 * cad + 0.30 * a10 + 0.5 * male)
    hfpef = (~hfref) & (s("hfpef").uniform(size=n) < _logistic(
        -3.5 + 0.60 * a10 + 0.6 * (~male) + 0.6 * htn
        + 0.08 * (bmi - 28) + 0.5 * diabetes))
    hf = hfref | hfpef
    af = s("af").uniform(size=n) < _logistic(
        -3.4 + 0.75 * a10 + 1.0 * hf + 0.4 * htn + 0.3 * male
        + 0.05 * (bmi - 28))
    df["cad"] = cad.astype(int)
    df["af"] = af.astype(int)

    diag = np.full(n, "none", dtype=object)
    diag[cad] = "CCS"
    diag[hfpef] = "HFpEF"
    diag[hfref] = "HFrEF"
    diag[acs] = "ACS"
    df["main_diagnosis"] = diag

    ef = np.clip(s("ef").normal(62, 5, n), 52, 75)
    ef = np.where(cad & ~hfref, np.clip(s("ef_cad").normal(55, 6, n), 42, 70),
                  ef)
    ef = np.where(hfpef, np.clip(s("ef_hfpef").normal(58, 5, n), 50, 70), ef)
    ef = np.where(hfref, np.clip(s("ef_hfref").normal(30, 6, n), 15, 39), ef)
    df["lvef"] = np.round(ef)

    renal = np.where(df["egfr"] < 60, 1.8, 1.0)
    nt = (80 * np.exp(0.035 * (df["age"] - 50)) * renal
          * np.where(hfref, 25.0, np.where(hfpef, 9.0, 1.0))
          * np.where(af, 3.0, 1.0)
          * np.exp(s("ntprobnp").normal(0, 0.6, n)))
    df["ntprobnp"] = np.round(np.clip(nt, 10, 35000))
    trop = (6 * np.exp(0.02 * (df["age"] - 50))
            * np.where(df["egfr"] < 60, 1.6, 1.0) * np.where(hf, 1.8, 1.0)
            * np.exp(s("troponin").normal(0, 0.5, n)))
    trop = np.where(acs, trop + np.exp(s("troponin_acs").normal(
        np.log(250), 1.1, n)), trop)
    df["troponin"] = np.round(np.clip(trop, 3, 25000), 1)

    # ECG parameters of each patient
    lbbb = s("lbbb").uniform(size=n) < (0.02 + 0.22 * hfref)
    long_qt = s("long_qt").uniform(size=n) < 0.04
    hr = np.where(af, s("hr_af").normal(96, 16, n),
                  s("hr").normal(71, 10, n) + 7 * hfref + 3 * hfpef)
    hr = np.clip(hr, 45, 150)
    pr = np.clip(s("pr").normal(158, 20, n) + 0.5 * np.clip(
        df["age"] - 50, 0, None), 110, 290)
    qrs = np.where(lbbb, np.clip(s("qrs_lbbb").normal(148, 10, n), 125, 185),
                   np.clip(s("qrs").normal(88, 8, n) + 4 * male, 70, 112))
    qtc_f = (np.where(male, 408, 418) + s("qtc").normal(0, 16, n)
             + 22 * lbbb + 10 * hfref + 60 * long_qt)
    rr = 60.0 / hr
    qt = qtc_f * np.cbrt(rr)
    axis = np.where(lbbb, s("axis_lbbb").normal(-20, 25, n),
                    s("axis").normal(52, 22, n) - 4.0 * a10)
    axis = np.clip(axis, -85, 150)
    territory = np.full(n, "none", dtype=object)
    stemi = acs & (s("stemi").uniform(size=n) < 0.5)
    u = s("territory").uniform(size=n)
    territory[stemi & (u < 0.45)] = "anterior"
    territory[stemi & (u >= 0.45) & (u < 0.85)] = "inferior"
    territory[stemi & (u >= 0.85)] = "lateral"

    df["ecg_rhythm"] = np.where(af, "AF", "sinus")
    df["ecg_conduction"] = np.where(lbbb, "LBBB", "normal")
    df["ecg_hr"] = np.round(hr)
    df["ecg_pr"] = np.where(af, np.nan, np.round(pr))
    df["ecg_qrs"] = np.round(qrs)
    df["ecg_qt"] = np.round(qt)
    df["ecg_axis"] = np.round(axis)
    df["stemi_territory"] = territory
    df["ecg_hrv"] = np.round(np.clip(1.25 - 0.012 * (df["age"] - 40)
                                     - 0.3 * hf, 0.3, 1.5), 2)
    return df


def ecg_params(row):
    """ECG parameters of one patient (a row of the registry)."""
    return dict(
        rhythm=row["ecg_rhythm"], conduction=row["ecg_conduction"],
        hr_bpm=float(row["ecg_hr"]),
        pr_ms=float(row["ecg_pr"]) if row["ecg_rhythm"] == "sinus" else 160.0,
        qrs_ms=float(row["ecg_qrs"]), qt_ms=float(row["ecg_qt"]),
        axis_deg=float(row["ecg_axis"]), hrv=float(row["ecg_hrv"]),
        st_mv=0.3 if row["stemi_territory"] != "none" else 0.0,
        st_territory=row["stemi_territory"],
    )


def patient_ecg(cohort, patient_id, duration_s=10.0, fs=500, noise="low"):
    """The resting 12-lead ECG of one patient of the registry."""
    row = cohort.loc[cohort["patient_id"] == patient_id]
    if row.empty:
        raise KeyError(f"No patient with id {patient_id}")
    row = row.iloc[0]
    number = int(str(patient_id).split("-")[1])
    return simulate(ecg_params(row), duration_s=duration_s, fs=fs,
                    noise=noise, seed=DEFAULT_SEED * 10 + number,
                    patient_id=patient_id)
