# Prompt library, Week 10

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 10](README.md) · [Türkçe](../../tr/hafta-10/PROMPTLAR.md)

This library holds every prompt of the practice stops of Week 10, from the parts *Prompt and application* of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the Jupyter notebook, into the empty cell under the prompt of the same number, and runs there.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [Working with a prompt](#working-with-a-prompt)
2. [Stop 1: The AF model of the prototype](#stop-1-the-af-model-of-the-prototype)
3. [Stop 2: The explanation, the report and the service](#stop-2-the-explanation-the-report-and-the-service)
4. [Stop 3: The user test and version 1.1](#stop-3-the-user-test-and-version-11)
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

## Stop 1: The AF model of the prototype

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-10/lecture.html#stop-1) · Jupyter notebook: «Stop 1 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-10/NB10_clinical_decision_support.ipynb#scrollTo=stop-1-prompt)*

This stop starts the mini project of the session, an AF detection CDSS, with the model that predicts. The minutes of the 25 records of the AFDB are described by four numbers of their RR intervals, a logistic regression learns AF from the training records, its threshold is chosen on the validation records, and the test records give the AF burden and the alarm episodes of each record.

### Prompt 1.1: Four numbers of a minute

**Goal.** Describe every minute of the AFDB by four numbers of its RR intervals.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist of a telemetry ward wants a decision support prototype that flags minutes
of possible AF from the times of the beats. The first step is to describe each minute by numbers
that measure how irregular its RR intervals are.
Data: The notebook holds a table named "data" with the minutes of the MIT-BIH Atrial Fibrillation
Database (AFDB), 25 Holter recordings of about ten hours of people with mostly paroxysmal atrial
fibrillation (AF), cut into windows of one minute. Each row is a minute: "record" gives the
recording, "set" its set ("training", 15 records; "validation", 5 records; "test", 5 records), and
"start (s)" the start of the minute in seconds from the start of the recording. "AF" is 1 when more
than half of the minute lies in AF as marked by the experts, and 0 otherwise. Each cell of "RR
intervals (s)" holds the RR intervals of the minute in seconds, in their order, as a list of 20 or
more numbers.
Task: For every minute, compute four numbers from its RR intervals: the heart rate, 60 divided by
the mean interval; the coefficient of variation, the standard deviation of the intervals (with n −
1) divided by their mean; the RMSSD divided by the mean interval, where the RMSSD is the square root
of the mean of the squared differences between successive intervals; and the pNN50, the share of
successive differences larger than 0.05 seconds. Then compare the four numbers of the minutes with
and without AF in the training records.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the median of each number for the training minutes with AF and without AF, and keep
the median CV of the training minutes with AF, with three decimals, under the name "answer".
Test: The heart rate of every minute must lie between 20 and 250 per minute, and the pNN50 between 0
and 1.
```

**Expected result:** "answer" = 0.222

### Prompt 1.2: The model and its threshold

**Goal.** Fit version 1.0 of the AF model on the training records and choose its threshold on the validation records.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants the prototype to miss as few AF minutes as possible: At least 95
percent of them should raise an alarm. The false alarms are the price, and the test records must
stay untouched for the final judgement.
Data: The notebook holds a table named "data" with the minutes of the MIT-BIH Atrial Fibrillation
Database (AFDB), 25 Holter recordings of about ten hours of people with mostly paroxysmal atrial
fibrillation (AF), cut into windows of one minute. Each row is a minute: "record" gives the
recording, "set" its set ("training", 15 records; "validation", 5 records; "test", 5 records) and
"start (s)" the start of the minute in seconds. "AF" is 1 when more than half of the minute lies in
AF as marked by the experts, and 0 otherwise. Four numbers describe the RR intervals of the minute:
"heart rate" (per minute), "CV" (the standard deviation of the intervals divided by their mean),
"RMSSD/RR" (the root mean square of the successive differences divided by the mean interval) and
"pNN50" (the share of successive differences larger than 50 ms).
Task: Fit a logistic regression for AF on the training minutes only, with at most 3,000 iterations.
Its inputs are the heart rate, the natural logarithm of the CV, the natural logarithm of the
RMSSD/RR and the pNN50, each turned into a z-score with the mean and the standard deviation of the
training minutes. Compute the probability of AF for every validation minute and the area under the
ROC curve (AUC) on the validation minutes. Choose the threshold on the validation minutes only:
Among 0.05, 0.06, 0.07 and so on up to 0.95, take the highest value at which at least 95 percent of
the validation minutes with AF have a probability at or above it.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the validation AUC, the threshold and the coefficients of the model, and keep the
threshold, with two decimals, under the name "answer".
Test: No test minute may be used, and the share of the validation minutes with AF at or above the
threshold must be at least 0.95.
```

**Expected result:** "answer" = 0.37

### Prompt 1.3: AF burden and alarm episodes of the test records

**Goal.** Turn the probabilities of the test minutes into alarm episodes and an AF burden for every test record.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist does not review single minutes but runs of alarm minutes, and wants the AF
burden of each recording as the report will give it.
Data: The notebook holds a table named "data" with the minutes of the 5 test records of the MIT-BIH
Atrial Fibrillation Database, Holter recordings of people with mostly paroxysmal atrial fibrillation
(AF), cut into windows of one minute. Each row is a minute: "record" gives the recording and "start
(s)" the start of the minute in seconds. "AF" is 1 when more than half of the minute lies in AF as
marked by the experts, "AF share" is the share of the minute in AF, from 0 to 1, and "probability"
is the probability of AF that a model of the course gives the minute. The model raises an alarm for
a minute when its probability is at least 0.37.
Task: Within each record, sort the minutes by their start. An alarm episode is a run of consecutive
minutes with an alarm, and a false alarm episode is an episode in which no minute has AF. For each
record, compute the AF burden of the annotation, 100 times the mean AF share of its minutes; the AF
burden of the model, 100 times the share of its minutes with an alarm; the number of alarm episodes;
and the number of false alarm episodes.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each record, and keep the total number of false alarm episodes
of the test records under the name "answer".
Test: The alarm episodes of a record cannot be more than half of its minutes plus one, and the
burdens must lie between 0 and 100.
```

**Expected result:** "answer" = 22

## Stop 2: The explanation, the report and the service

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-10/lecture.html#stop-2) · Jupyter notebook: «Stop 2 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-10/NB10_clinical_decision_support.ipynb#scrollTo=stop-2-prompt)*

This stop completes the mini project of the session and follows one alarm and one patient. A false alarm minute of record 08219 is explained by the SHAP values of its four numbers, the result of VC-0128 of the telemetry ward is written as an HL7 FHIR report, the beat times of the same patient are sent to the prediction service of the course, and one hour of the ECG of VC-0128 is uploaded, its beats found and its minutes judged by the service.

### Prompt 2.1: Why the minute alarmed

**Goal.** Compute what each of the four numbers adds to the log-odds of AF in one false alarm minute.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The physician opens a false alarm of record 08219 and asks which numbers of the minute made
the model raise it, before looking at the strip.
Data: The notebook holds a table named "data" that describes one minute of record 08219 of the
MIT-BIH Atrial Fibrillation Database, a minute without AF in which a logistic regression of the
course raises an alarm. The first four rows are the four numbers of the minute: "number" names it,
"value in the minute" gives its value, "logarithm first" says whether the model takes the natural
logarithm of the value before anything else ("yes" or "no"), "mean, training" and "standard
deviation, training" are the mean and the standard deviation of the value, or of its logarithm, over
the training minutes, and "coefficient" is its coefficient in the model. The last row, "intercept",
holds only the intercept of the model in "coefficient".
Task: For each of the four numbers, take the natural logarithm of the value when "logarithm first"
says yes, subtract the mean and divide by the standard deviation to get its z-score, and multiply
the z-score by the coefficient: This is its contribution to the log-odds. Add the intercept and the
four contributions to get the log-odds of the minute, and turn it into a probability with 1 / (1 + e
to the power of minus the log-odds).
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with the z-score and the contribution of each number, print the log-odds and
the probability, and keep the probability, with three decimals, under the name "answer".
Test: The intercept plus the four contributions must give the log-odds, and the probability must lie
between 0 and 1.
```

**Expected result:** "answer" = 0.985

### Prompt 2.2: The report as HL7 FHIR resources

**Goal.** Write the result of VC-0128 as an HL7 FHIR R4 report that the information system of a hospital can read.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The 24-hour report of the prototype must reach the record of the patient as a preliminary
report, until a cardiologist confirms or rejects it, and it must say which model wrote it.
Data: The notebook holds a table named "data" with one row: the result of a decision support
prototype of the course for VC-0128, a patient of the telemetry ward of the virtual clinic, a
synthetic data set. "patient" gives the identifier of the patient, "AF burden (%)" the share of the
analysed minutes with an alarm of atrial fibrillation (AF), "alarm episodes" the number of runs of
consecutive alarm minutes and "longest episode (minutes)" the longest of them. "start of the
recording" and "end of the recording" give the period of the 24-hour recording, "model", "version"
and "SHA-256" name the model and the fingerprint of its file, and "time of the report" the time at
which the report is written, all times in the ISO format with their offset from UTC.
Task: Write a FHIR Bundle of type "collection" with four resources, each with an id and a fullUrl
under http://example.org/fhir. A Device "af-rr" with the name of the model, its version and a note
with the SHA-256. An Observation "af-burden" with the status "preliminary", the category
"procedure", a local code "af-burden" of the system http://example.org/vclinic with the text "AF
burden", the patient as subject, the period of the recording, the AF burden as a quantity in the
unit "%" of UCUM (system http://unitsofmeasure.org, code "%") and a reference to the Device. A
DiagnosticReport "af-report" with the status "preliminary", the text "Holter recording, AF
analysis", the patient, the time of the report, a reference to the Observation and a conclusion in
words. A Provenance that names the report as its target, records the time of the report and gives
the Device as its author. Then check that every reference inside the bundle points to a resource of
the bundle, apart from the patient.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the Observation as JSON, print the number of resources and of references that do not
resolve, and keep the value of the AF burden in the Observation under the name "answer".
Test: The bundle must hold four resources, no reference inside it may point to a missing resource,
and both statuses must be "preliminary".
```

**Expected result:** "answer" = 15.5

### Prompt 2.3: A request to the prediction service

**Goal.** Send the beat times of VC-0128 to the prediction service of the course and read its answer.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The web interface of the ward should not hold the model itself: It asks the prediction
service, which answers with the result and the version of the model.
Data: The notebook holds a table named "data" with one column, "beat time (s)": the times of the
104,314 beats that the monitor found in the 24-hour recording of VC-0128, a patient of the telemetry
ward of the virtual clinic, a synthetic data set, in seconds from the start of the recording. The
data cell has also started a prediction service of the course on this computer at the address
http://127.0.0.1:8765/predict. The service takes a request in JSON with the fields "patient_id" and
"beat_times_s" (a list of beat times in seconds) and answers in JSON with the model, its version and
fingerprint, the threshold, the minutes analysed, the minutes with an alarm of atrial fibrillation
(AF), the AF burden in percent and the alarm episodes.
Task: Build the request for patient "VC-0128" with all beat times, send it to the service as JSON
with the method POST, and read the answer as JSON. The service runs on this computer, so the request
must not go through a proxy server.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the size of the request in kilobytes, the model, its version and the first twelve
digits of its fingerprint, the minutes, the AF minutes and the AF burden, show the alarm episodes as
a table, and keep the number of AF minutes under the name "answer".
Test: The AF burden in the answer must be 100 times the AF minutes divided by the minutes, rounded
to one decimal.
```

**Expected result:** "answer" = 222

### Prompt 2.4: From an uploaded ECG to the AF minutes

**Goal.** Find the beats of an uploaded ECG and let the prediction service of the course judge every minute of it.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: In the mini project, the physician uploads one hour of the ECG of VC-0128 instead of the
beat times of the monitor, so the prototype must find the beats itself before the model can predict.
Data: The notebook holds a table named "data" with one hour of the ECG of VC-0128, a patient of the
telemetry ward of the virtual clinic, a synthetic data set: one column, "mV", with 900,000 values of
lead II in millivolts, sampled at 250 Hz, from 13:00 to 14:00. The first value lies 5 hours, 18,000
seconds, after the start of the recording at 08:00. The data cell has also started the prediction
service of the course on this computer at the address http://127.0.0.1:8765/predict. The service
takes a request in JSON with the fields "patient_id" and "beat_times_s" (a list of beat times in
seconds from the start of the recording) and answers in JSON with the model, its version and
fingerprint, the threshold, the minutes analysed, the minutes with an alarm of atrial fibrillation
(AF), the AF burden in percent and the alarm episodes, each with its start in seconds ("start_s")
and its minutes.
Task: Find the beats of the ECG. Filter the signal with a band-pass filter from 5 to 15 Hz, applied
forwards and backwards so that the peaks do not shift. Take as R peaks the local maxima of the
filtered signal that are higher than a third of its 99th percentile and at least 0.25 seconds apart.
Turn their positions into times in seconds from the start of the recording: Divide by 250 and add
18,000. Then send the beat times of patient "VC-0128" to the prediction service as JSON with the
method POST, without a proxy server, and read the answer as JSON.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of beats found, the minutes, the AF minutes and the AF burden, show the
alarm episodes as a table with their start as a time of day (the recording starts at 08:00), and
keep the number of AF minutes under the name "answer".
Test: One hour of ECG must give between 4,000 and 9,000 beats, and the AF burden in the answer must
be 100 times the AF minutes divided by the minutes, rounded to one decimal.
```

**Expected result:** "answer" = 39

## Stop 3: The user test and version 1.1

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-10/lecture.html#stop-3) · Jupyter notebook: «Stop 3 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-10/NB10_clinical_decision_support.ipynb#scrollTo=stop-3-prompt)*

This stop runs the user test and improves the prototype. The alarm episodes of the four patients of the telemetry ward show what a physician would review in 24 hours, version 1.1 adds the sample entropy and learns again on the training records, and the test records judge both versions once.

### Prompt 3.1: The alarm episodes of the ward

**Goal.** Count the alarm episodes that the physician of the ward would review in 24 hours, and the false ones among them.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The user test asks how much work the prototype gives the physician of the ward, and where
its false alarms come from.
Data: The notebook holds a table named "data" with the minutes of the 24-hour recordings of the four
patients of the telemetry ward of the virtual clinic, a synthetic data set: VC-0128 (paroxysmal
atrial fibrillation, premature atrial beats and two periods of electrode noise), VC-0347 (sinus
rhythm with frequent premature atrial beats, no AF), VC-0519 (persistent AF) and VC-0733 (sinus
rhythm with long periods of electrode noise, no AF). Each row is a minute: "patient" gives the
patient, "start (h)" the start of the minute in hours from the start of the recording, "AF" is 1
when more than half of the minute lies in AF in the truth of the recording, and "probability" is the
probability of AF from version 1.0 of a model of the course. The model raises an alarm when the
probability is at least 0.37.
Task: Within each patient, sort the minutes by their start. An alarm episode is a run of consecutive
minutes with an alarm, and a false alarm episode is an episode in which no minute has AF. For each
patient, count the alarm minutes, the false alarm minutes (alarm minutes without AF), the alarm
episodes and the false alarm episodes.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each patient, print the total of the alarm episodes and of the
false ones, and keep the total number of false alarm episodes under the name "answer".
Test: A patient without any AF minute can have no true alarm episode, and the false alarm episodes
cannot outnumber the alarm episodes.
```

**Expected result:** "answer" = 76

### Prompt 3.2: Version 1.1 with the sample entropy

**Goal.** Add the sample entropy as a fifth number, fit version 1.1 on the training records and count its false alarm episodes on the validation records.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The user test showed that premature beats raise most false alarms. Premature beats repeat
the same short and long intervals, while AF has no pattern, so a number that measures the pattern
may help. The test records must stay untouched.
Data: The notebook holds a table named "data" with the training and validation minutes of the
MIT-BIH Atrial Fibrillation Database (AFDB), 25 Holter recordings of about ten hours of people with
mostly paroxysmal atrial fibrillation (AF), cut into windows of one minute; the test records are not
in it. Each row is a minute: "record" gives the recording, "set" its set ("training", 15 records;
"validation", 5 records) and "start (s)" the start of the minute in seconds. "AF" is 1 when more
than half of the minute lies in AF as marked by the experts. Each cell of "RR intervals (s)" holds
the RR intervals of the minute in seconds, in their order. The four numbers of the minute are "heart
rate" (per minute), "CV", "RMSSD/RR" and "pNN50", as in the earlier steps.
Task: For every minute, also compute the sample entropy of its RR intervals with stretches of one
interval and a tolerance of 0.03 seconds: Of the first n − 1 intervals of the minute, count the
pairs that differ by at most 0.03 seconds (B), and count how many of these pairs are still alike
when each interval is followed by the next one (A). The sample entropy is the natural logarithm of B
divided by A; count A as 1 when it is 0, and give the minute the natural logarithm of n when B is 0.
Fit a logistic regression for AF on the training minutes with at most 3,000 iterations, on five
inputs: the heart rate, the natural logarithm of the CV, the natural logarithm of the RMSSD/RR, the
pNN50 and the sample entropy, each turned into a z-score with the mean and the standard deviation of
the training minutes. Choose the threshold on the validation minutes only: Among 0.05, 0.06, 0.07
and so on up to 0.95, take the highest value at which at least 95 percent of the validation minutes
with AF have a probability at or above it. Then, within each validation record, sort the minutes by
their start, find the alarm episodes, runs of consecutive alarm minutes, and count the false alarm
episodes, in which no minute has AF.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the validation AUC, the threshold, the number of false alarm episodes and the median
sample entropy of the training minutes with and without AF, and keep the number of false alarm
episodes under the name "answer".
Test: No test minute may be used, and the sample entropy of every minute must be 0 or more.
```

**Expected result:** "answer" = 69

### Prompt 3.3: Both versions on the test records

**Goal.** Open the test records once and compare the two versions of the model.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Before the clinic chooses a version for the trial of the ward, the cardiologist wants both
versions judged on records that neither of them has seen, with the gains and the costs of version
1.1.
Data: The notebook holds a table named "data" with the minutes of the 5 test records of the MIT-BIH
Atrial Fibrillation Database, Holter recordings of people with mostly paroxysmal atrial fibrillation
(AF), cut into windows of one minute. Each row is a minute: "record" gives the recording and "start
(s)" the start of the minute in seconds. "AF" is 1 when more than half of the minute lies in AF as
marked by the experts, and "AF share" is the share of the minute in AF, from 0 to 1. "probability,
version 1.0" and "probability, version 1.1" are the probabilities of AF from two versions of a model
of the course. Version 1.0 raises an alarm when its probability is at least 0.37, version 1.1 when
its probability is at least 0.28.
Task: Within each record, sort the minutes by their start. An alarm episode is a run of consecutive
minutes with an alarm, and a false alarm episode is an episode in which no minute has AF. For each
version, compute on all test minutes the AUC, the sensitivity (the share of AF minutes with an
alarm) and the specificity (the share of the other minutes without an alarm). Count the false alarm
episodes over the test records, and compute the error of the AF burden: for each record, the
absolute difference between 100 times the share of its minutes with an alarm and 100 times its mean
AF share, averaged over the records.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each version, and keep the sensitivity of version 1.1, with
three decimals, under the name "answer".
Test: Every AUC, sensitivity and specificity must lie between 0 and 1, and each threshold must be
the one chosen on the validation records.
```

**Expected result:** "answer" = 0.924

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

### Ask for a review of a decision support prototype

```text
Review the code below, which is part of a decision support prototype for physicians, and its web
interface. Check seven points. Are the records split by person, so that no minute of a test person
was used for training? Was the threshold chosen on validation data and never on the test? What is
the unit of an alarm, and how many alarms will a user see per patient and day? Does every output,
the screen, the report and the answer of a service, carry the version of the model and the
fingerprint of its file? Can the physician see the signal behind every alarm and reject it as easily
as confirm it, with a reason that goes into a log? Is every report honest about its status,
preliminary until a physician decides? Did any record of a real patient leave the institution, for
example to an online service? For each point, quote the lines that answer it, say whether they are
right, and propose a correction where they are not. Do not change anything else.
```

## Prompts of the weekly project

The [weekly project](README.md#weekly-project) can be built with four prompts, one for each step. The section *Weekly project* at the end of the Jupyter notebook prepares the table of each prompt and opens on its own. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Project step 1: The alarm episodes of the user test

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist runs a user test of an AF prototype on five validation records and on four
patients of a telemetry ward, and needs the list of alarm episodes to review, one row per episode.
Data: The notebook holds a table named "data" with the minutes of the user test: the 5 validation
records of the MIT-BIH Atrial Fibrillation Database and the 24-hour recordings of the four patients
of the telemetry ward of the virtual clinic, a synthetic data set. Each row is a minute: "source"
gives "AFDB" or "ward", "recording" the record or the patient, and "start (h)" the start of the
minute in hours from the start of the recording. "AF" is 1 when more than half of the minute lies in
atrial fibrillation (AF) in the annotation or the truth of the recording, and "probability, version
1.0" is the probability of AF from version 1.0 of a model of the course, which raises an alarm at
0.37 or more.
Task: Within each recording, sort the minutes by their start. An alarm episode is a run of
consecutive minutes with an alarm. Make one row per alarm episode with the source, the recording,
the start in hours, the length in minutes, the highest probability and whether any minute of the
episode has AF.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the first rows of the table and the number of episodes of each recording, and keep the
total number of alarm episodes under the name "answer".
Test: The lengths of the episodes must add up to the minutes with an alarm.
```

### Project step 2: The workload of the physician

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how many alarm episodes a physician would review per 24
hours with version 1.0, how many of them are false, and in which recordings the false ones gather.
Data: The notebook holds a table named "data" with the minutes of the user test: the 5 validation
records of the MIT-BIH Atrial Fibrillation Database and the 24-hour recordings of the four patients
of the telemetry ward of the virtual clinic, a synthetic data set. Each row is a minute: "source"
gives "AFDB" or "ward", "recording" the record or the patient, and "start (h)" the start of the
minute in hours from the start of the recording. "AF" is 1 when more than half of the minute lies in
atrial fibrillation (AF) in the annotation or the truth of the recording, and "probability, version
1.0" is the probability of AF from version 1.0 of a model of the course, which raises an alarm at
0.37 or more.
Task: Within each record, sort the minutes by their start. An alarm episode is a run of consecutive
minutes with an alarm, and a false alarm episode is an episode in which no minute has AF. For each
recording, count the minutes, the alarm episodes and the false alarm episodes, and give the alarm
episodes and the false ones per 24 hours of recording. Then give the same for the AFDB and for the
ward as a whole.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each recording and the two totals, and keep the share of false
alarm episodes over all recordings, with three decimals, under the name "answer".
Test: The false alarm episodes of a recording cannot exceed its alarm episodes.
```

### Project step 3: An improved version on the validation records

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The user test showed that premature beats raise most false alarms. The cardiologist wants
an improved version, fitted on the training records and judged on the validation records only.
Data: The notebook holds a table named "data" with the minutes of the MIT-BIH Atrial Fibrillation
Database (AFDB), 25 Holter recordings of about ten hours of people with mostly paroxysmal atrial
fibrillation (AF), cut into windows of one minute. The test records are not in it. Each row is a
minute: "record" gives the recording, "set" its set ("training", 15 records; "validation", 5
records), and "start (s)" the start of the minute in seconds from the start of the recording. "AF"
is 1 when more than half of the minute lies in AF as marked by the experts, and 0 otherwise. Each
cell of "RR intervals (s)" holds the RR intervals of the minute in seconds, in their order, as a
list of 20 or more numbers. The four numbers of the minute are "heart rate", "CV", "RMSSD/RR" and
"pNN50".
Task: For every minute, also compute the sample entropy of its RR intervals with stretches of one
interval and a tolerance of 0.03 seconds: Of the first n − 1 intervals of the minute, count the
pairs that differ by at most 0.03 seconds (B), and count how many of these pairs are still alike
when each interval is followed by the next one (A). The sample entropy is the natural logarithm of B
divided by A; count A as 1 when it is 0, and give the minute the natural logarithm of n when B is 0.
Fit a logistic regression for AF on the training minutes with at most 3,000 iterations, on five
inputs: the heart rate, the natural logarithm of the CV, the natural logarithm of the RMSSD/RR, the
pNN50 and the sample entropy, each turned into a z-score with the mean and the standard deviation of
the training minutes. Choose the threshold on the validation minutes only: Among 0.05, 0.06, 0.07
and so on up to 0.95, take the highest value at which at least 95 percent of the validation minutes
with AF have a probability at or above it. Give the validation AUC, the sensitivity and the
specificity at the threshold, and the false alarm episodes of every validation record.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the results, print the coefficients and the threshold, and keep the threshold, with two
decimals, under the name "answer".
Test: No test minute may be used, and the sensitivity on the validation records must be at least
0.95.
```

### Project step 4: Both versions on the test records and the change log

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist opens the test records once for both versions and writes the change log of
the new version, with its gains and its costs.
Data: The notebook holds a table named "data" with the minutes of the 5 test records of the MIT-BIH
Atrial Fibrillation Database, Holter recordings of people with mostly paroxysmal atrial fibrillation
(AF), cut into windows of one minute. Each row is a minute: "record" gives the recording and "start
(s)" the start of the minute in seconds; "AF" is 1 when more than half of the minute lies in AF as
marked by the experts, and "AF share" is the share of the minute in AF. Each cell of "RR intervals
(s)" holds the RR intervals of the minute in seconds, and the four numbers of the minute are "heart
rate", "CV", "RMSSD/RR" and "pNN50".
Task: Version 1.0 uses four inputs: the heart rate, the natural logarithm of the CV, the natural
logarithm of the RMSSD/RR and the pNN50; version 1.1 adds the sample entropy of the RR intervals
with stretches of one interval and a tolerance of 0.03 seconds. Use the two versions of step 3 and
of Stop 1 exactly as they were fitted on the training minutes, with their thresholds from the
validation minutes. Within each record, sort the minutes by their start. An alarm episode is a run
of consecutive minutes with an alarm, and a false alarm episode is an episode in which no minute has
AF. For each version, compute on the test minutes the AUC, the sensitivity, the specificity, the
false alarm episodes and the mean absolute error of the AF burden per record, in percentage points.
Then write a change log of the new version with its version number, the change, the reason, the
threshold, the effects on the validation and on the test records, and what did not improve.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the table of the two versions and print the change log, and keep the sensitivity of the
new version on the test records, with three decimals, under the name "answer".
Test: The test records must be used once for each version, and no threshold may be changed after
looking at them.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
