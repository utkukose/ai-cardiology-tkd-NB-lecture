> **Türkçe:** Bu eğitim Türkçe yürütülmektedir. **[Bu haftanın Türkçe sayfasına geçin](../../tr/hafta-05/README.md)**

<div align="center">

# Week 5: Time series analysis and ECG artificial intelligence

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology

*Automatic diagnosis from the ECG: Full analysis of the 12 leads*

[Course home](../../README.md) · [Syllabus](../../SYLLABUS.md) · [Setup](../../SETUP.md) · [Türkçe](../../tr/hafta-05/README.md)

</div>

## About the week

The first two hours analyse the electrocardiogram (ECG) with 1D CNN and LSTM. The ECG is modelled as a time series, twelve leads of numbers in their order, on the 12-lead ECGs of PTB-XL, a public collection of 21,799 clinical recordings. A rule from RR intervals detects atrial fibrillation (AF) as a cardiologist would, a one-dimensional convolutional network (1D CNN) learns several rhythm labels at once, and the features that separate AF, ventricular tachycardia (VT) and supraventricular tachycardia (SVT) are traced on the ECG and in synthetic recordings. A GRU and an LSTM read the RR intervals as a sequence, and the mini project detects the nine classes of the PhysioNet 2020 Challenge with multi-label classification. The last two hours turn to advanced ECG models and clinical integration: the automatic detection of ST elevation and depression in acute myocardial infarction (AMI) as a STEMI alarm, a QTc prolongation risk algorithm, Holter analysis of a synthetic 24-hour recording of the virtual clinic, and an overview of FDA/CE-approved ECG products with artificial intelligence (AI). The week closes with the review of a time-series pipeline written by an AI assistant.

4 hours in the session and about 3 hours for the weekly project.

## The case of the week

Record 13913 of PTB-XL, a man of 68 years with sinus tachycardia and an acute anterior and lateral infarction. Which rhythm does a program report from the 12,000 numbers of the recording, does it raise a STEMI alarm, and how often is such an alarm right?

## Materials

| Material | Open | What it is for |
|---|---|---|
| **Lecture page** | [Open the lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html) | The teaching of the week. It is read from top to bottom, leads to the practice stops and holds no code and no prompts. |
| **Interactive lab** | [Open the interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lab.html) | Parts A to F, without code, open where the lecture page reaches them. Part F is the prompt workshop. The self-assessment and the learning log are in the lab too. |
| **Jupyter notebook** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-05/NB05_time_series_and_ecg_ai.ipynb)<br>[Download for Jupyter](NB05_time_series_and_ecg_ai.ipynb) | The practice stops are worked here: Part 1 is the prompt path and Part 2 the Python path. The notebook runs in Google Colab with nothing to install, or in Jupyter on your own computer. |
| **Prompt library** | [PROMPTS.md](PROMPTS.md) | Every prompt of the prompt path and of the weekly project, with prompts for repairing, explaining and reviewing code. On GitHub, each prompt has a copy button. |
| **PDF notes** | [Week05_Lecture_Notes.pdf](Week05_Lecture_Notes.pdf) | The printable version of the lecture page. |

## Study path

The lecture page is read from top to bottom, and it opens the parts of the interactive lab where they belong. At each practice stop, the work continues in the Jupyter notebook on one of two paths. On the **prompt path** (Part 1 of the notebook), an AI assistant writes the code from ready prompts, and the participant runs it and checks the result. On the **Python path** (Part 2), participants write the code themselves. Both paths reach the same results. At the end of every lab part and of every stop in the Jupyter notebook, a link takes you back to the lecture page, to the place where reading continues. If you lose your place, come back to this table. Participants who attend the session complete the steps there. The times help those who follow the week on their own, for example after a missed session.

| Step | What to do | Prompt path (Part 1) | Python path (Part 2) |
|---|---|---|---|
| 1 | [Read](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html) the case of the week and the first two hours of the lecture page up to Practice stop 1: the ECG as a time series, 1D CNN for AF, VT and SVT, LSTM, multi-label classification and the mini project, with Parts A, B and C of the interactive lab and the knowledge checks | 1 hour 10 minutes | 1 hour 10 minutes |
| 2 | **[Practice stop 1: Mini project: Rhythm, from a rule to the nine classes of the PhysioNet 2020 Challenge](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#stop-1)** | Part 1, Stop 1 ([prompts](PROMPTS.md#stop-1-mini-project-rhythm-from-a-rule-to-the-nine-classes-of-the-physionet-2020-challenge))<br>35 minutes | Python step 5, Sections 1 to 5, with the nine classes of the PhysioNet 2020 Challenge at the end of Section 4<br>1 hour 50 minutes |
| 3 | [Read on](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#last-two-hours-advanced-ecg-models-and-clinical-integration) up to Practice stop 2: the automatic detection of ST elevation and depression in AMI with the 3D scene, and the automatic ST measurement, with Part D of the interactive lab | 40 minutes | 40 minutes |
| 4 | **[Practice stop 2: ST elevation: the median beat, the J point and the alarm](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#stop-2)** | Part 1, Stop 2 ([prompts](PROMPTS.md#stop-2-st-elevation-the-median-beat-the-j-point-and-the-alarm))<br>25 minutes | Sections 6 and 7<br>50 minutes |
| 5 | [Read on](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#qt-prolongation-and-its-risk) up to Practice stop 3: the QTc prolongation risk algorithm and Holter analysis, with the animation of the Holter recording | 35 minutes | 35 minutes |
| 6 | **[Practice stop 3: Long-term monitoring: windows, AF burden and false alarms](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#stop-3)** | Part 1, Stop 3 ([prompts](PROMPTS.md#stop-3-long-term-monitoring-windows-af-burden-and-false-alarms))<br>20 minutes | Sections 8 and 9<br>45 minutes |
| 7 | [Read](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#ecg-algorithms-with-regulatory-approval) the overview of FDA/CE-approved ECG products, the review of a time-series pipeline with Parts E and F of the interactive lab, the paper of the week, the stage of the virtual clinic and the section on your own data; on the Python path, Section 10 as well | 40 minutes | 55 minutes |
| 8 | Take the self-assessment of [the interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lab.html) (tab: Check yourself), write the reflection and export the learning log | 20 minutes | 20 minutes |
| | **Total without the weekly project** | **4 hours 45 minutes** | **7 hours 5 minutes** |
| 9 | Complete [the weekly project](#weekly-project), on either path | [Prompts](PROMPTS.md#prompt-path-of-the-weekly-project)<br>3 hours | 3 hours |

<table>
<tr><td width="50%"><img src="screenshots/lab_part_b_rr_rule.png" alt="Interactive lab, Part B: the coefficients of variation of the test fold with the threshold of the rule for AF, the alarms, the sensitivity, the specificity and the positive predictive value, and the RR intervals of a recording with ventricular premature complexes." width="100%"></td><td width="50%"><img src="screenshots/notebook_12lead_case.png" alt="Jupyter notebook, Section 1: the 12-lead ECG of the case of the week from PTB-XL." width="100%"></td></tr>
<tr><td>Interactive lab, Part B: the coefficients of variation of the test fold with the threshold of the rule for AF, the alarms, the sensitivity, the specificity and the positive predictive value, and the RR intervals of a recording with ventricular premature complexes.</td><td>Jupyter notebook, Section 1: the 12-lead ECG of the case of the week from PTB-XL.</td></tr>
<tr><td width="50%"><img src="screenshots/lab_part_d_st.png" alt="Interactive lab, Part D: the median beats of the twelve leads of the case with the PR level and the J point, and the decision of the STEMI alarm." width="100%"></td><td width="50%"><img src="screenshots/lecture_holter_windows.png" alt="Lecture page: the windows of the 24-hour Holter recording of the virtual clinic, with the threshold of the alarm and its false alarms." width="100%"></td></tr>
<tr><td>Interactive lab, Part D: the median beats of the twelve leads of the case with the PR level and the J point, and the decision of the STEMI alarm.</td><td>Lecture page: the windows of the 24-hour Holter recording of the virtual clinic, with the threshold of the alarm and its false alarms.</td></tr>
</table>

## Weekly project

**Project.** STEMI alarm system: Automatic detection of ST deviation from AMI ECGs (PTB-XL).

**What to do.** Build an automatic STEMI alarm on the 12-lead ECGs of PTB-XL and judge it as a chest pain unit would. First, measure the ST deviation at the J point of the twelve leads on the median beat of every recording of folds 9 and 10. Second, apply the criteria of the universal definition: the cut-points of V2 and V3 by sex and age, 1 mm in the other leads and the three lead groups; the alarm fires when two leads of one group reach their cut-points. Third, compare the alarm with the acute myocardial infarctions of the two folds, the recordings whose infarction stage is Stadium I or Stadium I-II. Report the sensitivity, the specificity and the positive predictive value, and count the false alarms by the statements of the recording, for example left bundle branch block, left ventricular hypertrophy and a normal ECG. Fourth, show the three missed infarctions and the three false alarms with the largest ST elevation as median beats, and write in half a page what the alarm would need before it could run in an emergency department.

**Where to look.** Lecture: section "Automatic detection of ST elevation/depression (AMI)", with its subsections "ST elevation and depression: The criteria of the universal definition" and "Measuring the ST segment automatically: The median beat and the J point". Interactive lab: Part D. Jupyter notebook: Part 1, Stop 2, or Part 2, Sections 6 and 7.

**Prompt path.** The project can also be built with four prompts, one for each step, from the [prompt library](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-05/PROMPTS.md#prompt-path-of-the-weekly-project). The section "Weekly project on the prompt path" at the end of Part 1 of the Jupyter notebook prepares the table of each prompt. The test of each prompt must hold before the next prompt is used.

**Example.** Suppose the alarm fires in 30 of 40 acute infarctions and in 60 of 4,000 other recordings. The sensitivity is $30/40 = 0.75$, the specificity $(4000 - 60)/4000 = 3940/4000 = 0.985$ and the positive predictive value $30/(30 + 60) = 0.333$: Two of three alarms would be false, although the alarm is right in 98.5 percent of the recordings without an infarction.

**What to submit.** A report of one to two pages in the [report template](../templates/Report_Template.docx), with the table of the sensitivity, the specificity and the positive predictive value, the count of the false alarms by statement, the figure of the six median beats and the half page on what the alarm would need. Add the AI usage log (tool, prompt, what was checked, what was changed) and the Jupyter notebook with its outputs. Figures with ECGs of PTB-XL carry the credit "PTB-XL, CC BY 4.0".

**Submission.** The weekly project is submitted before the session of Week 6 by e-mail to utkukose@sdu.edu.tr or utkukose@gmail.com. The e-mail holds the items listed under What to submit and the learning log exported from the interactive lab. Weekly projects count for 40 percent of the assessment, and the rubric is in the syllabus.

## Learning outcomes

By the end of the week, participants are expected to model an ECG as a time series, to explain its sampling frequency and its labels, and to keep the recordings of one patient in one set. They should be able to detect AF with a rule from RR intervals, to explain one-dimensional convolution and its receptive field, and to tell AF, VT and SVT apart by the regularity of the RR intervals, the width of the QRS complex and the P waves. They should be able to explain how the gates of an LSTM and a GRU capture temporal dependencies, and to judge a multi-label network label by label, with thresholds chosen on a validation set, as in the nine classes of the PhysioNet 2020 Challenge. Finally, they should be able to measure the ST segment on a median beat, to apply the criteria of ST elevation of the universal definition as an alarm and to judge its false alarms, to compute a QTc prolongation risk score, to read a 24-hour recording in windows, and to name what the approval of an ECG product covers.

## Training flow of the session

The four-hour session of the week follows the plan below. It is shared to show how the materials fit together in a live session.

| Time | Activity |
|---|---|
| 0:00 to 0:15 | The case of the week and the route of the week. Every participant opens the notebook in Google Colab or in Jupyter and runs Section 0. It downloads the 12-lead ECGs of four folds of PTB-XL at 100 Hz, about 216 MB, from PhysioNet. |
| 0:15 to 0:55 | First two hours, ECG analysis with 1D CNN and LSTM: the ECG modelled as a time series, a rule for AF from RR intervals with Part B, one-dimensional convolution with Part A, AF, VT and SVT on the ECG and in the network, the LSTM and the GRU, and multi-label classification with Part C of the interactive lab. |
| 0:55 to 1:45 | Mini project of the session, Practice stop 1, in two groups, the prompt path and the Python path: The PhysioNet 2020 Challenge and its nine classes. A one-dimensional network learns the rhythm labels of PTB-XL in about two minutes, its thresholds are chosen on fold 9 and it is compared with the rule on fold 10; on the Python path, the end of Section 4 trains it for the nine classes of the Challenge. |
| 1:45 to 2:00 | Break. |
| 2:00 to 2:35 | Last two hours, advanced ECG models and clinical integration: the automatic detection of ST elevation and depression in AMI, with the 3D scene, the criteria of the universal definition, and the median beat and the J point with Part D. Practice stop 2: the ST deviation of the case and the alarm on the test fold. |
| 2:35 to 3:20 | The QTc prolongation risk algorithm, and Holter analysis with the 24-hour recording of the virtual clinic. Practice stop 3: the risk score of four inpatients, windows, the AF burden and the false alarms of one day. |
| 3:20 to 4:00 | An overview of FDA/CE-approved ECG AI products, the review of a time-series pipeline with Parts E and F, the paper of the week, the rhythm and STEMI alarm of the virtual clinic, the section on your own data and the weekly project. |

## With your own data

The lecture page closes with a section on applying the methods of the week to your own data: which question fits which method, what to check first, the approval of the ethics committee, the Turkish Law on the Protection of Personal Data (KVKK) and where to compute. [Read it on the lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#with-your-own-data).

## Optional research assignment

Search PubMed for one study, published in 2020 or later, that detected atrial fibrillation or an acute myocardial infarction automatically on ECGs and compared the algorithm with cardiologists. Summarise it in half a page: the patients, the hospitals and the devices, the reference and how many readers gave it, the sensitivity, the specificity and the positive predictive value, the prevalence in the test set, and whether the test came from another hospital. The three questions of [the paper of the week](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#the-paper-of-the-week) can guide the summary. The assignment is not graded, and it prepares the half page of the weekly project.

## The virtual clinic after this week

In Week 5 the virtual clinic gets a rhythm and STEMI alarm. A one-dimensional network trained on PTB-XL and the criteria of ST elevation read the resting ECGs of the 500 patients of the clinic, and a synthetic 24-hour Holter recording of one patient shows the windows and the false alarms of long-term monitoring. The results are in the section [The virtual clinic, stage 5](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#the-virtual-clinic-stage-5-rhythm-and-stemi-alarm) of the lecture page.

## Next week

**Week 6: NLP and clinical text mining.** The reports of the clinic become data: tokens, word representations and pretrained language models extract diagnoses, drugs and the degree of stenosis from text in Turkish and English. See the [plan of the course](../../README.md#the-eleven-weeks).

---

<div align="center">

**Prof. Dr. Utku Kose**

Full Professor, Department of Computer Engineering, Süleyman Demirel University, Isparta, Türkiye<br>
Founding Director, AI Application and Research Center (YAZEM), Süleyman Demirel University<br>
Head of the Computer Science Division, Department of Computer Engineering, Süleyman Demirel University<br>
Additional affiliations: University of North Dakota (USA), Universidad Panamericana (Mexico City, Mexico), Vel Tech University (Chennai, India)<br>
IEEE Senior Member, ACM Professional Member

[ORCID 0000-0002-9652-6415](https://orcid.org/0000-0002-9652-6415) | [utkukose.com](https://www.utkukose.com) | [github.com/utkukose](https://github.com/utkukose)

[utkukose@sdu.edu.tr](mailto:utkukose@sdu.edu.tr) | [utku.kose@und.edu](mailto:utku.kose@und.edu) | [ukose@up.edu.mx](mailto:ukose@up.edu.mx) | [utkukose@gmail.com](mailto:utkukose@gmail.com)

*First version: November 2026. Content CC BY 4.0, code MIT.*

</div>
