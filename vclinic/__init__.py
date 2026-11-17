"""vclinic: the virtual cardiology clinic of the course.

Synthetic patients, their 12-lead electrocardiograms and small helpers used
across the weeks of the course. The data are synthetic teaching material
and are not for clinical use.
"""
from .ecg import (LEADS, LEAD_VECTORS, LEAD_MATRIX, ECG, simulate, project,
                  direction, frontal_axis)
from .cohort import make_cohort, patient_ecg, ecg_params, TRUE_EFFECTS

__version__ = "1.0.0"
