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

The registry of a clinic is a table: one row per patient, one column per variable. In this stop, the 303 patients of the Cleveland data and the first 500 patients of the virtual clinic are summarised by a mean, a share and a count, each with a clinical question behind it.

### Step 1.1: The mean age of the patients with disease

**Goal.** Find out how old, on average, the Cleveland patients with coronary artery disease were.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 1, where the data below and the course
package vclinic, with its module measure, are already loaded. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) are available.
Data: `heart` is a table with the 303 patients of the Cleveland Clinic in the UCI Heart Disease data
set, one row per patient. The columns used here are age (years), sex (1 for men, 0 for women) and
disease, which is 1 when at least one major coronary artery was narrowed by more than 50 percent of
its diameter at angiography, and 0 otherwise.
Task: Select the patients with coronary artery disease, that is, those whose value in the column
disease is 1, and compute their mean age. Also print how many patients were selected.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the mean age in years, rounded to one decimal. Keep the result under the name
`mean_age` and print it with a short label. Return only the code, as one block, with a short comment
above each step.
Test: For comparison, also print the mean age of all 303 patients, which is 54.4 years; the mean of
the patients with disease must differ from it.
```

**Expected result:** `mean_age` = 56.6

### Step 1.2: The share of women

**Goal.** Find out which percentage of the Cleveland patients were women.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 1, where the data below and the course
package vclinic, with its module measure, are already loaded. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) are available.
Data: `heart` is a table with the 303 patients of the Cleveland Clinic in the UCI Heart Disease data
set, one row per patient. The columns used here are age (years), sex (1 for men, 0 for women) and
disease, which is 1 when at least one major coronary artery was narrowed by more than 50 percent of
its diameter at angiography, and 0 otherwise.
Task: Count the women, the patients whose value in the column sex is 0, and divide their number by
the number of all patients. Also print the share of men.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the share of women in percent, rounded to one decimal. Keep the result under the name
`pct_women` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: The shares of women and men must add up to 100 percent.
```

**Expected result:** `pct_women` = 32.0

### Step 1.3: Patients with HFrEF in the virtual clinic

**Goal.** Count the patients of the virtual clinic who have heart failure with reduced ejection fraction, and see the ejection fraction of every diagnosis in one figure.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 1, where the data below and the course
package vclinic, with its module measure, are already loaded. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) are available.
Data: `clinic` is a table with the first 500 synthetic patients of the virtual clinic, one row per
patient. The columns used here are patient_id; main_diagnosis, which is "none", "CCS" (chronic
coronary syndrome), "ACS" (acute coronary syndrome), "HFrEF" (heart failure with reduced ejection
fraction) or "HFpEF" (heart failure with preserved ejection fraction); and lvef, the left
ventricular ejection fraction in percent.
Task: Count the patients whose main diagnosis is "HFrEF". Then draw a box plot of the ejection
fraction (lvef) for each main diagnosis, with the diagnoses on the horizontal axis and the ejection
fraction in percent on the vertical axis.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the number of patients with HFrEF as a whole number. Keep the result under the name
`n_hfref` and print it with a short label. Return only the code, as one block, with a short comment
above each step.
Test: Also print the number of patients of every diagnosis; the five numbers must add up to 500.
```

**Expected result:** `n_hfref` = 47

## Stop 2: The ECG as data

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html#stop-2) · The same result on the Python path: Sections 3 to 5*

A digital ECG is a table of numbers: one column per lead, one row per sample. In this stop, the 12-lead ECG of the case of the week, VC-0317, is drawn and measured, and the QT interval of another patient is corrected for the heart rate by two formulas.

### Step 2.1: A strip of lead II

**Goal.** Draw the first 2.5 seconds of lead II and see how many numbers such a strip holds.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 1, where the data below and the course
package vclinic, with its module measure, are already loaded. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) are available.
Data: `case` holds the resting 12-lead ECG of patient VC-0317 of the virtual clinic, 10 seconds
long. `case.fs` is its sampling frequency, 500 samples per second. `case.leads` is a table with one
column per lead (I, II, III, aVR, aVL, aVF, V1 to V6) and one row per sample, in millivolts.
Task: Take lead II of the case and keep its first 2.5 seconds; the number of samples in them is the
sampling frequency times 2.5. Plot them with the time in seconds on the horizontal axis and the
voltage in millivolts on the vertical axis.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the number of samples in the 2.5 seconds as a whole number. Keep the result under the
name `n_samples` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: The time axis of the plot must end at 2.5 seconds.
```

**Expected result:** `n_samples` = 1250

### Step 2.2: The heart rate from the R peaks

**Goal.** Find the R peaks of lead II and compute the heart rate from the intervals between them.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 1, where the data below and the course
package vclinic, with its module measure, are already loaded. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) are available.
Data: `case` holds the resting 12-lead ECG of patient VC-0317 of the virtual clinic, 10 seconds
long. `case.fs` is its sampling frequency, 500 samples per second. `case.leads` is a table with one
column per lead (I, II, III, aVR, aVL, aVF, V1 to V6) and one row per sample, in millivolts. The
course package has a ready R-peak detector, `measure.detect_r_peaks`. It receives one lead and its
sampling frequency and returns the positions of the R peaks as sample numbers.
Task: Find the R peaks of the whole lead II with the R-peak detector of the course package. Turn the
distances between successive peaks into seconds by dividing them by the sampling frequency. The
heart rate is 60 divided by the mean RR interval in seconds.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the heart rate in beats per minute, rounded to one decimal, and also print the number
of R peaks. Keep the result under the name `hr_bpm` and print it with a short label. Return only the
code, as one block, with a short comment above each step.
Test: The 10-second recording must hold about 14 R peaks.
```

**Expected result:** `hr_bpm` = 84.9

### Step 2.3: The QTc by two formulas

**Goal.** Correct the QT interval of patient VC-0254 for her fast heart rate with the formulas of Fridericia and Bazett, and compare the two.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 1, where the data below and the course
package vclinic, with its module measure, are already loaded. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) are available.
Data: In the registry of the virtual clinic, patient VC-0254 has a QT interval of 343 ms at a heart
rate of 98 beats per minute.
Task: Compute the RR interval in seconds as 60 divided by the heart rate. Then compute the corrected
QT interval (QTc) with two formulas: Fridericia's formula divides the QT by the cube root of RR, and
Bazett's formula divides it by the square root of RR.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the QTc by Fridericia's formula in milliseconds, rounded to one decimal, and also print
the QTc by Bazett's formula. Keep the result under the name `qtc_fridericia` and print it with a
short label. Return only the code, as one block, with a short comment above each step.
Test: At a heart rate of 60 beats per minute, both formulas must return the QT itself.
```

**Expected result:** `qtc_fridericia` = 403.9

## Stop 3: Real recordings and a function to check

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html#stop-3) · The same result on the Python path: Sections 6 to 9*

Real recordings bring their own noise, annotations and units. In this stop, record 100 of the MIT-BIH Arrhythmia Database is read with the beat labels of its cardiologists, and the heart rate variability is computed from its normal beats. Then a real 12-lead ECG of the PTB database is drawn, and a QTc function written by an AI assistant is checked and corrected.

### Step 3.1: The beats of record 100

**Goal.** Count the beats of a 30-minute recording by the labels that cardiologists gave them.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 1, where the data below and the course
package vclinic, with its module measure, are already loaded. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) are available.
Data: `ann_symbols` is the list of the labels that cardiologists gave to record 100 of the MIT-BIH
Arrhythmia Database, one label per annotation in the order of time: N for a normal beat, A for an
atrial premature beat, V for a premature ventricular contraction and + for a change of rhythm, which
is not a beat. `ann_samples` holds the position of each label as a sample number, and `fs_mit` is
the sampling frequency, 360 samples per second.
Task: Count how often each label occurs in ann_symbols and print the counts.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the number of atrial premature beats, the label A, as a whole number. Keep the result
under the name `n_apb` and print it with a short label. Return only the code, as one block, with a
short comment above each step.
Test: The labels N, A and V together must count 2273 beats.
```

**Expected result:** `n_apb` = 33

### Step 3.2: Heart rate variability: SDNN

**Goal.** Measure how much the intervals between normal beats vary over 30 minutes.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 1, where the data below and the course
package vclinic, with its module measure, are already loaded. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) are available.
Data: `ann_symbols` is the list of the labels that cardiologists gave to record 100 of the MIT-BIH
Arrhythmia Database, one label per annotation in the order of time: N for a normal beat, A for an
atrial premature beat, V for a premature ventricular contraction and + for a change of rhythm, which
is not a beat. `ann_samples` holds the position of each label as a sample number, and `fs_mit` is
the sampling frequency, 360 samples per second.
Task: Keep only the labels that are beats, that is, all labels except +. From the positions of the
beats and the sampling frequency, compute the RR intervals between successive beats in milliseconds.
Keep only the intervals between two normal beats, both labelled N: these are the NN intervals. The
SDNN is their standard deviation, computed as for a sample, with the number of intervals minus one
in the denominator. Also print the mean NN interval.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the SDNN in milliseconds, rounded to one decimal. Keep the result under the name `sdnn`
and print it with a short label. Return only the code, as one block, with a short comment above each
step.
Test: The mean NN interval must lie between 700 and 900 ms.
```

**Expected result:** `sdnn` = 36.0

### Step 3.3: A real 12-lead ECG

**Goal.** Draw a real 12-lead ECG of a patient with an acute myocardial infarction as on ECG paper, and measure its heart rate.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 1, where the data below and the course
package vclinic, with its module measure, are already loaded. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) are available.
Data: `ptb` is a table with record s0010_re of patient 1 of the PTB Diagnostic ECG Database: 38.4
seconds recorded with 1000 samples per second (`fs_ptb`), one column per lead (i, ii, iii, avr, avl,
avf, v1 to v6 and the three Frank leads vx, vy and vz), in millivolts. `header` is the list of the
text lines of the header file of the record. The course package has a ready R-peak detector,
`measure.detect_r_peaks`. It receives one lead and its sampling frequency and returns the positions
of the R peaks as sample numbers.
Task: First print the lines of header that begin with "Reason for admission" or "Acute infarction".
Then draw the first 3 seconds of the twelve standard leads in a grid of three rows and four columns,
with the name of the lead above each panel. Finally, find the R peaks of lead ii with the R-peak
detector of the course package and compute the heart rate as 60 divided by the mean RR interval in
seconds.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the heart rate in beats per minute, rounded to one decimal. Keep the result under the
name `hr_ptb` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: The printed lines must name an infero-lateral infarction.
```

**Expected result:** `hr_ptb` = 81.8

### Step 3.4: Correcting the function of an assistant

**Goal.** An AI assistant wrote a function for the QTc from a short prompt and returned an impossible QTc of 17 ms. Find the two errors and correct them.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 1, where the data below and the course
package vclinic, with its module measure, are already loaded. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) are available.
Data: The function of the assistant: def qtc(qt_samples, rr_samples, fs=360): qt_ms = qt_samples /
fs * 1000; rr_ms = rr_samples / fs * 1000; return qt_ms / rr_ms ** 0.5. On an ECG recorded with 500
samples per second, a QT of 196 samples and an RR interval of 353 samples were measured.
Task: Write a corrected function named qtc_bazett. It receives the QT and the RR interval as numbers
of samples, and the sampling frequency, which must always be given and never assumed. It turns the
QT into milliseconds and the RR interval into seconds, and returns Bazett's QTc: the QT in
milliseconds divided by the square root of the RR interval in seconds. Then compute the QTc of the
measurement above with it.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the QTc in milliseconds, rounded to one decimal. Keep the result under the name
`qtc_fixed` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: With a QT of 200 samples and an RR interval of 500 samples at 500 samples per second, the
function must return 400 ms, because the RR interval is then exactly 1 second.
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
for example a heart rate of 60 beats per minute, where the RR interval is exactly 1 second. Each
test should stop the code with a clear message when the result is wrong. Explain in one sentence
what each test protects against.

[paste the function here]
```

## Prompt path of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. Each step builds on the one before it, so the test of a step must hold before the next prompt is sent. The report lists all four prompts in the AI usage log.

### Step 1: Extend measure_ecg with the frontal axis

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 1. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) and the course package vclinic are available.
Data: The measuring tool measure_ecg of Section 5 with its helper tools for the R peaks and the
boundaries of the QRS complex. The course package has a tool, vclinic.frontal_axis, that gives the
frontal QRS axis in degrees from the net QRS voltages of leads I and aVF.
Task: Write a new measuring tool named measure_ecg_axis that returns everything measure_ecg returns
and, in addition, the frontal axis in degrees under the name axis_deg. For each beat, take the net
QRS voltage of leads I and aVF: the largest positive plus the largest negative value between the
onset and the end of the QRS complex, measured from the median voltage of the 30 ms before the
onset. Give the medians over all beats to vclinic.frontal_axis.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: The new tool and its result for patient VC-0317. Return only the code, as one block, with a
short comment above each step.
Test: The registry gives an axis of 21 degrees for VC-0317. The measured axis should lie within
about 10 degrees of it, because the net voltages also contain the small septal and terminal forces.
```

### Step 2: Ten patients against the truth

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 1. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) and the course package vclinic are available.
Data: The table clinic with the columns patient_id, ecg_rhythm ("sinus" or "AF") and ecg_conduction
("normal", "LBBB" or "RBBB"). The ECG of a patient comes from the tool patient_ecg of the course
package vclinic, which receives the table clinic and the number of the patient. The part truth of
the ECG holds the true heart rate, PR interval, QRS duration, QT interval and axis.
Task: Choose ten patients, at least two of them with atrial fibrillation or a bundle branch block.
Measure each with measure_ecg_axis, telling the tool that the rhythm is not sinus for the patients
with atrial fibrillation. Build a table with the measured value, the true value and their difference
for the heart rate, the PR interval, the QRS duration, the QT interval and the axis.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: A table with one row per patient. Return only the code, as one block, with a short comment
above each step.
Test: The table has ten rows, and for VC-0317 the differences in PR, QRS and QT are only a few
milliseconds.
```

### Step 3: The two real records

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 1. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) and the course package vclinic are available.
Data: leads_ptb, the twelve leads of the PTB record, and fs_ptb, 1000 samples per second, from
Section 8. found, the detected R peaks of MIT-BIH record 100 as sample positions, and fs_mit, 360
samples per second, from Section 6.
Task: Measure the PTB record with measure_ecg_axis, and compute the mean heart rate of MIT-BIH
record 100 from its detected beats.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: The measurements of the PTB record and the mean heart rate of record 100. Return only the
code, as one block, with a short comment above each step.
Test: For the PTB record, Section 8 reports a heart rate of 81.8 beats per minute, a PR interval of
225 ms, a QRS duration of 137 ms and a QT of 436.7 ms.
```

### Step 4: Bazett or Fridericia for each patient

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 1. The usual packages for tables,
calculations and plots (pandas, NumPy and Matplotlib) and the course package vclinic are available.
Data: The table of step 2 with the measured QT and heart rate of each patient, and the sex of each
patient from clinic.
Task: For each patient, compute the QTc by Bazett's and by Fridericia's formula, and decide whether
it is prolonged, with the limits of 460 ms for women and 450 ms for men. List the patients for whom
the two formulas disagree.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: The table with two new columns and the list of the disagreements. Return only the code, as
one block, with a short comment above each step.
Test: VC-0317, a woman at 85 beats per minute, is prolonged by Bazett's formula and not by
Fridericia's.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
