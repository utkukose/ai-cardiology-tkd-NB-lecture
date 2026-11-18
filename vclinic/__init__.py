"""vclinic: the virtual cardiology clinic of the course.

Synthetic patients, their 12-lead electrocardiograms and small helpers used
across the weeks of the course. The synthetic data are teaching material and
are not for clinical use. The modules acdc, camus and echonet read public data
sets that every participant downloads from their source: ACDC (cine cardiac
magnetic resonance), CAMUS (apical echocardiograms with expert outlines) and
EchoNet-Dynamic (echocardiography, with personal registration).
"""
from .ecg import (LEADS, LEAD_VECTORS, LEAD_MATRIX, ECG, simulate, project,
                  direction, frontal_axis)
from .cohort import make_cohort, patient_ecg, ecg_params, TRUE_EFFECTS
from .followup import add_followup, PHENOGROUPS
from .imaging import echo_images, make_cmr_set, ECHO_CLASSES, CMR_CLASSES

__version__ = "1.5.0"
