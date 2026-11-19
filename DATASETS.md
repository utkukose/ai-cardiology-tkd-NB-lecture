# Data sets

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Course home](README.md) · [Türkçe](DATASETS.tr.md)

Every data set of the course is either synthetic or public. The files of Week 1 are included in the [data](data) folder, so that the Jupyter notebooks run without registration. Each data set keeps its own license, and its citation is given below.

## Data sets of Week 1

| Data set | Files in the repository | Source and license | Used in |
|---|---|---|---|
| UCI Heart Disease, Cleveland data [1, 2] | `data/uci-heart-disease/processed.cleveland.data`: 303 patients, 14 variables | UCI Machine Learning Repository, [doi:10.24432/C52P4X](https://doi.org/10.24432/C52P4X); Creative Commons Attribution 4.0 International (CC BY 4.0) | Week 1, Section 1; Week 2, Python step 2 and Sections 1 to 4; Week 9, Python step 9, practice stops 1 to 3 and Sections 1 to 4 and 10 |
| MIT-BIH Arrhythmia Database, record 100 [3, 4, 5] | `data/physionet/mitdb/100.hea`, `100.dat`, `100.atr`: 30 minutes of two leads (MLII and V5) at 360 Hz with beat annotations | PhysioNet, [doi:10.13026/C2F305](https://doi.org/10.13026/C2F305); Open Data Commons Attribution License v1.0 (ODC-By 1.0) | Week 1, Section 6 |
| PTB Diagnostic ECG Database, patient 001, record s0010_re [5, 6, 7] | `data/physionet/ptbdb/patient001/s0010_re.hea`, `.dat`, `.xyz`: 38.4 seconds of the 12 standard leads and the 3 Frank leads at 1000 Hz | PhysioNet, [doi:10.13026/C28C71](https://doi.org/10.13026/C28C71); ODC-By 1.0 | Week 1, Section 8 |
| Example caliper measurements | `data/examples/example_caliper_measurements.csv`: 20 interval measurements of five patients of the virtual clinic | Created for the course; CC BY 4.0 | Week 1, Section 5 |

The record of the PTB database comes from an 81-year-old woman admitted with an acute inferolateral myocardial infarction, as stated in its header file. The files are unchanged copies of the files published on PhysioNet and in the UCI repository.

## The virtual clinic

The course package `vclinic` creates the patients of the virtual clinic at run time. `vclinic.make_cohort(500)` returns a registry of 500 synthetic patients with demographic data, risk factors, laboratory values, the ejection fraction, the main diagnosis and the parameters of the electrocardiogram (ECG). `vclinic.patient_ecg` returns the 12-lead ECG of a patient together with the true values of its intervals and beat times. The same seed always gives the same patients, so every participant sees the same clinic. The relations between the variables follow broad clinical patterns, and their effect sizes are documented in `vclinic.TRUE_EFFECTS`. From Week 2, `vclinic.add_followup` adds echocardiographic variables, the phenogroup of heart failure and up to five years of follow-up, with death or hospitalisation for heart failure as the event. The data are teaching material and are not for clinical use. From Week 3, the package also reads real images from public archives with the modules `vclinic.acdc` and `vclinic.echonet`, described below.

## Data sets of Week 3

No file of Week 3 is stored in the repository. Each participant obtains the images from their source and accepts its terms, and the package reads them where they are saved.

| Data set | Access | Source and license | Used in |
|---|---|---|---|
| ACDC, Automated Cardiac Diagnosis Challenge [8]: 150 cine cardiac magnetic resonance (CMR) examinations of the University Hospital of Dijon in five groups, with expert contours of the left ventricular cavity, the myocardium and the right ventricular cavity at end-diastole and end-systole. The course uses the 90 examinations of the groups normal (NOR), dilated cardiomyopathy (DCM) and hypertrophic cardiomyopathy (HCM). | `vclinic.acdc.download()` saves the files of the three groups, about 105 MB, from the public database of the Human Heart Project to the folder `data/acdc` of the course folder, in Google Colab and in Jupyter alike. No registration is needed. | [ACDC](https://www.creatis.insa-lyon.fr/Challenge/acdc/), University of Lyon (CREATIS) and University Hospital of Dijon; Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0), for non-commercial scientific research. Figures of the course that show these images carry the credit "ACDC, CC BY-NC-SA 4.0" and fall under the same license. | Week 3, Python step 3, practice stops 1 and 2 and Sections 1 to 9 |
| EchoNet-Dynamic [9]: 10,030 apical four-chamber echocardiography videos of Stanford University Medical Center, 112 × 112 pixels, with the ejection fraction, the volumes and the expert tracings of the left ventricle at end-diastole and end-systole | Each participant registers personally at the [Stanford AIMI](https://aimi.stanford.edu/datasets/echonet-dynamic-cardiac-ultrasound) site and receives a personal download link. `vclinic.echonet` reads the zip file or the unpacked folder in `data/echonet`. The course does not share the files or the link. | Stanford University School of Medicine EchoNet-Dynamic Dataset Research Use Agreement: personal, non-commercial research use; every user registers individually. Dataset [doi:10.71718/yqp5-y078](https://doi.org/10.71718/yqp5-y078) | Week 3, practice stop 3 and Section 10, for participants with a registration |

## Data sets of Week 4

No file of Week 4 is stored in the repository either. Each participant downloads the images and the weights from their source, and the package reads them where they are saved.

| Data set | Access | Source and license | Used in |
|---|---|---|---|
| CAMUS, Cardiac Acquisitions for Multi-structure Ultrasound Segmentation [10]: apical two-chamber and four-chamber echocardiograms of 500 patients of the University Hospital of Saint-Étienne, recorded with a GE Vivid E95 machine. Each view comes with the outlines of an expert of the left ventricular cavity, the myocardium and the left atrium at end-diastole and end-systole, its image quality and the ejection fraction. The course uses 300 patients: 200 of the training set and the 50 patients each of the validation and the test set. | `vclinic.camus.download()` saves the end-diastolic and end-systolic frames of the 300 patients with their outlines and information files, about 227 MB, from the public database of the Human Heart Project to the folder `data/camus` of the course folder, in Google Colab and in Jupyter alike. No registration is needed. | [CAMUS](https://www.creatis.insa-lyon.fr/Challenge/camus/), University of Lyon (CREATIS) and University Hospital of Saint-Étienne; Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0), for non-commercial scientific research, with a citation of the paper of CAMUS in every use. Figures of the course that show these images carry the credit "CAMUS, CC BY-NC-SA 4.0" and fall under the same license. | Week 4, Python step 4, practice stops 2 and 3 and Sections 5 to 10; Week 7, practice stop 1 and Section 4; Week 9, practice stop 2, Sections 5 to 7 and the weekly project |
| ImageNet weights of EfficientNet-B0 [11, 12]: the weights of the network trained on the 1,000 classes of the ImageNet challenge, about 21 MB | Section 0 of the notebook downloads them once through torchvision to the cache of PyTorch on the computer. | Distributed with [torchvision](https://pytorch.org/vision/stable/models/efficientnet.html), whose code is under the BSD 3-Clause License. The weights were trained on ImageNet, whose terms allow non-commercial research and education; the course uses them for teaching only. | Week 4, Python step 4, practice stop 1 and Sections 1 to 4; Week 7, practice stop 1 and Section 4 |

## Data sets of Week 5

No recording of PTB-XL is stored in the repository. Each participant downloads the recordings from PhysioNet, and the package reads them where they are saved.

| Data set | Access | Source and license | Used in |
|---|---|---|---|
| PTB-XL [13, 14]: 21,799 clinical 12-lead ECGs of 10 seconds from 18,869 patients, recorded with devices of Schiller AG between 1989 and 1996 and described by up to two cardiologists with 71 statements of the SCP-ECG standard, divided by patient into ten folds. The course uses the recordings at 100 Hz of folds 1 and 2 (training), 9 (validation) and 10 (test), 8,737 recordings of 7,573 patients. | `vclinic.ptbxl.download()` saves the two tables and the 8,737 recordings, about 216 MB, from PhysioNet to the folder `data/ptbxl` of the course folder, in Google Colab and in Jupyter alike. No registration is needed. | [PTB-XL 1.0.3](https://doi.org/10.13026/kfzx-aw45), Physikalisch-Technische Bundesanstalt, on PhysioNet; Creative Commons Attribution 4.0 International (CC BY 4.0), with a citation of the paper and of the data set in every use. Figures of the course that show these recordings carry the credit "PTB-XL, CC BY 4.0". | Week 5, practice stops 1 and 2, Sections 1 to 8 and the weekly project |
| Synthetic 24-hour Holter recording of patient VC-0128 of the virtual clinic: three episodes of paroxysmal AF, an hour of frequent atrial premature beats and two periods of electrode noise, with the truth beat by beat | `vclinic.holter.recording()` writes it in a few seconds; nothing is downloaded. | Synthetic, part of the course package (MIT License). | Week 5, practice stop 3 and Section 9 |

## Data sets of Week 6

Week 6 stores no data in the repository. The course package writes the report archive on the computer of the participant, and the tokenizer and the weights of the pretrained model come from the Hugging Face Hub.

| Data set | Access | Source and license | Used in |
|---|---|---|---|
| Report archive of the virtual clinic: one discharge summary for each of 3,600 synthetic patients, 3,000 from hospital A in full sentences, in Turkish and in English, and 600 from hospital B in a short style, with the annotated diagnoses, drugs and procedures and the assertion of every diagnosis; and 2,311 synthetic coronary angiography reports with their arteries, segments and stenoses | `vclinic.reports.archive()` and `vclinic.reports.angiography_archive()` write them in a few seconds; nothing is downloaded. | Synthetic, part of the course package (MIT License). | Week 6, all sections and practice stops |
| Tiny Turkish BERT model `ytu-ce-cosmos/turkish-tiny-bert-uncased` [15]: 2 layers, 128 numbers per token, a vocabulary of 32,000 pieces and about 4.6 million parameters, pretrained on more than 75 GB of Turkish text | Section 0 and Python step 6 of the notebook download the tokenizer and the weights, about 19 MB, once through transformers to the cache of Hugging Face on the computer. | Cosmos Research Lab of Yıldız Technical University, on the [Hugging Face Hub](https://huggingface.co/ytu-ce-cosmos/turkish-tiny-bert-uncased); MIT License. | Week 6, Sections 6 to 8 and practice stop 2 |

## Data sets of Week 7

Week 7 stores no data in the repository. The course package draws the angiograms of the virtual clinic on the computer of the participant, ARCADE is downloaded from Zenodo, and the weights of ViT-B/16 come through torchvision. The echocardiograms of CAMUS and the weights of EfficientNet-B0 are those of Week 4.

| Data set | Access | Source and license | Used in |
|---|---|---|---|
| Synthetic coronary angiograms of the virtual clinic: a view of the left and a view of the right coronary artery, 512 × 512 pixels, for each of the 2,311 patients with an angiography, drawn from the lesions of the registry of Week 6, with the place, the degree and the box of every stenosis | `vclinic.angiogram.patient_frames()` draws the two views of a patient, and `vclinic.angiogram.patches()` cuts the patches of a set; nothing is downloaded. | Synthetic, part of the course package (MIT License). | Week 7, Python step 7, Sections 1, 2 and 5, practice stop 2 |
| ARCADE, Automatic Region-based Coronary Artery Disease diagnostics using X-ray angiography imagEs [16]: the stenosis set, 1,500 X-ray coronary angiograms of 512 × 512 pixels with the outlines of the stenotic plaques drawn by experts, split into 1,000 images for training, 200 for validation and 300 for the test | `vclinic.arcade.download()` downloads the archive, about 452 MB, once from Zenodo, checks its MD5 checksum and keeps the stenosis set in the folder `data/arcade` of the course folder. | [ARCADE on Zenodo](https://doi.org/10.5281/zenodo.10390295); Creative Commons CC0 1.0. Figures of the course that show these images carry the credit "ARCADE, Popov et al. 2024, CC0". | Week 7, Sections 6 to 10, practice stops 2 and 3 and the weekly project |
| ImageNet weights of ViT-B/16 [12, 17]: the weights of the vision transformer trained by torchvision on the 1,000 classes of the ImageNet challenge, 86.6 million parameters, about 330 MB | Section 0 of the notebook downloads them once through torchvision to the cache of PyTorch on the computer. | Distributed with [torchvision](https://pytorch.org/vision/stable/models/vision_transformer.html), whose code is under the BSD 3-Clause License. The weights were trained on ImageNet, whose terms allow non-commercial research and education; the course uses them for teaching only. | Week 7, Sections 3, 4 and 8 and practice stop 1 |

## Data sets of Week 8

Week 8 stores no data in the repository. The course package draws the registry and the chest pain unit of the virtual clinic on the computer of the participant; nothing is downloaded.

| Data set | Access | Source and license | Used in |
|---|---|---|---|
| Registry of the virtual clinic with follow-up: 3,600 synthetic patients drawn as in Week 2. The 3,227 patients with a heart failure event within 24 months or with at least 24 months of follow-up enter the mini project, with the measurements of their ECG, six echocardiographic variables and three laboratory values | `vclinic.followup.add_followup(vclinic.cohort.make_cohort(3600))` draws it in a few seconds; nothing is downloaded. | Synthetic, part of the course package (MIT License). | Week 8, Sections 1 to 3 and practice stop 1 |
| Chest pain unit of the virtual clinic: 4,000 synthetic presentations with chest pain at hospital A and 1,000 at hospital B. Each presentation has a clinical table, a triage note in Turkish and in English, a 12-lead ECG of 10 seconds, high-sensitivity troponin at arrival and after one hour, a bedside echocardiogram for about half of the patients, the HEART score and major adverse cardiac events within 30 days. The patients of hospital B are older and sicker, its troponin I assay has another upper reference limit, and its notes are shorter | `vclinic.triage.presentations("A")` and `vclinic.triage.presentations("B")` write the tables in a few seconds, and `vclinic.triage.ecg_array()` draws the ECGs; nothing is downloaded. | Synthetic, part of the course package (MIT License). | Week 8, Python step 8, Sections 4 to 10, practice stops 2 and 3 and the weekly project |

## Data sets of Week 9

Week 9 stores no new data in the repository. It returns to three data sets described above.

| Data set | Access | Source and license | Used in |
|---|---|---|---|
| UCI Heart Disease, Cleveland data [1, 2]: 303 patients referred for coronary angiography, with the split of Week 2 into 227 training and 76 test patients | In the repository, as in Week 1 | UCI Machine Learning Repository; CC BY 4.0 | Week 9, Python step 9, practice stops 1 to 3 and Sections 1 to 4 and 10 |
| CAMUS [10]: the 300 patients of Week 4, with 600 apical two-chamber and four-chamber views, their expert outlines and the ejection fraction | Section 0 of the notebook downloads them again, about 250 MB, only when they are missing | CC BY-NC-SA 4.0, as in Week 4; figures carry the credit "CAMUS, CC BY-NC-SA 4.0" | Week 9, practice stop 2, Sections 5 to 7 and the weekly project |
| Chest pain unit of the virtual clinic: 4,000 synthetic presentations with chest pain at hospital A and 1,000 at hospital B, as in Week 8 | `vclinic.triage` draws them on the computer; nothing is downloaded | Synthetic data of the course package (MIT License) | Week 9, practice stop 3 and Sections 8 to 10 |

## Data sets of Week 10

Week 10 stores no recording in the repository. Each participant downloads the files of the MIT-BIH Atrial Fibrillation Database from PhysioNet, and the course package draws the telemetry ward of the virtual clinic on the computer.

| Data set | Access | Source and license | Used in |
|---|---|---|---|
| MIT-BIH Atrial Fibrillation Database (AFDB) [18, 19]: 25 Holter recordings of about 10 hours of people with atrial fibrillation, mostly paroxysmal, made at Beth Israel Hospital in Boston, with two ECG signals at 250 samples per second, rhythm annotations prepared by hand and beat annotations from an automatic detector; records 00735 and 03665 have no signals. Split by record, the course uses 15 records for training, 5 for validation and the user test and 5 for the test, cut into 14,883 windows of one minute | `vclinic.afdb.download()` saves the 75 header and annotation files of the 25 records and the signal files of records 04936, 06426 and 08219, about 86 MB, from PhysioNet to the folder `data/afdb` of the course folder and checks every file against the SHA-256 sums that PhysioNet publishes; no registration is needed. | [MIT-BIH AFDB 1.0.0](https://doi.org/10.13026/C2MW2D) on PhysioNet; Open Data Commons Attribution License v1.0 (ODC-By 1.0), with a citation of the paper and of the database in every use. Figures of the course that show these recordings carry the credit "MIT-BIH AFDB, PhysioNet, ODC-By 1.0". | Week 10, Sections 1 to 6 and 10, practice stops 1 to 3 and the weekly project |
| Telemetry ward of the virtual clinic: 24-hour recordings of four synthetic patients, VC-0128 (paroxysmal AF, premature atrial beats and two periods of electrode noise), VC-0347 (sinus rhythm with frequent premature atrial beats), VC-0519 (persistent AF) and VC-0733 (sinus rhythm with long periods of electrode noise). Each recording holds the beat times that a monitor would find and a lead II ECG of any ten seconds | `vclinic.holter.ward()` draws them in a few seconds; nothing is downloaded. | Synthetic, part of the course package (MIT License). | Week 10, Sections 7 to 9, practice stops 2 and 3 and the interactive lab |

## Data sets of later weeks

The data sets of later weeks are documented here when each week is published. The program plans the data of the PhysioNet/Computing in Cardiology Challenge 2020 and public data sets of echocardiography and cardiac magnetic resonance. Where a data set requires a personal registration, as EchoNet-Dynamic does, the notebook marks the cells that need it, and participants without a registration follow the run of the instructor.

## References

1. Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989). *Heart Disease* [Data set]. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X
2. Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J.-J., Sandhu, S., Guppy, K. H., Lee, S., & Froelicher, V. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. *The American Journal of Cardiology, 64*(5), 304–310. https://doi.org/10.1016/0002-9149(89)90524-9
3. Moody, G. B., & Mark, R. G. (2005). *MIT-BIH Arrhythmia Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C2F305
4. Moody, G. B., & Mark, R. G. (2001). The impact of the MIT-BIH Arrhythmia Database. *IEEE Engineering in Medicine and Biology Magazine, 20*(3), 45–50. https://doi.org/10.1109/51.932724
5. Goldberger, A. L., Amaral, L. A. N., Glass, L., Hausdorff, J. M., Ivanov, P. Ch., Mark, R. G., Mietus, J. E., Moody, G. B., Peng, C.-K., & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. *Circulation, 101*(23), e215–e220. https://doi.org/10.1161/01.CIR.101.23.e215
6. Bousseljot, R., Kreiseler, D., & Schnabel, A. (2004). *The PTB Diagnostic ECG Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C28C71
7. Bousseljot, R., Kreiseler, D., & Schnabel, A. (1995). Nutzung der EKG-Signaldatenbank CARDIODAT der PTB über das Internet. *Biomedizinische Technik / Biomedical Engineering, 40*(s1), 317–318. https://doi.org/10.1515/bmte.1995.40.s1.317
8. Bernard, O., Lalande, A., Zotti, C., Cervenansky, F., Yang, X., Heng, P.-A., Cetin, I., Lekadir, K., Camara, O., Gonzalez Ballester, M. A., Sanroma, G., Napel, S., Petersen, S., Tziritas, G., Grinias, E., Khened, M., Kollerathu, V. A., Krishnamurthi, G., Rohe, M.-M., Pennec, X., Sermesant, M., Isensee, F., Jager, P., Maier-Hein, K. H., Full, P. M., Wolf, I., Engelhardt, S., Baumgartner, C. F., Koch, L. M., Wolterink, J. M., Isgum, I., Jang, Y., Hong, Y., Patravali, J., Jain, S., Humbert, O., & Jodoin, P.-M. (2018). Deep learning techniques for automatic MRI cardiac multi-structures segmentation and diagnosis: Is the problem solved? *IEEE Transactions on Medical Imaging, 37*(11), 2514–2525. https://doi.org/10.1109/TMI.2018.2837502
9. Ouyang, D., He, B., Ghorbani, A., Yuan, N., Ebinger, J., Langlotz, C. P., Heidenreich, P. A., Harrington, R. A., Liang, D. H., Ashley, E. A., & Zou, J. Y. (2020). Video-based AI for beat-to-beat assessment of cardiac function. *Nature, 580*(7802), 252–256. https://doi.org/10.1038/s41586-020-2145-8
10. Leclerc, S., Smistad, E., Pedrosa, J., Østvik, A., Cervenansky, F., Espinosa, F., Espeland, T., Berg, E. A. R., Jodoin, P.-M., Grenier, T., Lartizien, C., D'hooge, J., Lovstakken, L., & Bernard, O. (2019). Deep learning for segmentation using an open large-scale dataset in 2D echocardiography. *IEEE Transactions on Medical Imaging, 38*(9), 2198–2210. https://doi.org/10.1109/TMI.2019.2900516
11. Tan, M., & Le, Q. (2019). EfficientNet: Rethinking model scaling for convolutional neural networks. In *Proceedings of the 36th International Conference on Machine Learning, PMLR 97* (pp. 6105–6114). https://proceedings.mlr.press/v97/tan19a.html
12. Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., Huang, Z., Karpathy, A., Khosla, A., Bernstein, M., Berg, A. C., & Fei-Fei, L. (2015). ImageNet large scale visual recognition challenge. *International Journal of Computer Vision, 115*(3), 211–252. https://doi.org/10.1007/s11263-015-0816-y
13. Wagner, P., Strodthoff, N., Bousseljot, R.-D., Kreiseler, D., Lunze, F. I., Samek, W., & Schaeffter, T. (2020). PTB-XL, a large publicly available electrocardiography dataset. *Scientific Data, 7*(1), Article 154. https://doi.org/10.1038/s41597-020-0495-6
14. Wagner, P., Strodthoff, N., Bousseljot, R., Samek, W., & Schaeffter, T. (2022). *PTB-XL, a large publicly available electrocardiography dataset (version 1.0.3)* [Data set]. PhysioNet. https://doi.org/10.13026/kfzx-aw45
15. Kesgin, H. T., Yüce, M. K., & Amasyali, M. F. (2023). *Developing and evaluating tiny to medium-sized Turkish BERT models* (arXiv:2307.14134). arXiv. https://doi.org/10.48550/arXiv.2307.14134
16. Popov, M., Amanturdieva, A., Zhaksylyk, N., Alkanov, A., Saniyazbekov, A., Aimyshev, T., Ismailov, E., Bulegenov, A., Kuzhukeyev, A., Kulanbayeva, A., Kalzhanov, A., Temenov, N., Kolesnikov, A., Sakhov, O., & Fazli, S. (2024). Dataset for automatic region-based coronary artery disease diagnostics using X-ray angiography images. *Scientific Data, 11*, Article 20. https://doi.org/10.1038/s41597-023-02871-z
17. Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., Uszkoreit, J., & Houlsby, N. (2021). An image is worth 16x16 words: Transformers for image recognition at scale. In *9th International Conference on Learning Representations (ICLR 2021)*. https://openreview.net/forum?id=YicbFdNTTy
18. Moody, G. B., & Mark, R. G. (1983). A new method for detecting atrial fibrillation using R-R intervals. *Computers in Cardiology, 10*, 227–230. https://physionet.org/content/afdb/1.0.0/
19. Moody, G. B., & Mark, R. G. (1992). *MIT-BIH Atrial Fibrillation Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C2MW2D

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
