# Prompt library, Week 5

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 5](README.md) · [Türkçe](../../tr/hafta-05/PROMPTLAR.md)

This library holds every prompt of the practice stops of Week 5, from the parts *Prompt and application* of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the Jupyter notebook, into the empty cell under the prompt of the same number, and runs there.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [Working with a prompt](#working-with-a-prompt)
2. [Stop 1: Mini project: Rhythm, from a rule to the nine classes of the PhysioNet 2020 Challenge](#stop-1-mini-project-rhythm-from-a-rule-to-the-nine-classes-of-the-physionet-2020-challenge)
3. [Stop 2: ST elevation: the median beat, the J point and the alarm](#stop-2-st-elevation-the-median-beat-the-j-point-and-the-alarm)
4. [Stop 3: Long-term monitoring: windows, AF burden and false alarms](#stop-3-long-term-monitoring-windows-af-burden-and-false-alarms)
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

## Stop 1: Mini project: Rhythm, from a rule to the nine classes of the PhysioNet 2020 Challenge

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#stop-1) · Jupyter notebook: «Stop 1 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-05/NB05_time_series_and_ecg_ai.ipynb#scrollTo=stop-1-prompt)*

This stop is the mini project of the session. The 12-lead ECGs of PTB-XL are read first as a cardiologist reads the rhythm, from the RR intervals, and then by a one-dimensional convolutional network that learns six labels at once. The network is trained on folds 1 and 2, its thresholds are chosen on fold 9, and both the rule and the network are judged on fold 10. The last step judges the same network trained for the nine classes of the PhysioNet 2020 Challenge.

### Prompt 1.1: A rule from the RR intervals

**Goal.** Test the first half of the clinical rule for AF, irregularly irregular RR intervals, on the test fold.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how well a simple rule from the RR intervals detects atrial
fibrillation (AF) in 12-lead ECGs of 10 seconds.
Data: The notebook holds a table named "data" with the 2,198 recordings of the test fold of PTB-XL,
a public collection of clinical 12-lead ECGs of 10 seconds. Each row is a recording: "record" gives
its number, "RR" holds its RR intervals in seconds, found from the R peaks of all 12 leads, and "AF"
is 1 when the cardiologists described atrial fibrillation and 0 otherwise.
Task: For every recording with at least three RR intervals, compute the coefficient of variation:
the standard deviation of the intervals, with the number of intervals minus one in the denominator,
divided by their mean. Call a recording AF when its coefficient of variation is above 0.10. Compare
the rule with the column "AF" and compute its sensitivity, its specificity and its positive
predictive value. Also draw the coefficients of variation of the recordings with and without AF as
two histograms, with a vertical line at 0.10.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of alarms and the three values, and keep the sensitivity, with three
decimals, under the name "answer".
Test: The alarms must equal the true alarms plus the false alarms, and the sensitivity must equal
the true alarms divided by the recordings with AF.
```

**Expected result:** "answer" = 0.914

### Prompt 1.2: A one-dimensional network for six labels

**Goal.** Train a network that reads the whole signal of the 12 leads and gives six labels at once. The training takes about a minute.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to train a network that reads 12-lead ECGs of 10 seconds and
recognises six findings of rhythm at once, and to know how well it separates them on new recordings.
Data: The notebook holds a table named "data" with 6,539 recordings of PTB-XL, a public collection
of clinical 12-lead ECGs of 10 seconds. Each row is a recording: "set" gives its set ("training",
folds 1 and 2, 4,356 recordings; "validation", fold 9, 2,183 recordings), and each cell of the
column "ECG" holds the recording as an array of 12 leads × 1,000 samples in mV, recorded at 100 Hz,
with the leads in the order I, II, III, aVR, aVL, aVF and V1 to V6. The six columns "SR", "AFIB",
"STACH", "SBRAD", "SARRH" and "PVC" are 1 when the cardiologists gave the statement and 0 otherwise:
sinus rhythm, atrial fibrillation, sinus tachycardia, sinus bradycardia, sinus arrhythmia and
ventricular premature complexes.
Task: Build a one-dimensional convolutional network that gives one score to each of the six labels.
It has four convolutional layers along time, each with stride 2 and each followed by batch
normalisation and ReLU: 32 kernels of 7 samples over the 12 leads, then 64 kernels of 5, 64 kernels
of 5 and 128 kernels of 3 samples. The mean of each of the 128 channels over time goes to a last
linear layer with six outputs. Before training, limit the values of the signals to the range from −5
to 5 mV. Train it on the training recordings for 15 epochs, in shuffled groups of 64 recordings,
with the binary cross-entropy of the six labels as the loss and the Adam optimiser. Use a one-cycle
learning rate with a highest value of 0.003. After every epoch, compute the area under the ROC curve
(AUC) of each label on the validation recordings and their mean, and keep the weights of the epoch
where the mean is highest. Make the random choices the same in every run by using the number 2026 as
the starting value.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of parameters, the mean AUC of every epoch and the best epoch, and keep the
best mean AUC, with three decimals, under the name "answer".
Test: The network must have 59,622 parameters, and the mean AUC must lie between 0.5 and 1.
```

**Expected result:** "answer" = 0.881

### Prompt 1.3: Each label on the test fold

**Goal.** Judge the network of the course label by label on recordings that it never saw.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know, for each of six findings of rhythm, how well a network
separates the 12-lead ECGs with the finding from those without it.
Data: The notebook holds a table named "data" with the 2,198 recordings of the test fold of PTB-XL.
Each row is a recording: "record" gives its number. The six columns "SR", "AFIB", "STACH", "SBRAD",
"SARRH" and "PVC" are 1 when the cardiologists gave the statement and 0 otherwise: sinus rhythm,
atrial fibrillation, sinus tachycardia, sinus bradycardia, sinus arrhythmia and ventricular
premature complexes. The six columns "probability SR" to "probability PVC" hold the probabilities
that a one-dimensional convolutional network, trained on folds 1 and 2, gave to the six labels.
Task: For each of the six labels, compute the area under the ROC curve (AUC) of its probability
against its column of 0 and 1. Draw the six ROC curves in one figure, with the AUC of each in the
legend.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print a small table with the label, the number of recordings with the label and the AUC, and
keep the AUC of "AFIB", with three decimals, under the name "answer".
Test: Every AUC must lie between 0 and 1, and the numbers of recordings must add up to at least
2,198, because a recording can carry several labels.
```

**Expected result:** "answer" = 0.975

### Prompt 1.4: Thresholds chosen on fold 9

**Goal.** Turn the probabilities into decisions with one threshold per label, chosen on fold 9 and judged on fold 10.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to turn the probabilities of a network for six findings of rhythm
into decisions, with one threshold for each finding chosen on recordings that are kept apart from
the test.
Data: The notebook holds a table named "data" with the 4,381 recordings of folds 9 and 10 of PTB-XL.
Each row is a recording: "record" gives its number and "set" its set ("validation", fold 9; "test",
fold 10). The six columns "SR", "AFIB", "STACH", "SBRAD", "SARRH" and "PVC" are 1 when the
cardiologists gave the statement and 0 otherwise: sinus rhythm, atrial fibrillation, sinus
tachycardia, sinus bradycardia, sinus arrhythmia and ventricular premature complexes. The six
columns "probability SR" to "probability PVC" hold the probabilities that a one-dimensional
convolutional network, trained on folds 1 and 2, gave to the six labels.
Task: For each label, choose on the validation recordings the threshold of the probability at which
sensitivity plus specificity is highest. Apply each threshold to the test recordings: A label is
given when its probability reaches its threshold. Compute the sensitivity, the specificity and the
positive predictive value of each label on the test recordings.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print a table with the label, its threshold and the three values, and keep the positive
predictive value of "AFIB" on the test recordings, with three decimals, under the name "answer".
Test: The thresholds must come from the validation recordings only, and every sensitivity and
specificity must lie between 0 and 1.
```

**Expected result:** "answer" = 0.636

### Prompt 1.5: The nine classes of the PhysioNet 2020 Challenge

**Goal.** Judge class by class a network trained for the nine classes of CPSC 2018, one of the databases of the PhysioNet 2020 Challenge. The training takes about a minute.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how well a network recognises nine findings of the 12-lead
ECG at once, from a normal ECG to ST elevation, and which findings it misses.
Data: The notebook holds a table named "data" with the 2,198 recordings of the test fold of PTB-XL.
Each row is a recording: "record" gives its number. The nine columns "Normal", "AF", "I-AVB",
"LBBB", "RBBB", "PAC", "PVC", "STD" and "STE" are 1 when the cardiologists gave the finding and 0
otherwise: a normal ECG, atrial fibrillation, first-degree atrioventricular block, left and right
bundle branch block, premature atrial and ventricular contractions, ST depression and ST elevation,
the nine classes of the China Physiological Signal Challenge 2018, a database of the PhysioNet 2020
Challenge. The nine columns "probability Normal" to "probability STE" hold the probabilities that a
one-dimensional convolutional network, trained on folds 1 and 2, gave to the nine classes.
Task: For each of the nine classes, count the recordings with the class and compute the area under
the ROC curve (AUC) of its probability against its column of 0 and 1. Draw the nine AUC values as a
horizontal bar chart, sorted from the lowest to the highest, with a dashed line at 0.5.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print a table with the class, the number of recordings and the AUC, and keep the mean AUC of
the nine classes, with three decimals, under the name "answer".
Test: Every AUC must lie between 0 and 1, and every class must have at least one recording in the
table.
```

**Expected result:** "answer" = 0.848

## Stop 2: ST elevation: the median beat, the J point and the alarm

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#stop-2) · Jupyter notebook: «Stop 2 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-05/NB05_time_series_and_ecg_ai.ipynb#scrollTo=stop-2-prompt)*

The case of the week, record 13913, is read here as a STEMI alarm reads it. The single beats are aligned on their R peaks and their median gives one clean beat for each lead. The ST deviation at the J point is measured against the PR segment, the criteria of the universal definition decide the alarm, and the same alarm is then tried on the recordings of the test fold with left bundle branch block.

### Prompt 2.1: The median beat of the case

**Goal.** Build from the single beats of the case one clean beat for each lead, as the software of an ECG machine does before it measures.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to build the median beat of a 12-lead ECG of 10 seconds, one clean
beat for each lead, before the ST segment is measured.
Data: The notebook holds a table named "data" with record 13913 of PTB-XL, the 12-lead ECG of 10
seconds of a man of 68 years, recorded at 100 Hz. Each row is a sample, 10 ms after the one before:
"time" gives its time in seconds, the twelve columns "I" to "V6" the values of the twelve leads in
mV, and "R peak" is 1 at the samples of the R peaks and 0 elsewhere.
Task: Cut out every beat from 0.30 s before to 0.55 s after its R peak, and keep only the beats
whose window lies entirely inside the 10 seconds. For each lead, take the median of these beats
sample by sample: the median beat. Draw the median beat of V2 over the single beats of V2 in light
grey, with the time in ms from the R peak on the horizontal axis.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of beats used, and keep it under the name "answer".
Test: Each beat must hold 86 samples, from −300 to 550 ms, and the median beat of V2 must lie inside
the range of its single beats at every sample.
```

**Expected result:** "answer" = 19

### Prompt 2.2: ST at the J point and the criteria of the universal definition

**Goal.** Measure the ST deviation of the twelve leads of the case and apply the criteria of the universal definition, as an automatic STEMI alarm does.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to measure the ST deviation at the J point in the twelve leads of a
median beat and to see whether the ECG meets the ST criteria of the fourth universal definition of
myocardial infarction.
Data: The notebook holds a table named "data" with the median beat of the 12 leads of record 13913
of PTB-XL, the ECG of a man of 68 years: the median of his single beats, sample by sample, aligned
on their R peaks. Each row is a sample, 10 ms after the one before: "time" gives its time in ms from
the R peak, from −300 to 550 ms, and the twelve columns "I" to "V6" the values of the twelve leads
in mV. In this median beat, the QRS complex begins 70 ms before the R peak and ends, at the J point,
50 ms after it, as the slopes of all twelve leads show.
Task: For each lead, take as the reference level the mean of the values at 130, 120, 110 and 100 ms
before the R peak, the 40 ms of the PR segment that end 20 ms before the QRS onset. The ST deviation
of a lead is its value at the J point, 50 ms after the R peak, minus its reference level. A lead
meets the criterion of the fourth universal definition of myocardial infarction when its ST
elevation at the J point reaches its cut-point: 0.2 mV in V2 and V3 for men of 40 years or more,
0.25 mV for men under 40 and 0.15 mV for women, and 0.1 mV in every other lead. The alarm fires when
at least two leads of the same group meet the criterion. The groups of contiguous leads are anterior
(V1 to V6), inferior (II, III and aVF) and lateral (I and aVL); aVR belongs to no group.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the ST deviation of each lead in mV and in mm (1 mm = 0.1 mV), the leads that meet the
criterion and the groups in which the alarm fires, and keep the number of leads that meet the
criterion under the name "answer".
Test: The ST deviations of III and of aVR must be negative, because the report of the cardiologists
describes ST depression in III.
```

**Expected result:** "answer" = 9

### Prompt 2.3: The alarm in left bundle branch block

**Goal.** Try the same alarm on all recordings of the test fold and see what it does in left bundle branch block, where the criteria do not apply.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to apply an automatic STEMI alarm, based on the ST criteria of the
fourth universal definition of myocardial infarction, to all ECGs of a test set and to see how often
it fires in complete left bundle branch block.
Data: The notebook holds a table named "data" with the 2,198 recordings of the test fold of PTB-XL.
Each row is a recording: "record" gives its number, "sex" the sex of the patient ("M" or "F"), "age"
the age in years, and "LBBB" is 1 when the cardiologists described a complete left bundle branch
block and 0 otherwise. The twelve columns "I" to "V6" hold the ST deviation of the twelve leads in
mV: the value at the J point of the median beat of the recording minus the level of its PR segment.
Task: A lead meets the criterion of the fourth universal definition of myocardial infarction when
its ST elevation at the J point reaches its cut-point: 0.2 mV in V2 and V3 for men of 40 years or
more, 0.25 mV for men under 40 and 0.15 mV for women, and 0.1 mV in every other lead. The alarm
fires when at least two leads of the same group meet the criterion. The groups of contiguous leads
are anterior (V1 to V6), inferior (II, III and aVF) and lateral (I and aVL); aVR belongs to no
group. Apply the alarm to every recording, with the cut-points of V2 and V3 chosen by the sex and
the age of its patient. Count the alarms among all recordings and among the recordings with left
bundle branch block.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of alarms among all recordings and among the recordings with left bundle
branch block, with the numbers of recordings, and keep the number of alarms among the recordings
with left bundle branch block under the name "answer".
Test: There must be 2,198 recordings, 54 of them with left bundle branch block, and the alarms among
them cannot be more than 54.
```

**Expected result:** "answer" = 51

## Stop 3: Long-term monitoring: windows, AF burden and false alarms

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#stop-3) · Jupyter notebook: «Stop 3 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-05/NB05_time_series_and_ecg_ai.ipynb#scrollTo=stop-3-prompt)*

A Holter recorder of the virtual clinic has followed patient VC-0128 for 24 hours. In this stop the beats of the recording are read in windows of 30 seconds, as the algorithm of a recorder does: The irregularity of the RR intervals in each window decides the alarm, the windows with an alarm give the AF burden, and the false alarms are traced back to their hours. The recording is synthetic, so the truth is known beat by beat, and nothing has to be downloaded.

### Prompt 3.1: The irregularity of the rhythm in windows of 30 seconds

**Goal.** Read the 24 hours as a monitor does, window by window, and count the windows whose RR intervals are irregular.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to read a 24-hour Holter recording in windows of 30 seconds and to
see in how many windows the RR intervals are irregular enough for an alarm of atrial fibrillation
(AF).
Data: The notebook holds a table named "data" with the beats of a 24-hour Holter recording of
patient VC-0128 of the virtual clinic, a 76-year-old woman with palpitations, as the beat detector
of the recorder found them. The recording starts at 08:00. Each row is a beat: "time" gives the time
of the beat in seconds from the start of the recording, and "RR" the interval from the previous beat
in seconds.
Task: Divide the 24 hours into windows of 30 seconds, starting at the beginning of the recording,
and give each beat to the window in which its time falls. In every window that holds at least five
RR intervals, compute the irregularity of the rhythm as the coefficient of variation: the standard
deviation of its RR intervals, with the number of intervals minus one in the denominator, divided by
their mean. Draw the coefficient of variation of every window against the clock time, with a
horizontal line at 0.10.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of windows, and keep the number of windows whose coefficient of variation
is above 0.10 under the name "answer".
Test: There must be 2,880 windows of 30 seconds, and the coefficients of variation must all be
positive.
```

**Expected result:** "answer" = 519

### Prompt 3.2: The AF burden

**Goal.** Turn the windows into the number that a Holter report gives: the share of the day spent in AF.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants the AF burden of a 24-hour Holter recording, the share of the
recording spent in atrial fibrillation, as an algorithm that reads windows of 30 seconds would
report it.
Data: The notebook holds a table named "data" with the beats of a 24-hour Holter recording of
patient VC-0128 of the virtual clinic, a 76-year-old woman with palpitations, as the beat detector
of the recorder found them. The recording starts at 08:00. Each row is a beat: "time" gives the time
of the beat in seconds from the start of the recording, and "RR" the interval from the previous beat
in seconds.
Task: Divide the 24 hours into windows of 30 seconds, starting at the beginning of the recording,
and give each beat to the window in which its time falls. In every window that holds at least five
RR intervals, compute the irregularity of the rhythm as the coefficient of variation: the standard
deviation of its RR intervals, with the number of intervals minus one in the denominator, divided by
their mean. Call a window AF when its coefficient of variation is above 0.10. The AF burden is the
number of AF windows times 30 seconds, divided by the 24 hours of the recording. Also find the clock
times of the first and the last AF window.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of AF windows, and keep the AF burden, in percent with one decimal, under
the name "answer".
Test: The burden must equal the share of AF windows among all windows of 30 seconds, times 100.
```

**Expected result:** "answer" = 18.0

### Prompt 3.3: Where the false alarms come from

**Goal.** Compare the alarm with the confirmed episodes and find the hours of its false alarms, as the reader of a Holter recording would.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to compare the AF alarm of a 24-hour Holter recording with the
episodes that a cardiologist confirmed, and to see at which hours of the day the false alarms occur.
Data: The notebook holds a table named "data" with the beats of a 24-hour Holter recording of
patient VC-0128 of the virtual clinic, a 76-year-old woman with palpitations, as the beat detector
of the recorder found them. The recording starts at 08:00. Each row is a beat: "time" gives the time
of the beat in seconds from the start of the recording, and "RR" the interval from the previous beat
in seconds. The column "AF" is 1 for the beats of the episodes of atrial fibrillation that a
cardiologist confirmed on the whole recording, and 0 for all other beats.
Task: Divide the 24 hours into windows of 30 seconds, starting at the beginning of the recording,
and give each beat to the window in which its time falls. In every window that holds at least five
RR intervals, compute the irregularity of the rhythm as the coefficient of variation: the standard
deviation of its RR intervals, with the number of intervals minus one in the denominator, divided by
their mean. Call a window AF when its coefficient of variation is above 0.10. A window is a true AF
window when more than half of its beats belong to a confirmed episode. Count the false alarms, the
AF windows that are not true AF windows, and the missed windows, the true AF windows without an
alarm. Then count the false alarms for each clock hour.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of missed windows and a small table of the false alarms by clock hour, and
keep the total number of false alarms under the name "answer".
Test: The false alarms of all hours must add up to the total, and the AF windows must equal the true
AF windows with an alarm plus the false alarms.
```

**Expected result:** "answer" = 75

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

### Ask for a review of a time-series pipeline

```text
Review the code below, which reads 12-lead ECGs and reports a model or an alarm. Check six points.
Are the recordings of one patient kept in one set, training, validation or test? Are the sampling
frequency and the units right? Are the leads taken by their names and not by their positions? Were
the thresholds chosen on the validation set and not on the test set? Are the results reported for
each label, together with how often the label occurs? Is the rule of each measurement stated: the
baseline, the J point and the cut-points by sex and age? For every problem, quote the line, explain
the consequence in clinical words and give the corrected line. Do not change anything else.
```

## Prompts of the weekly project

The [weekly project](README.md#weekly-project) can be built with four prompts, one for each step. The section *Weekly project* at the end of the Jupyter notebook prepares the table of each prompt and opens on its own. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Project step 1: The alarm against the acute infarctions

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to judge an automatic STEMI alarm, based on the ST criteria of the
fourth universal definition of myocardial infarction, as a chest pain unit would: how many acute
infarctions it finds and how many of its alarms are right.
Data: The notebook holds a table named "data" with the 4,381 recordings of folds 9 and 10 of PTB-XL.
Each row is a recording: "record" gives its number, "set" its set ("validation" or "test"), "sex"
the sex of the patient ("M" or "F") and "age" the age in years. "acute infarction" is 1 when the
cardiologists classified an infarction of the recording as acute (stage I or I-II) and 0 otherwise,
and "statements" lists the codes of all their statements, separated by commas, for example "CLBBB"
for complete left bundle branch block, "LVH" for left ventricular hypertrophy and "PACE" for a
pacemaker. The twelve columns "I" to "V6" hold the ST deviation of the twelve leads in mV: the value
at the J point of the median beat of the recording minus the level of its PR segment.
Task: A lead meets the criterion of the fourth universal definition of myocardial infarction when
its ST elevation at the J point reaches its cut-point: 0.2 mV in V2 and V3 for men of 40 years or
more, 0.25 mV for men under 40 and 0.15 mV for women, and 0.1 mV in every other lead. The alarm
fires when at least two leads of the same group meet the criterion. The groups of contiguous leads
are anterior (V1 to V6), inferior (II, III and aVF) and lateral (I and aVL); aVR belongs to no
group. Apply the alarm to every recording, with the cut-points of V2 and V3 chosen by the sex and
the age of its patient. Compare the alarm with the column "acute infarction" and compute its
sensitivity, its specificity and its positive predictive value, for all recordings and for each set.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with the numbers of recordings, acute infarctions and alarms and the three
values, one row for each set and one for all, and keep the sensitivity for all recordings, with
three decimals, under the name "answer".
Test: There must be 4,381 recordings and 26 acute infarctions, and the true alarms cannot be more
than 26.
```

### Project step 2: Where the false alarms come from

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know which diagnoses the false alarms of an automatic STEMI alarm
carry, to see where its criteria do not fit.
Data: The notebook holds a table named "data" with the 4,381 recordings of folds 9 and 10 of PTB-XL.
Each row is a recording: "record" gives its number, "set" its set ("validation" or "test"), "sex"
the sex of the patient ("M" or "F") and "age" the age in years. "acute infarction" is 1 when the
cardiologists classified an infarction of the recording as acute (stage I or I-II) and 0 otherwise,
and "statements" lists the codes of all their statements, separated by commas, for example "CLBBB"
for complete left bundle branch block, "LVH" for left ventricular hypertrophy and "PACE" for a
pacemaker. The twelve columns "I" to "V6" hold the ST deviation of the twelve leads in mV: the value
at the J point of the median beat of the recording minus the level of its PR segment.
Task: A lead meets the criterion of the fourth universal definition of myocardial infarction when
its ST elevation at the J point reaches its cut-point: 0.2 mV in V2 and V3 for men of 40 years or
more, 0.25 mV for men under 40 and 0.15 mV for women, and 0.1 mV in every other lead. The alarm
fires when at least two leads of the same group meet the criterion. The groups of contiguous leads
are anterior (V1 to V6), inferior (II, III and aVF) and lateral (I and aVL); aVR belongs to no
group. Apply the alarm to every recording, with the cut-points of V2 and V3 chosen by the sex and
the age of its patient. A false alarm is an alarm in a recording without an acute infarction. Count,
for every statement, the false alarms whose recording carries it, and for the statements "CLBBB",
"PACE" and "LVH" also the share of their recordings that raise the alarm.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the 15 statements with the most false alarms, and keep the number of false alarms in
recordings with "CLBBB" under the name "answer".
Test: The false alarms of a statement cannot be more than the recordings that carry it, and the
total of false alarms must equal the alarms minus the true alarms of step 1.
```

### Project step 3: A sweep of the cut-points

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to see how the sensitivity and the positive predictive value of an
automatic STEMI alarm change when all its cut-points are raised together.
Data: The notebook holds a table named "data" with the 4,381 recordings of folds 9 and 10 of PTB-XL.
Each row is a recording: "record" gives its number, "set" its set ("validation" or "test"), "sex"
the sex of the patient ("M" or "F") and "age" the age in years. "acute infarction" is 1 when the
cardiologists classified an infarction of the recording as acute (stage I or I-II) and 0 otherwise,
and "statements" lists the codes of all their statements, separated by commas, for example "CLBBB"
for complete left bundle branch block, "LVH" for left ventricular hypertrophy and "PACE" for a
pacemaker. The twelve columns "I" to "V6" hold the ST deviation of the twelve leads in mV: the value
at the J point of the median beat of the recording minus the level of its PR segment.
Task: A lead meets the criterion of the fourth universal definition of myocardial infarction when
its ST elevation at the J point reaches its cut-point: 0.2 mV in V2 and V3 for men of 40 years or
more, 0.25 mV for men under 40 and 0.15 mV for women, and 0.1 mV in every other lead. The alarm
fires when at least two leads of the same group meet the criterion. The groups of contiguous leads
are anterior (V1 to V6), inferior (II, III and aVF) and lateral (I and aVL); aVR belongs to no
group. Apply the alarm to every recording, with the cut-points of V2 and V3 chosen by the sex and
the age of its patient. Repeat the alarm with every cut-point raised by 0, 0.05, 0.10, 0.15 and 0.20
mV. For each margin, compute the sensitivity, the specificity and the positive predictive value
against the column "acute infarction", and draw the sensitivity and the positive predictive value
against the margin.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each margin, and keep the sensitivity with a margin of 0.10
mV, with three decimals, under the name "answer".
Test: The number of alarms cannot rise when the margin grows, and the row with a margin of 0 must
equal the result of step 1.
```

### Project step 4: Leaving out the recordings where the criteria do not apply

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to judge an automatic STEMI alarm only on the ECGs to which the ST
criteria of the universal definition apply, leaving out left bundle branch block and paced rhythms.
Data: The notebook holds a table named "data" with the 4,381 recordings of folds 9 and 10 of PTB-XL.
Each row is a recording: "record" gives its number, "set" its set ("validation" or "test"), "sex"
the sex of the patient ("M" or "F") and "age" the age in years. "acute infarction" is 1 when the
cardiologists classified an infarction of the recording as acute (stage I or I-II) and 0 otherwise,
and "statements" lists the codes of all their statements, separated by commas, for example "CLBBB"
for complete left bundle branch block, "LVH" for left ventricular hypertrophy and "PACE" for a
pacemaker. The twelve columns "I" to "V6" hold the ST deviation of the twelve leads in mV: the value
at the J point of the median beat of the recording minus the level of its PR segment.
Task: Leave out every recording whose statements include "CLBBB" or "PACE". A lead meets the
criterion of the fourth universal definition of myocardial infarction when its ST elevation at the J
point reaches its cut-point: 0.2 mV in V2 and V3 for men of 40 years or more, 0.25 mV for men under
40 and 0.15 mV for women, and 0.1 mV in every other lead. The alarm fires when at least two leads of
the same group meet the criterion. The groups of contiguous leads are anterior (V1 to V6), inferior
(II, III and aVF) and lateral (I and aVL); aVR belongs to no group. Apply the alarm to every
recording, with the cut-points of V2 and V3 chosen by the sex and the age of its patient. Compute
the sensitivity, the specificity and the positive predictive value against the column "acute
infarction" on the recordings that remain, and compare them with step 1.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of recordings left out and the three values, and keep the positive
predictive value, with three decimals, under the name "answer".
Test: The recordings left out and those that remain must add up to 4,381.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
