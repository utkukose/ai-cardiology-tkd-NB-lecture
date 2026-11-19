# Prompt library, Week 9

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 9](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-09/PROMPTLAR.md)

This library holds every prompt of the prompt path of Week 9, Part 1 of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the notebook, into the empty cell of the step of the same number, and runs there. The [guide to the prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [How a step works](#how-a-step-works)
2. [Stop 1: The clinical factors behind the model for coronary artery disease](#stop-1-the-clinical-factors-behind-the-model-for-coronary-artery-disease)
3. [Stop 2: LIME for one patient, and where the echo network looks](#stop-2-lime-for-one-patient-and-where-the-echo-network-looks)
4. [Stop 3: Shift, monitoring and subgroups](#stop-3-shift-monitoring-and-subgroups)
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

## Stop 1: The clinical factors behind the model for coronary artery disease

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-09/lecture.html#stop-1) · The same result on the Python path: Python step 9, Sections 1 to 3*

This stop is the mini project of the session. The two models of Week 2 for coronary artery disease, a random forest and a logistic regression, learn on the training patients of the Cleveland data. Their predictions for patient 172, a 59-year-old woman, are shared among her eight clinical variables with exact Shapley values; for the logistic regression, a closed form gives the same values on the scale of the log-odds. The last step turns the values of every test patient into a global explanation.

### Step 1.1: The two models of Week 2

**Goal.** Fit the two models of Week 2 again on the training patients and judge them on the test patients.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to rebuild the two models for coronary artery disease of an earlier
analysis, so that the quality and safety committee can review them before they are used.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography. Each row is a patient: "patient"
gives the number of the patient in the data (0 to 302) and "set" the set of Week 2 ("training", 227
patients; "test", 76 patients). The clinical variables are "age" (years), "sex" ("man" or "woman"),
"resting blood pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the highest heart rate
during the exercise test, per minute), "exercise angina" (1 when the exercise test brought on
angina), "ST depression" (the depression of the ST segment during exercise compared with rest, mm)
and "chest pain type" ("typical angina", "atypical angina", "non-anginal pain" or "no pain").
"disease" is 1 when the angiogram showed coronary artery disease and 0 otherwise.
Task: Turn the table into the columns of a model, in this order: age, sex as 1 for a man and 0 for a
woman, resting blood pressure, cholesterol, maximum heart rate, exercise angina, ST depression, and
three columns of 0 and 1 for atypical angina, non-anginal pain and no pain, with typical angina as
the reference. Keep the rows in the order of the table. Fit two models on the training patients: a
logistic regression with columns standardised on the training patients and at most 1,000 iterations,
and a random forest of 300 trees. Fix the random seed to 2026 so that the result can be repeated.
Compute the area under the ROC curve (AUC) of both models on the test patients, and the probability
that each gives patient 172.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the two test AUCs and the two probabilities of patient 172, and keep the test AUC of
the forest, with three decimals, under the name "answer".
Test: No test patient may be used to fit either model, and the AUC must lie between 0 and 1.
```

**Expected result:** "answer" = 0.904

### Step 1.2: Shapley values of patient 172

**Goal.** Share the probability that the forest gives patient 172 among her eight clinical variables.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee asks why the forest gives patient 172, a 59-year-old woman with angina on the
exercise test, a high probability of coronary artery disease, compared with the average patient.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography. Each row is a patient: "patient"
gives the number of the patient in the data (0 to 302) and "set" the set of Week 2 ("training", 227
patients; "test", 76 patients). The clinical variables are "age" (years), "sex" ("man" or "woman"),
"resting blood pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the highest heart rate
during the exercise test, per minute), "exercise angina" (1 when the exercise test brought on
angina), "ST depression" (the depression of the ST segment during exercise compared with rest, mm)
and "chest pain type" ("typical angina", "atypical angina", "non-anginal pain" or "no pain").
"disease" is 1 when the angiogram showed coronary artery disease and 0 otherwise.
Task: Turn the table into the columns of a model, in this order: age, sex as 1 for a man and 0 for a
woman, resting blood pressure, cholesterol, maximum heart rate, exercise angina, ST depression, and
three columns of 0 and 1 for atypical angina, non-anginal pain and no pain, with typical angina as
the reference. Keep the rows in the order of the table. Fit a random forest of 300 trees on the
training patients. Fix the random seed to 2026 so that the result can be repeated. Treat the eight
clinical variables as eight players; the three columns of the chest pain type always move together
as one player. For patient 172, compute exact Shapley values of the probability that the forest
gives: For each of the 256 groups of players, give the players of the group the values of the
patient and the other players the values of each training patient in turn, predict, and average over
the training patients; this is the value of the group. The Shapley value of a player is the sum,
over all groups without it, of the value of the group with the player minus the value without it,
times the weight s!(7 − s)!/8!, where s is the size of the group without the player. Check that the
eight values add up to the prediction for the patient minus the value of the empty group.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the eight Shapley values from the largest absolute value to the smallest, with the
value of the empty group and the prediction, and keep the Shapley value of the chest pain type, with
three decimals, under the name "answer".
Test: The eight values must add up to the prediction minus the value of the empty group, to the
sixth decimal.
```

**Expected result:** "answer" = 0.155

### Step 1.3: The closed form of the logistic regression

**Goal.** Compute the Shapley values of the logistic regression for patient 172 on the scale of the log-odds with a closed form.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee wants to see why the logistic regression gives patient 172 a lower
probability than the forest, and in which variables the two models differ.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography. Each row is a patient: "patient"
gives the number of the patient in the data (0 to 302) and "set" the set of Week 2 ("training", 227
patients; "test", 76 patients). The clinical variables are "age" (years), "sex" ("man" or "woman"),
"resting blood pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the highest heart rate
during the exercise test, per minute), "exercise angina" (1 when the exercise test brought on
angina), "ST depression" (the depression of the ST segment during exercise compared with rest, mm)
and "chest pain type" ("typical angina", "atypical angina", "non-anginal pain" or "no pain").
"disease" is 1 when the angiogram showed coronary artery disease and 0 otherwise.
Task: Turn the table into the columns of a model, in this order: age, sex as 1 for a man and 0 for a
woman, resting blood pressure, cholesterol, maximum heart rate, exercise angina, ST depression, and
three columns of 0 and 1 for atypical angina, non-anginal pain and no pain, with typical angina as
the reference. Keep the rows in the order of the table. Fit a logistic regression on the training
patients, with columns standardised on the training patients and at most 1,000 iterations. On the
scale of the log-odds, the Shapley value of a variable for a patient is its coefficient per unit of
the original column times the value of the patient minus the mean of the training patients; for the
chest pain type, add the three terms of its columns. Compute the eight values for patient 172 and
check that they add up to the log-odds of the patient minus the mean log-odds of the training
patients.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the eight values with the variables, and keep the value of sex, with three decimals,
under the name "answer".
Test: The eight values must add up to the log-odds of the patient minus the mean log-odds of the
training patients.
```

**Expected result:** "answer" = -1.175

### Step 1.4: From one patient to all patients

**Goal.** Compute the Shapley values of the forest for every test patient and rank the variables.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee wants to know which clinical variables the forest relies on across all test
patients, and whether any of them reflects how the patients were referred rather than their disease.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography. Each row is a patient: "patient"
gives the number of the patient in the data (0 to 302) and "set" the set of Week 2 ("training", 227
patients; "test", 76 patients). The clinical variables are "age" (years), "sex" ("man" or "woman"),
"resting blood pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the highest heart rate
during the exercise test, per minute), "exercise angina" (1 when the exercise test brought on
angina), "ST depression" (the depression of the ST segment during exercise compared with rest, mm)
and "chest pain type" ("typical angina", "atypical angina", "non-anginal pain" or "no pain").
"disease" is 1 when the angiogram showed coronary artery disease and 0 otherwise.
Task: Turn the table into the columns of a model, in this order: age, sex as 1 for a man and 0 for a
woman, resting blood pressure, cholesterol, maximum heart rate, exercise angina, ST depression, and
three columns of 0 and 1 for atypical angina, non-anginal pain and no pain, with typical angina as
the reference. Keep the rows in the order of the table. Fit a random forest of 300 trees on the
training patients. Fix the random seed to 2026 so that the result can be repeated. Treat the eight
clinical variables as eight players; the three columns of the chest pain type always move together
as one player. For every test patient, compute exact Shapley values of the probability that the
forest gives: For each of the 256 groups of players, give the players of the group the values of the
patient and the other players the values of each training patient in turn, predict, and average over
the training patients; this is the value of the group. The Shapley value of a player is the sum,
over all groups without it, of the value of the group with the player minus the value without it,
times the weight s!(7 − s)!/8!, where s is the size of the group without the player. Check that the
eight values add up to the prediction for the patient minus the value of the empty group. Then
compute for each variable the mean of the absolute Shapley values over the test patients, and count
the test patients in which each variable has the largest absolute value.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the mean absolute values from the largest to the smallest with the counts, and keep the
mean absolute value of the chest pain type, with three decimals, under the name "answer".
Test: The counts must add up to the number of test patients.
```

**Expected result:** "answer" = 0.138

## Stop 2: LIME for one patient, and where the echo network looks

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-09/lecture.html#stop-2) · The same result on the Python path: Sections 4 to 7*

This stop explains predictions in two more ways. LIME imitates the forest of Stop 1 around patient 172 with a weighted linear model, and a repetition with twenty seeds shows how stable its answer is. A small convolutional network then learns to flag an ejection fraction below 45 percent on echocardiograms of CAMUS, and its Grad-CAM maps are compared with the expert outlines of the left ventricle.

### Step 2.1: LIME for patient 172

**Goal.** Explain the probability that the forest gives patient 172 with a weighted linear model fitted around her.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee wants a second explanation of the prediction for patient 172, made in another
way than the Shapley values, to see whether the two agree.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography. Each row is a patient: "patient"
gives the number of the patient in the data (0 to 302) and "set" the set of Week 2 ("training", 227
patients; "test", 76 patients). The clinical variables are "age" (years), "sex" ("man" or "woman"),
"resting blood pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the highest heart rate
during the exercise test, per minute), "exercise angina" (1 when the exercise test brought on
angina), "ST depression" (the depression of the ST segment during exercise compared with rest, mm)
and "chest pain type" ("typical angina", "atypical angina", "non-anginal pain" or "no pain").
"disease" is 1 when the angiogram showed coronary artery disease and 0 otherwise.
Task: Turn the table into the columns of a model, in this order: age, sex as 1 for a man and 0 for a
woman, resting blood pressure, cholesterol, maximum heart rate, exercise angina, ST depression, and
three columns of 0 and 1 for atypical angina, non-anginal pain and no pain, with typical angina as
the reference. Keep the rows in the order of the table. Fit a random forest of 300 trees on the
training patients. Fix the random seed to 2026 so that the result can be repeated. Treat the eight
clinical variables as eight players; the three columns of the chest pain type always move together
as one player. Explain the probability that the forest gives patient 172 with LIME. Draw the
neighbours of the patient: In each neighbour, draw one training patient at random, and let each of
the eight players keep the value of patient 172 with a probability of one half or otherwise take the
value of the drawn training patient. Record for each neighbour which players kept the value of the
patient (1) and which were replaced (0). Weight each neighbour by exp(−d²/w²), where d is the square
root of the number of players replaced and w = 0.75 × √8. Fit a ridge regression with a penalty of 1
of the probabilities of the forest for the neighbours on the eight columns of 0 and 1, with these
weights; its eight coefficients are the explanation. Draw first the 0 and 1 of all neighbours and
then their training patients, from one random generator. Use 2,000 neighbours and the seed 2026.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the eight coefficients from the largest absolute value to the smallest, and keep the
coefficient of the chest pain type, with three decimals, under the name "answer".
Test: The weight of a neighbour that keeps all eight values of the patient must be 1.
```

**Expected result:** "answer" = 0.145

### Step 2.2: How stable is LIME?

**Goal.** Repeat LIME with few neighbours and twenty seeds, and see how often the leading variable changes.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee wants to know whether an explanation by LIME would stay the same if it were
run again, before it trusts an explanation of a single patient.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography. Each row is a patient: "patient"
gives the number of the patient in the data (0 to 302) and "set" the set of Week 2 ("training", 227
patients; "test", 76 patients). The clinical variables are "age" (years), "sex" ("man" or "woman"),
"resting blood pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the highest heart rate
during the exercise test, per minute), "exercise angina" (1 when the exercise test brought on
angina), "ST depression" (the depression of the ST segment during exercise compared with rest, mm)
and "chest pain type" ("typical angina", "atypical angina", "non-anginal pain" or "no pain").
"disease" is 1 when the angiogram showed coronary artery disease and 0 otherwise.
Task: Turn the table into the columns of a model, in this order: age, sex as 1 for a man and 0 for a
woman, resting blood pressure, cholesterol, maximum heart rate, exercise angina, ST depression, and
three columns of 0 and 1 for atypical angina, non-anginal pain and no pain, with typical angina as
the reference. Keep the rows in the order of the table. Fit a random forest of 300 trees on the
training patients. Fix the random seed to 2026 so that the result can be repeated. Treat the eight
clinical variables as eight players; the three columns of the chest pain type always move together
as one player. Explain the probability that the forest gives patient 172 with LIME. Draw the
neighbours of the patient: In each neighbour, draw one training patient at random, and let each of
the eight players keep the value of patient 172 with a probability of one half or otherwise take the
value of the drawn training patient. Record for each neighbour which players kept the value of the
patient (1) and which were replaced (0). Weight each neighbour by exp(−d²/w²), where d is the square
root of the number of players replaced and w = 0.75 × √8. Fit a ridge regression with a penalty of 1
of the probabilities of the forest for the neighbours on the eight columns of 0 and 1, with these
weights; its eight coefficients are the explanation. Draw first the 0 and 1 of all neighbours and
then their training patients, from one random generator. Use only 100 neighbours, and repeat with
the seeds 1 to 20. For each seed, find the player with the largest absolute coefficient.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show how often each player comes first, and the smallest and largest coefficient of the
chest pain type, and keep the share of seeds in which the chest pain type comes first, with two
decimals, under the name "answer".
Test: The counts of the players must add up to 20.
```

**Expected result:** "answer" = 0.7

### Step 2.3: A network for a low ejection fraction

**Goal.** Train a small convolutional network that flags an ejection fraction below 45 percent on one view.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee reviews a network that reads echocardiograms. Before its maps are judged, the
cardiologist wants to know how well it flags a low ejection fraction on views of patients it has not
seen.
Data: The notebook holds a table named "data" with 600 views of CAMUS, a public data set of
echocardiograms: the apical two-chamber and four-chamber views of 300 patients. Each row is a view:
"patient" gives the patient, "view" the view ("2CH" or "4CH"), "set" the set of the patient
("training", 200 patients; "validation", 50 patients; "test", 50 patients) and "image quality" the
grade of the experts ("Good", "Medium" or "Poor"). Each cell of "end-diastole" and of "end-systole"
holds the frame as an image of 96 × 96 pixels with values from 0 to 1, and each cell of "outline"
the expert outline of the left ventricular cavity and the myocardium, at end-diastole or
end-systole, at the same size: 1 inside and 0 outside. "low ejection fraction" is 1 when the
ejection fraction of the patient is below 45 percent and 0 otherwise.
Task: Build a small convolutional network for one view that takes the end-diastolic and the
end-systolic frame as two channels of 96 × 96 pixels. It has four blocks, and each block is a
convolution with 3 × 3 kernels that keeps the size (16, 32, 64 and 64 channels), batch
normalisation, ReLU and a 2 × 2 max pooling. After the blocks, the network takes the mean of every
channel over the image and applies a dropout of 0.3, and a linear layer with one output gives the
logit of a low ejection fraction. Train it on the training views with Adam (learning rate 0.001,
weight decay 0.0001) and the binary cross-entropy for 30 epochs in shuffled groups of 32 views,
shifting each group at random by up to 4 pixels in each direction, and keep the weights of the epoch
with the best AUC on the validation views. Seed the random generator of the network library with
2026 before building the network and again before training. Compute the AUC on the test views.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the best validation AUC and the test AUC, and keep the test AUC, with three decimals,
under the name "answer".
Test: No test view may be used to choose the epoch, and the views of one patient must stay in one
set.
```

**Expected result:** "answer" = 0.796

### Step 2.4: Grad-CAM maps against the expert outline

**Goal.** Compute the Grad-CAM map of every test view and the share of the map inside the expert outline.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee wants to know whether the network flags a low ejection fraction from the left
ventricle, where the expert looks, or from other parts of the image.
Data: The notebook holds a table named "data" with 600 views of CAMUS, a public data set of
echocardiograms: the apical two-chamber and four-chamber views of 300 patients. Each row is a view:
"patient" gives the patient, "view" the view ("2CH" or "4CH"), "set" the set of the patient
("training", 200 patients; "validation", 50 patients; "test", 50 patients) and "image quality" the
grade of the experts ("Good", "Medium" or "Poor"). Each cell of "end-diastole" and of "end-systole"
holds the frame as an image of 96 × 96 pixels with values from 0 to 1, and each cell of "outline"
the expert outline of the left ventricular cavity and the myocardium, at end-diastole or
end-systole, at the same size: 1 inside and 0 outside. "low ejection fraction" is 1 when the
ejection fraction of the patient is below 45 percent and 0 otherwise.
Task: Build a small convolutional network for one view that takes the end-diastolic and the
end-systolic frame as two channels of 96 × 96 pixels. It has four blocks, and each block is a
convolution with 3 × 3 kernels that keeps the size (16, 32, 64 and 64 channels), batch
normalisation, ReLU and a 2 × 2 max pooling. After the blocks, the network takes the mean of every
channel over the image and applies a dropout of 0.3, and a linear layer with one output gives the
logit of a low ejection fraction. Train it on the training views with Adam (learning rate 0.001,
weight decay 0.0001) and the binary cross-entropy for 30 epochs in shuffled groups of 32 views,
shifting each group at random by up to 4 pixels in each direction, and keep the weights of the epoch
with the best AUC on the validation views. Seed the random generator of the network library with
2026 before building the network and again before training. For every test view, compute the
Grad-CAM map of the output at the ReLU of the last block, before its pooling. To do so, take the
gradient of the output with respect to the 64 feature maps of 12 × 12 at that layer, use the mean
gradient of each channel as its weight and form the weighted sum of the 64 maps. Keep only the
positive part of the sum and enlarge it to 96 × 96 by bilinear interpolation. For each view, compute
the share of the sum of the map that falls inside the outline. Report the mean of the shares over
the test views and, for comparison, the mean share of the image that the outline covers.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the two means, and keep the mean share of the maps inside the outline, with three
decimals, under the name "answer".
Test: Every share must lie between 0 and 1, and no map may be computed from a network in training
mode.
```

**Expected result:** "answer" = 0.317

## Stop 3: Shift, monitoring and subgroups

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-09/lecture.html#stop-3) · The same result on the Python path: Sections 8 to 10*

This stop asks whether a model stays reliable. A classifier learns to tell the presentations of hospital B from those of hospital A in the chest pain unit of Week 8, before any outcome is known. The observed and expected events at B are then followed in the order of arrival. The risk model is judged in groups of sex and age at a threshold for discharge, and the model for coronary artery disease is fitted with and without sex.

### Step 3.1: Can the two hospitals be told apart?

**Goal.** Train a classifier that tells the presentations of hospital B from those of hospital A by their inputs, without any outcome.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: A risk model of the chest pain unit of hospital A is to be used at hospital B. Before the
first outcomes arrive, the committee wants to know whether the patients and the records of B look
like those of A, and where they differ.
Data: The notebook holds a table named "data" with the presentations with chest pain of two
hospitals of the virtual clinic, a synthetic data set: 4,000 at hospital A and 1,000 at hospital B.
Each row is a presentation: "hospital" gives the hospital ("A" or "B") and "set" its set
("training", "validation" and "test" at A; "hospital B" at B). The clinical table gives "age"
(years), "sex" ("man" or "woman"), seven risk factors that are 1 when present ("smoker", "diabetes",
"hypertension", "hyperlipidaemia", "obesity", "family history" and "known coronary artery disease"),
"heart rate" (per minute), "systolic pressure" (mmHg) and "eGFR". Troponin is given in multiples of
the upper reference limit of the assay of each hospital: "troponin at arrival" and "troponin after
one hour", which is empty when it was not measured. The bedside echocardiogram gives "echocardiogram
done" (1 or 0), and when it was done "ejection fraction" (%) and "wall motion abnormality" (1 when a
regional abnormality was seen); both are empty otherwise. "triage note" is the note of the triage
nurse in Turkish.
Task: Build the inputs of a risk model for MACE for every presentation: The clinical table (age, sex
as 1 for a man, the seven risk factors, heart rate, systolic pressure, eGFR); the troponin (the
logarithm of the troponin at arrival, the logarithm of the troponin after one hour with the value at
arrival when it was not measured, the change in one hour with 0 when it was not measured, and 1 when
the second troponin was measured); the echocardiogram (echocardiogram done, the ejection fraction
with 60 when it was not done, the wall motion abnormality with 0 when it was not done); and the note
as 20 numbers (TF-IDF of words and word pairs that occur in at least 3 notes, with sublinear term
frequency, fitted on the training notes of A and reduced to 20 components by a singular value
decomposition fitted on the same notes, with the seed 2026). Then fit a logistic regression with
standardised columns and at most 5,000 iterations that tells hospital B (1) from hospital A (0),
with the predictions from a five-fold stratified cross-validation of all 5,000 presentations,
shuffled with the seed 2026, and compute its AUC. Repeat with the columns of each group of inputs
alone.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the AUC for all inputs and for each group, and keep the AUC for all inputs, with three
decimals, under the name "answer".
Test: No outcome may be used, and the note model may learn from the training notes of A only.
```

**Expected result:** "answer" = 0.988

### Step 3.2: Observed against expected events at hospital B

**Goal.** Follow observed minus expected events at hospital B in the order of arrival and find the first alarm.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The model of hospital A is now used at hospital B, and the outcomes of its patients arrive
one after the other. The committee wants a simple chart that raises an alarm when the model expects
too few or too many events.
Data: The notebook holds a table named "data" with the 1,000 presentations with chest pain of a
second hospital, B, of the virtual clinic, a synthetic data set, in the order in which they arrived.
Each row is a presentation: "order" gives its place in time, "probability" the probability of a
major adverse cardiac event within 30 days from a model that learned at the first hospital, A, and
"MACE" is 1 when such an event followed and 0 otherwise.
Task: Go through the presentations in their order. After each presentation m, compute the sum of
MACE minus the sum of the probabilities up to m, and the band 1.96 times the square root of the sum
of p(1 − p) up to m. Find the first presentation at which the difference lies above the band, and
draw the difference with the band against the order.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the chart, print the difference and the band after all presentations, and keep the
order of the first presentation above the band under the name "answer".
Test: The band must start near 0 and widen with the number of presentations.
```

**Expected result:** "answer" = 253

### Step 3.3: Subgroups at a threshold for discharge

**Goal.** Choose a threshold for discharge on the validation presentations and judge it on the test presentations by sex and age.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee wants to know whether a threshold for discharge that is safe on average is
also safe for women, for men, for patients under 65 and for patients aged 65 or more.
Data: The notebook holds a table named "data" with the 800 validation and the 800 test presentations
of a chest pain unit of the virtual clinic, a synthetic data set. Each row is a presentation: "set"
gives its set ("validation" or "test"), "sex" the sex ("man" or "woman"), "age" the age in years,
"probability" the probability of a major adverse cardiac event within 30 days from a model of the
course that learned on the training presentations, and "MACE" is 1 when such an event followed and 0
otherwise.
Task: Choose the threshold on the validation presentations only: the largest probability at which at
most 2 percent of the validation presentations with MACE fall at or below it. Presentations at or
below the threshold are sent home. On the test presentations, for all, for women, for men, for
patients under 65 and for patients aged 65 or more, compute the number of presentations and of MACE,
the area under the ROC curve (AUC), the mean probability, the observed share of MACE, the number
sent home, the MACE among them and the sensitivity.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each group, and keep the sensitivity in women, with three
decimals, under the name "answer".
Test: The threshold must come from the validation presentations only.
```

**Expected result:** "answer" = 0.956

### Step 3.4: A model without sex

**Goal.** Fit the logistic regression of Week 2 with and without sex and compare its calibration and its errors in women and men.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Someone proposes to remove sex from the model for coronary artery disease so that it treats
women and men alike. The committee wants to know what this would do to the predictions for women and
for men.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography. Each row is a patient: "patient"
gives the number of the patient in the data (0 to 302) and "set" the set of Week 2 ("training", 227
patients; "test", 76 patients). The clinical variables are "age" (years), "sex" ("man" or "woman"),
"resting blood pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the highest heart rate
during the exercise test, per minute), "exercise angina" (1 when the exercise test brought on
angina), "ST depression" (the depression of the ST segment during exercise compared with rest, mm)
and "chest pain type" ("typical angina", "atypical angina", "non-anginal pain" or "no pain").
"disease" is 1 when the angiogram showed coronary artery disease and 0 otherwise.
Task: Turn the table into the columns of a model, in this order: age, sex as 1 for a man and 0 for a
woman, resting blood pressure, cholesterol, maximum heart rate, exercise angina, ST depression, and
three columns of 0 and 1 for atypical angina, non-anginal pain and no pain. Keep the rows in the
order of the table and use all 303 patients. Get a prediction for every patient from a five-fold
stratified cross-validation, shuffled with the seed 2026, of a logistic regression with standardised
columns and at most 1,000 iterations; do it once with sex and once without the column of sex. For
women and for men, compare the mean predicted risk with the observed share of disease, and compute
the sensitivity and the specificity at a probability of 0.5.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each model and sex, and keep the mean predicted risk of the
women without sex, with three decimals, under the name "answer".
Test: Every prediction must come from a fold that did not hold the patient.
```

**Expected result:** "answer" = 0.417

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

### Ask for a review of an explanation

```text
Review the code below, which explains the predictions of a model for patients and draws the result.
Check seven points. Whom is each patient compared with: Is the background a set of real training
patients rather than a single artificial row? Are the columns of one variable, such as the dummy
columns of a categorical variable, explained together? Does the explanation stay the same when the
seed or the number of samples changes? Has every saliency map passed a sanity check with a network
whose weights were made random? Does any sentence read a contribution as a cause, or as advice for a
patient? Are the results reported for women and men and for groups of age? Could any image or record
of a real patient leave the institution? For each point, quote the line concerned, say whether it is
right, and give the corrected code where it is not.
```

## Prompt path of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. The section *Weekly project on the prompt path* at the end of Part 1 of the Jupyter notebook prepares the table of each prompt. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Step 1: The accuracy of the echo network

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee reviews a network that flags a low ejection fraction on echocardiograms and
wants its accuracy for single views and for patients, with intervals, before it looks at the maps.
Data: The notebook holds a table named "data" with 600 views of CAMUS, a public data set of
echocardiograms: the apical two-chamber and four-chamber views of 300 patients. Each row is a view:
"patient" gives the patient, "view" the view ("2CH" or "4CH"), "set" the set of the patient
("training", 200 patients; "validation", 50 patients; "test", 50 patients) and "image quality" the
grade of the experts ("Good", "Medium" or "Poor"). Each cell of "end-diastole" and of "end-systole"
holds the frame as an image of 96 × 96 pixels with values from 0 to 1, and each cell of "outline"
the expert outline of the left ventricular cavity and the myocardium, at end-diastole or
end-systole, at the same size: 1 inside and 0 outside. "low ejection fraction" is 1 when the
ejection fraction of the patient is below 45 percent and 0 otherwise.
Task: Build a small convolutional network for one view that takes the end-diastolic and the
end-systolic frame as two channels of 96 × 96 pixels. It has four blocks, and each block is a
convolution with 3 × 3 kernels that keeps the size (16, 32, 64 and 64 channels), batch
normalisation, ReLU and a 2 × 2 max pooling. After the blocks, the network takes the mean of every
channel over the image and applies a dropout of 0.3, and a linear layer with one output gives the
logit of a low ejection fraction. Train it on the training views with Adam (learning rate 0.001,
weight decay 0.0001) and the binary cross-entropy for 30 epochs in shuffled groups of 32 views,
shifting each group at random by up to 4 pixels in each direction, and keep the weights of the epoch
with the best AUC on the validation views. Seed the random generator of the network library with
2026 before building the network and again before training. Compute the AUC on the test views, and
on the test patients with the mean of the probabilities of the two views of each patient. Give each
AUC a 95 percent interval from 2,000 bootstrap samples of the test views or of the test patients,
from the 2.5th to the 97.5th percentile. Fix the random seed to 2026 so that the result can be
repeated.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with the two AUCs and their intervals, and keep the test AUC per view, with
three decimals, under the name "answer".
Test: No test view may be used to choose the epoch, and the bootstrap of the patients must draw
patients, not views.
```

### Step 2: The maps against the expert outline

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee wants to know whether the network looks at the left ventricle when it flags a
low ejection fraction, and whether this differs between views with a low and a normal ejection
fraction, between right and wrong predictions and between grades of image quality.
Data: The notebook holds a table named "data" with the 100 test views of CAMUS of the course, a
public data set of echocardiograms: the apical two-chamber and four-chamber views of 50 patients.
Each row is a view: "patient", "view", "set" and "image quality" (the grade of the experts: "Good",
"Medium" or "Poor") describe it. "end-diastole" and "end-systole" hold the frames as images of 96 ×
96 pixels with values from 0 to 1, "outline" holds the expert outline of the left ventricular cavity
and the myocardium at the same size, 1 inside and 0 outside, and "low ejection fraction" is 1 when
the ejection fraction of the patient is below 45 percent. Two columns come from the echo network of
the course, trained on the training views: "probability", its probability of a low ejection
fraction, and "map", its Grad-CAM map at the last block, an image of 96 × 96 values of 0 or more.
Task: For every view, compute three measures: the share of the sum of "map" that falls inside
"outline"; 1 when the pixel with the highest value of "map" lies inside "outline", and 0 otherwise;
and the share of the image that "outline" covers. A prediction is right when "probability" is at
least 0.5 for a view with a low ejection fraction, or below 0.5 for a view without. Show the means
of the three measures for all views, for views with a low and with a normal ejection fraction, for
right and for wrong predictions and for each grade of image quality, with the number of views in
each group.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the table of the groups, and keep the mean share inside the outline over all views,
with three decimals, under the name "answer".
Test: Every share must lie between 0 and 1, and the groups of each comparison must add up to 100
views.
```

### Step 3: Sanity checks of the maps

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee wants to know whether the maps depend on what the network learned. A map that
stays the same when the weights of the network are replaced by random ones describes the image, not
the model, and one random draw can mislead.
Data: The notebook holds a table named "data" with 600 views of CAMUS, a public data set of
echocardiograms: the apical two-chamber and four-chamber views of 300 patients. Each row is a view:
"patient" gives the patient, "view" the view ("2CH" or "4CH"), "set" the set of the patient
("training", 200 patients; "validation", 50 patients; "test", 50 patients) and "image quality" the
grade of the experts ("Good", "Medium" or "Poor"). Each cell of "end-diastole" and of "end-systole"
holds the frame as an image of 96 × 96 pixels with values from 0 to 1, and each cell of "outline"
the expert outline of the left ventricular cavity and the myocardium, at end-diastole or
end-systole, at the same size: 1 inside and 0 outside. "low ejection fraction" is 1 when the
ejection fraction of the patient is below 45 percent and 0 otherwise.
Task: Build a small convolutional network for one view that takes the end-diastolic and the
end-systolic frame as two channels of 96 × 96 pixels. It has four blocks, and each block is a
convolution with 3 × 3 kernels that keeps the size (16, 32, 64 and 64 channels), batch
normalisation, ReLU and a 2 × 2 max pooling. After the blocks, the network takes the mean of every
channel over the image and applies a dropout of 0.3, and a linear layer with one output gives the
logit of a low ejection fraction. Train it on the training views with Adam (learning rate 0.001,
weight decay 0.0001) and the binary cross-entropy for 30 epochs in shuffled groups of 32 views,
shifting each group at random by up to 4 pixels in each direction, and keep the weights of the epoch
with the best AUC on the validation views. Seed the random generator of the network library with
2026 before building the network and again before training. For every test view, compute the
Grad-CAM map of the output at the ReLU of the last block, before its pooling. To do so, take the
gradient of the output with respect to the 64 feature maps of 12 × 12 at that layer, use the mean
gradient of each channel as its weight and form the weighted sum of the 64 maps. Keep only the
positive part of the sum and enlarge it to 96 × 96 by bilinear interpolation. For each view, compute
the share of the sum of the map that falls inside the outline. Then repeat the following for each
seed from 1 to 20, twice: once for a copy of the trained network whose last block and output layer
get new random weights, and once for a copy whose layers all get new random weights. Seed the random
generator of the network library with the seed just before the new weights are drawn, and keep the
trained network unchanged. For the copy, compute the same maps; for each view, compute the Spearman
rank correlation between the 9,216 pixels of the map of the trained network and those of the map of
the copy, leaving a view out when one of the two maps has the same value at every pixel, and the
share of the map of the copy inside the outline. For each copy, record the mean rank correlation,
the mean share inside the outline and the number of empty maps. For each kind of copy, report the
median and the range over the 20 seeds of the mean rank correlation and of the mean share inside the
outline, and the number of seeds in which more than half of the maps are empty, next to the mean
share inside the outline of the trained network.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the results in a small table, and keep the median of the mean rank correlation for the
copies with a random last block, with three decimals, under the name "answer".
Test: Every rank correlation must lie between −1 and 1, and the trained network must give the same
maps before and after the copies are made.
```

### Step 4: Six views for the committee

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The committee wants to see the maps of a few views next to the expert outlines, including
views where the network was wrong.
Data: The notebook holds a table named "data" with the 100 test views of CAMUS of the course, a
public data set of echocardiograms: the apical two-chamber and four-chamber views of 50 patients.
Each row is a view: "patient", "view", "set" and "image quality" (the grade of the experts: "Good",
"Medium" or "Poor") describe it. "end-diastole" and "end-systole" hold the frames as images of 96 ×
96 pixels with values from 0 to 1, "outline" holds the expert outline of the left ventricular cavity
and the myocardium at the same size, 1 inside and 0 outside, and "low ejection fraction" is 1 when
the ejection fraction of the patient is below 45 percent. Two columns come from the echo network of
the course, trained on the training views: "probability", its probability of a low ejection
fraction, and "map", its Grad-CAM map at the last block, an image of 96 × 96 values of 0 or more.
Task: Choose six views: two views with a low ejection fraction and a "probability" of at least 0.5,
one view with a low ejection fraction and a "probability" below 0.5, one view without a low ejection
fraction and a "probability" of at least 0.5, one view without a low ejection fraction and a
"probability" below 0.5, and the view of image quality "Poor" with the highest "probability". Draw
them in two rows of three panels: the end-diastolic frame in grey, "map" on top in a warm colour
scale with partial transparency, and "outline" as a contour line. Put the patient, the view, the
probability, the true class and the share of the map inside the outline in the title of each panel,
and write "CAMUS, CC BY-NC-SA 4.0" under the figure.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the figure, and keep the patients and views of the six panels as a list under the name
"answer".
Test: At least two of the six panels must show a wrong prediction.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
