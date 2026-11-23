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
| Environment | Google Colab, with nothing to install, or Jupyter in Anaconda on the participant's own computer, as the participant prefers |
| Practice in the Jupyter notebook | Every practice stop has three parts: Python basics for writing the code, ready prompts with which an artificial intelligence (AI) assistant writes it, and the complete ready application |
| Prerequisites | No programming experience and no previous knowledge of AI. A Google account for Colab, or Anaconda installed before Week 1 ([SETUP.md](SETUP.md)) |
| Contact | utkukose@sdu.edu.tr, utkukose@gmail.com |

## Description

The program teaches cardiologists and other specialist physicians to analyse cardiology data with Python and to build, validate and explain AI models. It moves from tables and signals in the first weeks to images, text and data fusion. It ends with explainable models, a prototype of a clinical decision support system and a final project. A virtual cardiology clinic of synthetic patients runs through all weeks, and real public data sets accompany every topic. Coding with AI assistants is taught from the first week under explicit safety rules.

The learning outcomes of the course are listed on the [course home page](README.md#course-learning-outcomes), and each week page lists the outcomes of its week.

## Weekly plan

Each session lasts four hours and has two halves of about two hours. Each week also has a mini project in the session and a weekly project as homework. The plan follows the program of the Turkish Society of Cardiology and is refined as each week is published.

### Week 1: Python and cardiology data basics

The first two hours, an introduction to Python and the Jupyter Notebook environment, cover the introduction and first use of the Anaconda and Jupyter Notebook environment, variables, lists and loops with medical examples, reading and processing a patient table with pandas and a first cardiological plot with Matplotlib. The last two hours work with electrocardiogram (ECG) data. They cover access to the PhysioNet and MIT-BIH data sets, reading and processing ECGs with the wfdb library, R-peak detection with NeuroKit2, the calculation of heart rate variability (HRV) and the visualisation of the 12 leads. The same part treats the ECG as data and measures its intervals automatically. **Mini project in the session:** Loading the Kaggle Heart Disease data set, which comes from the Cleveland data of the UCI Heart Disease collection, statistical summary and visualisation. **Weekly project:** A script that visualises the ECG and calculates its basic measurements, PR, QRS and QT, automatically. **Data:** UCI Heart Disease (Cleveland), MIT-BIH Arrhythmia Database, PTB Diagnostic ECG Database. **Stage of the virtual clinic:** Patient registry and ECG laboratory.

Materials: [Week page](en/week-01/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lab.html) · [Jupyter notebook](en/week-01/NB01_python_and_ecg_basics.ipynb) · [Prompt library](en/week-01/PROMPTS.md) · [PDF notes](en/week-01/Week01_Lecture_Notes.pdf)

### Week 2: Machine learning fundamentals

The first two hours, on classification and regression, cover the modelling pipeline with scikit-learn, logistic regression for the risk of coronary artery disease (CAD), the comparison of a decision tree with a random forest, cross-validation, the area under the receiver operating characteristic curve (ROC-AUC) and the interpretation of sensitivity and specificity. The last two hours, on clustering and patient segmentation, cover finding subgroups of patients with k-means, visualisation with uniform manifold approximation and projection (UMAP) and t-distributed stochastic neighbour embedding (t-SNE), survival analysis with the Kaplan-Meier curve and dealing with imbalanced data with the synthetic minority over-sampling technique (SMOTE). **Mini project in the session:** A CAD prediction model with the Cleveland Heart Disease data set, with ROC curve and AUC analysis. **Weekly project:** HFpEF vs HFrEF patient clustering with Kaplan-Meier survival analysis. **Data:** UCI Heart Disease (Cleveland) and the registry of the virtual clinic with follow-up. **Stage of the virtual clinic:** Risk outpatient clinic.

Materials: [Week page](en/week-02/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lab.html) · [Jupyter notebook](en/week-02/NB02_machine_learning_fundamentals.ipynb) · [Prompt library](en/week-02/PROMPTS.md) · [PDF notes](en/week-02/Week02_Lecture_Notes.pdf)

### Week 3: Deep learning and CNN fundamentals

The first two hours, on artificial neural networks and CNNs, cover the neuron, the layer and the activation function with a medical analogy, a first model with the Keras Sequential API, the convolution operation that finds edges and patterns in an image, and pooling, dropout and batch normalisation. The last two hours, on advanced convolutional neural networks (CNNs) and model evaluation, cover the VGG16 and ResNet50 architectures at the level of ideas, image augmentation for cardiac images, the interpretation of the confusion matrix and the F1 score, and the detection and prevention of overfitting. **Mini project in the session:** Classification of normal and abnormal echocardiograms of the EchoNet-Dynamic data set, with an ejection fraction below 50 percent as abnormal, for participants with a personal registration. **Weekly project:** Cardiac MRI, ACDC data set: Automatic classification of dilated and hypertrophic cardiomyopathy. **Data:** ACDC, cine cardiac magnetic resonance examinations of 90 patients with a normal heart, DCM or HCM, downloaded from their public source; EchoNet-Dynamic, echocardiography videos with a personal registration. **Stage of the virtual clinic:** Imaging laboratory.

Materials: [Week page](en/week-03/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lab.html) · [Jupyter notebook](en/week-03/NB03_deep_learning_and_cnns.ipynb) · [Prompt library](en/week-03/PROMPTS.md) · [PDF notes](en/week-03/Week03_Lecture_Notes.pdf)

### Week 4: Transfer learning: Adapting ready-made power to cardiology

The first two hours, on the principles of transfer learning, cover the models pretrained on ImageNet, EfficientNet and DenseNet, the choice between feature extraction and fine-tuning, the replacement of the last layers for cardiac targets and the ways to reach a high performance with little data. The last two hours, on segmentation and measurement automation, cover the U-Net architecture for cardiac segmentation, the automatic measurement of the left ventricular ejection fraction (EF) with Simpson's method, pixel-wise segmentation training and the methodology of clinical validation. **Mini project in the session:** Classification of cardiomyopathy from few labelled images with EfficientNet-B0: the groups of ACDC on cine cardiac magnetic resonance, and a reduced against a normal EF on the echocardiograms of CAMUS, which carry no cardiomyopathy labels. **Weekly project:** Left ventricular segmentation with the CAMUS data set and automatic calculation of the EF. **Data:** ACDC from Week 3. CAMUS, the apical two-chamber and four-chamber echocardiograms of 500 patients with expert outlines, of which the course downloads 300 from their public source. The ImageNet weights of EfficientNet-B0. **Stage of the virtual clinic:** Echo measurement: Automatic ejection fraction.

Materials: [Week page](en/week-04/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-04/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-04/lab.html) · [Jupyter notebook](en/week-04/NB04_transfer_learning.ipynb) · [Prompt library](en/week-04/PROMPTS.md) · [PDF notes](en/week-04/Week04_Lecture_Notes.pdf)

### Week 5: Time series analysis and ECG artificial intelligence

The first two hours, on ECG analysis with 1D CNN and LSTM, cover the modelling of the ECG as a time series, one-dimensional convolutional networks (1D CNN) for the detection of arrhythmias such as AF, VT and SVT, the LSTM for temporal dependencies and multi-label classification. The last two hours, on advanced ECG models and clinical integration, cover the automatic detection of ST elevation and depression in acute myocardial infarction (AMI), a QTc prolongation risk algorithm, Holter analysis as long-term monitoring with artificial intelligence and an overview of FDA/CE-approved ECG products with artificial intelligence. **Mini project in the session:** PhysioNet 2020 Challenge: Detection of nine rhythm disorders from the 12-lead ECG. The nine classes of CPSC 2018 are learned on the PTB-XL part of the Challenge by a one-dimensional convolutional network, with the AUC of every class on fold 10. **Weekly project:** STEMI alarm system: Automatic detection of ST deviation from AMI ECGs (PTB-XL). **Data:** PTB-XL, 8,737 12-lead ECGs of four folds downloaded from PhysioNet; a synthetic 24-hour Holter recording and the ECGs of the virtual clinic. **Stage of the virtual clinic:** Rhythm and STEMI alarm.

Materials: [Week page](en/week-05/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lab.html) · [Jupyter notebook](en/week-05/NB05_time_series_and_ecg_ai.ipynb) · [Prompt library](en/week-05/PROMPTS.md) · [PDF notes](en/week-05/Week05_Lecture_Notes.pdf)

### Week 6: NLP and clinical text mining

The first two hours, on NLP fundamentals and clinical text processing, cover tokenization and lemmatization, the concepts of TF-IDF and word embedding, BERT and BioBERT loaded from the Hugging Face Hub and Turkish medical language models such as BERTurk. The last two hours, on advanced clinical NLP applications, cover named entity recognition (NER) of drugs, diagnoses and procedures, the automatic summarisation of radiology reports, the detection of eligibility for clinical trials and, as a concept, clinical assistants built on large language models (LLM). **Mini project in the session:** Automatic extraction of diagnoses (STEMI, AF, HF) from synthetic Turkish discharge summaries: An NER pipeline. **Weekly project:** Cardiac angiography report NLP pipeline: Automatic extraction of the degree of stenosis and the affected vessel. **Data:** Synthetic reports of the virtual clinic in Turkish and English. **Stage of the virtual clinic:** Report archive: Clinical text.

Materials: [Week page](en/week-06/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-06/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-06/lab.html) · [Jupyter notebook](en/week-06/NB06_clinical_text_mining.ipynb) · [Prompt library](en/week-06/PROMPTS.md) · [PDF notes](en/week-06/Week06_Lecture_Notes.pdf)

### Week 7: Vision Transformer (ViT): The new generation in image processing

The first two hours, on the attention mechanism and the ViT architecture, cover the limits of CNNs and their lack of global context, self-attention as the relation between different regions of an image, the patch embedding that cuts an image into patches of 16 × 16 pixels, and a vision transformer built with PyTorch next to a ready one loaded from Hugging Face. The last two hours, on hybrid CNN-ViT models and medical imaging, cover the shifted window attention of the Swin Transformer, the hybrid architecture of a CNN backbone and a transformer head, the analysis of coronary angiograms for the detection of stenoses and the visualisation of attention maps with their clinical interpretation. **Mini project in the session:** Training a mini ViT on CIFAR-10, then transfer to EchoNet; participants without a personal registration for EchoNet-Dynamic use the echocardiograms of CAMUS. **Weekly project:** Coronary angiography: Stenosis detection, CNN vs ViT vs hybrid comparison + attention maps. **Data:** Synthetic angiograms of the virtual clinic; ARCADE, 1,500 X-ray coronary angiograms with outlined stenoses downloaded from Zenodo; the echocardiograms of CAMUS; CIFAR-10, 60,000 colour photographs of ten classes from the University of Toronto; EchoNet-Dynamic with a personal registration. **Stage of the virtual clinic:** Catheterisation laboratory.

Materials: [Week page](en/week-07/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lab.html) · [Jupyter notebook](en/week-07/NB07_vision_transformers.ipynb) · [Prompt library](en/week-07/PROMPTS.md) · [PDF notes](en/week-07/Week07_Lecture_Notes.pdf)

### Week 8: Multimodal artificial intelligence and data fusion

The first two hours, on the principles of multimodal AI, cover early fusion against late fusion against hybrid fusion, the combination of different data types in one model, attention-based fusion mechanisms and the management of missing data as the clinical reality. The last two hours, on a cardiovascular risk scoring system, cover the design of an AI model as an alternative to SCORE2 and Framingham, an early warning model for suspected ACS, the fusion of biomarkers, clinical variables and imaging, and the importance of calibration and confidence intervals. **Mini project in the session:** Heart failure risk classification with a fusion model of the ECG signal, echocardiography and laboratory values. **Weekly project:** Real-time MACE prediction model: Simulation of a triage scenario (synthetic MIMIC-IV). **Data:** The registry of the virtual clinic with follow-up, and its chest pain unit at two hospitals: clinical tables, triage notes, 12-lead ECGs, troponins and echocardiograms of the same synthetic presentations. **Stage of the virtual clinic:** Heart team: Data fusion.

Materials: [Week page](en/week-08/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lab.html) · [Jupyter notebook](en/week-08/NB08_multimodal_ai_and_data_fusion.ipynb) · [Prompt library](en/week-08/PROMPTS.md) · [PDF notes](en/week-08/Week08_Lecture_Notes.pdf)

### Week 9: Model reliability and explainable artificial intelligence (XAI)

The first two hours, on explainable AI methods, cover the black box problem and why clinicians do not trust it, SHAP values that show how much each feature contributed, LIME with its local explanations and Grad-CAM, which shows where a CNN looks. The last two hours, on AI reliability and clinical validation, cover the pitfalls of a distribution shift (data drift), model calibration and a confidence score, the detection of bias by sex, age and ethnicity, and the legal and ethical framework of GDPR and the Turkish Law on the Protection of Personal Data (KVKK). **Mini project in the session:** SHAP in a CAD prediction model: Which clinical factor (LDL, age, EF?) influences the model most? **Weekly project:** Visualising with Grad-CAM where an echocardiography model looks, compared with the reading of an expert. **Data:** The Cleveland data of Week 2, the registry of the virtual clinic with LDL, age and the ejection fraction, the 300 patients of CAMUS of Week 4 and the chest pain unit of the virtual clinic at two hospitals. **Stage of the virtual clinic:** Quality and safety committee: XAI.

Materials: [Week page](en/week-09/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-09/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-09/lab.html) · [Jupyter notebook](en/week-09/NB09_reliability_and_explainable_ai.ipynb) · [Prompt library](en/week-09/PROMPTS.md) · [PDF notes](en/week-09/Week09_Lecture_Notes.pdf)

### Week 10: Clinical decision support systems (CDSS)

The first two hours, on CDSS design principles, cover what a clinical decision support system (CDSS) is and its integration into the clinical workflow, web interface development with Streamlit, an introduction to the HL7 FHIR standard (conceptual) and a real-time prediction API with Flask and FastAPI. The last two hours, on deployment and publishing, cover model versioning and the update strategy, human oversight in clinical AI (human-in-the-loop), an introduction to the FDA De Novo and CE MDR processes, and patient consent and data privacy under the Turkish Law on the Protection of Personal Data (KVKK). **Mini project in the session:** AF detection CDSS: Upload an ECG → the model predicts → SHAP shows the explanation → a report is produced. **Weekly project:** User test session: Improving the CDSS prototype with feedback. **Data:** The MIT-BIH Atrial Fibrillation Database and the telemetry ward of the virtual clinic, with an ECG file of one hour of VC-0128. **Stage of the virtual clinic:** Decision support at the bedside.

Materials: [Week page](en/week-10/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-10/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-10/lab.html) · [Jupyter notebook](en/week-10/NB10_clinical_decision_support.ipynb) · [Prompt library](en/week-10/PROMPTS.md) · [PDF notes](en/week-10/Week10_Lecture_Notes.pdf)

### Week 11: Final project and graduation

The first two hours, on final project development, cover the problem selection, a real question from the participant's own clinic, the data preparation and the model selection, the model training, optimisation and XAI integration, and the design of the evaluation of clinical validity. The last two hours, on presentation, closing and discussions of the future, hold the final project presentations of 5 to 7 minutes per person, the evaluation by the jury and the participants, the certificate ceremony, and the career paths and resources in cardiology AI. **Mini project in the session:** Personal or group final project: An end-to-end AI pipeline on a real cardiology problem. **Weekly project:** Final project presentation and the personal action plan "How will I use AI in my clinical practice?". **Data:** Chosen by each participant (see the final project page). **Stage of the virtual clinic:** Own units: Final projects.

Materials: [Week page](en/week-11/README.md) · [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-11/lecture.html) · [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-11/lab.html) · [Jupyter notebook](en/week-11/NB11_final_project_workshop.ipynb) · [Prompt library](en/week-11/PROMPTS.md) · [PDF notes](en/week-11/Week11_Lecture_Notes.pdf)

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

Generative AI tools are allowed in this course and are part of its teaching. Four rules apply. First, no patient data enter a prompt: no names, dates of birth, hospital numbers or recordings of real patients. Second, every use of an AI tool for a weekly or final project is recorded in the AI usage log, with the tool, the prompt, what was checked and what was changed. Third, the participant is responsible for every line of submitted code and must be able to explain it. Code written with an assistant is checked with the code safety checklist before its results are used. Fourth, the interpretation and the discussion in the reports are the participant's own. An assistant may help with the language, and such help is recorded in the log as well. The [prompts](PROMPT_PATH.md) of the Jupyter notebooks follow the same rules, and code written with them is assessed like code typed by hand.

## Data protection and ethics

The course uses synthetic data and public research data only. Real patient data from the participant's institution may be used in the final project only with the permission of the institution and, where required, the approval of an ethics committee. Such data are processed on a computer of the institution in line with the Turkish Law on the Protection of Personal Data (KVKK) [1]. They never enter a cloud service or an AI chat. The synthetic patients of the virtual clinic are teaching material and are not for clinical use.

## Attendance

The certificate requires attendance of at least 80 percent of the sessions, that is, at least 9 of the 11 sessions. A participant who misses a session follows the week with its study path, which gives the times for self-study.

## Materials and environment

Each week has a week page with links to its lecture page, interactive lab, Jupyter notebook, prompt library and PDF notes. [SETUP.md](SETUP.md) explains the two places where the notebooks run, Google Colab and Jupyter on one's own computer, and the [start-here notebook](en/start-here/NB00_start_here.ipynb) introduces a first prompt and the first lines of Python before Week 1. [DATASETS.md](DATASETS.md) lists the data sets with their licenses, and [PYTHON_PATH.md](PYTHON_PATH.md) lists the Python basics of the weeks. [PROMPT_PATH.md](PROMPT_PATH.md) describes how to work with the prompts and the AI assistants that work with them, and [OWN_DATA.md](OWN_DATA.md) explains how to apply the methods of the course to the data of one's own clinic.

## Communication

Questions about the content can be asked in the sessions or by e-mail to utkukose@sdu.edu.tr or utkukose@gmail.com. Errors in the materials can be reported in the [issues](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/issues) of the repository.

## References

1. Kişisel Verilerin Korunması Kanunu [Law on the Protection of Personal Data], Law No. 6698. (2016). *Resmî Gazete, 29677 (7 April 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5
---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
