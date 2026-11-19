> **Türkçe:** Bu eğitim Türkçe yürütülmektedir. **[Bu haftanın Türkçe sayfasına geçin](../../tr/hafta-08/README.md)**

<div align="center">

# Week 8: Multimodal artificial intelligence and data fusion

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology

*From five kinds of data in a chest pain unit to a calibrated risk of major adverse cardiac events, at the bedside and at another hospital*

[Course home](../../README.md) · [Syllabus](../../SYLLABUS.md) · [Setup](../../SETUP.md) · [Türkçe](../../tr/hafta-08/README.md)

</div>

## About the week

The virtual clinic opens a chest pain unit, and its heart team brings five kinds of data together: the clinical table, the triage note, the 12-lead ECG, two troponins and a bedside echocardiogram. Early fusion puts all features side by side, late fusion combines the probabilities of single models, and hybrid and attention-based fusion learn a joint representation, with masks for missing modalities. In the mini project, fusing the ECG, the echocardiogram and the laboratory values adds nothing measurable over the laboratory alone for heart failure events (AUC 0.830 against 0.849). In the chest pain unit, fusion reaches an AUC of 0.914 for major adverse cardiac events within 30 days, above the troponin alone (0.883) and close to the HEART score (0.903). The second half asks whether the probabilities can be trusted: calibration on the test set and at a second hospital, where the model ranks the patients as well but underestimates their risk until it is updated with local patients, intervals for every difference, and thresholds for discharge compared with HEART 0 to 3. The week closes with the review of a fusion pipeline written by an AI assistant.

4 hours in the session and about 3 hours for the weekly project.

## The route of the week

The lecture page is the main route of the week. It holds no code and no prompts, and it is read from top to bottom together with the interactive lab. At each practice stop, every participant chooses one of two paths in the Jupyter notebook: the **prompt path** (Part 1), on which an artificial intelligence (AI) assistant writes the code from ready prompts and the participant runs and checks it, or the **Python path** (Part 2), on which the participant writes the code. Both paths reach the same results. The notebook runs in Google Colab, with nothing to install, or in Jupyter on your own computer ([setup](../../SETUP.md)).

| Main route: lecture page and interactive lab | Practice stop | Prompt path (Part 1) | Python path (Part 2) |
|---|---|---|---|
| [The data of a heart team: The chest pain unit of the virtual clinic](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#the-data-of-a-heart-team-the-chest-pain-unit-of-the-virtual-clinic)<br>[Early, late and hybrid fusion](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#early-late-and-hybrid-fusion)<br>[Attention-based fusion: Modalities as tokens](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#attention-based-fusion-modalities-as-tokens)<br>[Missing modalities](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#missing-modalities) | **[Stop 1: Heart failure events from the ECG, the echocardiogram and the laboratory](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#stop-1)** | Stop 1 | Python step 8 and Sections 1 to 3 |
| [A risk model for triage: HEART and the fused models](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#a-risk-model-for-triage-heart-and-the-fused-models)<br>[Calibration: Do the probabilities mean what they say?](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#calibration-do-the-probabilities-mean-what-they-say)<br>[Intervals: How sure is a difference?](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#intervals-how-sure-is-a-difference) | **[Stop 2: Major adverse cardiac events in the chest pain unit: HEART, single modalities and fusion](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#stop-2)** | Stop 2 | Sections 4 to 8 |
| [Another hospital: Drift and recalibration](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#another-hospital-drift-and-recalibration)<br>[Thresholds for discharge and net benefit](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#thresholds-for-discharge-and-net-benefit) | **[Stop 3: Triage: another hospital, a threshold for discharge and net benefit](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#stop-3)** | Stop 3 | Sections 9 and 10 |
| [Working with an AI assistant, part 8: Reviewing a fusion pipeline](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#ai-pair-programming-part-8-reviewing-a-fusion-pipeline)<br>[The paper of the week](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#the-paper-of-the-week)<br>[The virtual clinic, stage 8: Heart team](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#the-virtual-clinic-stage-8-heart-team) | The section on your own data, the paper of the week and the virtual clinic | – | – |

## Materials

| Material | Open | What it holds |
|---|---|---|
| **Lecture page (main route)** | [Open the lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html) | The case, the concepts with worked examples, a three-dimensional (3D) scene of the patients in the space of three modality scores, two animations, knowledge checks, three practice stops, the section on your own data, review cards and references. No code and no prompts. |
| **Interactive lab** | [Open the interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lab.html) | Parts A to F without code, including the prompt workshop of Part F, a self-assessment, a reflection and the learning log to export |
| **Jupyter notebook** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-08/NB08_multimodal_ai_and_data_fusion.ipynb)<br>[Download for Jupyter](NB08_multimodal_ai_and_data_fusion.ipynb) | Part 1, the prompt path: three stops with eleven steps, each with a ready prompt, a data cell for its table, a cell for the code of the AI assistant, an automatic check and ready code, and the weekly project in four prompts. Part 2, the Python path: Python step 8, Sections 1 to 10 with Exercises A to J and the challenges of seven fields. |
| **Prompt library** | [PROMPTS.md](PROMPTS.md) | All prompts of the prompt path with a copy button on GitHub, the prompts for repairing and reviewing code and the prompt path of the weekly project |
| **PDF notes** | [Week08_Lecture_Notes.pdf](Week08_Lecture_Notes.pdf) | The lecture page in print form, with its practice stops and the section on your own data |

<table>
<tr><td width="50%"><img src="screenshots/lab_part_a_late_fusion.png" alt="Interactive lab, Part A: the five modality probabilities of a patient combined by the mean of the logits and by stacking, step by step." width="100%"></td><td width="50%"><img src="screenshots/notebook_calibration.png" alt="Jupyter notebook, Section 9: the calibration measures and the reliability curves of early fusion, stacking and the mean of the logits on the test set of hospital A." width="100%"></td></tr>
<tr><td>Interactive lab, Part A: the five modality probabilities of a patient combined by the mean of the logits and by stacking, step by step.</td><td>Jupyter notebook, Section 9: the calibration measures and the reliability curves of early fusion, stacking and the mean of the logits on the test set of hospital A.</td></tr>
<tr><td width="50%"><img src="screenshots/lab_part_d_discharge.png" alt="Interactive lab, Part D: a threshold for discharge over the predicted risks of the test patients, with the share discharged and the missed events next to HEART 0 to 3." width="100%"></td><td width="50%"><img src="screenshots/lecture_fusion.png" alt="Lecture page: four ways to fuse the data of one patient, step by step." width="100%"></td></tr>
<tr><td>Interactive lab, Part D: a threshold for discharge over the predicted risks of the test patients, with the share discharged and the missed events next to HEART 0 to 3.</td><td>Lecture page: four ways to fuse the data of one patient, step by step.</td></tr>
</table>

## The case of the week

Patient CP-3304 is a 58-year-old woman with pressing chest pain, a normal ECG, a rising troponin and a HEART score of 5. How should a program combine what the team knows about her, and can its probabilities be trusted at the bedside and at another hospital?

## Learning outcomes

By the end of the week, participants are expected to explain early, late, hybrid and attention-based fusion with their formulas, to combine the scores of several modalities by hand and to choose a way of handling missing modalities. They should be able to build a multimodal risk model and to compare it with each single modality and with a clinical score such as HEART, with intervals from a bootstrap of patients. They should be able to judge the calibration of a model by its intercept, its slope, its Brier score and a reliability curve, and to update a model for another hospital. Finally, they should be able to choose a threshold for a clinical decision on the validation set, to report its result with intervals and net benefit, and to review a fusion pipeline written by an AI assistant.

## Study path

Participants who attend the session complete the main route and the practice stops there. Participants who follow the week on their own, for example after a missed session, can plan with the times below.

| Step | Activity | Prompt path | Python path |
|---|---|---|---|
| 1 | Read the case of the week and the lecture page up to Practice stop 1, with Parts A and B of the interactive lab, the 3D scene of the patients in the space of three modality scores, the animation of the four ways to fuse and the knowledge checks | 1 hour 15 minutes | 1 hour 15 minutes |
| 2 | Practice stop 1, the mini project of the session: Part 1, Stop 1 on the prompt path, or Python step 8 and Sections 1 to 3 on the Python path | 35 minutes | 1 hour 30 minutes |
| 3 | Read on up to Practice stop 2: the HEART score, calibration with its animation and Part C of the interactive lab, and intervals | 35 minutes | 35 minutes |
| 4 | Practice stop 2: Part 1, Stop 2, or Sections 4 to 8 | 40 minutes | 1 hour 30 minutes |
| 5 | Read on up to Practice stop 3: another hospital and recalibration, and thresholds and net benefit with Part D of the interactive lab | 30 minutes | 30 minutes |
| 6 | Practice stop 3: Part 1, Stop 3, or Sections 9 and 10 | 35 minutes | 45 minutes |
| 7 | Read the review of a fusion pipeline with Parts E and F of the interactive lab, the paper of the week, the stage of the virtual clinic and the section on your own data | 40 minutes | 40 minutes |
| 8 | Take the self-assessment of the interactive lab (tab: Check yourself), write the reflection and export the learning log | 20 minutes | 20 minutes |
| | **Total without the weekly project** | **5 hours 10 minutes** | **7 hours 5 minutes** |
| 9 | Complete the weekly project, on either path | 3 hours | 3 hours |

## Training flow of the session

The four-hour session of the week follows the plan below. It is shared to show how the materials fit together in a live session.

| Time | Activity |
|---|---|
| 0:00 to 0:15 | The case of the week and the route of the week. Every participant opens the notebook in Google Colab or in Jupyter and runs Section 0. Nothing has to be downloaded: The chest pain unit, its ECGs and the registry are drawn on the computer of the participant in less than a minute. |
| 0:15 to 1:00 | Main route: the data of a heart team, early, late and hybrid fusion with the 3D scene, the animation and Part A, attention-based fusion with Part B, and missing modalities. |
| 1:00 to 1:35 | Mini project of the session, Practice stop 1, in two groups, the prompt path and the Python path: heart failure events from the ECG, the echocardiogram and the laboratory values, each alone and fused, and the bootstrap of the difference. |
| 1:35 to 1:50 | Break. |
| 1:50 to 2:35 | Main route: the HEART score, calibration with its animation and Part C, and intervals. Practice stop 2: HEART, single modalities and fusion for MACE in the chest pain unit, and the calibration of two kinds of late fusion. |
| 2:35 to 3:20 | Main route: another hospital and recalibration, and thresholds and net benefit with Part D. Practice stop 3: the update at hospital B, a threshold for discharge against HEART 0 to 3 and net benefit. |
| 3:20 to 4:00 | The review of a fusion pipeline with Parts E and F, the paper of the week, the chest pain unit of the virtual clinic, the section on your own data and the weekly project. |

## Weekly project

**What to do.** Build a model for major adverse cardiac events (MACE) within 30 days from the five modalities of the chest pain unit and judge it as a heart team would before using it. First, fit a logistic regression on each modality alone and one on all of them together (early fusion), with the regularisation chosen on the validation set, and give their test AUCs with 95 percent intervals from 2,000 bootstrap samples of the test patients, together with the difference of each to the HEART score in the same samples. Second, judge the calibration of early fusion on the test set by its intercept, its slope, its Brier score and a reliability curve of ten groups; then do the same at hospital B for the 700 patients after its first 300, before and after an update of the intercept learned on the first 300. Third, choose two thresholds for discharge on the validation set, one that sends home as many patients as HEART 0 to 3 and one that keeps the sensitivity at 98 percent, and report for each, on the test set and at hospital B, the share discharged and the MACE among the discharged with Wilson intervals, next to HEART 0 to 3. Fourth, draw the decision curve of the model and of the rule "admit every patient with HEART 4 or more" for threshold probabilities from 1 to 30 percent, and write half a page for a heart team on whether the model should be used, for which decision and with what local check.

**Where to look.** Lecture: sections "Calibration: Do the probabilities mean what they say?", "Another hospital: Drift and recalibration" and "Thresholds for discharge and net benefit". Interactive lab: Parts C and D. Jupyter notebook: Part 1, Stops 2 and 3, or Part 2, Sections 4 to 10.

**Prompt path.** The project can also be built with four prompts, one for each step, from the [prompt library](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-08/PROMPTS.md#prompt-path-of-the-weekly-project). The section "Weekly project on the prompt path" at the end of Part 1 of the Jupyter notebook prepares the table of each prompt. The test of each prompt must hold before the next prompt is used.

**Example.** With the threshold that sends home as many validation patients as HEART 0 to 3, early fusion of the course sent home 388 of the 800 test patients, and 9 of them had a MACE: $9/388 = 0.023$. HEART 0 to 3 sent home 380 with 8 events, $8/380 = 0.021$. With 800 test patients, the two rules cannot be told apart for the decision to discharge.

**What to submit.** A report of one to two pages in the [report template](../templates/Report_Template.docx), with the table of the models and their intervals, the calibration measures and the reliability curves at both hospitals, the table of the two thresholds with HEART 0 to 3, the decision curve and the half page for the heart team. Add the AI usage log (tool, prompt, what was checked, what was changed) and the Jupyter notebook with its outputs.

**Submission.** The weekly project is submitted before the session of Week 9 by e-mail to utkukose@sdu.edu.tr or utkukose@gmail.com. The e-mail holds the items listed under What to submit and the learning log exported from the interactive lab. Weekly projects count for 40 percent of the assessment, and the rubric is in the syllabus.

## With your own data

The lecture page closes with a section on applying the methods of the week to your own data: which question fits which method, what to check first, the approval of the ethics committee, the Turkish Law on the Protection of Personal Data (KVKK) and where to compute. [Read it on the lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#with-your-own-data).

## Optional research assignment

Search PubMed for one study, published in 2020 or later, that combined two or more kinds of cardiac data in one model, such as the ECG, images, laboratory values or clinical notes. Summarise it in half a page: the modalities, how they were fused (early, late, hybrid or attention), how missing modalities were handled, the outcome and the reference, the comparison with each modality alone and with a clinical score, whether calibration was reported, and whether the test came from another hospital. The three questions of [the paper of the week](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#the-paper-of-the-week) can guide the summary. The assignment is not graded, and it prepares the half page of the weekly project.

## The virtual clinic after this week

In Week 8 the virtual clinic opens a chest pain unit and a heart team: 4,000 presentations at hospital A and 1,000 at hospital B, each with a clinical table, a triage note in Turkish, a 12-lead ECG, two troponins and, for about half of the patients, a bedside echocardiogram. The results are in the section [The virtual clinic, stage 8](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#the-virtual-clinic-stage-8-heart-team) of the lecture page.

## Next week

**Week 9: Model reliability and explainable artificial intelligence.** The quality and safety committee asks why a model says what it says: Grad-CAM maps of the echo model compared with the reading of an expert. See the [plan of the course](../../README.md#the-eleven-weeks).

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
