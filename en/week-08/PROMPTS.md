# Prompt library, Week 8

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 8](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-08/PROMPTLAR.md)

This library holds every prompt of the prompt path of Week 8, Part 1 of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the notebook, into the empty cell of the step of the same number, and runs there. The [guide to the prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [How a step works](#how-a-step-works)
2. [Stop 1: Heart failure events from the ECG, the echocardiogram and the laboratory](#stop-1-heart-failure-events-from-the-ecg-the-echocardiogram-and-the-laboratory)
3. [Stop 2: Major adverse cardiac events in the chest pain unit: HEART, single modalities and fusion](#stop-2-major-adverse-cardiac-events-in-the-chest-pain-unit-heart-single-modalities-and-fusion)
4. [Stop 3: Triage: another hospital, a threshold for discharge and net benefit](#stop-3-triage-another-hospital-a-threshold-for-discharge-and-net-benefit)
5. [Prompts for repairing, explaining and reviewing code](#prompts-for-repairing-explaining-and-reviewing-code)
6. [Prompt path of the weekly project](#prompt-path-of-the-weekly-project)

## How a step works

| Step | What to do |
|---|---|
| 1. Read | Read the goal of the step in the notebook. |
| 2. Prepare the data | Run the data cell under the prompt. It prepares the table "data" that the prompt describes and shows it. |
| 3. Copy and send | Copy the prompt and send it to an AI assistant: Gemini in Google Colab, or ChatGPT, Claude, Copilot or Gemini in another browser tab. |
| 4. Run | Paste the code of the assistant into the cell below the data cell and run it. |
| 5. Check | Run the check cell. It prints *correct* or *not yet* and the value of the result "answer". |
| 6. Repair | If the check prints *not yet*, send the repair prompt with the code. If the result is still wrong, run the *Ready code* cell, which gives the correct result. |
| 7. Explain and log | Ask the assistant to explain the code in plain language, and write the tool, the prompt and what was checked in the AI usage log. |

## Stop 1: Heart failure events from the ECG, the echocardiogram and the laboratory

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#stop-1) · The same result on the Python path: Python step 8, Sections 1 to 3*

This stop is the mini project of the session. The patients of the registry of the virtual clinic are described by three modalities: the ECG, the echocardiogram and the laboratory values. A model is built for each modality alone and for all three together, early and late fusion are compared, and the last step asks how sure the difference between fusion and the best single modality is.

### Step 1.1: The laboratory values alone

**Goal.** Build a first model for heart failure events from the three laboratory values.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how well NT-proBNP, eGFR and troponin alone predict death or
a hospitalisation for heart failure within 24 months, as a baseline for models that add the ECG and
the echocardiogram.
Data: The notebook holds a table named "data" with 3,227 patients of the registry of the virtual
clinic, a synthetic cohort: the patients who were followed for at least 24 months or had an event
before. Each row is a patient: "patient" gives the patient, "set" the set ("training", 1,936
patients; "validation", 640; "test", 651), and "event" is 1 when the patient died or was admitted to
hospital for heart failure within 24 months and 0 otherwise. The ECG gives "heart rate" (per
minute), "QRS" and "QT" (ms), "left bundle branch block" and "atrial fibrillation" (1 when present).
The echocardiogram gives "ejection fraction" (%), "end-diastolic diameter" (mm), "left atrial volume
index" (mL/m²), "E/e'", "TAPSE" (mm) and "LV mass index" (g/m²). The laboratory gives "NT-proBNP"
(pg/mL), "eGFR" (mL/min/1.73 m²) and "troponin" (high-sensitivity, ng/L).
Task: Use the logarithm of NT-proBNP and of troponin, since both are strongly skewed. Use the three
laboratory values as the features. Standardise the columns with the training patients and fit a
logistic regression on the training patients. Choose the amount of regularisation by the area under
the ROC curve (AUC) on the validation patients, trying 0.01, 0.1, 1 and 10 for the inverse of its
strength, and compute the AUC of the chosen model on the test patients.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the chosen strength and the validation and test AUC, and keep the test AUC, with three
decimals, under the name "answer".
Test: The AUC must lie between 0 and 1, and no test patient may be used before the last step.
```

**Expected result:** "answer" = 0.849

### Step 1.2: Early fusion of three modalities

**Goal.** Put the 14 values of the three modalities side by side and fit one model on them.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether a model that sees the ECG, the echocardiogram and
the laboratory values of a patient together predicts heart failure events better than the laboratory
values alone.
Data: The notebook holds a table named "data" with 3,227 patients of the registry of the virtual
clinic, a synthetic cohort: the patients who were followed for at least 24 months or had an event
before. Each row is a patient: "patient" gives the patient, "set" the set ("training", 1,936
patients; "validation", 640; "test", 651), and "event" is 1 when the patient died or was admitted to
hospital for heart failure within 24 months and 0 otherwise. The ECG gives "heart rate" (per
minute), "QRS" and "QT" (ms), "left bundle branch block" and "atrial fibrillation" (1 when present).
The echocardiogram gives "ejection fraction" (%), "end-diastolic diameter" (mm), "left atrial volume
index" (mL/m²), "E/e'", "TAPSE" (mm) and "LV mass index" (g/m²). The laboratory gives "NT-proBNP"
(pg/mL), "eGFR" (mL/min/1.73 m²) and "troponin" (high-sensitivity, ng/L).
Task: Use the logarithm of NT-proBNP and of troponin, since both are strongly skewed. The three
modalities are the ECG (heart rate, QRS, QT, left bundle branch block, atrial fibrillation), the
echocardiogram (ejection fraction, end-diastolic diameter, left atrial volume index, E/e', TAPSE, LV
mass index) and the laboratory (NT-proBNP, eGFR, troponin). Use all 14 values together as the
features of one model. Standardise the columns with the training patients and fit a logistic
regression on the training patients. Choose the amount of regularisation by the area under the ROC
curve (AUC) on the validation patients, trying 0.01, 0.1, 1 and 10 for the inverse of its strength,
and compute the AUC of the chosen model on the test patients.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the chosen strength and the validation and test AUC, and keep the test AUC, with three
decimals, under the name "answer".
Test: The model must use 14 features, and the AUC must lie between 0 and 1.
```

**Expected result:** "answer" = 0.83

### Step 1.3: Late fusion by the mean of the logits

**Goal.** Fit one model for each modality and combine their predictions by the mean of their logits.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to compare a single model on all values with three separate models,
one for each modality, whose opinions are averaged.
Data: The notebook holds a table named "data" with 3,227 patients of the registry of the virtual
clinic, a synthetic cohort: the patients who were followed for at least 24 months or had an event
before. Each row is a patient: "patient" gives the patient, "set" the set ("training", 1,936
patients; "validation", 640; "test", 651), and "event" is 1 when the patient died or was admitted to
hospital for heart failure within 24 months and 0 otherwise. The ECG gives "heart rate" (per
minute), "QRS" and "QT" (ms), "left bundle branch block" and "atrial fibrillation" (1 when present).
The echocardiogram gives "ejection fraction" (%), "end-diastolic diameter" (mm), "left atrial volume
index" (mL/m²), "E/e'", "TAPSE" (mm) and "LV mass index" (g/m²). The laboratory gives "NT-proBNP"
(pg/mL), "eGFR" (mL/min/1.73 m²) and "troponin" (high-sensitivity, ng/L).
Task: Use the logarithm of NT-proBNP and of troponin, since both are strongly skewed. The three
modalities are the ECG (heart rate, QRS, QT, left bundle branch block, atrial fibrillation), the
echocardiogram (ejection fraction, end-diastolic diameter, left atrial volume index, E/e', TAPSE, LV
mass index) and the laboratory (NT-proBNP, eGFR, troponin). For each modality separately:
standardise the columns with the training patients and fit a logistic regression on the training
patients. Choose the amount of regularisation by the area under the ROC curve (AUC) on the
validation patients, trying 0.01, 0.1, 1 and 10 for the inverse of its strength, and compute the AUC
of the chosen model on the test patients. Then turn the three probabilities of every patient into
logits, log(p / (1 − p)), take their mean, turn the mean back into a probability and compute its AUC
on the test patients.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the test AUC of each modality and of their late fusion, and keep the AUC of the late
fusion, with three decimals, under the name "answer".
Test: There must be three models, one for each modality, and the AUC must lie between 0 and 1.
```

**Expected result:** "answer" = 0.833

### Step 1.4: How sure is the difference?

**Goal.** Draw the test patients again and again with replacement and see how often early fusion beats the laboratory alone.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether the difference between a model of three modalities
and the laboratory values alone, measured on a few hundred test patients with few events, would hold
on other patients.
Data: The notebook holds a table named "data" with 3,227 patients of the registry of the virtual
clinic, a synthetic cohort: the patients who were followed for at least 24 months or had an event
before. Each row is a patient: "patient" gives the patient, "set" the set ("training", 1,936
patients; "validation", 640; "test", 651), and "event" is 1 when the patient died or was admitted to
hospital for heart failure within 24 months and 0 otherwise. The ECG gives "heart rate" (per
minute), "QRS" and "QT" (ms), "left bundle branch block" and "atrial fibrillation" (1 when present).
The echocardiogram gives "ejection fraction" (%), "end-diastolic diameter" (mm), "left atrial volume
index" (mL/m²), "E/e'", "TAPSE" (mm) and "LV mass index" (g/m²). The laboratory gives "NT-proBNP"
(pg/mL), "eGFR" (mL/min/1.73 m²) and "troponin" (high-sensitivity, ng/L).
Task: Use the logarithm of NT-proBNP and of troponin, since both are strongly skewed. The three
modalities are the ECG (heart rate, QRS, QT, left bundle branch block, atrial fibrillation), the
echocardiogram (ejection fraction, end-diastolic diameter, left atrial volume index, E/e', TAPSE, LV
mass index) and the laboratory (NT-proBNP, eGFR, troponin). Fit the model of the laboratory values
and the model of all 14 values as follows. Standardise the columns with the training patients and
fit a logistic regression on the training patients. Choose the amount of regularisation by the area
under the ROC curve (AUC) on the validation patients, trying 0.01, 0.1, 1 and 10 for the inverse of
its strength, and compute the AUC of the chosen model on the test patients. Then draw 2,000
bootstrap samples, each drawing as many test patients as there are with replacement. Fix the random
seed to 2026 so that the result can be repeated. In every sample that contains patients with and
without an event, compute the AUC of both models and the difference, early fusion minus the
laboratory. Report the mean difference, its 95 percent interval from the 2.5th to the 97.5th
percentile, and the share of samples in which the difference is above 0.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the mean difference and its interval, and keep the share, with three decimals, under
the name "answer".
Test: The share must lie between 0 and 1, and both models must be compared on the same patients of
every sample.
```

**Expected result:** "answer" = 0.041

## Stop 2: Major adverse cardiac events in the chest pain unit: HEART, single modalities and fusion

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#stop-2) · The same result on the Python path: Sections 4 to 8*

The chest pain unit of the virtual clinic predicts MACE within 30 days. The HEART score sets the bar. A model fuses the clinical table, the troponins and the echocardiogram, a second model stacks five single models, and the last step asks whether the probabilities of two kinds of late fusion can be trusted.

### Step 2.1: The HEART score

**Goal.** Add up the five items of the HEART score and see how well the total separates the presentations with and without a MACE.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants the result of the HEART score on the test presentations of the chest
pain unit, the bar that every model of the unit must clear.
Data: The notebook holds a table named "data" with the 800 test presentations of a chest pain unit
of the virtual clinic, a synthetic data set. Each row is a presentation: "presentation" gives its
number, the five columns "history", "ECG", "age", "risk factors" and "troponin" give the points of
the five items of the HEART score (0, 1 or 2 each), and "MACE" is 1 when a major adverse cardiac
event (myocardial infarction, urgent revascularisation or death) followed within 30 days and 0
otherwise.
Task: Add up the five items into the HEART score (0 to 10). Compute its AUC against the column
"MACE". Then form the groups 0 to 3, 4 to 6 and 7 to 10 and give, for each, the number of
presentations, its share and the share of MACE in it.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the table of the three groups, and keep the AUC, with three decimals, under the name
"answer".
Test: Every score must lie between 0 and 10, and the three groups must hold all 800 presentations.
```

**Expected result:** "answer" = 0.903

### Step 2.2: Early fusion of the clinical table, the troponins and the echocardiogram

**Goal.** Put the clinical values, the troponins and the echocardiogram of every presentation in one row, fill the gaps with a marker, and fit one model.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants a risk model for MACE within 30 days from what the team knows one
hour after arrival, without the ECG and the note, keeping the patients whose second troponin or
echocardiogram is missing.
Data: The notebook holds a table named "data" with the 4,000 presentations with chest pain of a
chest pain unit of the virtual clinic, a synthetic data set. Each row is a presentation:
"presentation" gives its number and "set" its set ("training", 2,400; "validation", 800; "test",
800). The clinical table gives "age" (years), "sex" ("man" or "woman"), seven risk factors that are
1 when present ("smoker", "diabetes", "hypertension", "hyperlipidaemia", "obesity", "family history"
and "known coronary artery disease"), "heart rate" (per minute), "systolic pressure" (mmHg) and
"eGFR". High-sensitivity troponin T is given in multiples of the upper reference limit of the assay:
"troponin at arrival" and "troponin after one hour", which is empty when it was not measured. The
bedside echocardiogram gives "echocardiogram done" (1 or 0), and when it was done "ejection
fraction" (%) and "wall motion abnormality" (1 when a regional abnormality was seen); both are empty
otherwise. "HEART" is the HEART score, and "MACE" is 1 when a major adverse cardiac event followed
within 30 days and 0 otherwise.
Task: Build the features of every presentation: age, sex as 1 for a man, the seven risk factors,
heart rate, systolic pressure and eGFR; the logarithm of the troponin at arrival, the logarithm of
the troponin after one hour (the value at arrival when it was not measured), the change in one hour
(0 when not measured) and a column that is 1 when the second troponin was measured; whether the
echocardiogram was done, the ejection fraction (60 when not done) and the wall motion abnormality (0
when not done). Do not use the HEART score. Standardise the columns with the training presentations
and fit a logistic regression on the training presentations. Choose the amount of regularisation by
the area under the ROC curve (AUC) on the validation presentations, trying 0.01, 0.1, 1 and 10 for
the inverse of its strength, and compute the AUC of the chosen model on the test presentations.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the chosen strength and the validation and test AUC, and keep the test AUC, with three
decimals, under the name "answer".
Test: All 4,000 presentations must be kept, the model must use 19 features, and the HEART score must
not be among them.
```

**Expected result:** "answer" = 0.9

### Step 2.3: Stacking five single models

**Goal.** Learn on the validation presentations how much each of five single models should count, and test the combination.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist has five models, each reading one modality of a presentation with chest
pain, and wants to combine their opinions into one risk with weights learned from data rather than
an equal vote.
Data: The notebook holds a table named "data" with the 800 validation and the 800 test presentations
of a chest pain unit of the virtual clinic, a synthetic data set. Each row is a presentation: "set"
gives its set ("validation" or "test"), and five columns give the probability of a major adverse
cardiac event within 30 days that five models of the course give from one modality each, all trained
on the training presentations: "probability, clinical", "probability, troponin", "probability,
echocardiogram", "probability, ECG network" and "probability, note". "MACE" is 1 when such an event
followed and 0 otherwise.
Task: Turn the five probabilities of every presentation into logits, log(p / (1 − p)). Fit a
logistic regression of MACE on the five logits on the validation presentations only, with the
default regularisation. Report its five weights and its intercept, and compute the AUC of its
probabilities on the test presentations. Compare it with the mean of the five logits.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the weights, the intercept and the test AUC of stacking and of the mean, and keep the
test AUC of stacking, with three decimals, under the name "answer".
Test: Stacking must learn on the validation presentations only, and every weight must be printed.
```

**Expected result:** "answer" = 0.922

### Step 2.4: Can the probabilities be trusted?

**Goal.** Judge the calibration of two models with almost the same AUC: early fusion and the mean of the logits.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to tell patients their risk of MACE and to send home those below a
threshold, and wants to know whether the probabilities of two models that rank the patients equally
well mean what they say.
Data: The notebook holds a table named "data" with the 800 test presentations of a chest pain unit
of the virtual clinic, a synthetic data set. Each row is a presentation: "probability, early fusion"
is the probability of a major adverse cardiac event within 30 days from a model of the course that
uses all five modalities together, "probability, mean of the logits" the probability from the mean
of the logits of five single-modality models, and "MACE" is 1 when such an event followed and 0
otherwise.
Task: For both probability columns, compute the AUC and the mean predicted risk against the share of
MACE. Compute the calibration intercept (the shift of the logits that makes the mean predicted risk
equal to the observed share, with the slope fixed at 1), the calibration slope (a logistic
regression of MACE on the logit of the probability, without regularisation) and the Brier score.
Then draw a reliability curve for each: Sort the presentations by the probability, cut them into ten
groups of equal size, and plot the mean probability of each group against its share of MACE, with
the diagonal.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the AUC, the mean predicted risk, the intercept, the slope and the Brier score of both
models, show the two curves, and keep the calibration slope of the mean of the logits, with two
decimals, under the name "answer".
Test: The two curves must have ten points each, and the Brier scores must lie between 0 and 1.
```

**Expected result:** "answer" = 2.78

## Stop 3: Triage: another hospital, a threshold for discharge and net benefit

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#stop-3) · The same result on the Python path: Sections 9 and 10*

A model that leaves its hospital must be checked where it is used. The first step updates the model at hospital B with its first patients. The second chooses a threshold for discharge on the validation presentations and compares it with HEART 0 to 3 on the test presentations. The last asks for the net benefit of the model and of HEART for the decision to admit.

### Step 3.1: An update for another hospital

**Goal.** Shift the logits of the model so that its mean risk matches the share of events of the first 300 patients of hospital B, and check the next 700.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist of hospital B wants to use a model from hospital A, whose patients and
practice differ, and wants to correct the level of its risks with the first patients of B before
relying on it.
Data: The notebook holds a table named "data" with the 1,000 presentations with chest pain of a
second hospital, B, of the virtual clinic, a synthetic data set, in the order in which they arrived.
Each row is a presentation: "order" gives its place in time, "probability" the probability of a
major adverse cardiac event within 30 days from a model that learned at the first hospital, A, and
"MACE" is 1 when such an event followed and 0 otherwise.
Task: Turn the probabilities into logits. On the first 300 presentations, find the shift that, added
to every logit, makes the mean of the shifted probabilities equal to the share of MACE of these 300
(for example by Newton steps). Add the shift to the logits of all presentations. For the remaining
700, report the mean predicted risk before and after the update, the observed share of MACE and the
AUC before and after.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the shift, the means, the observed share and the two AUCs, and keep the shift, with
two decimals, under the name "answer".
Test: Only the first 300 presentations may be used to find the shift, and the AUC must not change.
```

**Expected result:** "answer" = 0.37

### Step 3.2: A threshold for discharge

**Goal.** Choose on the validation presentations a threshold of the model that sends home as many patients as HEART 0 to 3, and count the MACE among the test patients it sends home.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether discharging by the risk of a model instead of by
HEART 0 to 3, with the same number of patients sent home, would miss fewer major adverse cardiac
events.
Data: The notebook holds a table named "data" with the 800 validation and the 800 test presentations
of a chest pain unit of the virtual clinic, a synthetic data set. Each row is a presentation: "set"
gives its set ("validation" or "test"), "HEART" the HEART score (0 to 10), "probability" the
probability of a major adverse cardiac event within 30 days from a model of the course that uses
five modalities, and "MACE" is 1 when such an event followed and 0 otherwise.
Task: On the validation presentations, count the patients with HEART 0 to 3; call this number k.
Sort the validation presentations by the probability; the threshold is the probability of the k-th
lowest. On the test presentations, send home every patient at or below the threshold, and report the
number sent home, the MACE among them, their share with a 95 percent Wilson interval, and the
sensitivity for MACE. Report the same for HEART 0 to 3 on the test presentations.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the threshold and both results, and keep the number of MACE among the test patients
sent home by the model under the name "answer".
Test: The threshold must come from the validation presentations only, and the number sent home by
the model must be close to that of HEART.
```

**Expected result:** "answer" = 9

### Step 3.3: Net benefit for the decision to admit

**Goal.** Compute the net benefit of admitting by the risk of the model and by HEART 4 or more, at a threshold probability of 20 percent.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist would admit a patient with a risk of 20 percent of MACE, accepting four
unnecessary admissions for every event caught, and wants to know whether the probabilities of a
model serve this decision better than the rule "admit every patient with HEART 4 or more".
Data: The notebook holds a table named "data" with the 800 test presentations of a chest pain unit
of the virtual clinic, a synthetic data set. Each row is a presentation: "HEART" gives the HEART
score (0 to 10), "probability" the probability of a major adverse cardiac event within 30 days from
a model of the course that uses five modalities, and "MACE" is 1 when such an event followed and 0
otherwise.
Task: At the threshold probability t = 0.20, count the true positives (MACE among the admitted) and
the false positives (no MACE among the admitted), once for admitting every patient whose probability
is at least t and once for admitting every patient with HEART 4 or more. The net benefit is the true
positives divided by the number of patients minus the false positives divided by the number of
patients times t / (1 − t). Also give the net benefit of admitting everyone.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the counts and the net benefit of the three strategies, and keep the net benefit of
the model, with three decimals, under the name "answer".
Test: The net benefit of admitting no one is 0, and that of the model must be computed on all 800
test presentations.
```

**Expected result:** "answer" = 0.125

## Prompts for repairing, explaining and reviewing code

These prompts work with the code of any step. The parts in square brackets are replaced before the prompt is sent.

### Repair code that runs but does not pass the check

```text
The code below was written for this task: [paste the Task line of the prompt]. It runs, but the
check of the course prints "not yet". Find the error, explain it in two sentences and return the
corrected code. The result must still be kept under the name "answer".

[paste the code here]
```

### Understand an error message

```text
Running the code below in a Jupyter notebook gives the error message that follows. Explain the cause
in plain language and return the corrected code.

[paste the code here]

[paste the error message here]
```

### Explain the code

```text
Explain the code below line by line for a physician who does not write code. Then name two ways in
which it could give a wrong result without an error message.

[paste the code here]
```

### Ask for a review of a fusion pipeline

```text
Review the code below, which joins several kinds of data of patients into a risk model and reports
its accuracy. Check seven points. Does every input exist at the time of the decision, with no value
recorded later? Can any input reveal the outcome, such as a final diagnosis, a type of event or a
length of stay? Are scaling, filling of missing values, text models and every reduction learned on
the training data only? Are the thresholds and every other choice taken from the validation data,
never from the test data? Is calibration reported next to discrimination, with the intercept, the
slope and the Brier score? Are the units and the assays of every laboratory value the same across
hospitals, or converted, for example troponin in multiples of the upper reference limit of its
assay? Could any record or free text of a real patient leave the institution? For each point, quote
the line concerned, say whether it is right, and give the corrected code where it is not.
```

## Prompt path of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. The section *Weekly project on the prompt path* at the end of Part 1 of the Jupyter notebook prepares the table of each prompt. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Step 1: Single modalities, fusion and HEART

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to compare models for MACE within 30 days from each modality of a
chest pain unit and from all of them together with the HEART score, with intervals that show how
sure each difference is.
Data: The notebook holds a table named "data" with the 4,000 presentations with chest pain of a
chest pain unit of the virtual clinic, a synthetic data set. Each row is a presentation:
"presentation" gives its number and "set" its set ("training", 2,400; "validation", 800; "test",
800). The clinical table gives "age" (years), "sex" ("man" or "woman"), seven risk factors that are
1 when present ("smoker", "diabetes", "hypertension", "hyperlipidaemia", "obesity", "family history"
and "known coronary artery disease"), "heart rate" (per minute), "systolic pressure" (mmHg) and
"eGFR". High-sensitivity troponin T is given in multiples of the upper reference limit of the assay:
"troponin at arrival" and "troponin after one hour", which is empty when it was not measured. The
bedside echocardiogram gives "echocardiogram done" (1 or 0), and when it was done "ejection
fraction" (%) and "wall motion abnormality" (1 when a regional abnormality was seen); both are empty
otherwise. "HEART" is the HEART score, and "MACE" is 1 when a major adverse cardiac event followed
within 30 days and 0 otherwise. Two more columns come from models of the course trained on the
training presentations: "ECG score", the logit of the probability of MACE that a network gives from
the 12-lead ECG, and "note score", the logit of the probability from the triage note.
Task: Build five groups of features: the clinical table (age, sex as 1 for a man, the seven risk
factors, heart rate, systolic pressure, eGFR); the troponin (the logarithm of the troponin at
arrival, the logarithm of the troponin after one hour with the value at arrival when it was not
measured, the change in one hour with 0 when not measured, and a column that is 1 when the second
troponin was measured); the echocardiogram (whether it was done, the ejection fraction with 60 and
the wall motion abnormality with 0 when not done); the ECG score; and the note score. Fit a model on
each group alone and one on all groups together (early fusion), each as follows. Standardise the
columns with the training presentations and fit a logistic regression on the training presentations.
Choose the amount of regularisation by the area under the ROC curve (AUC) on the validation
presentations, trying 0.01, 0.1, 1 and 10 for the inverse of its strength, and compute the AUC of
the chosen model on the test presentations. Give every AUC a 95 percent interval from 2,000
bootstrap samples of the test presentations, from the 2.5th to the 97.5th percentile, and compute
the difference of each model to the HEART score in the same samples. Fix the random seed to 2026 so
that the result can be repeated.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each model and for HEART: its test AUC with the interval and
its difference to HEART with the interval; keep the test AUC of early fusion, with three decimals,
under the name "answer".
Test: No test presentation may be used for a choice, and the HEART score must not be a feature of
any model.
```

### Step 2: Calibration at two hospitals

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether the probabilities of a risk model for MACE can be
trusted on the test patients of the hospital where it learned and at a second hospital, before and
after an update with its first patients.
Data: The notebook holds a table named "data" with presentations with chest pain of two hospitals of
the virtual clinic, a synthetic data set: the 800 validation and the 800 test presentations of
hospital A and the 1,000 presentations of hospital B. Each row is a presentation: "set" gives
"validation", "test" or "hospital B", "order" the place in time of a presentation of B (1 to 1,000;
0 for A), "HEART" the HEART score (0 to 10), "probability" the probability of a major adverse
cardiac event within 30 days from a model of hospital A that fuses five modalities, and "MACE" is 1
when such an event followed and 0 otherwise.
Task: For the test presentations of A, compute the mean predicted risk against the share of MACE.
Compute the calibration intercept (the shift of the logits that makes the mean predicted risk equal
to the observed share, with the slope fixed at 1), the calibration slope (a logistic regression of
MACE on the logit of the probability, without regularisation) and the Brier score. Draw a
reliability curve of ten groups of equal size with the diagonal. For hospital B, find on the
presentations with order 1 to 300 the shift of the logits that makes their mean predicted risk equal
to their share of MACE, add it to the logits of all presentations of B, and repeat the measures and
the curve for the presentations with order 301 to 1,000, before and after the update.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the measures in a table with three rows (A test, B before, B after) and the three
curves; keep the calibration intercept at B after the update, with two decimals, under the name
"answer".
Test: Only the presentations of B with order 1 to 300 may be used to find the shift.
```

### Step 3: Two thresholds for discharge

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to choose a threshold for discharging patients with chest pain by
the risk of a model, and to know how many events it would miss at the hospital where it was chosen
and at another hospital, next to HEART 0 to 3.
Data: The notebook holds a table named "data" with presentations with chest pain of two hospitals of
the virtual clinic, a synthetic data set: the 800 validation and the 800 test presentations of
hospital A and the 1,000 presentations of hospital B. Each row is a presentation: "set" gives
"validation", "test" or "hospital B", "order" the place in time of a presentation of B (1 to 1,000;
0 for A), "HEART" the HEART score (0 to 10), "probability" the probability of a major adverse
cardiac event within 30 days from a model of hospital A that fuses five modalities, and "MACE" is 1
when such an event followed and 0 otherwise.
Task: Choose two thresholds on the validation presentations of A only. First: count the validation
presentations with HEART 0 to 3, k, and take the k-th lowest probability. Second: the largest
probability at which at most 2 percent of the validation presentations with MACE fall at or below
it. For each threshold and for HEART 0 to 3, report on the test presentations of A and on the
presentations of B with order 301 to 1,000: the number and the share sent home (at or below the
threshold), the MACE among them with a 95 percent Wilson interval, and the sensitivity for MACE.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each rule at each hospital, and keep the number of MACE among
the test presentations of A sent home at the first threshold under the name "answer".
Test: Both thresholds must come from the validation presentations of A only.
```

### Step 4: A decision curve for the heart team

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to show a heart team for which decision a risk model for MACE helps,
by comparing its net benefit with that of the HEART score over a range of thresholds for admission.
Data: The notebook holds a table named "data" with presentations with chest pain of two hospitals of
the virtual clinic, a synthetic data set: the 800 validation and the 800 test presentations of
hospital A and the 1,000 presentations of hospital B. Each row is a presentation: "set" gives
"validation", "test" or "hospital B", "order" the place in time of a presentation of B (1 to 1,000;
0 for A), "HEART" the HEART score (0 to 10), "probability" the probability of a major adverse
cardiac event within 30 days from a model of hospital A that fuses five modalities, and "MACE" is 1
when such an event followed and 0 otherwise.
Task: Use the test presentations of A. For every threshold probability t from 0.01 to 0.30 in steps
of 0.01, compute the net benefit of admitting every presentation whose probability is at least t, of
admitting every presentation with HEART 4 or more, and of admitting everyone: the true positives
divided by the number of presentations minus the false positives divided by the number of
presentations times t / (1 − t). Draw the three curves with the line at 0 for admitting no one.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the decision curve and print the three net benefits at 0.05, 0.10, 0.20 and 0.30; keep
the net benefit of the model at 0.20, with three decimals, under the name "answer".
Test: The net benefit of admitting no one is 0 at every threshold.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
