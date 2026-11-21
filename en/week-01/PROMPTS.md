# Prompt library, Week 1

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 1](README.md) · [Türkçe](../../tr/hafta-01/PROMPTLAR.md)

This library holds every prompt of the practice stops of Week 1, from the parts *Prompt and application* of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the Jupyter notebook, into the empty cell under the prompt of the same number, and runs there.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [Working with a prompt](#working-with-a-prompt)
2. [Stop 1: Mini project: The Kaggle Heart Disease data set](#stop-1-mini-project-the-kaggle-heart-disease-data-set)
3. [Stop 2: The ECG as data](#stop-2-the-ecg-as-data)
4. [Stop 3: Real recordings and a careless prompt](#stop-3-real-recordings-and-a-careless-prompt)
5. [Prompts for repairing, explaining and reviewing code](#prompts-for-repairing-explaining-and-reviewing-code)
6. [Prompts of the weekly project](#prompts-of-the-weekly-project)

## Working with a prompt

| Step | What to do |
|---|---|
| 1. Read | Read the goal of the prompt in the Jupyter notebook. |
| 2. Prepare the data | Run the data cell under the prompt. It prepares the table "data" that the prompt describes and shows it, so the prompt also works when the Jupyter notebook is opened at this place. |
| 3. Copy and send | Copy the prompt and send it to an AI assistant: Gemini in Google Colab, or ChatGPT, Claude, Copilot or Gemini in another browser tab. |
| 4. Run | Paste the code of the assistant into the cell below the data cell and run it. |
| 5. Check | Run the check cell. It prints *correct* or *not yet* and the value of the result "answer". |
| 6. Repair | If the check prints *not yet*, send the repair prompt with the code. If the result is still wrong, run the *Ready code* cell, which gives the correct result. |
| 7. Explain and log | Ask the assistant to explain the code in plain language, and write the tool, the prompt and what was checked in the AI usage log. |

## Stop 1: Mini project: The Kaggle Heart Disease data set

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html#stop-1) · Jupyter notebook: «Stop 1 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-01/NB01_python_and_ecg_basics.ipynb#scrollTo=stop-1-prompt)*

This stop is the mini project of the session: loading the Kaggle Heart Disease data set, the Cleveland data of the UCI Heart Disease collection, with a statistical summary and a visualisation. The registry of a clinic is a table: one row per patient, one column per variable. In this stop, the 303 patients of the data set and the first 500 patients of the virtual clinic are summarised by a mean, a share and a count, each with a clinical question behind it.

### Prompt 1.1: The mean age of the patients with disease

**Goal.** Find out how old, on average, the Cleveland patients with coronary artery disease were.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know the mean age of the patients with coronary artery disease
among 303 patients who underwent coronary angiography at the Cleveland Clinic.
Data: The notebook holds a table named "data". Each row is a patient: The column "age" gives the age
in years. The column "CAD" says "yes" when at least one major coronary artery was narrowed by more
than 50 percent of its diameter at angiography, and "no" otherwise.
Task: Select the patients with coronary artery disease and compute their mean age. Also print how
many patients were selected.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the mean age in years with one decimal and keep it under the name "answer".
Test: For comparison, also print the mean age of all patients, which must be 54.4 years. The mean of
the patients with disease must differ from it.
```

**Expected result:** "answer" = 56.6

### Prompt 1.2: The share of women

**Goal.** Find out which percentage of the Cleveland patients were women.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know which percentage of the 303 patients who underwent coronary
angiography at the Cleveland Clinic were women.
Data: The notebook holds a table named "data". Each row is a patient: The column "age" gives the age
in years, and the column "sex" says "female" or "male".
Task: Divide the number of women by the number of all patients and express the share in percent.
Compute the percentage of men in the same way.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the percentage of women with one decimal and keep it under the name "answer". Also
print the percentage of men.
Test: The two percentages must add up to 100.
```

**Expected result:** "answer" = 32.0

### Prompt 1.3: Patients with HFrEF in the virtual clinic

**Goal.** Count the patients of the virtual clinic who have heart failure with reduced ejection fraction, and see the ejection fraction of every diagnosis in one figure.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to count the patients with heart failure with reduced ejection
fraction (HFrEF) among the 500 synthetic patients of the virtual clinic, and to see how the ejection
fraction differs between the diagnoses.
Data: The notebook holds a table named "data". Each row is a patient: The column "patient" gives the
number of the patient, the column "main diagnosis" the main diagnosis and the column "LVEF" the left
ventricular ejection fraction in percent. The main diagnosis is one of "none", "CCS" (chronic
coronary syndrome), "ACS" (acute coronary syndrome), "HFrEF" (heart failure with reduced ejection
fraction) and "HFpEF" (heart failure with preserved ejection fraction).
Task: Count the patients whose main diagnosis is HFrEF. Then draw a box plot of the ejection
fraction for each main diagnosis, with the diagnoses on the horizontal axis and the ejection
fraction in percent on the vertical axis.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of patients with HFrEF and keep it under the name "answer". Show the plot
as well.
Test: Also print the number of patients of every diagnosis; the five numbers must add up to 500. No
patient with HFrEF may have an ejection fraction above 40 percent.
```

**Expected result:** "answer" = 47

## Stop 2: The ECG as data

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html#stop-2) · Jupyter notebook: «Stop 2 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-01/NB01_python_and_ecg_basics.ipynb#scrollTo=stop-2-prompt)*

A digital ECG is a table of numbers: one column per lead, one row per sample. In this stop, lead II of the ECG of the case of the week, VC-0317, is drawn and measured, and the QT interval of another patient is corrected for the heart rate by two formulas.

### Prompt 2.1: A strip of lead II

**Goal.** Draw the first 2.5 seconds of lead II and see how many numbers such a strip holds.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to see the first 2.5 seconds of lead II from the 10-second resting
ECG of a 67-year-old woman, and to know how many samples this strip holds.
Data: The notebook holds a table named "data". Each row is one moment of the recording: The column
"time" gives the time in seconds, and the column "II" the voltage of lead II in millivolts. The
recording was sampled 500 times per second.
Task: Keep the rows whose time is less than 2.5 seconds and count them. Draw this part with the time
in seconds on the horizontal axis and the voltage in millivolts on the vertical axis.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of samples in these 2.5 seconds and keep it under the name "answer". Show
the plot as well.
Test: The time axis of the plot must start at 0 and end at 2.5 seconds.
```

**Expected result:** "answer" = 1250

### Prompt 2.2: The heart rate from the R peaks

**Goal.** Find the R peaks of lead II and compute the heart rate from the intervals between them.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to measure the heart rate of a 67-year-old woman from her 10-second
resting ECG.
Data: The notebook holds a table named "data". Each row is one moment of the recording: The column
"time" gives the time in seconds, and the column "II" the voltage of lead II in millivolts. The
recording was sampled 500 times per second.
Task: Find the R peaks. Accept as R peaks the peaks that exceed half of the highest value and lie at
least 0.3 seconds apart. Compute the heart rate in beats per minute from the mean time between
successive R peaks.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the heart rate with one decimal and keep it under the name "answer". Draw lead II with
the R peaks marked.
Test: About 14 R peaks must be found in the 10 seconds, and the heart rate must lie between 40 and
150 beats per minute.
```

**Expected result:** "answer" = 84.9

### Prompt 2.3: The QTc by two formulas

**Goal.** Correct the QT interval of patient VC-0254 for his fast heart rate with the formulas of Fridericia and Bazett, and compare the two.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to correct the QT interval of a 58-year-old man with a fast heart
rate by two formulas and to compare the results.
Data: The notebook holds a table named "data" with one row: The column "patient" gives the number of
the patient, the column "heart rate" the heart rate in beats per minute and the column "QT" the QT
interval in milliseconds.
Task: Compute the RR interval in seconds as 60 divided by the heart rate. Then correct the QT
interval with two formulas: Fridericia's formula divides the QT by the cube root of RR, and Bazett's
formula divides it by the square root of RR.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the QTc of Fridericia in milliseconds with one decimal and keep it under the name
"answer". Also print the QTc of Bazett.
Test: At a heart rate of 60 beats per minute, both formulas must give the QT itself.
```

**Expected result:** "answer" = 403.9

## Stop 3: Real recordings and a careless prompt

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html#stop-3) · Jupyter notebook: «Stop 3 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-01/NB01_python_and_ecg_basics.ipynb#scrollTo=stop-3-prompt)*

Real recordings bring their own noise, annotations and units. In this stop, record 100 of the MIT-BIH Arrhythmia Database is read with the beat labels of its cardiologists, and the heart rate variability is computed from its normal beats. Then a real 12-lead ECG of the PTB database is drawn. Finally, a QTc calculation that an AI assistant wrote from a short and careless prompt is requested again with the prompt card, and its result is checked.

### Prompt 3.1: The beats of record 100

**Goal.** Count the beats of a 30-minute recording by the labels that cardiologists gave them.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Record 100 of the MIT-BIH Arrhythmia Database is a 30-minute ambulatory ECG of a
69-year-old man. The cardiologist wants to count the beats of this recording by the labels that
cardiologists gave them.
Data: The notebook holds a table named "data". Each row is a mark that the cardiologists placed on
the recording: The column "time" gives its place in seconds, and the column "label" its kind. "N"
marks a normal beat, "A" an atrial premature beat and "V" a premature ventricular contraction; "+"
marks a change of rhythm and is not a beat.
Task: Count how often each label occurs and print the counts.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of atrial premature beats and keep it under the name "answer".
Test: The labels N, A and V together must count 2273 beats.
```

**Expected result:** "answer" = 33

### Prompt 3.2: Heart rate variability: SDNN

**Goal.** Measure how much the intervals between normal beats vary over 30 minutes.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to measure the heart rate variability of record 100 of the MIT-BIH
Arrhythmia Database, a 30-minute ambulatory ECG of a 69-year-old man, by the SDNN.
Data: The notebook holds a table named "data". Each row is a mark that the cardiologists placed on
the recording: The column "time" gives its place in seconds, and the column "label" its kind. "N"
marks a normal beat, "A" an atrial premature beat and "V" a premature ventricular contraction; "+"
marks a change of rhythm and is not a beat.
Task: Keep only the beats, that is, all labels except "+". Compute the RR intervals between
successive beats in milliseconds. Keep only the intervals between two normal beats, both labelled
"N": These are the NN intervals. The SDNN is their standard deviation; compute it as for a sample,
with the number of intervals minus one in the denominator. Also print the mean NN interval.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the SDNN in milliseconds with one decimal and keep it under the name "answer".
Test: The mean NN interval must lie between 700 and 900 ms.
```

**Expected result:** "answer" = 36.0

### Prompt 3.3: A real 12-lead ECG

**Goal.** Draw a real 12-lead ECG of a patient with an acute myocardial infarction as on ECG paper, and measure its heart rate.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to see the real 12-lead ECG of an 81-year-old woman admitted with an
acute infero-lateral myocardial infarction in the layout of ECG paper, and to measure her heart
rate.
Data: The notebook holds a table named "data". Each row is one moment of the recording: The column
"time" gives the time in seconds, and the columns "I", "II", "III", "aVR", "aVL", "aVF" and "V1" to
"V6" give the voltage of the twelve standard leads in millivolts. The recording lasts 38.4 seconds
and was sampled 1000 times per second.
Task: Draw the first 3 seconds of the twelve leads in three rows and four columns, as on ECG paper:
I, II and III in the first column, aVR, aVL and aVF in the second, V1 to V3 in the third and V4 to
V6 in the fourth, with the name of the lead above each panel. Then find the R peaks of lead I.
Accept as R peaks the peaks that exceed half of the highest value and lie at least 0.3 seconds
apart. Compute the heart rate in beats per minute from the mean time between successive R peaks.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the heart rate with one decimal and keep it under the name "answer". Show the figure
as well.
Test: The heart rate must lie between 40 and 150 beats per minute, and the number of R peaks must
fit it: At 80 beats per minute, 38.4 seconds hold about 51 beats.
```

**Expected result:** "answer" = 81.8

### Prompt 3.4: From a careless prompt to the prompt card

**Goal.** From the short prompt "write a python function that gives the qtc from qt and rr in samples", an AI assistant wrote code that returned an impossible QTc of 17 ms. The data cell of this prompt shows this result. With this prompt, the same calculation is requested again with the seven fields of the prompt card, and the result is checked.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: On an ECG sampled 500 times per second, the QT interval and the RR interval were measured
as numbers of samples. The cardiologist wants the QT interval corrected by Bazett's method, in
milliseconds.
Data: The notebook holds a table named "data" with one row: The column "QT" gives the QT interval
and the column "RR" the RR interval, both as numbers of samples. The recording was sampled 500 times
per second.
Task: Turn the QT interval into milliseconds and the RR interval into seconds. Correct the QT by
Bazett's method: Divide the QT in milliseconds by the square root of the RR interval in seconds.
Constraints: Use only this table. Do not assume the number of samples per second; use the 500 given
here. The code must not read files, download anything from the internet or install programs.
Output: Print the corrected QT in milliseconds with one decimal and keep it under the name "answer".
Test: The same calculation must give exactly 400 ms for a QT of 200 samples and an RR interval of
500 samples, because the RR interval is then exactly 1 second.
```

**Expected result:** "answer" = 466.5

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

### Ask for tests

```text
Write three short tests for the code below, with inputs whose correct result is known by hand, for
example a heart rate of 60 beats per minute, where the RR interval is exactly 1 second. Each test
should stop the code with a clear message when the result is wrong. Explain in one sentence what
each test protects against.

[paste the code here]
```

## Prompts of the weekly project

The [weekly project](README.md#weekly-project) can be built with four prompts, one for each step. The section *Weekly project* at the end of the Jupyter notebook prepares the table of each prompt and opens on its own. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Project step 1: The frontal axis of the case

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to measure the frontal QRS axis of a 67-year-old woman from her
resting ECG, beat by beat.
Data: The notebook holds a table named "data". Each row is a beat: The column "beat" gives its
number, and the columns "I" and "aVF" give the net QRS voltage of these leads in millivolts. The net
voltage is the largest positive plus the largest negative deflection of the QRS complex.
Task: For every beat, build the vector whose horizontal component is the voltage of lead I and whose
vertical component is the voltage of lead aVF divided by 0.866. The frontal axis is the angle of
this vector in degrees, measured from the direction of lead I, with positive angles towards the
feet. Then take the median axis of all beats and print whether it lies in the normal range of −30 to
+90 degrees.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the median axis in degrees with one decimal and keep it under the name "answer".
Test: A beat with 0.9 mV in lead I and −0.3 mV in lead aVF must give an axis of about −21 degrees.
The registry gives an axis of 21 degrees for this patient, and the result should lie within about 10
degrees of it, because the net voltages also hold the small septal and terminal forces.
```

### Project step 2: Ten patients against the truth

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how well an automatic ECG measurement agrees with the true
values in ten patients of the virtual clinic, among them patients with atrial fibrillation or left
bundle branch block.
Data: The notebook holds a table named "data". Each row is one measurement of one patient: The
column "patient" gives the number of the patient, "rhythm" says "sinus" or "AF", and "conduction"
says "normal" or "LBBB" (left bundle branch block). The column "measure" names the measurement
("heart rate", "PR", "QRS", "QT" or "axis"), "measured" gives the value of the automatic measurement
and "true" the true value. Heart rates are in beats per minute, intervals in milliseconds and axes
in degrees. There is no PR interval in atrial fibrillation, so these cells are empty.
Task: Compute the difference, measured minus true, for every row. For each measurement, print the
mean absolute difference and the largest absolute difference with the patient in whom it occurs.
Then show all differences in one table, with one row per patient and one column per measurement.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the two summaries and the table, and keep the mean absolute difference of the QT
interval in milliseconds under the name "answer".
Test: The table must have ten rows. For patient VC-0317, the differences of the PR, QRS and QT
intervals must be only a few milliseconds.
```

### Project step 3: The heart rate of record 100 over thirty minutes

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to see how the heart rate of a 69-year-old man changes over his
30-minute ambulatory ECG, record 100 of the MIT-BIH Arrhythmia Database.
Data: The notebook holds a table named "data". Each row is a mark that the cardiologists placed on
the recording: The column "time" gives its place in seconds, and the column "label" its kind. "N"
marks a normal beat, "A" an atrial premature beat and "V" a premature ventricular contraction; "+"
marks a change of rhythm and is not a beat.
Task: Keep only the beats, that is, all labels except "+". For every beat after the first, compute
the heart rate as 60 divided by the RR interval in seconds. Plot this heart rate against the time in
minutes. Then compute the mean heart rate of the whole recording as 60 divided by the mean RR
interval.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the mean heart rate in beats per minute with one decimal and keep it under the name
"answer". Show the plot as well.
Test: An RR interval of exactly 1 second must give 60 beats per minute, and the mean heart rate must
lie between 60 and 90 beats per minute.
```

### Project step 4: Bazett or Fridericia for each patient

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: For ten patients of the virtual clinic, the cardiologist wants to know whether the choice
between Bazett's and Fridericia's correction changes the decision that the QT interval is prolonged.
Data: The notebook holds a table named "data". Each row is a patient: The column "patient" gives the
number of the patient, and "sex" says "female" or "male". The column "heart rate" gives the measured
heart rate in beats per minute, and "QT" the measured QT interval in milliseconds.
Task: For every patient, compute the RR interval in seconds as 60 divided by the heart rate. Compute
the QTc by Bazett's formula, the QT divided by the square root of RR, and by Fridericia's formula,
the QT divided by the cube root of RR. Call a QTc prolonged when it is 460 ms or longer in a woman,
or 450 ms or longer in a man. List the patients for whom the two formulas lead to different
decisions.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print a table with the two corrections and the two decisions, and the list of the
disagreements. Keep the number of patients with different decisions under the name "answer".
Test: Patient VC-0317, a woman at about 85 beats per minute, must be prolonged by Bazett's formula
and not by Fridericia's.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
