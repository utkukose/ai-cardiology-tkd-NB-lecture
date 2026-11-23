# Prompt library, Week 11

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 11](README.md) · [Türkçe](../../tr/hafta-11/PROMPTLAR.md)

This library holds every prompt of the practice stops of Week 1, from the parts *Prompt and application* of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the Jupyter notebook, into the empty cell under the prompt of the same number, and runs there.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [Working with a prompt](#working-with-a-prompt)
2. [Stop 1: The question, the data and a reference](#stop-1-the-question-the-data-and-a-reference)
3. [Stop 2: Uncertainty and calibration](#stop-2-uncertainty-and-calibration)
4. [Stop 3: The rule-out and its limits](#stop-3-the-rule-out-and-its-limits)
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

## Stop 1: The question, the data and a reference

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-11/lecture.html#stop-1) · Jupyter notebook: «Stop 1 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-11/NB11_final_project_workshop.ipynb#scrollTo=stop-1-prompt)*

This stop is the first half of the workshop on the final projects, on the worked project of the week. The data of the Cleveland patients are audited, the size that a model of ten parameters needs is compared with the training patients, and the reference of age, sex and chest pain type is tested once on the test patients. After the stop, the same three steps are repeated on the data of your own final project.

### Prompt 1.1: The audit of the data

**Goal.** Count the missing values of the data, column by column, and see which columns the project uses.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: A cardiologist plans a final project on ruling out coronary artery disease after an
exercise test, so that some patients need not be referred for angiography. Before any model, the
data are audited: Which columns have missing values, and are they columns that the decision would
have at its moment?
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography after an exercise test, with all
their columns. Each row is a patient: "patient" gives the number of the patient in the data (0 to
302). The eight variables of the project are "age" (years), "sex" ("man" or "woman"), "chest pain
type" ("typical angina", "atypical angina", "non-anginal pain" or "no pain"), "resting blood
pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the highest heart rate during the
exercise test, per minute), "exercise angina" (1 when the exercise test brought on angina) and "ST
depression" (the depression of the ST segment during exercise compared with rest, mm). Five more
columns come from the data set: "fasting blood sugar above 120" (1 when the fasting blood sugar was
above 120 mg/dL), "resting ECG" (0 normal, 1 an abnormality of the ST segment or the T wave, 2 left
ventricular hypertrophy), "ST slope" (the slope of the ST segment at peak exercise: 1 up, 2 flat, 3
down), "vessels on fluoroscopy" (the number of major vessels coloured by fluoroscopy, 0 to 3) and
"thallium scan" (3 normal, 6 fixed defect, 7 reversible defect). An empty cell is a missing value.
"disease" is 1 when the angiogram showed more than 50 percent narrowing of the diameter of at least
one major coronary artery, and 0 otherwise.
Task: Count the missing values of every column except "patient". The project uses nine columns: the
eight variables and "disease". Mark for each column whether the project uses it, and add up the
missing values of the columns that it does not use. Also give the number of patients, the number
with disease and their share.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with the missing values of each column and whether the project uses it, print
the counts of the patients, and keep the number of missing values in the columns that the project
does not use under the name "answer".
Test: The nine columns that the project uses must have no missing value, and the table must hold 303
patients.
```

**Expected result:** "answer" = 6

### Prompt 1.2: How much data the model needs

**Goal.** Compute the three minimum sizes of Riley and colleagues for a model of ten parameters and compare them with the training patients.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The full model of the project has ten parameters: seven variables and three columns for the
chest pain type. The cardiologist wants to know whether 227 training patients are enough, and takes
the R squared of the reference of age, sex and chest pain type as the anticipated value.
Data: The notebook holds a table named "data" with the 227 training patients of the Cleveland data
of the UCI Heart Disease data set, patients referred for coronary angiography after an exercise
test. Each row is a patient: "patient" gives the number of the patient in the data, and
"probability, reference" the probability of coronary artery disease that a reference model of the
course, a logistic regression on the age, the sex and the chest pain type, gives the patient after
it was fitted on these same patients. "disease" is 1 when the angiogram showed more than 50 percent
narrowing of the diameter of at least one major coronary artery, and 0 otherwise.
Task: Compute the Cox-Snell R squared of the probabilities: Take the log-likelihood of the
probabilities, the sum over the patients of the natural logarithm of the probability given to the
outcome that the patient had, and the log-likelihood of a model that gives every patient the overall
share of disease; the R squared is one minus the exponential of two times the difference, null minus
model, divided by the number of patients. Then compute the three minimum sizes of Riley and
colleagues for a model with 10 parameters. The largest R squared that the share of disease allows is
one minus the exponential of two times the log-likelihood of the overall share, divided by the
number of patients. Size (i), for a shrinkage of 0.9, is 10 divided by (0.9 minus 1) times the
natural logarithm of one minus the R squared divided by 0.9. Size (ii) uses the same formula with
the shrinkage replaced by the R squared divided by the sum of the R squared and 0.05 times the
largest R squared. Size (iii) is (1.96 divided by 0.05) squared, times the share of disease, times
one minus the share. Round every size up to a whole patient.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the Cox-Snell R squared, the largest R squared, the three sizes and the number of
training patients, and keep size (i) under the name "answer".
Test: The R squared must lie between 0 and the largest R squared, and size (iii) must not depend on
the probabilities.
```

**Expected result:** "answer" = 241

### Prompt 1.3: The reference on the test patients

**Goal.** Fit the reference model of age, sex and chest pain type on the training patients and test it once on the test patients.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Before the cardiologist asks whether the results of the exercise test help, the project
needs the bar to clear: what a cardiologist knows before the test, the age, the sex and the type of
chest pain.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography after an exercise test. Each row
is a patient: "patient" gives the number of the patient in the data (0 to 302) and "set" the set of
Week 2 ("training", 227 patients; "test", 76 patients). The clinical variables are "age" (years),
"sex" ("man" or "woman"), "chest pain type" ("typical angina", "atypical angina", "non-anginal pain"
or "no pain"), "resting blood pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the
highest heart rate during the exercise test, per minute), "exercise angina" (1 when the exercise
test brought on angina) and "ST depression" (the depression of the ST segment during exercise
compared with rest, mm). "disease" is 1 when the angiogram showed more than 50 percent narrowing of
the diameter of at least one major coronary artery, and 0 otherwise.
Task: Make the inputs of the reference: the age, a column that is 1 for men and 0 for women, and
three columns of 0 and 1 for atypical angina, non-anginal pain and no pain, so that typical angina
is the reference category. Turn each input into a z-score with the mean and the standard deviation
of the training patients, and fit the usual logistic regression for disease, with its standard
settings and at most 1,000 iterations, on the training patients only. Compute the probability of
disease for every test patient and the area under the ROC curve (AUC) on the test patients.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of training and test patients and the test AUC of the reference, and keep
the AUC, with three decimals, under the name "answer".
Test: The model must be fitted on 227 training patients only, and the AUC must lie between 0.5 and
1.
```

**Expected result:** "answer" = 0.9

## Stop 2: Uncertainty and calibration

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-11/lecture.html#stop-2) · Jupyter notebook: «Stop 2 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-11/NB11_final_project_workshop.ipynb#scrollTo=stop-2-prompt)*

This stop asks how sure the results are. The bootstrap gives the intervals of the AUCs of the reference and of the full model, and of their difference in the same resamples; the calibration slope asks whether the probabilities of the full model hold on the test patients.

### Prompt 2.1: The intervals of the two AUCs

**Goal.** Give the test AUCs of the reference and of the full model with their bootstrap intervals.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The report of the final project gives every result with its uncertainty. With 76 test
patients, the cardiologist wants to know how far each AUC could move with other patients of the same
kind.
Data: The notebook holds a table named "data" with the 76 test patients of the Cleveland data of the
UCI Heart Disease data set, patients referred for coronary angiography after an exercise test. Each
row is a patient: "patient" gives the number of the patient in the data, "probability, reference"
the probability of coronary artery disease from a reference model of the course (a logistic
regression on the age, the sex and the chest pain type), and "probability, model" the probability
from the full model of the course (the same with the resting blood pressure, the cholesterol and
three results of the exercise test added). Both models were fitted on the 227 training patients
only. "disease" is 1 when the angiogram showed more than 50 percent narrowing of the diameter of at
least one major coronary artery, and 0 otherwise.
Task: Draw 2,000 resamples of the test patients: Each resample draws as many patients as the table
has, with replacement, with a random number generator started with the seed 2026. Skip a resample
that holds patients of one outcome only. In each resample, compute the area under the ROC curve
(AUC) of the reference and of the model on the same patients, and the difference, model minus
reference. The 95 percent interval of a result runs from the 2.5th to the 97.5th percentile of its
values over the resamples.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of resamples used and a table with the AUC of each model and of the
difference on all test patients, with their 2.5th and 97.5th percentiles, and keep the 2.5th
percentile of the AUC of the model, with three decimals, under the name "answer".
Test: Each interval must contain the AUC of all test patients, and the same resamples must serve
both models.
```

**Expected result:** "answer" = 0.872

### Prompt 2.2: The interval of the gain

**Goal.** Give the difference between the full model and the reference with its bootstrap interval, computed on the same resamples.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The question of the project is whether the results of the exercise test add to what the
cardiologist knew before the test. The answer is the interval of the difference, not the two AUCs
side by side.
Data: The notebook holds a table named "data" with the 76 test patients of the Cleveland data of the
UCI Heart Disease data set, patients referred for coronary angiography after an exercise test. Each
row is a patient: "patient" gives the number of the patient in the data, "probability, reference"
the probability of coronary artery disease from a reference model of the course (a logistic
regression on the age, the sex and the chest pain type), and "probability, model" the probability
from the full model of the course (the same with the resting blood pressure, the cholesterol and
three results of the exercise test added). Both models were fitted on the 227 training patients
only. "disease" is 1 when the angiogram showed more than 50 percent narrowing of the diameter of at
least one major coronary artery, and 0 otherwise.
Task: Draw 2,000 resamples of the test patients: Each resample draws as many patients as the table
has, with replacement, with a random number generator started with the seed 2026. Skip a resample
that holds patients of one outcome only. In each resample, compute the area under the ROC curve
(AUC) of the reference and of the model on the same patients, and the difference, model minus
reference. The 95 percent interval of a result runs from the 2.5th to the 97.5th percentile of its
values over the resamples. Also give the share of the resamples in which the difference is 0 or
less.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the table of the three results with their intervals and the share of resamples in
which the model is not better, and keep the 2.5th percentile of the difference, with three decimals,
under the name "answer".
Test: The difference must be computed in each resample from the two AUCs of that resample, not from
two separate sets of resamples.
```

**Expected result:** "answer" = −0.02

### Prompt 2.3: Calibration on the test patients

**Goal.** Compute the calibration intercept and slope of the full model on the test patients.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: A rule-out uses the probabilities themselves. The cardiologist wants to know whether they
are right on average and whether they are too extreme or too modest.
Data: The notebook holds a table named "data" with the 76 test patients of the Cleveland data of the
UCI Heart Disease data set, patients referred for coronary angiography after an exercise test. Each
row is a patient: "patient" gives the number of the patient in the data, and "probability, model"
the probability of coronary artery disease from a logistic regression of the course on eight
clinical variables, fitted on the 227 training patients only. "disease" is 1 when the angiogram
showed more than 50 percent narrowing of the diameter of at least one major coronary artery, and 0
otherwise.
Task: Turn every probability into its log-odds, the natural logarithm of the probability divided by
one minus the probability. The calibration intercept comes from a logistic regression for disease
with only an intercept and the log-odds as a fixed offset; the calibration slope is the coefficient
of the log-odds in a logistic regression for disease with an intercept and the log-odds as its only
input. Fit both without any penalty, for example by Newton steps.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the mean probability, the observed share of disease, the calibration intercept and the
calibration slope, and keep the slope, with three decimals, under the name "answer".
Test: A model that is perfectly calibrated would give an intercept of 0 and a slope of 1; the
intercept must have the sign of the observed share minus the mean probability.
```

**Expected result:** "answer" = 1.241

## Stop 3: The rule-out and its limits

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-11/lecture.html#stop-3) · Jupyter notebook: «Stop 3 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-11/NB11_final_project_workshop.ipynb#scrollTo=stop-3-prompt)*

This stop turns the probabilities into a decision. The rule-out threshold is chosen on the cross-validated probabilities of the training patients, the test patients show how many referrals it would spare, and the women and men of the test set show whether the rule-out can be called safe in both groups.

### Prompt 3.1: The rule-out threshold

**Goal.** Choose the rule-out threshold on the cross-validated probabilities of the training patients.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: A patient below the threshold would not be referred for angiography, so the threshold must
keep a very high sensitivity: at least 95 percent of the patients with disease must lie at or above
it. The test patients must play no part in the choice.
Data: The notebook holds a table named "data" with the 227 training patients of the Cleveland data
of the UCI Heart Disease data set, patients referred for coronary angiography after an exercise
test. Each row is a patient: "patient" gives the number of the patient in the data, and
"probability, cross-validated" the probability of coronary artery disease from a logistic regression
of the course on eight clinical variables, computed by five-fold cross-validation: Each patient gets
the probability of a model that was fitted on the other four fifths of the training patients.
"disease" is 1 when the angiogram showed more than 50 percent narrowing of the diameter of at least
one major coronary artery, and 0 otherwise.
Task: Among the thresholds 0.01, 0.02 and so on up to 0.50, take the highest at which at least 95
percent of the training patients with disease have a probability at or above it. Give the
sensitivity at that threshold and the share of the training patients whose probability lies below
it.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the threshold, the sensitivity and the share ruled out on the training patients, and
keep the threshold, with two decimals, under the name "answer".
Test: The sensitivity at the threshold must be at least 0.95, and at the next threshold of the grid
it must be below 0.95.
```

**Expected result:** "answer" = 0.18

### Prompt 3.2: The rule-out on the test patients

**Goal.** Apply the threshold to the test patients once and give the sensitivity, the specificity and the negative predictive value with their Wilson intervals.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how many referrals the rule-out would spare, whether it
misses any patient with disease, and how sure these numbers are with 76 patients.
Data: The notebook holds a table named "data" with the 76 test patients of the Cleveland data of the
UCI Heart Disease data set, patients referred for coronary angiography after an exercise test. Each
row is a patient: "patient" gives the number of the patient in the data, and "probability, model"
the probability of coronary artery disease from a logistic regression of the course on eight
clinical variables, fitted on the 227 training patients only. "disease" is 1 when the angiogram
showed more than 50 percent narrowing of the diameter of at least one major coronary artery, and 0
otherwise. The rule-out threshold of the project, chosen on the training patients, is 0.18: A
patient whose probability lies below it would not be referred for angiography.
Task: A patient is ruled out when the probability lies below the threshold. Count the patients with
and without disease among the ruled out and among the referred, and compute the sensitivity, the
specificity and the negative predictive value, the share free of disease among the patients ruled
out. Give each proportion with its 95 percent Wilson interval: For k of n, with z = 1.96, the centre
is (k/n plus z squared over 2n) divided by (1 plus z squared over n), and the half-width is z times
the square root of (k/n times one minus k/n, divided by n, plus z squared over 4n squared), divided
by (1 plus z squared over n).
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the table of the four counts, print the three proportions with their Wilson intervals,
and keep the number of patients ruled out under the name "answer".
Test: The four counts must add up to 76, and every interval must lie between 0 and 1 and contain its
proportion.
```

**Expected result:** "answer" = 27

### Prompt 3.3: Women and men

**Goal.** Give the sensitivity of the rule-out in women and in men with the lower bounds of their Wilson intervals.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: A rule-out has to be safe in every group in which it is used. The test set holds fewer
women than men, and fewer of the women have disease.
Data: The notebook holds a table named "data" with the 76 test patients of the Cleveland data of the
UCI Heart Disease data set, patients referred for coronary angiography after an exercise test. Each
row is a patient: "patient" gives the number of the patient in the data, "sex" is "man" or "woman",
and "probability, model" the probability of coronary artery disease from a logistic regression of
the course on eight clinical variables, fitted on the 227 training patients only. "disease" is 1
when the angiogram showed more than 50 percent narrowing of the diameter of at least one major
coronary artery, and 0 otherwise. The rule-out threshold of the project, chosen on the training
patients, is 0.18.
Task: For women and for men separately, count the patients, the patients with disease, the patients
with disease at or above the threshold and the patients ruled out, and compute the sensitivity. Give
each proportion with its 95 percent Wilson interval: For k of n, with z = 1.96, the centre is (k/n
plus z squared over 2n) divided by (1 plus z squared over n), and the half-width is z times the
square root of (k/n times one minus k/n, divided by n, plus z squared over 4n squared), divided by
(1 plus z squared over n).
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each sex, with the lower bound of the Wilson interval of the
sensitivity, and keep the lower bound for women, with three decimals, under the name "answer".
Test: The patients of the two rows must add up to 76, and a sensitivity of 1 must have an upper
bound of 1.
```

**Expected result:** "answer" = 0.646

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

### Ask for a review of a final project

```text
Review the code below, which is the analysis of a final project of a course for physicians on
artificial intelligence. Check seven points. Is every input known at the moment of the clinical
decision, or does any input come from a later test? Was the test set opened once, after every choice
was made on the training data? Is the number of patients with the outcome large enough for the
number of parameters of the model? Is the model compared with a simple reference on the same test
patients? Does every result carry an interval, and is the gain over the reference given as the
interval of a difference computed on the same resamples? Was the decision threshold chosen on the
training data only? Does any line send data of patients outside this computer? For each point,
answer yes, no or not clear, with the line of the code that shows it.

[paste the code here]
```

## Prompts of the weekly project

The [weekly project](README.md#weekly-project) can be built with four prompts, one for each step. The section *Weekly project* at the end of the Jupyter notebook prepares the table of each prompt and opens on its own. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Project step 1: The audit of the data and the split

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: A cardiologist builds a final project on ruling out coronary artery disease after an
exercise test. Before any model, the data are audited and split once into training and test
patients. For a final project of your own, rewrite the Data line for your own table: its columns,
their units and the meaning of the outcome, in words, and never a row of a patient.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography after an exercise test, with all
their columns. Each row is a patient: "patient" gives the number of the patient in the data (0 to
302). The eight variables of the project are "age" (years), "sex" ("man" or "woman"), "chest pain
type" ("typical angina", "atypical angina", "non-anginal pain" or "no pain"), "resting blood
pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the highest heart rate during the
exercise test, per minute), "exercise angina" (1 when the exercise test brought on angina) and "ST
depression" (the depression of the ST segment during exercise compared with rest, mm). Five more
columns come from the data set: "fasting blood sugar above 120" (1 when the fasting blood sugar was
above 120 mg/dL), "resting ECG" (0 normal, 1 an abnormality of the ST segment or the T wave, 2 left
ventricular hypertrophy), "ST slope" (the slope of the ST segment at peak exercise: 1 up, 2 flat, 3
down), "vessels on fluoroscopy" (the number of major vessels coloured by fluoroscopy, 0 to 3) and
"thallium scan" (3 normal, 6 fixed defect, 7 reversible defect). An empty cell is a missing value.
"disease" is 1 when the angiogram showed more than 50 percent narrowing of the diameter of at least
one major coronary artery, and 0 otherwise.
Task: Give the number of patients, the number and the share with disease, and the missing values of
every column. Then split the patients once, with all rows of a patient in the same set: a quarter of
them for the test, with the same share of disease in both sets, using the seed 2026 for the random
numbers. Give the numbers of patients and of patients with disease in each set.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the table of the missing values and the table of the two sets, and keep the number of
test patients with disease under the name "answer".
Test: The two sets must add up to all patients, and no patient may be in both.
```

### Project step 2: A reference, the model and the interval of the gain

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist compares the full model with what is known before the exercise test, on
the same test patients, and gives the gain with its interval.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography after an exercise test. Each row
is a patient: "patient" gives the number of the patient in the data (0 to 302) and "set" the set of
Week 2 ("training", 227 patients; "test", 76 patients). The clinical variables are "age" (years),
"sex" ("man" or "woman"), "chest pain type" ("typical angina", "atypical angina", "non-anginal pain"
or "no pain"), "resting blood pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the
highest heart rate during the exercise test, per minute), "exercise angina" (1 when the exercise
test brought on angina) and "ST depression" (the depression of the ST segment during exercise
compared with rest, mm). "disease" is 1 when the angiogram showed more than 50 percent narrowing of
the diameter of at least one major coronary artery, and 0 otherwise.
Task: Make the inputs of the reference: the age, a column that is 1 for men and 0 for women, and
three columns of 0 and 1 for atypical angina, non-anginal pain and no pain, so that typical angina
is the reference category. Turn each input into a z-score with the mean and the standard deviation
of the training patients, and fit the usual logistic regression for disease, with its standard
settings and at most 1,000 iterations, on the training patients only. The full model uses the same
inputs and adds the resting blood pressure, the cholesterol, the maximum heart rate, exercise angina
and the ST depression, fitted in the same way. Compute the probability of disease of both models for
every test patient and their AUCs on the test patients. Draw 2,000 resamples of the test patients:
Each resample draws as many patients as the table has, with replacement, with a random number
generator started with the seed 2026. Skip a resample that holds patients of one outcome only. In
each resample, compute the area under the ROC curve (AUC) of the reference and of the model on the
same patients, and the difference, model minus reference. The 95 percent interval of a result runs
from the 2.5th to the 97.5th percentile of its values over the resamples.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with the AUCs of the two models and of the difference with their intervals, and
keep the 2.5th percentile of the difference, with three decimals, under the name "answer".
Test: No test patient may be used to fit either model, and both models must be judged on the same
resamples.
```

### Project step 3: Calibration and the decision threshold

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist chooses the rule-out threshold of the full model on the training patients
and checks the calibration before the test patients are opened.
Data: The notebook holds a table named "data" with the 303 patients of the Cleveland data of the UCI
Heart Disease data set, patients referred for coronary angiography after an exercise test. Each row
is a patient: "patient" gives the number of the patient in the data (0 to 302) and "set" the set of
Week 2 ("training", 227 patients; "test", 76 patients). The clinical variables are "age" (years),
"sex" ("man" or "woman"), "chest pain type" ("typical angina", "atypical angina", "non-anginal pain"
or "no pain"), "resting blood pressure" (mmHg), "cholesterol" (mg/dL), "maximum heart rate" (the
highest heart rate during the exercise test, per minute), "exercise angina" (1 when the exercise
test brought on angina) and "ST depression" (the depression of the ST segment during exercise
compared with rest, mm). "disease" is 1 when the angiogram showed more than 50 percent narrowing of
the diameter of at least one major coronary artery, and 0 otherwise.
Task: Fit the full model of step 2 by five-fold cross-validation on the training patients, with the
folds drawn with the same share of disease and the seed 2026, so that every training patient gets
the probability of a model that did not see that patient. On these probabilities, compute the
calibration intercept and slope as in Stop 2, and choose the highest threshold among 0.01, 0.02 and
so on up to 0.50 at which at least 95 percent of the training patients with disease have a
probability at or above it. Then fit the full model on all training patients, apply the threshold
once to the test patients and count the patients ruled out, with and without disease.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the calibration of the cross-validated probabilities, the threshold and the counts on
the test patients, and keep the number of test patients ruled out under the name "answer".
Test: The threshold must be chosen before any test patient is used, and the sensitivity on the
training patients at the threshold must be at least 0.95.
```

### Project step 4: The table of results for the report

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The report of the final project follows TRIPOD+AI: Every result comes with its interval,
overall and in the groups in which the model would be used.
Data: The notebook holds a table named "data" with the 76 test patients of the Cleveland data of the
UCI Heart Disease data set, patients referred for coronary angiography after an exercise test. Each
row is a patient: "patient" gives the number of the patient in the data, "sex" is "man" or "woman",
"probability, reference" the probability of coronary artery disease from a reference model of the
course (a logistic regression on the age, the sex and the chest pain type), and "probability, model"
the probability from the full model of the course (the same with the resting blood pressure, the
cholesterol and three results of the exercise test added). Both models were fitted on the 227
training patients only. "disease" is 1 when the angiogram showed more than 50 percent narrowing of
the diameter of at least one major coronary artery, and 0 otherwise. The rule-out threshold of the
project, chosen on the training patients, is 0.18.
Task: Draw 2,000 resamples of the test patients: Each resample draws as many patients as the table
has, with replacement, with a random number generator started with the seed 2026. Skip a resample
that holds patients of one outcome only. In each resample, compute the area under the ROC curve
(AUC) of the reference and of the model on the same patients, and the difference, model minus
reference. The 95 percent interval of a result runs from the 2.5th to the 97.5th percentile of its
values over the resamples. Then, at the rule-out threshold of 0.18, compute the sensitivity, the
specificity and the negative predictive value for all test patients, for women and for men. Give
each proportion with its 95 percent Wilson interval: For k of n, with z = 1.96, the centre is (k/n
plus z squared over 2n) divided by (1 plus z squared over n), and the half-width is z times the
square root of (k/n times one minus k/n, divided by n, plus z squared over 4n squared), divided by
(1 plus z squared over n). Write all results into one table with the columns result, group, value,
lower bound and upper bound, ready to be copied into the report.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the table, and keep the lower bound of the negative predictive value of all test
patients, with three decimals, under the name "answer".
Test: Every interval must contain its value and lie between 0 and 1, except the interval of the
difference of the AUCs, which can be negative.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
