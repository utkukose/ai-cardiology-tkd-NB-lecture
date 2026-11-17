"""Echocardiographic details and follow-up of the registry (from Week 2).

add_followup() takes a table made by make_cohort() and returns a copy with
new columns: echocardiographic measurements, a hidden phenogroup of the
patients with heart failure, and the time to the first event (death or
hospitalisation for heart failure) during follow-up.

Every value of a patient comes from its own stream of random numbers and
is indexed by the number of the patient, so a patient keeps the same values
when the table is filtered, reordered or made larger.

The phenogroup is the truth that the clustering of Week 2 tries to recover
without seeing it. The data are synthetic teaching material and are not for
clinical use.
"""

import numpy as np
import pandas as pd

from .cohort import DEFAULT_SEED, _stream

PHENOGROUPS = ("none", "HFrEF", "HFpEF-metabolic", "HFpEF-cardiorenal")

# Monthly hazard of the first event (death or hospitalisation for heart
# failure) for a patient of 70 years with an eGFR of 60 mL/min/1.73 m2 or
# more, before the other multipliers in add_followup().
BASE_HAZARD = {
    "none": 0.0009,
    "HFrEF": 0.0075,
    "HFpEF-metabolic": 0.0038,
    "HFpEF-cardiorenal": 0.0070,
}


def _numbers(cohort):
    return cohort["patient_id"].str.slice(3).astype(int).to_numpy()


def _draw(seed, name, numbers, kind="uniform", *args):
    size = int(numbers.max())
    rng = _stream(seed, "followup-" + name)
    values = getattr(rng, kind)(*args, size=size) if args else getattr(rng, kind)(size=size)
    return values[numbers - 1]


def add_followup(cohort, seed=DEFAULT_SEED, horizon_months=60.0):
    """Copy of the registry with echo details, phenogroups and follow-up."""
    df = cohort.copy()
    num = _numbers(df)
    u = lambda name: _draw(seed, name, num)
    z = lambda name: _draw(seed, name, num, "normal", 0.0, 1.0)

    age = df["age"].to_numpy(float)
    female = (df["sex"] == "F").to_numpy()
    bmi = df["bmi"].to_numpy(float)
    diab = df["diabetes"].to_numpy(bool)
    htn = df["hypertension"].to_numpy(bool)
    af = df["af"].to_numpy(bool)
    egfr = df["egfr"].to_numpy(float)
    diag = df["main_diagnosis"].to_numpy()
    hfref = diag == "HFrEF"
    hfpef = diag == "HFpEF"

    # Hidden phenogroup of heart failure with preserved ejection fraction
    metabolic = (bmi - 30) / 4 + 1.2 * diab - (age - 68) / 9 + 0.6 * z("pheno-m")
    renal = (age - 72) / 7 + 1.0 * af + (60 - egfr) / 15 + 0.4 * female + 0.6 * z("pheno-r")
    group = np.full(len(df), "none", dtype=object)
    group[hfpef & (metabolic >= renal)] = "HFpEF-metabolic"
    group[hfpef & (metabolic < renal)] = "HFpEF-cardiorenal"
    group[hfref] = "HFrEF"
    metab = group == "HFpEF-metabolic"
    renalg = group == "HFpEF-cardiorenal"

    # Echocardiographic measurements
    lvedd = (np.where(female, 45.0, 49.0) + 2.2 * z("lvedd")
             + np.where(hfref, 13.0 + 3.0 * z("lvedd-ref"), 0.0)
             + np.where(hfpef, -1.0, 0.0))
    ivs = (np.where(female, 8.6, 9.4) + 0.9 * z("ivs") + 1.2 * htn
           + np.where(metab, 2.6, 0.0) + np.where(renalg, 1.4, 0.0)
           + np.where(hfref, -0.8, 0.0))
    lvmi = (np.where(female, 78.0, 90.0) + 12.0 * z("lvmi") + 8.0 * htn
            + np.where(metab, 34.0, 0.0) + np.where(renalg, 20.0, 0.0)
            + np.where(hfref, 38.0, 0.0))
    lavi = (26.0 + 5.0 * z("lavi") + 10.0 * af + np.where(hfpef, 9.0, 0.0)
            + np.where(renalg, 7.0, 0.0) + np.where(hfref, 12.0, 0.0))
    ee = (7.8 + 1.8 * z("ee") + 0.06 * (age - 60)
          + np.where(metab, 5.0, 0.0) + np.where(renalg, 7.5, 0.0)
          + np.where(hfref, 7.0, 0.0))
    tapse = (23.5 + 2.8 * z("tapse") - 0.04 * (age - 60)
             + np.where(hfref, -6.5, 0.0) + np.where(renalg, -5.0, 0.0)
             + np.where(metab, -1.0, 0.0))
    df["lvedd_mm"] = np.round(np.clip(lvedd, 36, 80), 0)
    df["ivs_mm"] = np.round(np.clip(ivs, 6.0, 18.0), 1)
    df["lv_mass_index"] = np.round(np.clip(lvmi, 45, 220), 0)
    df["lavi"] = np.round(np.clip(lavi, 14, 80), 0)
    df["e_e_prime"] = np.round(np.clip(ee, 4.0, 30.0), 1)
    df["tapse_mm"] = np.round(np.clip(tapse, 8.0, 32.0), 0)
    df["hf_phenogroup"] = group

    # Time to the first event: death or hospitalisation for heart failure
    hazard = np.array([BASE_HAZARD[g] for g in group])
    nt = np.log(df["ntprobnp"].to_numpy(float))
    hazard = (hazard * 1.35 ** ((age - 70) / 10) * np.where(egfr < 60, 1.35, 1.0)
              * np.where(af, 1.15, 1.0) * 1.15 ** np.clip(nt - np.log(400), -3, 4))
    event_time = -np.log(1 - u("time")) / hazard
    admin = 36.0 + (horizon_months - 36.0) * u("admin")
    lost = -np.log(1 - u("lost")) * 240.0
    censor = np.minimum(admin, lost)
    event = event_time <= censor
    p_death = np.where(group == "none", 0.70, 0.45)
    death = event & (u("cause") < p_death)
    df["followup_months"] = np.round(np.maximum(np.where(event, event_time, censor), 0.1), 1)
    df["event"] = event.astype(int)
    df["event_type"] = np.where(~event, "none", np.where(death, "death", "hf_hospitalisation"))
    return df
