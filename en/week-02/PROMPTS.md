# Prompt library, Week 2

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 2](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-02/PROMPTLAR.md)

This library holds every prompt of Week 2, written on the prompt card of the course. Each prompt can be copied into an artificial intelligence (AI) assistant as it stands. The code that comes back goes into the Jupyter notebook, below the exercise or prompt challenge of the same name, and runs there. In the exercises, the line with `teach.check` tells at once whether the result is right. The [prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [The prompt cycle](#the-prompt-cycle)
2. [Prompts of the exercises](#prompts-of-the-exercises)
3. [Prompt challenges of the sections](#prompt-challenges-of-the-sections)
4. [Patterns for explaining, repairing and reviewing code](#patterns-for-explaining-repairing-and-reviewing-code)
5. [Prompt route of the weekly project](#prompt-route-of-the-weekly-project)

## The prompt cycle

| Step | What to do |
|---|---|
| 1. Describe | Copy the prompt card of the exercise, or write it with the seven fields: role, context, data, task, constraints, output and test. |
| 2. Generate | Send the prompt to an AI assistant. |
| 3. Run | Paste the code into the empty cell below the exercise and run it. |
| 4. Check | Read the result of `teach.check`, *correct* or *not yet*, and the test of the prompt. A result of *not yet* goes back to the assistant with the repair pattern. |
| 5. Explain | Ask the assistant for a line-by-line explanation, then explain the code once more in your own words. |
| 6. Log | Add the tool, the prompt, what was checked and what was changed to the AI usage log. |

## Prompts of the exercises

Each exercise of the Jupyter notebook has its prompt route in a folded cell right below it. The prompts below are the same. Paste the code from the assistant into the empty answer cell of the exercise and run it.

### Exercise 2.1: Missing cells of the table

*Jupyter notebook, "Python step 2: Data for models"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: A pandas DataFrame named `heart` holds the Cleveland data of the UCI Heart Disease data set:
303 patients, one row per patient. The column disease is 0 or 1: 1 for coronary artery disease
(CAD), 0 for none. Missing values are NaN.
Task: Count all missing cells of `heart`, over all rows and columns.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The number of missing cells as an integer. Store it in a variable named `answer` and end the
code with the line `teach.check("Exercise 2.1", answer)`. Return only the code in one block, with a
short comment above each step.
Test: First test the method on `pd.DataFrame({"a": [1, None], "b": [None, 4]})`, which must give 2.
Then print the number of missing values of each column that has any; only the columns ca and thal
may appear.
```

### Exercise 2.2: Size of the test set

*Jupyter notebook, "Python step 2: Data for models"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `X`, a DataFrame with 303 rows and 10 numeric columns, and `y`, a Series with 303 values 0 or
1.
Task: Split `X` and `y` with
`train_test_split(X, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE)` and count the
patients of the test set.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The number of patients in the test set. Store it in a variable named `answer` and end the
code with the line `teach.check("Exercise 2.2", answer)`. Return only the code in one block, with a
short comment above each step.
Test: Print the sizes of both sets; they must add up to 303.
```

### Exercise 2.3: Accuracy of a first pipeline

*Jupyter notebook, "Python step 2: Data for models"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `X_train`, `X_test`, `y_train` and `y_test` come from
`train_test_split(X, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE)`. `X` has the columns
age (years), sex (1 man, 0 woman), trestbps (resting systolic blood pressure, mmHg), chol (serum
cholesterol, mg/dL), thalach (maximum heart rate, bpm), exang (exercise angina, 0 or 1), oldpeak (ST
depression, mm) and three dummy columns of the chest pain type, cp_2.0, cp_3.0 and cp_4.0. `y` is
the column disease.
Task: Build `make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))`, fit it on the
training set and compute its accuracy on the test set with `score`.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The accuracy on the test set, rounded to three decimals. Store it in a variable named
`answer` and end the code with the line `teach.check("Exercise 2.3", answer)`. Return only the code
in one block, with a short comment above each step.
Test: Print also the accuracy on the training set; it should be of the same size and not 1.0.
```

### Exercise A: The probability of the case with typical angina

*Jupyter notebook, Section 1, "A first model: Logistic regression for coronary artery disease"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `model`, a fitted pipeline of StandardScaler and LogisticRegression for CAD, and `case`, a
one-row DataFrame with the columns of `X`: age 57 years, sex 1, trestbps 119 mmHg, chol 230 mg/dL,
thalach 132 bpm, exang 1, oldpeak 1.6 mm, cp_2.0 1, cp_3.0 0 and cp_4.0 0.
Task: Copy `case`, set cp_2.0 to 0 so that all three chest pain columns are 0 (typical angina), and
compute the probability of CAD with `model.predict_proba`.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The probability, rounded to three decimals. Store it in a variable named `answer` and end
the code with the line `teach.check("Exercise A", answer)`. Return only the code in one block, with
a short comment above each step.
Test: Print the probability of the unchanged `case` as well; the two probabilities must differ and
both lie between 0 and 1.
```

### Exercise B: The AUC on the test set

*Jupyter notebook, Section 2, "Measuring a model: Confusion matrix and ROC curve"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `model`, a fitted pipeline for CAD, and the test set `X_test`, `y_test` (76 patients; `y_test`
is 0 or 1, with 1 for CAD).
Task: Compute the area under the receiver operating characteristic curve (AUC) of the probabilities
of `model` on the test set with `roc_auc_score`.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The AUC, rounded to three decimals. Store it in a variable named `answer` and end the code
with the line `teach.check("Exercise B", answer)`. Return only the code in one block, with a short
comment above each step.
Test: Compute also the AUC of 1 minus the probabilities; the two values must add up to 1.
```

### Exercise C: Sensitivity at the threshold 0.5

*Jupyter notebook, Section 2, "Measuring a model: Confusion matrix and ROC curve"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `model`, a fitted pipeline for CAD, and the test set `X_test`, `y_test` (76 patients, 35 of
them with CAD; `y_test` is 0 or 1).
Task: Label a patient positive when the probability of CAD is 0.5 or more, count TP, FP, TN and FN
with `confusion_matrix(...).ravel()` and compute the sensitivity TP / (TP + FN).
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The sensitivity, rounded to three decimals. Store it in a variable named `answer` and end
the code with the line `teach.check("Exercise C", answer)`. Return only the code in one block, with
a short comment above each step.
Test: Print TP and FN; their sum must be 35, the number of test patients with CAD.
```

### Exercise D: Cross-validated AUC

*Jupyter notebook, Section 3, "Cross-validation and data leakage"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `X` and `y`, the 303 Cleveland patients (`y` is 0 or 1, with 1 for CAD), and `pipe`, an
unfitted pipeline of StandardScaler and LogisticRegression(max_iter=1000).
Task: Run a five-fold cross-validation with
`StratifiedKFold(5, shuffle=True, random_state=RANDOM_STATE)` and
`cross_val_score(..., scoring="roc_auc")`, and take the mean of the five AUC values.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The mean AUC, rounded to three decimals. Store it in a variable named `answer` and end the
code with the line `teach.check("Exercise D", answer)`. Return only the code in one block, with a
short comment above each step.
Test: Print the five AUC values; each must lie between 0.5 and 1.
```

### Exercise E: Gini impurity of the root

*Jupyter notebook, Section 4, "Decision trees and random forests"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `y_train`, the outcome of the 227 training patients, 0 or 1.
Task: Write a function `gini(n0, n1)` that returns 1 - (p0² + p1²) with p0 = n0 / (n0 + n1) and p1 =
n1 / (n0 + n1), and apply it to the counts of 0 and 1 in `y_train`.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The Gini impurity, rounded to three decimals. Store it in a variable named `answer` and end
the code with the line `teach.check("Exercise E", answer)`. Return only the code in one block, with
a short comment above each step.
Test: Check with assert statements that gini(50, 50) is 0.5 and gini(100, 0) is 0.0.
```

### Exercise F: The coefficient of smoking in the registry

*Jupyter notebook, Section 5, "The risk outpatient clinic: Coronary artery disease in the registry"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: A pandas DataFrame named `registry` holds 2000 synthetic patients of the virtual clinic, one
row per patient, made with `vclinic.add_followup(vclinic.make_cohort(2000, seed=RANDOM_STATE))`.
Among its columns are age (years), sex ("M" or "F"), smoker, diabetes, hypertension, family_history
and cad (0 or 1), ldl and hdl (mg/dL), egfr (mL/min/1.73 m²), lvef (%), ntprobnp (pg/mL), af (0 or
1), bmi (kg/m²), sbp (mmHg), main_diagnosis, followup_months (months) and event (1 for death or
hospitalisation for heart failure, 0 for censored).
Task: Code the variables as in `vclinic.TRUE_EFFECTS`: age_per_10y = (age - 60) / 10, male = 1 for
sex "M", smoker, diabetes, hypertension, ldl_per_40 = (ldl - 130) / 40, hdl_per_15 = (hdl - 50) / 15
and family_history. Fit `LogisticRegression(C=np.inf, max_iter=2000)` to the column cad and read the
coefficient of smoker.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The coefficient of smoker, rounded to two decimals. Store it in a variable named `answer`
and end the code with the line `teach.check("Exercise F", answer)`. Return only the code in one
block, with a short comment above each step.
Test: Print all learned coefficients next to the values of `vclinic.TRUE_EFFECTS`; each should lie
within about 0.2 of its true value.
```

### Exercise G: The PPV from the prevalence

*Jupyter notebook, Section 6, "Rare outcomes: Imbalanced data"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: A screening model with a sensitivity of 0.85 and a specificity of 0.90, used in a population
with a prevalence of 0.05 (5%).
Task: Write a function `ppv(se, sp, prev)` with Bayes' theorem, PPV = se × prev / (se × prev + (1 -
sp) × (1 - prev)), and apply it.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The PPV, rounded to three decimals. Store it in a variable named `answer` and end the code
with the line `teach.check("Exercise G", answer)`. Return only the code in one block, with a short
comment above each step.
Test: Check with an assert statement that ppv(0.85, 0.85, 0.5) returns 0.85.
```

### Exercise H: Silhouette of three clusters

*Jupyter notebook, Section 7, "Finding subgroups: k-means on the patients with heart failure"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `X_hf`, a NumPy array with one row per patient with heart failure and nine columns, such as
age (years), lvef (%) and tapse_mm (mm), standardised to z-scores.
Task: Fit `KMeans(n_clusters=3, n_init=10, random_state=RANDOM_STATE)` to `X_hf` and compute the
mean silhouette of its labels with `silhouette_score`.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The mean silhouette, rounded to three decimals. Store it in a variable named `answer` and
end the code with the line `teach.check("Exercise H", answer)`. Return only the code in one block,
with a short comment above each step.
Test: Print the number of patients in each cluster; the three numbers must add up to 407, the number
of rows of `X_hf`.
```

### Exercise I: Kaplan-Meier at 24 months

*Jupyter notebook, Section 8, "Survival analysis: Kaplan-Meier and the log-rank test"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `hf`, a DataFrame of the patients with heart failure with the columns main_diagnosis ("HFrEF"
or "HFpEF"), followup_months (months) and event (1 for death or hospitalisation, 0 for censored).
Task: Write a function `kaplan_meier(time, event)` that returns the times of the steps and the
survival after each step, with S(t) = product of (1 - d_i / n_i) over the event times up to t. Apply
it to the patients with HFrEF and read S at 24 months.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: S(24), rounded to three decimals. Store it in a variable named `answer` and end the code
with the line `teach.check("Exercise I", answer)`. Return only the code in one block, with a short
comment above each step.
Test: For the times 2, 3, 3, 5, 6, 8, 9, 11, 12, 12 months with the events 1, 1, 0, 1, 0, 1, 0, 1,
0, 0, the survival after month 11 must be 0.3657 after rounding to four decimals.
```

### Exercise J: The corrected model of the assistant

*Jupyter notebook, Section 9, "AI pair programming, part 2: Reviewing a model built by an assistant"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: A pandas DataFrame named `registry` holds 2000 synthetic patients of the virtual clinic, one
row per patient, made with `vclinic.add_followup(vclinic.make_cohort(2000, seed=RANDOM_STATE))`.
Among its columns are age (years), sex ("M" or "F"), smoker, diabetes, hypertension, family_history
and cad (0 or 1), ldl and hdl (mg/dL), egfr (mL/min/1.73 m²), lvef (%), ntprobnp (pg/mL), af (0 or
1), bmi (kg/m²), sbp (mmHg), main_diagnosis, followup_months (months) and event (1 for death or
hospitalisation for heart failure, 0 for censored). The column event_12m is 1 for an event within 12
months. The list `features` holds the columns age, egfr, lvef, ntprobnp, af, diabetes, bmi, sbp and
followup_months.
Task: Remove followup_months from the variables, because it is not known at the time of the
decision. Then compute the mean AUC of
`RandomForestClassifier(n_estimators=200, min_samples_leaf=5, random_state=RANDOM_STATE)` for
event_12m with a five-fold `StratifiedKFold(5, shuffle=True, random_state=RANDOM_STATE)`.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The mean cross-validated AUC, rounded to three decimals. Store it in a variable named
`answer` and end the code with the line `teach.check("Exercise J", answer)`. Return only the code in
one block, with a short comment above each step.
Test: Print also the AUC of the same forest fitted and scored on all patients; it must be clearly
higher than the cross-validated value, above 0.95.
```

## Prompt challenges of the sections

Each numbered section of the Jupyter notebook ends with a prompt challenge. It has a prompt but no prepared code and no `teach.check`. The checks below each prompt tell whether the result is right.

### Section 1: A forest plot of the odds ratios

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `model`, a fitted pipeline of StandardScaler and LogisticRegression for CAD, and `X`, whose
columns are the variables of the model.
Task: Draw the odds ratio per standard deviation of each variable as a point on a logarithmic
horizontal axis, with a vertical line at 1 and the variable names on the vertical axis.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure. Return only the code in one block, with a short comment above each step.
Test: Print the odds ratios as well; thalach must lie below 1 and oldpeak above 1.
```

**What to check.** The odds ratio per SD is about 0.58 for thalach and about 2.07 for oldpeak; sex and cp_4.0 are above 2.

### Section 2: Three thresholds side by side

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `p_test`, the probabilities of CAD of the 76 test patients, and `y_test`, their outcome.
Task: Build a table with one row for each of the thresholds 0.3, 0.5 and 0.7 and the columns Se, Sp,
PPV and NPV.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: A pandas DataFrame rounded to three decimals. Return only the code in one block, with a
short comment above each step.
Test: At 0.5 the table must show Se 0.800 and Sp 0.902, as in Section 2.
```

**What to check.** Sensitivity falls from 0.857 to 0.571 and specificity rises from 0.805 to 0.951 between the thresholds 0.3 and 0.7.

### Section 3: Logistic regression or random forest?

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `X` and `y`, the 303 Cleveland patients, and the folds
`cv = StratifiedKFold(5, shuffle=True, random_state=RANDOM_STATE)`.
Task: Compare the mean cross-validated AUC of the pipeline of StandardScaler and
LogisticRegression(max_iter=1000) with that of
`RandomForestClassifier(n_estimators=300, random_state=RANDOM_STATE)` on the same folds.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The two means and standard deviations. Return only the code in one block, with a short
comment above each step.
Test: The logistic regression must give the mean AUC of Exercise D.
```

**What to check.** Both models reach a mean AUC of about 0.87; the random forest is not better on these 303 patients.

### Section 4: How deep should a tree be?

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `X_train`, `X_test`, `y_train` and `y_test` come from
`train_test_split(X, y, test_size=0.25, stratify=y, random_state=RANDOM_STATE)`. `X` has the columns
age (years), sex (1 man, 0 woman), trestbps (resting systolic blood pressure, mmHg), chol (serum
cholesterol, mg/dL), thalach (maximum heart rate, bpm), exang (exercise angina, 0 or 1), oldpeak (ST
depression, mm) and three dummy columns of the chest pain type, cp_2.0, cp_3.0 and cp_4.0. `y` is
the column disease.
Task: Fit `DecisionTreeClassifier(max_depth=d, random_state=RANDOM_STATE)` for d from 1 to 8 on the
training set and plot the test AUC against the depth.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure and the eight AUC values. Return only the code in one block, with a short comment
above each step.
Test: The depth 3 must give the test AUC of the tree of Section 4.
```

**What to check.** The AUC peaks at a depth of 3, about 0.81, and falls below 0.75 for deeper trees: a picture of overfitting.

### Section 5: The risk of the case across the ages

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: A pandas DataFrame named `registry` holds 2000 synthetic patients of the virtual clinic, one
row per patient, made with `vclinic.add_followup(vclinic.make_cohort(2000, seed=RANDOM_STATE))`.
Among its columns are age (years), sex ("M" or "F"), smoker, diabetes, hypertension, family_history
and cad (0 or 1), ldl and hdl (mg/dL), egfr (mL/min/1.73 m²), lvef (%), ntprobnp (pg/mL), af (0 or
1), bmi (kg/m²), sbp (mmHg), main_diagnosis, followup_months (months) and event (1 for death or
hospitalisation for heart failure, 0 for censored). `cad_model` is a fitted LogisticRegression on
the table `risk_table(registry)`, and the function `risk_table(df)` codes the variables as in
`vclinic.TRUE_EFFECTS`.
Task: Take the row of patient VC-0246, change only the age from 40 to 80 years in steps of one year
and plot the probability of CAD of `cad_model` against the age.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure. Return only the code in one block, with a short comment above each step.
Test: At 57 years the curve must pass through the probability that Section 5 prints for VC-0246.
```

**What to check.** The curve rises from about 0.55 at 40 years to about 0.9 at 80 years and passes through about 0.76 at 57 years.

### Section 6: Two precision-recall curves

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `Xe_train`, `Xe_test`, `ye_train` and `ye_test`, the training and test sets of the event
within 12 months (prevalence about 0.034), with the columns age, egfr, lvef, the logarithm of
ntprobnp, af and diabetes.
Task: Fit a pipeline of StandardScaler and LogisticRegression(max_iter=1000) once without and once
with `class_weight="balanced"`, and draw both precision-recall curves in one figure with a
horizontal line at the prevalence.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure and the two average precisions. Return only the code in one block, with a short
comment above each step.
Test: The two average precisions must match the AP column of the table of Section 6.
```

**What to check.** The two curves almost overlap, with an average precision of about 0.10: Class weights move the threshold, not the ranking of the patients.

### Section 7: A heat map of the clusters

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `hf`, the DataFrame of the patients with heart failure with a column cluster (0, 1 or 2), and
`HF_FEATURES`, the list of the nine clustering variables.
Task: Compute the mean of each variable in each cluster, turn each variable into a z-score across
the three clusters and draw the table as a heat map with the values written in the cells.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure. Return only the code in one block, with a short comment above each step.
Test: The cluster with the lowest mean lvef must also have the highest mean ntprobnp.
```

**What to check.** One cluster has a low ejection fraction and the highest NT-proBNP (HFrEF), one is the oldest with a large left atrium and a low TAPSE, and one is the youngest with the highest BMI and eGFR.

### Section 8: Numbers at risk

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `hf`, the DataFrame of the patients with heart failure with the columns cluster,
followup_months and event.
Task: Build the table of the numbers at risk, the patients still followed and free of events, at 0,
12, 24, 36 and 48 months for each cluster, as printed under a Kaplan-Meier figure in a paper.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: A pandas DataFrame with one row per cluster. Return only the code in one block, with a short
comment above each step.
Test: At month 0 the numbers must equal the sizes of the clusters.
```

**What to check.** The numbers fall in every cluster, fastest in the cluster of the oldest patients.

### Section 9: A review of the assistant's model

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: The code of the AI assistant in Section 9, pasted into the prompt as text.
Task: Review the code with four questions: Which variables would not be known at the time of the
decision? Does any step learn from all patients before the split? On which patients is the AUC
measured? Is the outcome rare? Then return the corrected code.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: A short list of the problems and the corrected code. Return only the code in one block, with
a short comment above each step.
Test: The corrected code must report a cross-validated AUC, not the AUC on the training patients.
```

**What to check.** The review names the follow-up time as information from the future and the AUC measured on the training patients; the corrected AUC is about 0.85 instead of 1.0.

## Patterns for explaining, repairing and reviewing code

These four patterns work with the code of any exercise. The parts in square brackets are replaced before the prompt is sent.

### Explain the code

```text
Explain the following Python code line by line for a physician who is new to Python. Then name two
ways in which it could return a wrong result without an error message.

[paste the code here]
```

### Repair code that does not pass the check

```text
The code below was written for this task: [paste the task of the prompt]. It runs, but the check of
the course prints "not yet". Find the error, explain it in two sentences and return the corrected
code. Keep the variable names and the line with teach.check.

[paste the code here]
```

### Understand an error message

```text
Running the cell below in a Jupyter notebook gives the error message that follows. Explain the cause
in plain language and return the corrected code.

[paste the code here]

[paste the error message here]
```

### Ask for a model review

```text
Review the code below, which builds and evaluates a prediction model. Check four things: variables
that would not be known at the time of the decision, any step that learns from all patients before
the split, the patients on whom the performance is measured, and whether the outcome is rare. Answer
with a short list, then return the corrected code.

[paste the code here]
```

## Prompt route of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. Each step builds on the one before it, so the test of a step must hold before the next prompt is sent. The report lists all four prompts in the AI usage log.

### Step 1: Choose the number of phenogroups

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: `registry`, the 2000 patients of the virtual clinic with follow-up, from
`vclinic.add_followup(vclinic.make_cohort(2000, seed=RANDOM_STATE))`. The patients with heart
failure have main_diagnosis "HFrEF" or "HFpEF". Columns: age (years), sex, bmi (kg/m²), diabetes and
af (0 or 1), egfr (mL/min/1.73 m²), lvef (%), ntprobnp (pg/mL), lavi (mL/m²), e_e_prime,
lv_mass_index (g/m²), tapse_mm (mm), followup_months (months) and event (1 for death or
hospitalisation for heart failure, 0 for censored).
Task: Take the patients with heart failure, standardise the nine variables age, bmi, egfr, lvef, the
logarithm of ntprobnp, lavi, e_e_prime, lv_mass_index and tapse_mm, and fit k-means with k from 2 to
6 (n_init=10, random_state=RANDOM_STATE). Report the WCSS and the mean silhouette of each k, choose
k and give the clinical reason for the choice.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: A table of k, WCSS and silhouette, and a column cluster added to the DataFrame of the
patients with heart failure. Return only the code in one block, with a short comment above each
step.
Test: The number of patients with heart failure must be the same before and after the clustering,
and every cluster must hold at least 30 patients.
```

### Step 2: Describe and name the phenogroups

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: The DataFrame of the patients with heart failure from step 1, with its column cluster and the
columns of the registry.
Task: Build a table with the size of each cluster, the mean or the percentage of age, female sex,
bmi, diabetes, af, egfr, lvef, ntprobnp (median), lavi, e_e_prime, lv_mass_index and tapse_mm, and
the share of HFrEF. Propose a short clinical name for each cluster.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: A pandas DataFrame with one column per cluster. Return only the code in one block, with a
short comment above each step.
Test: The sizes in the table must add up to the number of patients with heart failure.
```

### Step 3: Prognosis by phenogroup

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: The DataFrame of step 1 with the columns cluster, main_diagnosis, followup_months and event,
and the functions `kaplan_meier(time, event)` and `logrank(time, event, group)` of Section 8 of the
Jupyter notebook.
Task: Draw the Kaplan-Meier curves of the clusters and, in a second panel, of HFrEF and HFpEF.
Report S(24) for each group and the log-rank test of each grouping.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure with two panels, a table of S(24) and the two log-rank tests. Return only the
code in one block, with a short comment above each step.
Test: The curves must start at 1 and never rise; the log-rank test of HFrEF against HFpEF must give
the p value of Section 8.
```

### Step 4: Compare with the hidden truth

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as plt
and the module stats of SciPy as stats, and scikit-learn is installed. The course package vclinic
with its module teach is available, and RANDOM_STATE = 2026.
Data: The DataFrame of step 1 with the columns cluster and hf_phenogroup, the phenogroup that the
course hid in each patient.
Task: Cross-tabulate the clusters with hf_phenogroup and compute the adjusted Rand index. Write
three sentences on what the clustering found that the ejection fraction alone misses.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The cross-table, the adjusted Rand index and the three sentences. Return only the code in
one block, with a short comment above each step.
Test: The adjusted Rand index must lie between −1 and 1; with k = 3 it should be clearly above 0.5.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
