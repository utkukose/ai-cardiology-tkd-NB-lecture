# Prompt library, Week 1

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 1](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-01/PROMPTLAR.md)

This library holds every prompt of the prompt path of Week 1, Part 1 of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the notebook, into the cell below the step of the same number, and runs there. The [guide to the prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [How a step works](#how-a-step-works)
2. [Stop 1: Patient tables](#stop-1-patient-tables)
3. [Stop 2: The ECG as data](#stop-2-the-ecg-as-data)
4. [Stop 3: Real recordings and a function to check](#stop-3-real-recordings-and-a-function-to-check)
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

## Stop 1: Patient tables

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html#stop-1) · The same result on the Python path: Python step 1, Sections 1 and 2*

The registry of a clinic is a table: one row per patient and one column per variable. In this stop the 303 patients of the Cleveland data and the first 500 patients of the virtual clinic are summarised with an average, a share and a count, each with a clinical question behind it.

### Step 1.1: The mean age of the patients with disease

**Goal.** Find out how old, on average, the Cleveland patients with coronary artery disease were.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt. The course package vclinic is imported, together with its module measure. RANDOM_STATE = 2026.
Data: `heart` is a pandas DataFrame with the 303 patients of the Cleveland Clinic in the UCI Heart
Disease data set, one row per patient. The columns used here: age (years), sex (1 man, 0 woman) and
disease (1 if at least one major coronary artery had a diameter narrowing of more than 50 percent at
angiography, otherwise 0).
Task: Select the patients whose disease value is 1 and compute their mean age. Print how many
patients were selected as well.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The mean age in years, rounded to one decimal. Save it in a variable named `mean_age` and
print it with a short label. Return only the code, in one block, with a short comment above each
step.
Test: The mean age of all 303 patients is 54.4 years; the result for the patients with disease must
differ from it.
```

**Expected result:** `mean_age` = 56.6

### Step 1.2: The share of women

**Goal.** Find out which percentage of the Cleveland patients were women.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt. The course package vclinic is imported, together with its module measure. RANDOM_STATE = 2026.
Data: `heart` is a pandas DataFrame with the 303 patients of the Cleveland Clinic in the UCI Heart
Disease data set, one row per patient. The columns used here: age (years), sex (1 man, 0 woman) and
disease (1 if at least one major coronary artery had a diameter narrowing of more than 50 percent at
angiography, otherwise 0).
Task: Count the patients with sex equal to 0 and divide by the number of all patients. Print the
share of men as well.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The share of women in percent, rounded to one decimal. Save it in a variable named
`pct_women` and print it with a short label. Return only the code, in one block, with a short
comment above each step.
Test: The shares of women and men must add up to 100.
```

**Expected result:** `pct_women` = 32.0

### Step 1.3: Patients with HFrEF in the virtual clinic

**Goal.** Count the patients of the virtual clinic who have heart failure with reduced ejection fraction, and see the ejection fraction of every diagnosis in one figure.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt. The course package vclinic is imported, together with its module measure. RANDOM_STATE = 2026.
Data: `clinic` is a pandas DataFrame with the first 500 synthetic patients of the virtual clinic,
one row per patient. The columns used here: patient_id, main_diagnosis ("none", "CCS" chronic
coronary syndrome, "ACS" acute coronary syndrome, "HFrEF" heart failure with reduced ejection
fraction or "HFpEF" heart failure with preserved ejection fraction) and lvef (left ventricular
ejection fraction, %).
Task: Count the patients whose main_diagnosis is "HFrEF". Then draw a box plot of lvef for each main
diagnosis, with the diagnosis on the x axis and the ejection fraction in percent on the y axis.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The number of patients with HFrEF, as an integer. Save it in a variable named `n_hfref` and
print it with a short label. Return only the code, in one block, with a short comment above each
step.
Test: The counts of the five diagnoses must add up to 500.
```

**Expected result:** `n_hfref` = 47

## Stop 2: The ECG as data

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html#stop-2) · The same result on the Python path: Sections 3 to 5*

A digital ECG is a table of numbers: one column per lead and one row per sample. In this stop the 12-lead ECG of the case of the week, VC-0317, is drawn and measured, and the QT interval of another patient is corrected for the heart rate with two formulas.

### Step 2.1: A strip of lead II

**Goal.** Draw the first 2.5 seconds of lead II and see how many numbers such a strip holds.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt. The course package vclinic is imported, together with its module measure. RANDOM_STATE = 2026.
Data: `case` is the resting 12-lead ECG of patient VC-0317 of the virtual clinic, an object of the
course package: `case.fs` is the sampling frequency (500 Hz), `case.leads` is a pandas DataFrame
with one column per lead (I, II, III, aVR, aVL, aVF, V1 to V6) and one row per sample, in
millivolts, and `case.lead("II")` returns lead II as a NumPy array. The recording lasts 10 seconds.
Task: Take lead II with case.lead("II") and keep its first 2.5 seconds, that is case.fs × 2.5
samples. Plot them with the time in seconds on the x axis and the amplitude in millivolts on the y
axis.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The number of samples in the 2.5 seconds, as an integer. Save it in a variable named
`n_samples` and print it with a short label. Return only the code, in one block, with a short
comment above each step.
Test: The time axis must end at 2.5 seconds.
```

**Expected result:** `n_samples` = 1250

### Step 2.2: The heart rate from the R peaks

**Goal.** Find the R peaks of lead II and compute the heart rate from the intervals between them.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt. The course package vclinic is imported, together with its module measure. RANDOM_STATE = 2026.
Data: `case` is the resting 12-lead ECG of patient VC-0317 of the virtual clinic, an object of the
course package: `case.fs` is the sampling frequency (500 Hz), `case.leads` is a pandas DataFrame
with one column per lead (I, II, III, aVR, aVL, aVF, V1 to V6) and one row per sample, in
millivolts, and `case.lead("II")` returns lead II as a NumPy array. The recording lasts 10 seconds.
`measure.detect_r_peaks(signal, fs)` of the course package takes one lead as a NumPy array and its
sampling frequency in Hz, and returns the sample numbers of the R peaks as a NumPy array.
Task: Find the R peaks of the whole lead II with measure.detect_r_peaks. Turn the differences
between successive peaks into seconds by dividing by case.fs, and compute the heart rate as 60
divided by the mean RR interval in seconds.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The heart rate in beats per minute, rounded to one decimal. Print the number of R peaks as
well. Save it in a variable named `hr_bpm` and print it with a short label. Return only the code, in
one block, with a short comment above each step.
Test: The 10-second recording must hold about 14 R peaks.
```

**Expected result:** `hr_bpm` = 84.9

### Step 2.3: The QTc by two formulas

**Goal.** Correct the QT interval of patient VC-0254 for her fast heart rate with the formulas of Fridericia and Bazett, and compare the two.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt. The course package vclinic is imported, together with its module measure. RANDOM_STATE = 2026.
Data: Patient VC-0254 of the virtual clinic has a QT interval of 343 ms at a heart rate of 98 beats
per minute in the registry.
Task: Compute the RR interval in seconds as 60 divided by the heart rate. Then compute the QTc with
Fridericia's formula, QT divided by the cube root of RR, and with Bazett's formula, QT divided by
the square root of RR.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The QTc by Fridericia's formula in milliseconds, rounded to one decimal. Print the QTc by
Bazett's formula as well. Save it in a variable named `qtc_fridericia` and print it with a short
label. Return only the code, in one block, with a short comment above each step.
Test: At a heart rate of 60 beats per minute both formulas must return the QT itself.
```

**Expected result:** `qtc_fridericia` = 403.9

## Stop 3: Real recordings and a function to check

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html#stop-3) · The same result on the Python path: Sections 6 to 9*

Real recordings bring noise, annotations and units of their own. In this stop record 100 of the MIT-BIH Arrhythmia Database is read with the beat labels of its cardiologists, and heart rate variability is computed from its normal beats. Then a real 12-lead ECG of the PTB database is drawn, and a QTc function written by an AI assistant is checked and corrected.

### Step 3.1: The beats of record 100

**Goal.** Count the beats of a 30-minute recording by the labels that cardiologists gave them.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt. The course package vclinic is imported, together with its module measure. RANDOM_STATE = 2026.
Data: `ann_symbols` is the list of the labels of record 100 of the MIT-BIH Arrhythmia Database, one
per annotation in the order of time: N normal beat, A atrial premature beat, V premature ventricular
contraction and + a change of rhythm, which is not a beat. `ann_samples` holds the sample number of
each label, and `fs_mit` is the sampling frequency, 360 Hz.
Task: Count how often each label occurs in ann_symbols and print the counts.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The number of atrial premature beats (label A), as an integer. Save it in a variable named
`n_apb` and print it with a short label. Return only the code, in one block, with a short comment
above each step.
Test: The labels N, A and V together must count 2273 beats.
```

**Expected result:** `n_apb` = 33

### Step 3.2: Heart rate variability: SDNN

**Goal.** Measure how much the intervals between normal beats vary over 30 minutes.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt. The course package vclinic is imported, together with its module measure. RANDOM_STATE = 2026.
Data: `ann_symbols` is the list of the labels of record 100 of the MIT-BIH Arrhythmia Database, one
per annotation in the order of time: N normal beat, A atrial premature beat, V premature ventricular
contraction and + a change of rhythm, which is not a beat. `ann_samples` holds the sample number of
each label, and `fs_mit` is the sampling frequency, 360 Hz.
Task: Keep the labels that are beats (all labels except +). Compute the RR intervals between
successive beats in milliseconds from ann_samples and fs_mit. Keep only the intervals whose two
beats are both labelled N, the normal-to-normal (NN) intervals. Compute the SDNN, the standard
deviation of the NN intervals with ddof=1, and print the mean NN interval as well.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The SDNN in milliseconds, rounded to one decimal. Save it in a variable named `sdnn` and
print it with a short label. Return only the code, in one block, with a short comment above each
step.
Test: The mean NN interval must lie between 700 and 900 ms.
```

**Expected result:** `sdnn` = 36.0

### Step 3.3: A real 12-lead ECG

**Goal.** Draw a real 12-lead ECG of a patient with an acute myocardial infarction as on ECG paper and measure its heart rate.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt. The course package vclinic is imported, together with its module measure. RANDOM_STATE = 2026.
Data: `ptb` is a pandas DataFrame with record s0010_re of patient 1 of the PTB Diagnostic ECG
Database: 38.4 seconds sampled at 1000 Hz (`fs_ptb`), one column per lead (i, ii, iii, avr, avl,
avf, v1 to v6 and the three Frank leads vx, vy and vz), in millivolts. `header` is the list of the
text lines of its header file. `measure.detect_r_peaks(signal, fs)` of the course package takes one
lead as a NumPy array and its sampling frequency in Hz, and returns the sample numbers of the R
peaks as a NumPy array.
Task: Print the lines of header that start with "Reason for admission" or "Acute infarction". Plot
the first 3 seconds of the twelve standard leads in a grid of three rows and four columns, with the
name of the lead in each panel. Then find the R peaks of lead ii with measure.detect_r_peaks and
compute the heart rate as 60 divided by the mean RR interval in seconds.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The heart rate in beats per minute, rounded to one decimal. Save it in a variable named
`hr_ptb` and print it with a short label. Return only the code, in one block, with a short comment
above each step.
Test: The printed lines must name an infero-lateral infarction.
```

**Expected result:** `hr_ptb` = 81.8

### Step 3.4: Correcting the function of an assistant

**Goal.** An AI assistant wrote a QTc function from a short prompt and returned an impossible QTc of 17 ms. Find the two errors and correct them.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt. The course package vclinic is imported, together with its module measure. RANDOM_STATE = 2026.
Data: The function of the assistant is def qtc(qt_samples, rr_samples, fs=360): qt_ms = qt_samples /
fs * 1000; rr_ms = rr_samples / fs * 1000; return qt_ms / rr_ms ** 0.5. A QT of 196 samples and an
RR interval of 353 samples were measured at 500 Hz.
Task: Write a corrected function qtc_bazett(qt_samples, rr_samples, fs) that takes fs without a
default value, converts the QT to milliseconds and the RR interval to seconds, and returns the QT in
milliseconds divided by the square root of the RR interval in seconds. Compute the QTc of the
measurement above with it.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The QTc in milliseconds, rounded to one decimal. Save it in a variable named `qtc_fixed` and
print it with a short label. Return only the code, in one block, with a short comment above each
step.
Test: With qt_samples = 200, rr_samples = 500 and fs = 500 the result must be 400 ms, because the RR
interval is then 1 s.
```

**Expected result:** `qtc_fixed` = 466.5

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

### Ask for tests

```text
Write three short tests for the function below, with inputs whose correct result is known by hand,
for example a heart rate of 60 bpm, where the RR interval is exactly 1 s. Use plain assert
statements and explain what each test protects against.

[paste the function here]
```

## Prompt path of the weekly project

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
