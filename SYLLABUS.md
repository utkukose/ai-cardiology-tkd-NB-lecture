# Syllabus

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Course home](README.md) · [Türkçe](SYLLABUS.tr.md)

## Course information

| Item | Details |
|---|---|
| Organizer | Turkish Society of Cardiology (Türk Kardiyoloji Derneği) |
| Instructor | Prof. Dr. Utku Kose, Süleyman Demirel University |
| Participants | Cardiologists and other specialist physicians, with or without programming experience |
| Format | 11 weeks, one session of 4 hours per week, 44 hours in total; about 80 percent hands-on work |
| Languages of the materials | English and Turkish |
| Environment | Jupyter in Anaconda on the participant's own computer; Google Colab as a fallback |
| Prerequisites | No programming experience. Anaconda installed before Week 1 ([SETUP.md](SETUP.md)) |
| Contact | utkukose@sdu.edu.tr, utkukose@gmail.com |

## Description

The program teaches cardiologists and other specialist physicians to analyse cardiology data with Python and to build, validate and explain artificial intelligence (AI) models. It moves from tables and signals in the first weeks to images, text and data fusion. It ends with explainable models, a prototype of a clinical decision support system and a final project. A virtual cardiology clinic of synthetic patients runs through all weeks, and real public data sets accompany every topic. Coding with AI assistants is taught from the first week under explicit safety rules.

The learning outcomes of the course are listed on the [course home page](README.md#course-learning-outcomes), and each week page lists the outcomes of its week.

## Weekly plan

Each session lasts four hours and has two halves of about two hours. Each week also has a mini project in the session and a weekly project as homework. The plan follows the program of the Turkish Society of Cardiology and is refined as each week is published.

### Week 1: Python and cardiology data basics

The first half introduces Jupyter in Anaconda, Python with clinical examples, patient tables with pandas and the first plots with Matplotlib. The second half treats the electrocardiogram (ECG) as data: PhysioNet records, the twelve leads, R-peak detection, heart rate variability and the automatic measurement of intervals. **Mini project in the session:** Loading, describing and plotting the Cleveland data of the UCI Heart Disease data set. **Weekly project:** Automatic measurement of PR, QRS and QT, with the frontal axis and two QT corrections. **Data:** UCI Heart Disease (Cleveland), MIT-BIH Arrhythmia Database, PTB Diagnostic ECG Database. **Stage of the virtual clinic:** Patient registry and ECG laboratory.

Materials: [Week page](en/week-01/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lab.html) · [Jupyter notebook](en/week-01/NB01_python_and_ecg_basics.ipynb) · [Prompt library](en/week-01/PROMPTS.md) · [PDF notes](en/week-01/Week01_Lecture_Notes.pdf)

### Week 2: Machine learning fundamentals

The first half builds classification and regression models with scikit-learn: logistic regression for the risk of coronary artery disease, decision trees and random forests, cross-validation, the receiver operating characteristic (ROC) curve, sensitivity and specificity. The second half finds subgroups of patients with k-means, visualises them in two dimensions, introduces Kaplan-Meier survival analysis and treats imbalanced data. **Mini project in the session:** A model that predicts coronary artery disease on the Cleveland data, with the ROC curve and the area under it. **Weekly project:** Clustering of heart failure with preserved and reduced ejection fraction, with Kaplan-Meier survival analysis. **Data:** UCI Heart Disease (Cleveland) and the registry of the virtual clinic with follow-up. **Stage of the virtual clinic:** Risk outpatient clinic.

Materials: [Week page](en/week-02/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lab.html) · [Jupyter notebook](en/week-02/NB02_machine_learning_fundamentals.ipynb) · [Prompt library](en/week-02/PROMPTS.md) · [PDF notes](en/week-02/Week02_Lecture_Notes.pdf)

### Week 3: Deep learning and convolutional neural networks

The first half explains artificial neural networks and convolutional neural networks (CNNs): neurons, layers, activation functions, convolution, pooling, dropout and batch normalisation. The second half compares known architectures, augments cardiac images and reads the confusion matrix and the F1 score, with attention to overfitting. **Mini project in the session:** Classification of normal and abnormal echocardiograms. **Weekly project:** Classification of dilated and hypertrophic cardiomyopathy on cardiac magnetic resonance images. **Data:** Echocardiographic frames and short-axis cardiac magnetic resonance slices of the virtual clinic. **Stage of the virtual clinic:** Echo laboratory.

Materials: [Week page](en/week-03/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lab.html) · [Jupyter notebook](en/week-03/NB03_deep_learning_and_cnns.ipynb) · [Prompt library](en/week-03/PROMPTS.md) · [PDF notes](en/week-03/Week03_Lecture_Notes.pdf)

### Week 4: Transfer learning

The first half adapts networks trained on millions of images to cardiac tasks: feature extraction, fine-tuning and learning from few labelled images. The second half segments the left ventricle with a U-Net, computes the ejection fraction with the method of discs and plans the clinical validation of an automatic measurement. **Mini project in the session:** Classification of cardiomyopathy from a small set of labelled echocardiograms with a pretrained network. **Weekly project:** Segmentation of the left ventricle and automatic ejection fraction. **Data:** Echocardiograms of the virtual clinic and public imaging data sets that require registration. **Stage of the virtual clinic:** Echo measurement: automatic ejection fraction.

Materials: In preparation

### Week 5: Time series analysis and ECG artificial intelligence

The first half models the ECG as a time series with one-dimensional CNNs and recurrent networks, and treats the multi-label classification of rhythms. The second half detects ST elevation and depression, estimates the risk of QT prolongation, discusses long-term monitoring and reviews ECG algorithms that have regulatory approval. **Mini project in the session:** Detection of rhythm disorders on 12-lead ECGs. **Weekly project:** A STEMI alarm: automatic detection of ST deviation on 12-lead ECGs. **Data:** ECGs of the virtual clinic, PhysioNet/Computing in Cardiology Challenge 2020 and PTB-XL. **Stage of the virtual clinic:** Rhythm and STEMI alarm.

Materials: In preparation

### Week 6: Natural language processing and clinical text mining

The first half covers tokenisation, word representations and pretrained language models from the Hugging Face Hub, including models for Turkish. The second half extracts named entities such as drugs, diagnoses and procedures, summarises reports and discusses large language models as clinical assistants. **Mini project in the session:** Extraction of diagnoses from synthetic Turkish discharge summaries. **Weekly project:** A pipeline that extracts the degree of stenosis and the vessel from angiography reports. **Data:** Synthetic reports of the virtual clinic in Turkish and English. **Stage of the virtual clinic:** Report archive: clinical text.

Materials: In preparation

### Week 7: Vision transformers

The first half explains attention, self-attention and the vision transformer, which splits an image into patches. The second half combines a convolutional backbone with a transformer head, detects coronary stenoses and reads attention maps clinically. **Mini project in the session:** A small vision transformer trained on natural images and transferred to echocardiography. **Weekly project:** Detection of stenosis on coronary angiograms: convolutional network, vision transformer and hybrid compared. **Data:** Angiograms of the virtual clinic and a public coronary angiography data set. **Stage of the virtual clinic:** Catheterisation laboratory.

Materials: In preparation

### Week 8: Multimodal artificial intelligence and data fusion

The first half compares early, late and hybrid fusion of different kinds of data, attention-based fusion and the handling of missing data. The second half designs a cardiovascular risk model that combines biomarkers, clinical variables and imaging, with attention to calibration and confidence intervals. **Mini project in the session:** A model that fuses the ECG, the echocardiogram and laboratory values to classify the risk of heart failure. **Weekly project:** Prediction of major adverse cardiovascular events (MACE) in a simulated triage. **Data:** All data of the same patients of the virtual clinic. **Stage of the virtual clinic:** Heart team: data fusion.

Materials: In preparation

### Week 9: Model reliability and explainable artificial intelligence

The first half explains the decisions of models with the explainable AI (XAI) methods SHAP, LIME and Grad-CAM. The second half examines dataset shift, calibration, bias by sex and age, and the legal and ethical frame of clinical AI, including the Turkish Law on the Protection of Personal Data (KVKK). **Mini project in the session:** The clinical factors that weigh most in the model for coronary artery disease, explained with SHAP. **Weekly project:** Grad-CAM maps of the echo model compared with the reading of an expert. **Data:** Models of the earlier weeks. **Stage of the virtual clinic:** Quality and safety committee: XAI.

Materials: In preparation

### Week 10: Clinical decision support systems

The first half designs a clinical decision support system (CDSS) for the clinical workflow, builds its web interface with Streamlit and introduces HL7 FHIR and prediction services. The second half covers versioning, human oversight, the regulatory routes for medical device software and patient consent. **Mini project in the session:** A decision support prototype for atrial fibrillation: ECG upload, prediction, explanation and report. **Weekly project:** A user test of the decision support prototype and its improvement. **Data:** ECGs of the virtual clinic and the MIT-BIH Atrial Fibrillation Database. **Stage of the virtual clinic:** Decision support at the bedside.

Materials: In preparation

### Week 11: Final project and certificate

The first half is a workshop on the final projects: the question, the data, the model, its explanation and the design of its clinical evaluation. The second half holds the presentations of the final projects, their evaluation and the closing of the program with the certificates. **Mini project in the session:** Final project work in the session. **Weekly project:** Final project: an end-to-end AI pipeline for a question of the participant's own clinic, and a personal action plan. **Data:** Chosen by each participant (see the final project page). **Stage of the virtual clinic:** Own units: final projects.

Materials: In preparation

## Assessment and certificate

| Component | Weight | Requirement for the certificate |
|---|---|---|
| Weekly projects (Weeks 1 to 10) | 40 percent | At least 70 percent in each project |
| Final project (presentation and code) | 40 percent | Evaluation by a jury and by the participants |
| Participation and active learning | 20 percent | Attendance of at least 80 percent |

Each weekly project is scored out of 100 points. The results, correct and checked against the truth of the virtual clinic or a reference, give 40 points. The methods, applied as taught and explained, give 20 points. The discussion of the clinical meaning and of the limitations gives 20 points. The AI usage log, the use of the code safety checklist and a notebook that reproduces every result give the last 20 points. The [final project page](en/final-project/README.md) gives the rubric of the final project.

## Submission of the weekly projects

Weekly projects are submitted by e-mail to utkukose@sdu.edu.tr or utkukose@gmail.com before the session of the following week. The subject line names the week and the participant, for example "TKD AI, Week 1, Name Surname". The e-mail holds the report written in the [report template](en/templates/Report_Template.docx) with the AI usage log, the completed Jupyter notebook and the learning log exported from the interactive lab.

## Rules for the use of generative AI

Generative AI tools are allowed in this course and are part of its teaching. Four rules apply. First, no patient data enter a prompt: no names, dates of birth, hospital numbers or recordings of real patients. Second, every use of an AI tool for a weekly or final project is recorded in the AI usage log, with the tool, the prompt, what was checked and what was changed. Third, the participant is responsible for every line of submitted code and must be able to explain it. Code written with an assistant is checked with the code safety checklist before its results are used. Fourth, the interpretation and the discussion in the reports are the participant's own. An assistant may help with the language, and such help is recorded in the log as well. The [prompt path](PROMPT_PATH.md) applies the same rules to every exercise, and code that comes from it is assessed like code typed by hand.

## Data protection and ethics

The course uses synthetic data and public research data only. Real patient data from the participant's institution may be used in the final project only with the permission of the institution and, where required, the approval of an ethics committee. Such data are processed on the participant's own computer in line with the Turkish Law on the Protection of Personal Data (KVKK) [1]. They never enter a cloud service or an AI chat. The synthetic patients of the virtual clinic are teaching material and are not for clinical use.

## Attendance

The certificate requires attendance of at least 80 percent of the sessions, that is, at least 9 of the 11 sessions. A participant who misses a session follows the week with its study path, which gives the times for self-study.

## Materials and environment

Each week has a week page with links to its lecture page, interactive lab, Jupyter notebook, prompt library and PDF notes. [SETUP.md](SETUP.md) explains the installation of Anaconda and the first run, and the [start-here notebook](en/start-here/NB00_start_here.ipynb) checks the computer before Week 1. [DATASETS.md](DATASETS.md) lists the data sets with their licenses, and [PYTHON_PATH.md](PYTHON_PATH.md) lists the Python steps of the weeks. [PROMPT_PATH.md](PROMPT_PATH.md) describes the prompt path and the AI assistants that work with it.

## Communication

Questions about the content can be asked in the sessions or by e-mail to utkukose@sdu.edu.tr or utkukose@gmail.com. Errors in the materials can be reported in the [issues](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/issues) of the repository.

## References

1. Kişisel Verilerin Korunması Kanunu [Law on the Protection of Personal Data], Law No. 6698. (2016). *Resmî Gazete, 29677 (7 April 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5
---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
