# Prompt library, Week 2

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 2](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-02/PROMPTLAR.md)

This library holds every prompt of the prompt path of Week 2, Part 1 of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the notebook, into the cell below the step of the same number, and runs there. The [guide to the prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [How a step works](#how-a-step-works)
2. [Stop 1: A first risk model](#stop-1-a-first-risk-model)
3. [Stop 2: Testing a model honestly](#stop-2-testing-a-model-honestly)
4. [Stop 3: Subgroups, survival and a model to review](#stop-3-subgroups-survival-and-a-model-to-review)
5. [Prompts for repairing, explaining and reviewing code](#prompts-for-repairing-explaining-and-reviewing-code)
6. [Prompt path of the weekly project](#prompt-path-of-the-weekly-project)

## How a step works

| Step | What to do |
|---|---|
| 1. Read | Read the goal of the step in the notebook. |
| 2. Copy and send | Copy the prompt and send it to an AI assistant: Gemini in Google Colab, or ChatGPT, Claude, Copilot or Gemini in another browser tab. |
| 3. Run | Paste the code of the assistant into the cell below the prompt and run it. |
| 4. Check | Run the check cell. It prints *correct* or *not yet* and the value of the result. |
| 5. Repair | If the check prints *not yet*, send the repair prompt with the code. If the result is still wrong, run the *Ready code* cell, which gives the correct result. |
| 6. Explain and log | Ask the assistant to explain the code in plain language, and write the tool, the prompt and what was checked in the AI usage log. |

## Stop 1: A first risk model

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lecture.html#stop-1) · The same result on the Python path: Python step 2, Sections 1 and 2*

The Cleveland patients of the UCI Heart Disease data set had an exercise test and a coronary angiography. In this stop a logistic regression is built from eight variables of the history and the exercise test, and its ability to recognise coronary artery disease is checked in patients that the model has not seen.

### Step 1.1: The model and its test AUC

**Goal.** Build the table of the model, split the patients into a training set and a test set, fit a logistic regression and measure it on the test set with the area under the ROC curve (AUC).

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 2, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib) and the machine
learning package scikit-learn are available. RANDOM_STATE holds the fixed value that the notebook
uses wherever chance plays a part.
Data: `heart` is a table with the 303 patients of the Cleveland Clinic in the UCI Heart Disease data
set, one row per patient. The columns used here are age (years); sex (1 for men, 0 for women); cp,
the type of chest pain (1 typical angina, 2 atypical angina, 3 non-anginal pain, 4 asymptomatic);
trestbps (resting blood pressure, mm Hg); chol (serum cholesterol, mg/dL); thalach (the highest
heart rate reached in the exercise test, beats per minute); exang (angina during exercise, 1 for
yes); oldpeak (ST depression during exercise compared with rest, mm); and disease, which is 1 when
at least one major coronary artery was narrowed by more than 50 percent of its diameter at
angiography, and 0 otherwise.
Task: Build the table X of the model from the columns age, sex, trestbps, chol, thalach, exang,
oldpeak and cp. The type of chest pain, cp, is a category: Turn it into yes/no columns, one for each
type, and leave out the first type, typical angina, as the reference. The outcome y is the column
disease. Split the patients at random into a training set of three quarters and a test set of one
quarter, so that the share of patients with disease is the same in both, and use RANDOM_STATE for
the random split. Standardise the variables with the means and standard deviations of the training
patients only, fit a logistic regression on the training set, and compute the area under the ROC
curve (AUC) of its predicted probabilities on the test set.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the AUC of the test set, rounded to three decimals. Keep the tables X, y, X_train,
X_test, y_train and y_test and the fitted model under the name model, because the next steps use
them. Keep the result under the name `auc_test` and print it with a short label. Return only the
code, as one block, with a short comment above each step.
Test: The test set must hold 76 patients, and the AUC must lie between 0.5 and 1.
```

**Expected result:** `auc_test` = 0.931

### Step 1.2: Sensitivity at the threshold 0.5

**Goal.** Turn the probabilities into decisions at the threshold 0.5 and find out how many of the patients with disease the model recognises.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 2, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib) and the machine
learning package scikit-learn are available. RANDOM_STATE holds the fixed value that the notebook
uses wherever chance plays a part.
Data: The fitted model, model, and the test set X_test and y_test of step 1.1 (y_test: 1 for
disease, 0 for none).
Task: Compute the probability of disease that the model gives to each test patient, and call a
patient positive when it is 0.5 or more. Count the true positives (TP), the patients with disease
who are called positive, and the false negatives (FN), the patients with disease who are called
negative. The sensitivity is TP / (TP + FN).
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the sensitivity, rounded to three decimals. Keep the result under the name
`sensitivity` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: TP + FN must equal the number of patients with disease in the test set, which is 35.
```

**Expected result:** `sensitivity` = 0.8

### Step 1.3: The odds ratio of the highest heart rate

**Goal.** Read from the model how the odds of coronary artery disease change when the highest heart rate of the exercise test is one standard deviation higher.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 2, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib) and the machine
learning package scikit-learn are available. RANDOM_STATE holds the fixed value that the notebook
uses wherever chance plays a part.
Data: The fitted model, model, of step 1.1: a logistic regression on standardised variables, fitted
on the training set. The names of the variables are the column names of X.
Task: Take the coefficients of the logistic regression, pair each with the name of its variable, and
turn every coefficient into an odds ratio per standard deviation: e raised to the power of the
coefficient. Print all odds ratios.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the odds ratio of thalach, rounded to two decimals. Keep the result under the name
`or_thalach` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: The odds ratio of oldpeak must be above 1.
```

**Expected result:** `or_thalach` = 0.58

## Stop 2: Testing a model honestly

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lecture.html#stop-2) · The same result on the Python path: Sections 3 to 6*

A single test set of 76 patients gives an uncertain estimate, and some models look better than they are. In this stop the test is repeated with cross-validation and a random forest is tried. Then the work turns to a rare outcome of the virtual clinic: death or a hospitalisation for heart failure within 12 months.

### Step 2.1: Five-fold cross-validation

**Goal.** Test the logistic regression of Stop 1 five times, each time on another fifth of the patients, and take the mean AUC.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 2, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib) and the machine
learning package scikit-learn are available. RANDOM_STATE holds the fixed value that the notebook
uses wherever chance plays a part.
Data: X and y of step 1.1: X holds the variables of the model for all 303 Cleveland patients, and y
their outcome, 1 for disease and 0 for none.
Task: Evaluate the same kind of model as in step 1.1, standardisation followed by a logistic
regression, with a five-fold cross-validation. Shuffle the patients with RANDOM_STATE and divide
them into five folds that keep the share of patients with disease. Train on four folds and compute
the AUC on the fifth, five times over, so that every fold is the test set once. Print the five AUC
values and their mean.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the mean AUC of the five folds, rounded to three decimals. Keep the result under the
name `auc_cv` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: Five values must be printed, each between 0.5 and 1.
```

**Expected result:** `auc_cv` = 0.871

### Step 2.2: A random forest

**Goal.** Train a more flexible model on the same patients and compare its test AUC with the logistic regression.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 2, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib) and the machine
learning package scikit-learn are available. RANDOM_STATE holds the fixed value that the notebook
uses wherever chance plays a part.
Data: The tables of step 1.1: X holds the variables of the model, age, sex, trestbps, chol, thalach,
exang, oldpeak and the yes/no columns of the types of chest pain, and y holds disease. X_train and
y_train are the training set; X_test and y_test are the test set, 76 of the 303 patients.
Task: Train a random forest of 300 trees on the training set, with RANDOM_STATE for its random
choices, and compute the AUC of its predicted probabilities on the test set.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the test AUC of the forest, rounded to three decimals. Keep the result under the name
`auc_forest` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: The AUC must lie between 0.5 and 1.
```

**Expected result:** `auc_forest` = 0.904

### Step 2.3: A rare outcome

**Goal.** Train a model of an event within 12 months, which only about 3 of 100 patients have, and see how class weights change what the model finds.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 2, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib) and the machine
learning package scikit-learn are available. RANDOM_STATE holds the fixed value that the notebook
uses wherever chance plays a part.
Data: `registry` is a table with the 2000 synthetic patients of the virtual clinic and their
follow-up, one row per patient. The columns used here are age (years), egfr (estimated glomerular
filtration rate, mL/min/1.73 m²), lvef (left ventricular ejection fraction, %), ntprobnp (N-terminal
pro-B-type natriuretic peptide, pg/mL), af (atrial fibrillation, 1 for yes), diabetes (1 for yes),
bmi (body mass index, kg/m²), sbp (systolic blood pressure, mm Hg) and event_12m, which is 1 when
the patient died or was admitted to hospital for heart failure within the first 12 months of
follow-up, and 0 otherwise.
Task: Build the table Xe from age, egfr, lvef, ntprobnp, af and diabetes, with ntprobnp replaced by
its natural logarithm; the outcome ye is event_12m. Split the patients at random into a training set
of 70 percent and a test set of 30 percent that keep the share of events, with RANDOM_STATE.
Standardise the variables with the training patients and fit a logistic regression with balanced
class weights, which give the few patients with an event as much weight in total as all the others.
Call a test patient positive when the probability is 0.5 or more, and compute the sensitivity on the
test set, TP / (TP + FN).
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the sensitivity, rounded to three decimals. Keep the result under the name
`se_balanced` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: The test set must hold 600 patients, 20 of them with an event. The same model without class
weights finds none of them at the threshold 0.5.
```

**Expected result:** `se_balanced` = 0.65

## Stop 3: Subgroups, survival and a model to review

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lecture.html#stop-3) · The same result on the Python path: Sections 7 to 9*

Patients with heart failure differ in more than their ejection fraction. In this stop subgroups are searched for without telling the method the answer, and survival over the follow-up is estimated. Then a model for which an AI assistant reported a perfect result is reviewed.

### Step 3.1: Three clusters

**Goal.** Let k-means find three groups among the patients with heart failure, then compare them with the hidden phenogroups.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 2, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib) and the machine
learning package scikit-learn are available. RANDOM_STATE holds the fixed value that the notebook
uses wherever chance plays a part.
Data: `hf` is a table with the 407 patients of the virtual clinic who have heart failure, those
whose main diagnosis is HFrEF or HFpEF. `HF_FEATURES` lists nine of its columns: age, bmi, egfr,
lvef, ntprobnp, lavi (left atrial volume index, mL/m²), e_e_prime (the E/e′ ratio), lv_mass_index
(left ventricular mass index, g/m²) and tapse_mm (tricuspid annular plane systolic excursion, mm).
The column hf_phenogroup holds the hidden phenogroup with which the clinic generated the data.
Task: Take the nine columns of HF_FEATURES, with ntprobnp replaced by its natural logarithm, and
standardise them. Divide the patients into three clusters with k-means, which is started ten times
from different random points, with RANDOM_STATE. Compare the clusters with the hidden phenogroups,
hf_phenogroup, by the adjusted Rand index.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the adjusted Rand index, rounded to three decimals. Keep the result under the name
`ari` and print it with a short label. Return only the code, as one block, with a short comment
above each step.
Test: The three clusters must hold the 407 patients together. An index of 1 means perfect agreement,
and 0 agreement by chance.
```

**Expected result:** `ari` = 0.706

### Step 3.2: Kaplan-Meier at 24 months

**Goal.** Estimate which share of the patients with HFrEF are alive and free of a hospitalisation for heart failure two years after the start of follow-up.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 2, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib) and the machine
learning package scikit-learn are available. RANDOM_STATE holds the fixed value that the notebook
uses wherever chance plays a part.
Data: `hf` is a table with the 407 patients of the virtual clinic who have heart failure, those
whose main diagnosis is HFrEF or HFpEF. `HF_FEATURES` lists nine of its columns: age, bmi, egfr,
lvef, ntprobnp, lavi (left atrial volume index, mL/m²), e_e_prime (the E/e′ ratio), lv_mass_index
(left ventricular mass index, g/m²) and tapse_mm (tricuspid annular plane systolic excursion, mm).
The column hf_phenogroup holds the hidden phenogroup with which the clinic generated the data.
followup_months is the time from the start of follow-up to the first event or to the end of
follow-up, in months. event is 1 for death or a hospitalisation for heart failure, and 0 for a
patient who left follow-up without an event (censored).
Task: For the patients whose main diagnosis is HFrEF, compute the Kaplan-Meier estimate of
event-free survival step by step. Start at 1. At every time at which at least one event occurs,
multiply the estimate by 1 − d/n, where d is the number of events at that time and n is the number
of patients still followed at that time, those whose follow-up time is at least that long. The
estimate at 24 months is the value after the last event time of 24 months or less.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the estimate at 24 months, rounded to three decimals. Keep the result under the name
`s24_hfref` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: The same calculation for the patients with HFpEF must give a higher value at 24 months.
```

**Expected result:** `s24_hfref` = 0.733

### Step 3.3: Reviewing the model of an assistant

**Goal.** An assistant reported an AUC of 1.000 for the event within 12 months. Find out what an honest evaluation of the same kind of model gives.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 2, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib) and the machine
learning package scikit-learn are available. RANDOM_STATE holds the fixed value that the notebook
uses wherever chance plays a part.
Data: `registry` is a table with the 2000 synthetic patients of the virtual clinic and their
follow-up, one row per patient. The columns used here are age (years), egfr (estimated glomerular
filtration rate, mL/min/1.73 m²), lvef (left ventricular ejection fraction, %), ntprobnp (N-terminal
pro-B-type natriuretic peptide, pg/mL), af (atrial fibrillation, 1 for yes), diabetes (1 for yes),
bmi (body mass index, kg/m²), sbp (systolic blood pressure, mm Hg) and event_12m, which is 1 when
the patient died or was admitted to hospital for heart failure within the first 12 months of
follow-up, and 0 otherwise. The model of the assistant also used followup_months, which is known
only after the follow-up, and measured its AUC on the same patients on which it was trained.
Task: Leave followup_months out of the variables, because it is not known at the time of the
decision. Predict event_12m from the columns age, egfr, lvef, ntprobnp, af, diabetes, bmi and sbp
with a random forest of 200 trees whose leaves hold at least 5 patients, with RANDOM_STATE. Measure
it with a five-fold cross-validation that shuffles the patients with RANDOM_STATE and keeps the
share of events in every fold, and take the mean AUC of the five folds.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the mean AUC, rounded to three decimals. Keep the result under the name `auc_review`
and print it with a short label. Return only the code, as one block, with a short comment above each
step.
Test: The AUC must be clearly below 1.000.
```

**Expected result:** `auc_review` = 0.849

## Prompts for repairing, explaining and reviewing code

These prompts work with the code of any step. The parts in square brackets are replaced before the prompt is sent.

### Repair code that runs but does not pass the check

```text
The code below was written for this task: [paste the Task line of the prompt]. It runs, but the
check of the course prints "not yet". Find the error, explain it in two sentences and return the
corrected code. Keep the name of the variable that holds the result.

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
Explain the following Python code line by line for a physician who is new to Python. Then name two
ways in which it could return a wrong result without an error message.

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

## Prompt path of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. Each step builds on the one before it, so the test of a step must hold before the next prompt is sent. The report lists all four prompts in the AI usage log.

### Step 1: Choose the number of phenogroups

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 2. The usual packages for tables,
calculations and plots (pandas, NumPy, Matplotlib and SciPy), the machine learning package
scikit-learn and the course package vclinic are available. RANDOM_STATE holds the fixed value that
the notebook uses wherever chance plays a part.
Data: registry, the 2000 patients of the virtual clinic with their follow-up. The patients with
heart failure have the main diagnosis "HFrEF" or "HFpEF". Columns: age (years), sex, bmi (kg/m²),
diabetes and af (0 or 1), egfr (mL/min/1.73 m²), lvef (%), ntprobnp (pg/mL), lavi (mL/m²),
e_e_prime, lv_mass_index (g/m²), tapse_mm (mm), followup_months (months) and event (1 for death or a
hospitalisation for heart failure, 0 for censored).
Task: Take the patients with heart failure and standardise the nine variables age, bmi, egfr, lvef,
the natural logarithm of ntprobnp, lavi, e_e_prime, lv_mass_index and tapse_mm. Divide them into
clusters with k-means for each number of clusters k from 2 to 6, starting the method ten times from
different random points, with RANDOM_STATE. Report for each k the within-cluster sum of squares
(WCSS) and the mean silhouette, choose k and give the clinical reason for the choice.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: A table of k, WCSS and silhouette, and a new column cluster in the table of the patients
with heart failure. Return only the code, as one block, with a short comment above each step.
Test: The number of patients with heart failure must be the same before and after the clustering,
and every cluster must hold at least 30 patients.
```

### Step 2: Describe and name the phenogroups

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 2. The usual packages for tables,
calculations and plots (pandas, NumPy, Matplotlib and SciPy), the machine learning package
scikit-learn and the course package vclinic are available. RANDOM_STATE holds the fixed value that
the notebook uses wherever chance plays a part.
Data: The table of the patients with heart failure from step 1, with its column cluster and the
columns of the registry.
Task: Build a table with the size of each cluster and the mean or the percentage of age, female sex,
bmi, diabetes, af, egfr, lvef, ntprobnp (as the median), lavi, e_e_prime, lv_mass_index and
tapse_mm, and the share of HFrEF. Propose a short clinical name for each cluster.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: A table with one column per cluster. Return only the code, as one block, with a short
comment above each step.
Test: The sizes in the table must add up to the number of patients with heart failure.
```

### Step 3: Prognosis by phenogroup

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 2. The usual packages for tables,
calculations and plots (pandas, NumPy, Matplotlib and SciPy), the machine learning package
scikit-learn and the course package vclinic are available. RANDOM_STATE holds the fixed value that
the notebook uses wherever chance plays a part.
Data: The table of step 1 with the columns cluster, main_diagnosis, followup_months and event, and
the tools kaplan_meier and logrank of Section 8 of the Jupyter notebook, for the survival curves and
the log-rank test.
Task: Draw the Kaplan-Meier curves of the clusters and, in a second panel, those of HFrEF and HFpEF.
Report the survival at 24 months of each group and the log-rank test of each of the two groupings.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: One figure with two panels, a table of the survival at 24 months and the two log-rank tests.
Return only the code, as one block, with a short comment above each step.
Test: The curves must start at 1 and never rise, and the log-rank test of HFrEF against HFpEF must
give the p value of Section 8.
```

### Step 4: Compare with the hidden truth

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 2. The usual packages for tables,
calculations and plots (pandas, NumPy, Matplotlib and SciPy), the machine learning package
scikit-learn and the course package vclinic are available. RANDOM_STATE holds the fixed value that
the notebook uses wherever chance plays a part.
Data: The table of step 1 with the columns cluster and hf_phenogroup, the phenogroup that the course
hid in each patient.
Task: Cross-tabulate the clusters with hf_phenogroup and compute the adjusted Rand index. Write
three sentences on what the clustering found that the ejection fraction alone misses.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: The cross-table, the adjusted Rand index and the three sentences. Return only the code, as
one block, with a short comment above each step.
Test: The adjusted Rand index must lie between −1 and 1, and with three clusters it should be
clearly above 0.5.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
