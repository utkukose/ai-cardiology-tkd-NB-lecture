# Prompt library, Week 1

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 1](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-01/PROMPTLAR.md)

This library holds every prompt of Week 1, written on the prompt card of the course. Each prompt can be copied into an artificial intelligence (AI) assistant as it stands. The code that comes back goes into the Jupyter notebook, below the exercise or prompt challenge of the same name, and runs there. In the exercises, the line with `teach.check` tells at once whether the result is right. The [prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [The prompt cycle](#the-prompt-cycle)
2. [Prompts of the exercises](#prompts-of-the-exercises)
3. [Prompt challenges of the sections](#prompt-challenges-of-the-sections)
4. [Patterns for explaining, repairing and testing code](#patterns-for-explaining-repairing-and-testing-code)
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

### Exercise 1.1: The RR interval from the heart rate

*Jupyter notebook, "Python step 1: Values, lists, dictionaries, decisions, loops and functions"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: A heart rate of 72 beats per minute (bpm).
Task: Compute the RR interval in seconds with RR = 60 / HR.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: Round the RR interval to three decimals. Store it in a variable named `answer` and end the
code with the line `teach.check("Exercise 1.1", answer)`. Return only the code in one block, with a
short comment above each step.
Test: Print also the RR interval at 60 bpm, which must be exactly 1.0 s.
```

### Exercise 1.2: A function for Fridericia's correction

*Jupyter notebook, "Python step 1: Values, lists, dictionaries, decisions, loops and functions"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The QT interval in milliseconds and the RR interval in seconds. The case of the week has a QT
of 391 ms at a heart rate of 85 bpm, so RR = 60 / 85 s.
Task: Write a function `qtc_fridericia(qt_ms, rr_s)` that returns the QT interval corrected with
Fridericia's formula, QTc = QT / RR^(1/3). Use it for the case of the week.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: Round the QTc of the case to one decimal. Store it in a variable named `answer` and end the
code with the line `teach.check("Exercise 1.2", answer)`. Return only the code in one block, with a
short comment above each step.
Test: Check with assert statements that qtc_fridericia(400, 1.0) returns 400.0 and that
qtc_fridericia(400, 0.729) returns 444.4 after rounding, because 0.729 is 0.9 cubed.
```

### Exercise 1.3: Counting with a loop

*Jupyter notebook, "Python step 1: Values, lists, dictionaries, decisions, loops and functions"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: A list named `clinic` holds patients as dictionaries with the keys "id", "hr" (heart rate in
bpm) and "qt" (QT interval in ms), for example {"id": "VC-0317", "hr": 85, "qt": 391}.
Task: Count the patients whose heart rate is above 80 bpm.
Constraints: Use a for loop and an if statement, without pandas. Use only these packages and the
variables named here. Do not load files and do not install anything.
Output: The number of patients. Store it in a variable named `answer` and end the code with the line
`teach.check("Exercise 1.3", answer)`. Return only the code in one block, with a short comment above
each step.
Test: For a list with the heart rates 72, 85 and 81, the same loop must count 2.
```

### Exercise A: Mean age of the patients with disease

*Jupyter notebook, Section 1, "The patient registry: The UCI Heart Disease data with pandas"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: A pandas DataFrame named `heart` holds the Cleveland data of the UCI Heart Disease data set,
one row per patient. The column age is in years, and the column disease is 1 for coronary artery
disease and 0 for none.
Task: Compute the mean age of the patients with disease equal to 1.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: Round the mean age to one decimal. Store it in a variable named `answer` and end the code
with the line `teach.check("Exercise A", answer)`. Return only the code in one block, with a short
comment above each step.
Test: Print the number of patients in each disease group; the two numbers must add up to 303.
```

### Exercise B: Percentage of women

*Jupyter notebook, Section 1, "The patient registry: The UCI Heart Disease data with pandas"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The DataFrame `heart`, with the column sex coded 1 for men and 0 for women.
Task: Compute the percentage of women among all patients.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: Round the percentage to one decimal. Store it in a variable named `answer` and end the code
with the line `teach.check("Exercise B", answer)`. Return only the code in one block, with a short
comment above each step.
Test: Compute the percentage of men in the same way and print the sum of the two percentages, which
must be 100.
```

### Exercise C: Counting a diagnosis in the virtual clinic

*Jupyter notebook, Section 2, "The virtual clinic opens"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: A pandas DataFrame named `clinic` holds the 500 synthetic patients of the virtual clinic. Its
column main_diagnosis holds one of the labels "none", "CCS", "HFpEF", "HFrEF" and "ACS".
Task: Count the patients whose main diagnosis is exactly "HFrEF".
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The number of patients as an integer. Store it in a variable named `answer` and end the code
with the line `teach.check("Exercise C", answer)`. Return only the code in one block, with a short
comment above each step.
Test: Print the counts of all diagnoses with value_counts(); they must add up to 500.
```

### Exercise D: Samples in one large box

*Jupyter notebook, Section 3, "The ECG as data: Samples, sampling frequency and units"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: An ECG sampled at 500 Hz. One large box of ECG paper lasts 0.2 s.
Task: Compute how many samples one large box holds, N = duration × sampling frequency.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The number of samples as an integer. Store it in a variable named `answer` and end the code
with the line `teach.check("Exercise D", answer)`. Return only the code in one block, with a short
comment above each step.
Test: One small box of 0.04 s must hold 20 samples at the same sampling frequency.
```

### Exercise E: The voltage of lead aVL

*Jupyter notebook, Section 4, "Twelve leads from one heart vector"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: `vclinic.LEAD_VECTORS` is a dictionary that maps each lead name, "I", "II", "III", "aVR",
"aVL", "aVF" and "V1" to "V6", to a NumPy array of three numbers. The axes point to the left (x), to
the feet (y) and to the front (z). The voltage of a lead in millivolts is the dot product of its
lead vector with the heart vector H.
Task: Compute the voltage of lead aVL for H = (0.6, 0.8, -0.2) mV.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: Round the voltage to three decimals and convert it to a float. Store it in a variable named
`answer` and end the code with the line `teach.check("Exercise E", answer)`. Return only the code in
one block, with a short comment above each step.
Test: Lead I has the vector (1, 0, 0), so the same code must give 0.6 mV for lead I.
```

### Exercise F: Fridericia's QTc from the registry

*Jupyter notebook, Section 5, "Measuring PR, QRS and QT"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: A QT interval of 343 ms at a heart rate of 98 bpm.
Task: Compute the QTc with Fridericia's formula, QTc = QT / RR^(1/3), with the RR interval in
seconds, RR = 60 / HR.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: Round the QTc to one decimal. Store it in a variable named `answer` and end the code with
the line `teach.check("Exercise F", answer)`. Return only the code in one block, with a short
comment above each step.
Test: At 60 bpm the RR interval is 1 s, so the QTc must equal the QT.
```

### Exercise G: The PR interval of patient VC-0188

*Jupyter notebook, Section 5, "Measuring PR, QRS and QT"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The notebook defines `measure_ecg(leads, fs)`. It takes a NumPy array of shape (samples, 12)
with the twelve leads in millivolts, in the order I, II, III, aVR, aVL, aVF, V1 to V6, and the
sampling frequency in Hz. It returns a dictionary with the keys "hr_bpm", "pr_ms", "qrs_ms",
"qt_ms", "qtc_bazett_ms" and "qtc_fridericia_ms". `vclinic.patient_ecg(clinic, patient_id)` returns
an ECG object, called `e` here. `e.leads` is a pandas DataFrame of the twelve leads, and `e.fs` is
the sampling frequency in Hz.
Task: Measure the PR interval of patient "VC-0188" and decide whether it meets the definition of a
first-degree atrioventricular block, a PR interval above 200 ms.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: Round the PR interval to the nearest millisecond and print the decision. Store it in a
variable named `answer` and end the code with the line `teach.check("Exercise G", answer)`. Return
only the code in one block, with a short comment above each step.
Test: Run the same code for patient "VC-0317", whose PR interval in the registry is 190 ms; the
measurement should lie within 10 ms of it.
```

### Exercise H: Atrial premature beats in MIT-BIH record 100

*Jupyter notebook, Section 6, "Finding every beat in a real recording: MIT-BIH record 100"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: A Python list named `ann_symbols` holds the annotation symbols of MIT-BIH record 100, one per
annotation: "N" for a normal beat, "A" for an atrial premature beat, "V" for a premature ventricular
contraction and "+" for a rhythm change.
Task: Count the atrial premature beats.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The number of beats as an integer. Store it in a variable named `answer` and end the code
with the line `teach.check("Exercise H", answer)`. Return only the code in one block, with a short
comment above each step.
Test: Count every symbol with collections.Counter and print the counts; their sum must equal
len(ann_symbols).
```

### Exercise I: RMSSD of five RR intervals

*Jupyter notebook, Section 7, "Heart rate variability"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The RR intervals 1000, 960, 1010, 990 and 1030 ms.
Task: Compute the root mean square of successive differences (RMSSD): Take the differences between
neighbouring intervals, square them, average the squares and take the square root.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: Round the RMSSD to two decimals. Store it in a variable named `answer` and end the code with
the line `teach.check("Exercise I", answer)`. Return only the code in one block, with a short
comment above each step.
Test: The intervals 800, 800 and 800 ms must give 0, and the intervals 800, 820 and 800 ms must give
20.
```

### Exercise J: A safe QTc from samples

*Jupyter notebook, Section 9, "AI pair programming: The code safety checklist"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: An ECG sampled at fs Hz; the QT interval and the RR interval are given as numbers of samples.
Task: Write a function `qtc_from_samples_fixed(qt_samples, rr_samples, fs)` without a default value
for fs. It converts the QT interval to milliseconds, qt_samples / fs × 1000, and the RR interval to
seconds, rr_samples / fs, and returns Bazett's QTc = QT / √RR in milliseconds. Use it for 196 and
353 samples at 500 Hz.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: Round the QTc to one decimal. Store it in a variable named `answer` and end the code with
the line `teach.check("Exercise J", answer)`. Return only the code in one block, with a short
comment above each step.
Test: For 200 and 500 samples at 500 Hz the QT is 400 ms and the RR interval 1 s, so the function
must return 400.0.
```

## Prompt challenges of the sections

Each numbered section of the Jupyter notebook ends with a prompt challenge. It has a prompt but no prepared code and no `teach.check`. The checks below each prompt tell whether the result is right.

### Section 1: Cholesterol by disease status

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The DataFrame `heart` with the columns chol, the serum cholesterol in mg/dL, and disease, 1
for coronary artery disease and 0 for none.
Task: Draw box plots of chol for the two disease groups side by side, with axis labels and units,
and print the median cholesterol of each group.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure and the two medians. Return only the code in one block, with a short comment
above each step.
Test: Print the size of each group; the two sizes must add up to 303.
```

**What to check.** The medians are 234.5 mg/dL without disease and 249.0 mg/dL with disease.

### Section 2: Diagnoses by sex

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The DataFrame `clinic` of the virtual clinic with the columns main_diagnosis and sex, coded
"F" or "M".
Task: Make a table of the number of patients for each main diagnosis by sex with pd.crosstab, with
row and column totals.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The table. Return only the code in one block, with a short comment above each step.
Test: The grand total must be 500.
```

**What to check.** The clinic holds 221 women and 279 men. Of the 47 patients with HFrEF, 16 are women and 31 are men.

### Section 3: One second of lead II, sample by sample

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: `case` is the ECG of the case of the week: case.time holds the times in seconds,
case.lead("II") the voltages of lead II in millivolts and case.fs the sampling frequency in Hz.
Task: Plot the first second of lead II with a small marker at every sample, with the time axis in
milliseconds and the voltage axis in millivolts, and print the number of plotted samples.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure and one number. Return only the code in one block, with a short comment above
each step.
Test: At 500 Hz one second holds 500 samples.
```

**What to check.** The printed number is 500, or 501 if both ends were included, and the time axis runs from 0 to 1000 ms.

### Section 4: The frontal axis of the whole clinic

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The DataFrame `clinic` with the column ecg_axis, the frontal QRS axis in degrees.
Task: Draw a histogram of ecg_axis with vertical lines at -30° and +90°. Print the number and the
percentage of patients with left axis deviation (axis below -30°) and with right axis deviation
(axis above +90°).
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure and four numbers. Return only the code in one block, with a short comment above
each step.
Test: The counts of the three groups, left, normal and right, must add up to 500.
```

**What to check.** Six patients (1.2 percent) have left axis deviation and 25 patients (5.0 percent) right axis deviation.

### Section 5: Bazett against Fridericia across heart rates

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The DataFrame `clinic` with the columns ecg_hr, the heart rate in bpm, and ecg_qt, the QT
interval in ms.
Task: For the first 50 patients, compute the QTc by Bazett, QT / √RR, and by Fridericia, QT /
RR^(1/3), with RR = 60 / ecg_hr in seconds. Plot the difference Bazett minus Fridericia against the
heart rate, with a horizontal line at zero, and print the largest difference.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure and one number. Return only the code in one block, with a short comment above
each step.
Test: At exactly 60 bpm both formulas give the same QTc, so the difference is zero.
```

**What to check.** The difference is positive in every patient above 60 bpm and negative in the three patients below 60 bpm. The largest difference is 48.6 ms.

### Section 6: Heart rate over thirty minutes

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: `found` holds the detected R peaks of MIT-BIH record 100 as sample positions, and `fs_mit` its
sampling frequency, 360 Hz.
Task: Compute the heart rate of every beat, 60 / RR with the RR interval in seconds, and plot it
against time in minutes. Print the mean heart rate.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure and one number. Return only the code in one block, with a short comment above
each step.
Test: An RR interval of 360 samples at 360 Hz lasts 1 s, that is, 60 bpm.
```

**What to check.** The mean heart rate is about 75.8 bpm, and the beat-to-beat rate ranges from about 53 to 115 bpm.

### Section 7: A Poincaré plot

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: `rr5` holds the RR intervals in milliseconds of five minutes of lead II of the case of the
week.
Task: Draw a Poincaré plot, each RR interval against the next one, with equal axes and the identity
line. Print SDNN, the standard deviation with ddof=1, and RMSSD.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure and two numbers. Return only the code in one block, with a short comment above
each step.
Test: For the intervals 800, 820 and 800 ms, the RMSSD is 20 ms.
```

**What to check.** SDNN and RMSSD equal the values printed earlier in Section 7, 17.7 ms and 17.4 ms.

### Section 8: The chest leads of a real infarction

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: `ptb` is a pandas DataFrame with the PTB record s0010_re: The columns v1 to v6 hold the chest
leads in millivolts, sampled at `fs_ptb`, 1000 Hz.
Task: Plot the first 3 seconds of V1 to V6 one under the other, with a shared time axis in seconds
and the voltage in millivolts.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure with six rows. Return only the code in one block, with a short comment above each
step.
Test: Three seconds at 1000 Hz hold 3000 samples per lead.
```

**What to check.** The figure has six rows of 3 s each. The header of the record states an acute inferolateral infarction: Which chest leads face the lateral wall?

### Section 9: A second opinion on AI-written code

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The function `qtc_from_samples` of this section, which an AI assistant wrote from a short
prompt: Paste its code below the prompt.
Task: Review the function with three questions. Are the units right? Is the sampling frequency
handled safely? Is the result physiological for a QT of 196 samples and an RR interval of 353
samples at 500 Hz? Then return a corrected function.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: A review in three short points and the corrected function. Return only the code in one
block, with a short comment above each step.
Test: The corrected function must return 400.0 ms for 200 and 500 samples at 500 Hz.
```

**What to check.** The review names two problems: the RR interval in milliseconds instead of seconds, and the default sampling frequency of 360 Hz.

## Patterns for explaining, repairing and testing code

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

### Ask for tests

```text
Write three short tests for the function below, with inputs whose correct result is known by hand,
for example a heart rate of 60 bpm, where the RR interval is exactly 1 s. Use plain assert
statements and explain what each test protects against.

[paste the function here]
```

## Prompt route of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. Each step builds on the one before it, so the test of a step must hold before the next prompt is sent. The report lists all four prompts in the AI usage log.

### Step 1: Extend measure_ecg with the frontal axis

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: `measure_ecg(leads, fs)` of Section 5 and its helper functions `detect_r_peaks` and
`qrs_bounds`. `vclinic.frontal_axis(v_i, v_avf)` returns the frontal axis in degrees from the net
QRS voltages of leads I and aVF.
Task: Write `measure_ecg_axis(leads, fs)`, which returns the dictionary of `measure_ecg` with one
more key, "axis_deg". For each beat, take the net QRS voltage of leads I and aVF, the largest
positive plus the largest negative value between QRS onset and QRS end, measured from the median of
the 30 ms before the onset. Pass the medians over all beats to vclinic.frontal_axis.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The function and its result for patient VC-0317. Return only the code in one block, with a
short comment above each step.
Test: The registry gives an axis of 21° for VC-0317. The measured axis should lie within about 10°
of it, because the net voltages also contain the small septal and terminal forces.
```

### Step 2: Ten patients against the truth

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The DataFrame `clinic` with the columns patient_id, ecg_rhythm ("sinus" or "AF") and
ecg_conduction ("normal", "LBBB" or "RBBB"), and `vclinic.patient_ecg(clinic, patient_id)`, whose
result `e` has the dictionary `e.truth` with the keys "hr_bpm", "pr_ms", "qrs_ms", "qt_ms" and
"axis_deg".
Task: Choose ten patients, at least two of them with atrial fibrillation or a bundle branch block.
Run `measure_ecg_axis` on each, with `sinus=False` for atrial fibrillation, and build a table with
the measured value, the true value and their difference for the heart rate, PR, QRS, QT and the
axis.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: A pandas DataFrame with one row per patient. Return only the code in one block, with a short
comment above each step.
Test: The table has ten rows, and for VC-0317 the differences in PR, QRS and QT are only a few
milliseconds.
```

### Step 3: The two real records

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: `leads_ptb`, a NumPy array of the twelve leads of the PTB record, and `fs_ptb`, 1000 Hz, from
Section 8. `found`, the detected R peaks of MIT-BIH record 100 as sample positions, and `fs_mit`,
360 Hz, from Section 6.
Task: Run `measure_ecg_axis` on the PTB record, and compute the mean heart rate of MIT-BIH record
100 from the detected beats.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The measurements of the PTB record and the mean heart rate of record 100. Return only the
code in one block, with a short comment above each step.
Test: For the PTB record, Section 8 reports a heart rate of 81.8 bpm, a PR interval of 225 ms, a QRS
duration of 137 ms and a QT of 436.7 ms.
```

### Step 4: Bazett or Fridericia for each patient

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, and the course package vclinic with its module teach is available.
Data: The table of step 2 with the measured QT and heart rate of each patient, and the sex of each
patient from `clinic`.
Task: For each patient, compute the QTc by Bazett and by Fridericia and decide whether it is
prolonged, with 460 ms for women and 450 ms for men. List the patients for whom the two formulas
disagree.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The table with two new columns and the list of disagreements. Return only the code in one
block, with a short comment above each step.
Test: VC-0317, a woman at 85 bpm, is prolonged by Bazett's formula and not by Fridericia's.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
