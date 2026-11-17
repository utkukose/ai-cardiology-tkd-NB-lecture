# Data sets

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Course home](README.md) · [Türkçe](DATASETS.tr.md)

Every data set of the course is either synthetic or public. The files of Week 1 are included in the [data](data) folder, so that the Jupyter notebooks run without registration. Each data set keeps its own license, and its citation is given below.

## Data sets of Week 1

| Data set | Files in the repository | Source and license | Used in |
|---|---|---|---|
| UCI Heart Disease, Cleveland data [1, 2] | `data/uci-heart-disease/processed.cleveland.data`: 303 patients, 14 variables | UCI Machine Learning Repository, [doi:10.24432/C52P4X](https://doi.org/10.24432/C52P4X); Creative Commons Attribution 4.0 International (CC BY 4.0) | Week 1, Section 1; Week 2, Python step 2 and Sections 1 to 4 |
| MIT-BIH Arrhythmia Database, record 100 [3, 4, 5] | `data/physionet/mitdb/100.hea`, `100.dat`, `100.atr`: 30 minutes of two leads (MLII and V5) at 360 Hz with beat annotations | PhysioNet, [doi:10.13026/C2F305](https://doi.org/10.13026/C2F305); Open Data Commons Attribution License v1.0 (ODC-By 1.0) | Week 1, Section 6 |
| PTB Diagnostic ECG Database, patient 001, record s0010_re [5, 6, 7] | `data/physionet/ptbdb/patient001/s0010_re.hea`, `.dat`, `.xyz`: 38.4 seconds of the 12 standard leads and the 3 Frank leads at 1000 Hz | PhysioNet, [doi:10.13026/C28C71](https://doi.org/10.13026/C28C71); ODC-By 1.0 | Week 1, Section 8 |
| Example caliper measurements | `data/examples/example_caliper_measurements.csv`: 20 interval measurements of five patients of the virtual clinic | Created for the course; CC BY 4.0 | Week 1, Section 5 |

The record of the PTB database comes from an 81-year-old woman admitted with an acute inferolateral myocardial infarction, as stated in its header file. The files are unchanged copies of the files published on PhysioNet and in the UCI repository.

## The virtual clinic

The course package `vclinic` creates the patients of the virtual clinic at run time. `vclinic.make_cohort(500)` returns a registry of 500 synthetic patients with demographic data, risk factors, laboratory values, the ejection fraction, the main diagnosis and the parameters of the electrocardiogram (ECG). `vclinic.patient_ecg` returns the 12-lead ECG of a patient together with the true values of its intervals and beat times. The same seed always gives the same patients, so every participant sees the same clinic. The relations between the variables follow broad clinical patterns, and their effect sizes are documented in `vclinic.TRUE_EFFECTS`. From Week 2, `vclinic.add_followup` adds echocardiographic variables, the phenogroup of heart failure and up to five years of follow-up, with death or hospitalisation for heart failure as the event. From Week 3, the module `vclinic.imaging` draws images: `echo_images` gives one end-diastolic frame of the parasternal short-axis view for each patient of a registry, drawn from the patient's own diameter and wall thickness, and `make_cmr_set` gives short-axis slices of cine cardiac magnetic resonance (CMR) for three classes, normal, dilated cardiomyopathy and hypertrophic cardiomyopathy. The data are teaching material and are not for clinical use.

## Files of Week 3

| File | Content | License | Used in |
|---|---|---|---|
| `data/examples/echo/VC-0821.png`, `VC-1873.png`, `VC-1212.png` | Three frames of the echo laboratory of the virtual clinic, 64 × 64 pixels in grey scale, one pixel = 2 mm: a normal ventricle, a dilated ventricle and a thick septum | Created for the course; CC BY 4.0 | Week 3, Python step 3 and Section 4 |
| `models/week03/echo_cnn.pt`, `echo_cnn.json` | The weights of the network of the echo laboratory (a PyTorch state dictionary with 10,098 parameters), the mean and the standard deviation of its normalisation and the names of its classes | Trained for the course on the frames of the virtual clinic; CC BY 4.0 | Week 3, Section 9 |

## Data sets of later weeks

The data sets of later weeks are documented here when each week is published. The program plans PTB-XL, the data of the PhysioNet/Computing in Cardiology Challenge 2020, the MIT-BIH Atrial Fibrillation Database and public data sets of echocardiography, cardiac magnetic resonance and coronary angiography. Some imaging data sets require registration and the acceptance of a data use agreement. For these weeks, the virtual clinic provides synthetic data so that every notebook also runs without registration.

## References

1. Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989). *Heart Disease* [Data set]. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X
2. Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J.-J., Sandhu, S., Guppy, K. H., Lee, S., & Froelicher, V. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. *The American Journal of Cardiology, 64*(5), 304–310. https://doi.org/10.1016/0002-9149(89)90524-9
3. Moody, G. B., & Mark, R. G. (2005). *MIT-BIH Arrhythmia Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C2F305
4. Moody, G. B., & Mark, R. G. (2001). The impact of the MIT-BIH Arrhythmia Database. *IEEE Engineering in Medicine and Biology Magazine, 20*(3), 45–50. https://doi.org/10.1109/51.932724
5. Goldberger, A. L., Amaral, L. A. N., Glass, L., Hausdorff, J. M., Ivanov, P. Ch., Mark, R. G., Mietus, J. E., Moody, G. B., Peng, C.-K., & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. *Circulation, 101*(23), e215–e220. https://doi.org/10.1161/01.CIR.101.23.e215
6. Bousseljot, R., Kreiseler, D., & Schnabel, A. (2004). *The PTB Diagnostic ECG Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C28C71
7. Bousseljot, R., Kreiseler, D., & Schnabel, A. (1995). Nutzung der EKG-Signaldatenbank CARDIODAT der PTB über das Internet. *Biomedizinische Technik / Biomedical Engineering, 40*(s1), 317–318. https://doi.org/10.1515/bmte.1995.40.s1.317

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
