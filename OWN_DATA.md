# Working with your own data

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Course home](README.md) · [Türkçe](OWN_DATA.tr.md)

The course works with synthetic patients and public research data, so that every notebook runs for everyone and the true answers are known. Its aim, however, is the data of the participant's own clinic. This guide brings together what the sections *With your own data* of the lecture pages say week by week: which question fits which method, how the data leave the hospital systems, what the law and the ethics committee require, and where the analysis is run.

The guide gives orientation, not legal advice. For every study, the ethics committee, the data protection officer and the legal department of the institution have the final word.

## 1. Before any data: the question and the permissions

| Step | What it means |
|---|---|
| A clear question | One outcome, one group of patients and one moment of decision: "Which patients with heart failure with reduced ejection fraction (HFrEF) are admitted to hospital within 12 months?" rather than "What does artificial intelligence find in our data?" |
| A written plan | The question, the patients, the variables, the planned analysis and the sample size, written before the data are seen. The sample size of a prediction model depends on the number of events [1]. |
| The ethics committee | Research on patient data, retrospective studies of records included, needs the approval of an ethics committee. |
| Data protection | Health data are special categories of personal data under the Turkish Law on the Protection of Personal Data (KVKK) [2]. The institution decides how they may be processed; its data protection officer and legal department are the contacts. |
| The institution | The permission of the hospital management and, for the export of the data, the help of the information technology or clinical engineering department |

## 2. Getting the data out of the hospital

| Data | Where they are | What to ask for | What to remove |
|---|---|---|---|
| Tables of patients | Hospital information system, registry of a study | An Excel or CSV file with one row per patient, and a data dictionary with the unit and the coding of every column | Names, national identity numbers, record and protocol numbers, addresses and telephone numbers; dates become ages and intervals |
| ECGs | Electrocardiograph, ECG management system | Raw signals in a digital format, such as XML (for example HL7 aECG), DICOM waveform, SCP-ECG or EDF, rather than PDF printouts | The name and identity number in the header of each file |
| Echocardiography, cardiac magnetic resonance, coronary angiography | Picture archiving and communication system (PACS) or the device | DICOM files, with cine loops where the method needs motion, rather than screen recordings | The identifiers in the DICOM header and the text burned into the image, such as the name and the date at the edge of an echo frame |
| Written reports | Hospital information system | Plain text of the echo, catheterisation or discharge reports | Names, dates, telephone numbers and places inside the text; automatic de-identification must be checked by reading |
| Laboratory values | Laboratory information system | A table with values, units and reference ranges | Identifiers as for the tables; units can change between laboratories and over the years |

A key that links the study numbers to the patients, if one is needed at all, stays in the hospital, apart from the data. Data with such a key are pseudonymised, not anonymous, and they remain personal data.

## 3. Which method for which question

| Data | Question | Methods of the course | Week |
|---|---|---|---|
| Table | Does a patient have a condition, or will an event occur? | Logistic regression, decision trees and random forests, cross-validation | 2 |
| Table | How long until an event? | Kaplan-Meier curves, the log-rank test and Cox regression | 2 |
| Table | Are there subgroups among the patients? | k-means on standardised variables | 2 |
| ECG signal | Intervals, heart rate and its variability | Signal processing, R-peak detection | 1 |
| ECG signal | Rhythm and diagnosis, ST deviation | One-dimensional convolutional and recurrent networks, labels with several classes at once | 5 |
| Echocardiography, cardiac magnetic resonance | Classification of images | Convolutional networks, transfer learning from pretrained networks | 3, 4 |
| Echocardiography, cardiac magnetic resonance | Measurements such as volumes and the ejection fraction | Segmentation with U-Net and the method of discs | 4 |
| Coronary angiography | Detection of stenoses | Convolutional networks and vision transformers | 7 |
| Written reports | Extraction of findings | Natural language processing | 6 |
| Several kinds at once | A combined risk | Data fusion, missing data and calibration | 8 |
| Any model | Can it be trusted and explained? | Explainable artificial intelligence (AI), distribution shift and bias | 9 |
| Any model | Use at the bedside | Clinical decision support systems (CDSS) | 10 |

## 4. How much data?

For prediction models from tables, the number of events counts more than the number of patients, and published methods calculate the minimum sample size from the expected number of events and the number of variables [1]. For images there is no fixed number. Training a network from scratch needs many labelled images; pretrained networks and transfer learning, the topic of Week 4, lower the need. A learning curve, the performance against the number of training images in a pilot, shows whether more data would help.

In every case, a part of the data is set aside as a test set before the first model and is used only once, at the end. A model meant for patient care is tested again on data from another hospital or another device, an external validation.

## 5. Where to compute, and the AI assistants

The data of real patients are analysed on a computer of the institution, in Jupyter (Anaconda), and never in a cloud notebook such as Google Colab or in an AI chat. The disk of a laptop that holds such data should be encrypted.

The prompts of the course work with one's own data as well, with one rule: The prompt describes the structure of the data, such as the names of the columns, their units, their codes and the sampling frequency, and never contains a row of a patient. A good habit is to test the code first on a synthetic table with the same columns, which the course package `vclinic` can produce, and to run it on the real data only after it passes. Pretrained language models that run on one's own computer, which Week 6 uses, keep the text of reports on that computer.

## 6. Reporting, and the step towards the clinic

A study that develops or tests a prediction model reports it with the TRIPOD+AI checklist [3]. A model that is to be used in patient care is a different matter from a study. Software intended for the diagnosis or treatment of patients can be a medical device under the Medical Device Regulation of Türkiye, which is aligned with the regulation of the European Union [4]. Such software must pass the conformity assessment of the regulation before it is put into use. A model of the course, or of a study, is therefore never used for decisions on patients without this process.

## 7. Who can help

| Question | Contact |
|---|---|
| Sample size, study design, statistics | A biostatistician of the institution |
| Ethics approval | The ethics committee of the institution |
| KVKK and data security | The data protection officer and the legal department of the institution |
| Exports from the hospital systems and from devices | The information technology or clinical engineering department |
| The final project of the course | The instructor of the course |

## A short checklist

1. One clear question and a written plan with the sample size.
2. The approval of the ethics committee and the permission of the institution.
3. A de-identified export with a data dictionary.
4. A computing environment on a computer of the institution.
5. Quality control: units, ranges, codes, duplicates and missing values.
6. A test set set aside before the first model.
7. A report that follows TRIPOD+AI, with its limitations.

## References

1. Riley, R. D., Ensor, J., Snell, K. I. E., Harrell, F. E., Jr., Martin, G. P., Reitsma, J. B., Moons, K. G. M., Collins, G., & van Smeden, M. (2020). Calculating the sample size required for developing a clinical prediction model. *BMJ, 368*, m441. https://doi.org/10.1136/bmj.m441
2. Kişisel Verilerin Korunması Kanunu [Law on the Protection of Personal Data], Law No. 6698. (2016). *Resmî Gazete, 29677 (7 April 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5
3. Collins, G. S., Moons, K. G. M., Dhiman, P., Riley, R. D., Beam, A. L., Van Calster, B., Ghassemi, M., Liu, X., Reitsma, J. B., van Smeden, M., Boulesteix, A.-L., Camaradou, J. C., Celi, L. A., Denaxas, S., Denniston, A. K., Glocker, B., Golub, R. M., Harvey, H., Heinze, G., Hoffman, M. M., Kengne, A. P., Lam, E., Lee, N., Loder, E. W., Maier-Hein, L., Mateen, B. A., McCradden, M. D., Oakden-Rayner, L., Ordish, J., Parnell, R., Rose, S., Singh, K., Wynants, L., & Logullo, P. (2024). TRIPOD+AI statement: Updated guidance for reporting clinical prediction models that use regression or machine learning methods. *BMJ, 385*, e078378. https://doi.org/10.1136/bmj-2023-078378
4. Tıbbi Cihaz Yönetmeliği [Medical Device Regulation], Türkiye İlaç ve Tıbbi Cihaz Kurumu [Turkish Medicines and Medical Devices Agency]. (2021). *Resmî Gazete, 31499 (Mükerrer) (2 June 2021)*. https://titck.gov.tr/storage/Archive/2021/contentFile/T%C4%B1bbi%20Cihaz%20Y%C3%B6netmeli%C4%9Fi_91969c4b-58b3-48cb-adfb-03c2cacd5632.pdf

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
