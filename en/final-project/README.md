# Final project

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · Week 11

[Course home](../../README.md) · [Syllabus](../../SYLLABUS.md) · [Türkçe](../../tr/final-projesi/README.md)

## Aim

The final project applies the methods of the course to a question from the participant's own clinical work. It builds an end-to-end pipeline: a clinical question, the data, a model or an analysis, an explanation of its decisions and a plan for its clinical evaluation. The project is presented in the session of Week 11 in 5 to 7 minutes and counts for 40 percent of the assessment. It can be done alone or in a group of two or three participants.

## Options

Seven options are open. Options A to F use synthetic or public data, and Option G uses data of the participant's institution. The last column names the weeks whose Jupyter notebooks give the starting code.

| Option | Question | Data | Starting point |
|---|---|---|---|
| A. ECG | A rhythm or ischaemia question on 12-lead ECGs | The virtual clinic, PTB-XL or the PhysioNet/Computing in Cardiology Challenge 2020 | Weeks 1 and 5 |
| B. Risk | A risk model from clinical variables, with an explanation of its predictions | The virtual clinic or UCI Heart Disease | Weeks 2 and 9 |
| C. Imaging | Classification or segmentation of echocardiograms or cardiac magnetic resonance images | The virtual clinic or a public imaging data set | Weeks 3, 4 and 7 |
| D. Text | Extraction of information from clinical reports | Synthetic reports of the virtual clinic | Week 6 |
| E. Fusion | A model that combines several kinds of data of the same patients | The virtual clinic | Week 8 |
| F. Decision support | A prototype of a clinical decision support system with explanations and a user test | Any of the above | Weeks 9 and 10 |
| G. Own question | A question from the participant's clinic | Institutional data, with the permission of the institution and, where required, ethics committee approval | Any week |

Institutional data are processed only on the participant's own computer, in line with the Turkish Law on the Protection of Personal Data (KVKK). They never enter a cloud notebook or an AI chat, and the report shows only aggregated results.

## What to submit

The submission holds four items. The report has four to six pages, written in the [report template](../templates/Report_Template.docx). It states the clinical question, the data and their source, the methods, the results with a measure of uncertainty, the explanation of the model, the limitations and a plan for the clinical evaluation. It ends with a personal action plan of half a page on how the participant will use AI in clinical practice. The Jupyter notebook or the scripts reproduce every result of the report. The AI usage log records every use of an AI assistant. The slides of the presentation complete the submission.

## Suggested milestones

| Week | Milestone |
|---|---|
| 6 | Choice of the option and a proposal of one paragraph, sent by e-mail |
| 9 | Data prepared and a first result |
| 10 | Explanation of the model and a draft of the presentation |
| 11 | Presentation in the session; the report and the code are sent within one week |

## Rubric

The jury scores the project out of 100 points with the rubric below. The participants also evaluate the presentations, and the jury takes their evaluation into account.

| Criterion | Points |
|---|---|
| Clinical question: clear, relevant and answerable with the data | 15 |
| Data: source, quality, preparation and protection | 15 |
| Methods: correct use of the methods of the course and a sound validation | 25 |
| Results: correct, with a measure of uncertainty and compared with a reference | 15 |
| Explanation and limitations: what the model uses, where it fails and what a clinical evaluation would need | 15 |
| Presentation and reproducibility: clear presentation, a notebook that reproduces the results and a complete AI usage log | 15 |

## Starting code

Each option builds on the Jupyter notebooks of the weeks named in the table of options. A starting notebook for each option is added to this page with the week that teaches its methods.

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · First version: November 2026 · Content CC BY 4.0, code MIT.*
