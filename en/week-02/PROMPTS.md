# Prompt library, Week 2

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 2](README.md) · [Türkçe](../../tr/hafta-02/PROMPTLAR.md)

This library holds every prompt of the practice stops of Week 2, from the parts *Prompt and application* of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the Jupyter notebook, into the empty cell under the prompt of the same number, and runs there.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [Working with a prompt](#working-with-a-prompt)
2. [Stop 1: Mini project: A CAD prediction model, ROC curve and AUC](#stop-1-mini-project-a-cad-prediction-model-roc-curve-and-auc)
3. [Stop 2: Testing a model honestly](#stop-2-testing-a-model-honestly)
4. [Stop 3: Subgroups, survival and a model to review](#stop-3-subgroups-survival-and-a-model-to-review)
5. [Prompts for repairing, explaining and reviewing code](#prompts-for-repairing-explaining-and-reviewing-code)
6. [Prompts of the weekly project](#prompts-of-the-weekly-project)

## Working with a prompt

| Step | What to do |
|---|---|
| 1. Read | Read the goal of the prompt in the Jupyter notebook. |
| 2. Prepare the data | Run the start cell of the part once, then the data cell under the prompt. The data cell prepares the table "data" that the prompt describes and shows it. |
| 3. Copy and send | Copy the prompt and send it to an AI assistant: Gemini in Google Colab, or ChatGPT, Claude, Copilot or Gemini in another browser tab. |
| 4. Run | Paste the code of the assistant into the cell below the data cell and run it. |
| 5. Check | Run the check cell. It prints *correct* or *not yet* and the value of the result "answer". |
| 6. Repair | If the check prints *not yet*, send the repair prompt with the code. If the result is still wrong, run the *Ready code* cell, which gives the correct result. |
| 7. Explain and log | Ask the assistant to explain the code in plain language, and write the tool, the prompt and what was checked in the AI usage log. |

## Stop 1: Mini project: A CAD prediction model, ROC curve and AUC

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lecture.html#stop-1) · Jupyter notebook: «Stop 1 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-02/NB02_machine_learning_fundamentals.ipynb#scrollTo=stop-1-prompt)*

The Cleveland patients of the UCI Heart Disease data set had an exercise test and a coronary angiography. In this stop a logistic regression is built from eight variables of the history and the exercise test, and its ability to recognise coronary artery disease is checked in patients that the model has not seen.

### Prompt 1.1: The model and its test AUC

**Goal.** Fit a logistic regression on the training set and measure it on the test set with the area under the ROC curve (AUC).

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Among 303 patients who had an exercise test and a coronary angiography at the Cleveland
Clinic, the cardiologist wants a model that predicts coronary artery disease from eight variables of
the history and the exercise test, tested on patients that the model has not seen.
Data: The notebook holds a table named "data". Each row is a patient: "age" gives the age in years,
and "sex" is 1 for men and 0 for women. The column "chest pain" says "typical angina", "atypical
angina", "non-anginal pain" or "asymptomatic". "resting blood pressure" gives the resting systolic
blood pressure in mm Hg, "cholesterol" the serum cholesterol in mg/dL and "highest heart rate" the
highest heart rate of the exercise test in beats per minute. "exercise angina" is 1 when angina
occurred during exercise and 0 otherwise, and "ST depression" gives the ST depression during
exercise compared with rest in mm. "CAD" is 1 when at least one major coronary artery was narrowed
by more than 50 percent of its diameter at angiography, and 0 otherwise. The column "set" says
"training" or "test"; the test set holds 76 patients.
Task: Turn the type of chest pain into three yes/no columns, with typical angina as the reference.
Use the eight variables other than "CAD" and "set" as the inputs of the model. Standardise them with
the means and the standard deviations of the training patients only. Fit a logistic regression on
the training set and compute the area under the ROC curve (AUC) of the probabilities that it gives
to the test patients.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the AUC of the test set with three decimals and keep it under the name "answer".
Test: The test set must hold 76 patients, and the AUC must lie between 0.5 and 1.
```

**Expected result:** "answer" = 0.931

### Prompt 1.2: Sensitivity at the threshold 0.5

**Goal.** Turn the probabilities of the model into decisions at the threshold 0.5 and find out how many of the patients with disease the model recognises.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know which share of the patients with coronary artery disease a
model recognises when it calls a patient positive at a probability of 0.5 or more.
Data: The notebook holds a table named "data". Each row is a patient of the test set: The column
"probability" gives the probability of coronary artery disease that the model gives to the patient,
and "CAD" the true state, 1 for disease and 0 for none.
Task: Call a patient positive when the probability is 0.5 or more. Count the true positives (TP),
the patients with disease who are called positive, and the false negatives (FN), the patients with
disease who are called negative. The sensitivity is TP / (TP + FN).
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print TP, FN and the sensitivity with three decimals, and keep the sensitivity under the
name "answer".
Test: TP + FN must equal the number of patients with disease in the table, which is 35.
```

**Expected result:** "answer" = 0.8

### Prompt 1.3: The odds ratio of the highest heart rate

**Goal.** Read from the model how the odds of coronary artery disease change when the highest heart rate of the exercise test is one standard deviation higher.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to see, as odds ratios, how the variables of a model of coronary
artery disease go with the odds of disease, above all the highest heart rate of the exercise test.
Data: The notebook holds a table named "data". Each row is a variable of a logistic regression that
was fitted on standardised variables: The column "variable" gives its name, and "coefficient" the
coefficient of the model, the change in the log odds for an increase of one standard deviation. The
coefficients of the types of chest pain compare each type with typical angina.
Task: Turn every coefficient into an odds ratio per standard deviation: e raised to the power of the
coefficient. Print all odds ratios with the names of their variables.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the odds ratio of the highest heart rate with two decimals and keep it under the name
"answer".
Test: A coefficient of 0 must give an odds ratio of exactly 1, and the odds ratio of the ST
depression must be above 1.
```

**Expected result:** "answer" = 0.58

## Stop 2: Testing a model honestly

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lecture.html#stop-2) · Jupyter notebook: «Stop 2 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-02/NB02_machine_learning_fundamentals.ipynb#scrollTo=stop-2-prompt)*

A single test set of 76 patients gives an uncertain estimate, and some models look better than they are. In this stop the test is repeated with cross-validation and a random forest is tried. Then the work turns to a rare outcome of the virtual clinic: death or a hospitalisation for heart failure within 12 months.

### Prompt 2.1: Five-fold cross-validation

**Goal.** Test the logistic regression of Stop 1 five times, each time on another fifth of the patients, and take the mean AUC.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants a more reliable estimate of the AUC of a model of coronary artery
disease than one test set of 76 patients can give, from 303 patients of the Cleveland Clinic.
Data: The notebook holds a table named "data". Each row is a patient: "age" gives the age in years,
and "sex" is 1 for men and 0 for women. The column "chest pain" says "typical angina", "atypical
angina", "non-anginal pain" or "asymptomatic". "resting blood pressure" gives the resting systolic
blood pressure in mm Hg, "cholesterol" the serum cholesterol in mg/dL and "highest heart rate" the
highest heart rate of the exercise test in beats per minute. "exercise angina" is 1 when angina
occurred during exercise and 0 otherwise, and "ST depression" gives the ST depression during
exercise compared with rest in mm. "CAD" is 1 when at least one major coronary artery was narrowed
by more than 50 percent of its diameter at angiography, and 0 otherwise. The column "fold" gives the
fold of the patient, 1 to 5; the share of patients with CAD is about the same in every fold.
Task: Turn the type of chest pain into three yes/no columns, with typical angina as the reference.
Use the eight variables other than "CAD" and "fold" as the inputs. For each fold in turn, use this
fold as the test set and the other four folds as the training set: Standardise the variables with
the training patients, fit a logistic regression and compute the AUC on the test fold. Print the
five AUC values and their mean.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the mean AUC of the five folds with three decimals and keep it under the name
"answer".
Test: Five values must be printed, each between 0.5 and 1.
```

**Expected result:** "answer" = 0.871

### Prompt 2.2: A random forest

**Goal.** Train a more flexible model on the same patients and compare its test AUC with the logistic regression.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: For 303 patients of the Cleveland Clinic, the cardiologist wants to know whether a random
forest, a more flexible model, predicts coronary artery disease better than a logistic regression.
Data: The notebook holds a table named "data". Each row is a patient: "age" gives the age in years,
and "sex" is 1 for men and 0 for women. The column "chest pain" says "typical angina", "atypical
angina", "non-anginal pain" or "asymptomatic". "resting blood pressure" gives the resting systolic
blood pressure in mm Hg, "cholesterol" the serum cholesterol in mg/dL and "highest heart rate" the
highest heart rate of the exercise test in beats per minute. "exercise angina" is 1 when angina
occurred during exercise and 0 otherwise, and "ST depression" gives the ST depression during
exercise compared with rest in mm. "CAD" is 1 when at least one major coronary artery was narrowed
by more than 50 percent of its diameter at angiography, and 0 otherwise. The column "set" says
"training" or "test"; the test set holds 76 patients.
Task: Turn the type of chest pain into three yes/no columns, with typical angina as the reference.
Use the eight variables other than "CAD" and "set" as the inputs. Train a random forest on the
training set. Make the random choices the same in every run by using the number 2026 as the starting
value. Compute the AUC of the probabilities that the forest gives to the test patients.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the test AUC of the forest with three decimals and keep it under the name "answer".
Test: The AUC must lie between 0.5 and 1. For comparison, also compute the test AUC of a logistic
regression on the same sets and print the two values side by side.
```

**Expected result:** "answer" = 0.911

### Prompt 2.3: A rare outcome

**Goal.** Train a model of an event within 12 months, which only about 3 of 100 patients have, and see how class weights change what the model finds.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Among the 2000 patients of the virtual clinic, the cardiologist wants a model that predicts
a rare event: death or a hospitalisation for heart failure within the first 12 months.
Data: The notebook holds a table named "data". Each row is a patient: "age" (years), "eGFR"
(estimated glomerular filtration rate, mL/min/1.73 m²), "LVEF" (left ventricular ejection fraction,
%), "NT-proBNP" (pg/mL), "AF" (atrial fibrillation, 1 for yes) and "diabetes" (1 for yes). "event"
is 1 for death or a hospitalisation for heart failure within the first 12 months, and 0 otherwise.
The column "set" says "training" or "test"; the test set holds 600 patients.
Task: Use the natural logarithm of NT-proBNP in place of NT-proBNP. Standardise the six variables
with the training patients and fit a logistic regression on the training set. Balance the classes in
training: The few patients with an event must carry as much weight in total as all the patients
without one. Call a test patient positive when the probability is 0.5 or more, and compute the
sensitivity, TP / (TP + FN).
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the sensitivity with three decimals and keep it under the name "answer".
Test: The test set must hold 600 patients, 20 of them with an event. The same model trained without
balancing the classes must find none of these events at the threshold 0.5.
```

**Expected result:** "answer" = 0.65

## Stop 3: Subgroups, survival and a model to review

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lecture.html#stop-3) · Jupyter notebook: «Stop 3 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-02/NB02_machine_learning_fundamentals.ipynb#scrollTo=stop-3-prompt)*

Patients with heart failure differ in more than their ejection fraction. In this stop subgroups are searched for without telling the method the answer, and survival over the follow-up is estimated. Then a model for which an AI assistant reported a perfect result is reviewed.

### Prompt 3.1: Three clusters

**Goal.** Let k-means find three groups among the patients with heart failure, then compare them with the hidden phenogroups.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Among the 407 patients with heart failure of the virtual clinic, the cardiologist wants to
find subgroups without telling the method any answer, and then to see how well they match the
phenogroups with which the clinic was built.
Data: The notebook holds a table named "data". Each row is a patient with heart failure: "age"
(years), "BMI" (body mass index, kg/m²), "eGFR" (estimated glomerular filtration rate, mL/min/1.73
m²), "LVEF" (left ventricular ejection fraction, %), "NT-proBNP" (pg/mL), "LAVI" (left atrial volume
index, mL/m²), "E/e'" (a ratio), "LV mass index" (left ventricular mass index, g/m²) and "TAPSE"
(tricuspid annular plane systolic excursion, mm). The column "phenogroup" holds the hidden group
with which the clinic generated the patient: "HFrEF", "HFpEF-metabolic" or "HFpEF-cardiorenal".
Task: Use the natural logarithm of NT-proBNP in place of NT-proBNP and standardise the nine
variables; do not use "phenogroup" for the clustering. Divide the patients into three clusters with
k-means. Run the method ten times from different random starting points and keep the best solution;
use the number 2026 as the starting value of the random choices. Then compare the clusters with the
phenogroups by the adjusted Rand index.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of patients in each cluster and the adjusted Rand index with three
decimals, and keep the index under the name "answer".
Test: The three clusters must hold the 407 patients together. An index of 1 means perfect agreement,
and 0 agreement by chance.
```

**Expected result:** "answer" = 0.706

### Prompt 3.2: Kaplan-Meier at 24 months

**Goal.** Estimate which share of the patients with HFrEF are alive and free of a hospitalisation for heart failure two years after the start of follow-up.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to estimate which share of the patients with HFrEF of the virtual
clinic are alive and free of a hospitalisation for heart failure 24 months after the start of
follow-up.
Data: The notebook holds a table named "data". Each row is a patient with heart failure: The column
"main diagnosis" says "HFrEF" or "HFpEF". "follow-up" gives the time from the start of follow-up to
the first event or to the end of follow-up in months. "event" is 1 for death or a hospitalisation
for heart failure, and 0 for a patient who left follow-up without an event (censored).
Task: For the patients whose main diagnosis is HFrEF, compute the Kaplan-Meier estimate of
event-free survival step by step. Start at 1. At every time at which at least one event occurs,
multiply the estimate by 1 − d/n, where d is the number of events at that time and n is the number
of patients still followed at that time, those whose follow-up is at least that long. The estimate
at 24 months is the value after the last event time of 24 months or less.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the estimate at 24 months with three decimals and keep it under the name "answer".
Test: The same calculation for the patients with HFpEF must give a higher value at 24 months.
```

**Expected result:** "answer" = 0.733

### Prompt 3.3: Reviewing the model of an assistant

**Goal.** An assistant reported an AUC of 1.000 for the event within 12 months. Its model used the length of follow-up and was measured on the patients on which it was trained. Find out what an honest evaluation of the same kind of model gives.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: For the 2000 patients of the virtual clinic, the cardiologist wants an honest estimate of
how well a random forest predicts death or a hospitalisation for heart failure within 12 months,
after an assistant reported a perfect result.
Data: The notebook holds a table named "data". Each row is a patient of the virtual clinic: "age"
(years), "eGFR" (estimated glomerular filtration rate, mL/min/1.73 m²), "LVEF" (left ventricular
ejection fraction, %), "NT-proBNP" (pg/mL), "AF" (atrial fibrillation, 1 for yes), "diabetes" (1 for
yes), "BMI" (body mass index, kg/m²) and "systolic blood pressure" (mm Hg). "follow-up" is the
length of follow-up in months, which is known only after the follow-up. "event" is 1 for death or a
hospitalisation for heart failure within the first 12 months, and 0 otherwise. "fold" gives the fold
of the patient, 1 to 5; the share of events is about the same in every fold.
Task: Leave "follow-up" out of the inputs, because it is not known at the time of the decision.
Predict "event" from the other eight variables with a random forest. Make the random choices the
same in every run by using the number 2026 as the starting value. Measure the model with a five-fold
cross-validation: Use each fold once as the test set and the other four folds as the training set,
and take the mean AUC of the five folds.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the mean AUC with three decimals and keep it under the name "answer".
Test: The cross-validated AUC must be clearly below 1.000. Also print the AUC of the same forest
when it is trained and measured on all patients; this value must be clearly higher.
```

**Expected result:** "answer" = 0.849

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

### Ask for a model review

```text
Review the code below, which builds and evaluates a prediction model. Check four points. Does the
model use a variable that would not be known at the time of the decision? Does any step learn from
all patients before the split? On which patients is the performance measured? Is the outcome rare?
Answer with a short list, then return the corrected code.

[paste the code here]
```

## Prompts of the weekly project

The [weekly project](README.md#weekly-project) can be built with four prompts, one for each step. The section *Weekly project* at the end of the Jupyter notebook prepares the table of each prompt and opens on its own. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Project step 1: Choose the number of phenogroups

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Among the 407 patients with heart failure of the virtual clinic, the cardiologist wants to
find phenogroups and to choose their number.
Data: The notebook holds a table named "data". Each row is a patient with heart failure: "age"
(years), "BMI" (body mass index, kg/m²), "eGFR" (estimated glomerular filtration rate, mL/min/1.73
m²), "LVEF" (left ventricular ejection fraction, %), "NT-proBNP" (pg/mL), "LAVI" (left atrial volume
index, mL/m²), "E/e'" (a ratio), "LV mass index" (left ventricular mass index, g/m²) and "TAPSE"
(tricuspid annular plane systolic excursion, mm).
Task: Use the natural logarithm of NT-proBNP and standardise the nine variables. For each number of
clusters from 2 to 6, divide the patients with k-means; run the method ten times from different
random starting points, keep the best solution and use the number 2026 as the starting value. For
each number of clusters, compute the within-cluster sum of squares (WCSS) and the mean silhouette.
Choose the number of clusters and give the clinical reason for the choice in one or two sentences.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print a table of the number of clusters, the WCSS and the silhouette, and keep the chosen
number of clusters, a whole number, under the name "answer".
Test: The WCSS must fall as the number of clusters rises, and every silhouette must lie between −1
and 1.
```

### Project step 2: Describe and name the phenogroups

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to describe the phenogroups of the patients with heart failure and
to give each a short clinical name.
Data: The notebook holds a table named "data". Each row is a patient with heart failure: "cluster"
gives the phenogroup found with the number of clusters chosen in project step 1. The other columns
hold "age" (years), "BMI" (kg/m²), "eGFR" (mL/min/1.73 m²), "LVEF" (%), "NT-proBNP" (pg/mL), "LAVI"
(mL/m²), "E/e'", "LV mass index" (g/m²), "TAPSE" (mm), "female" (1 for women), "diabetes" and "AF"
(1 for yes) and "main diagnosis" ("HFrEF" or "HFpEF").
Task: Build a table with one column per cluster: the number of patients; the mean of age, BMI, eGFR,
LVEF, LAVI, E/e', LV mass index and TAPSE; the median of NT-proBNP; and the percentage of women, of
diabetes, of AF and of HFrEF. Then propose a short clinical name for each cluster.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the table and the names, and keep the table under the name "answer".
Test: The numbers of patients in the table must add up to 407.
```

### Project step 3: Prognosis by phenogroup

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to compare the prognosis of the phenogroups with that of the two
classical groups, HFrEF and HFpEF.
Data: The notebook holds a table named "data". Each row is a patient with heart failure: "cluster"
gives the phenogroup of project step 1, and "main diagnosis" says "HFrEF" or "HFpEF". "follow-up"
gives the time to the first event or to the end of follow-up in months, and "event" is 1 for death
or a hospitalisation for heart failure and 0 for a patient who left follow-up without an event
(censored).
Task: Draw the Kaplan-Meier curves of event-free survival of the clusters in one panel, and of HFrEF
and HFpEF in a second panel. Compute the survival at 24 months of every group, and compare the
groups of each panel with a log-rank test.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the figure, the table of the survival at 24 months and the p values of the two log-rank
tests, and keep the p value of the clusters under the name "answer".
Test: Every curve must start at 1 and never rise.
```

### Project step 4: Compare with the hidden truth

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The virtual clinic hid a phenogroup in every patient with heart failure. The cardiologist
wants to know how well the clusters found in project step 1 recover them.
Data: The notebook holds a table named "data". Each row is a patient with heart failure: "cluster"
gives the cluster of project step 1, and "phenogroup" the hidden phenogroup, "HFrEF",
"HFpEF-metabolic" or "HFpEF-cardiorenal".
Task: Cross-tabulate the clusters with the phenogroups and compute the adjusted Rand index. Then
write three sentences on what the clustering found that the ejection fraction alone misses.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the cross-table, the index with three decimals and the three sentences, and keep the
index under the name "answer".
Test: The index must lie between −1 and 1; with three clusters it should be clearly above 0.5.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
