"""vclinic: the virtual cardiology clinic of the course.

Synthetic patients, their 12-lead electrocardiograms and small helpers used
across the weeks of the course. The synthetic data are teaching material and
are not for clinical use. The modules acdc, camus and echonet read public data
sets that every participant downloads from their source: ACDC (cine cardiac
magnetic resonance), CAMUS (apical echocardiograms with expert outlines) and
EchoNet-Dynamic (echocardiography, with personal registration). The module
ptbxl reads the 12-lead ECGs of PTB-XL, downloaded from PhysioNet, the module
beats finds their R peaks and measures the median beat, the ST deviation and
the QT interval, and the module holter makes a synthetic 24-hour recording of
the virtual clinic. The module reports writes the discharge summaries and the
coronary angiography reports of the report archive, in Turkish and English,
and the module coronary holds the coronary lesions of the patients, which the
angiography reports describe. The module angiogram draws these lesions as
synthetic X-ray coronary angiograms, and the module arcade reads ARCADE, a
public data set of coronary angiograms with expert outlines of stenoses,
downloaded from Zenodo. The module triage holds the chest pain unit of two
hospitals: presentations with a clinical table, a triage note, a 12-lead ECG,
two troponins, a bedside echocardiogram and the events of the next 30 days.
The module afdb reads the MIT-BIH Atrial Fibrillation Database, Holter
recordings with rhythm annotations, downloaded from PhysioNet.
"""
from .ecg import (LEADS, LEAD_VECTORS, LEAD_MATRIX, ECG, simulate, project,
                  direction, frontal_axis)
from .cohort import make_cohort, patient_ecg, ecg_params, TRUE_EFFECTS
from .followup import add_followup, PHENOGROUPS
from .sources import COURSE_RAW, install, local_file, local_files

__version__ = "1.11.0"
