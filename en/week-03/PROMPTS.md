# Prompt library, Week 3

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 3](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-03/PROMPTLAR.md)

This library holds every prompt of the prompt path of Week 3, Part 1 of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the notebook, into the empty cell of the step of the same number, and runs there. The [guide to the prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [How a step works](#how-a-step-works)
2. [Stop 1: Cine MR as numbers](#stop-1-cine-mr-as-numbers)
3. [Stop 2: A first convolutional network](#stop-2-a-first-convolutional-network)
4. [Stop 3: Mini project: EchoNet-Dynamic, normal or abnormal (with your registration)](#stop-3-mini-project-echonet-dynamic-normal-or-abnormal-with-your-registration)
5. [Prompts for repairing, explaining and reviewing code](#prompts-for-repairing-explaining-and-reviewing-code)
6. [Prompt path of the weekly project](#prompt-path-of-the-weekly-project)

## How a step works

| Step | What to do |
|---|---|
| 1. Read | Read the goal of the step in the notebook. |
| 2. Prepare the data | Run the data cell under the prompt. It prepares the table "data" that the prompt describes and shows it. |
| 3. Copy and send | Copy the prompt and send it to an AI assistant: Gemini in Google Colab, or ChatGPT, Claude, Copilot or Gemini in another browser tab. |
| 4. Run | Paste the code of the assistant into the cell below the data cell and run it. |
| 5. Check | Run the check cell. It prints *correct* or *not yet* and the value of the result "answer". |
| 6. Repair | If the check prints *not yet*, send the repair prompt with the code. If the result is still wrong, run the *Ready code* cell, which gives the correct result. |
| 7. Explain and log | Ask the assistant to explain the code in plain language, and write the tool, the prompt and what was checked in the AI usage log. |

## Stop 1: Cine MR as numbers

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html#stop-1) · The same result on the Python path: Python step 3, Sections 1 to 3*

The expert contours of ACDC turn each examination into numbers: volumes, the ejection fraction (EF) and the thickness of the walls. In this stop the three groups are described with these numbers, the EF of patient 134 is computed from the voxels of the contours, and the rules of ACDC are applied to every patient.

### Step 1.1: The ejection fraction of the three groups

**Goal.** See how the EF separates the three groups of ACDC.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: In the cardiac MR data set ACDC, the cardiologist wants to see how the left ventricular
ejection fraction differs between normal hearts, dilated cardiomyopathy and hypertrophic
cardiomyopathy.
Data: The notebook holds a table named "data" with the 90 patients of ACDC in the groups NOR
(normal), DCM (dilated cardiomyopathy) and HCM (hypertrophic cardiomyopathy). Each row is a patient:
"patient" gives the name, "group" the group, "LVEF" the left ventricular ejection fraction in
percent, "LVEDVI" the left ventricular end-diastolic volume indexed to the body surface area in
mL/m², and "thickest wall" the thickest segment of the wall at end-diastole in mm. All were measured
on the contours of the experts.
Task: Compute the mean LVEF of each group and print the three means with one decimal.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Keep the mean LVEF of the group DCM, with one decimal, under the name "answer".
Test: The mean of the group DCM must be below 40 percent, and that of the group HCM above 50
percent.
```

**Expected result:** "answer" = 19.8

### Step 1.2: The ejection fraction of patient 134 from the voxels

**Goal.** Compute volumes and the EF from the expert contours slice by slice, as the software of a CMR laboratory does.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to compute the end-diastolic and end-systolic volumes and the
ejection fraction of the left ventricle of patient 134 of ACDC by summing the contoured cavity slice
by slice.
Data: The notebook holds a table named "data". Each row is a short-axis slice of the examination,
from the base to the apex: "slice" gives its number, and "end-diastole" and "end-systole" give the
number of pixels inside the contour of the left ventricular cavity in that slice. One pixel measures
1.445 × 1.445 mm, and the slices are 10 mm thick.
Task: For each phase, add up the pixels of all slices and multiply the sum by the volume of one
voxel, 1.445 × 1.445 × 10 mm³; divide by 1,000 to get mL. This gives the end-diastolic volume EDV
and the end-systolic volume ESV. The EF is (EDV − ESV)/EDV × 100.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print EDV and ESV in mL and the EF in percent with one decimal, and keep the EF under the
name "answer".
Test: EDV must be larger than ESV and lie between 50 and 300 mL.
```

**Expected result:** "answer" = 62.2

### Step 1.3: The rules of ACDC on every patient

**Goal.** Classify the 90 patients with the definitions of ACDC and see where the measurements alone go wrong.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how often the measurement rules of the ACDC definitions
place a patient in the group given by the experts.
Data: The notebook holds a table named "data" with the 90 patients of ACDC in the groups NOR
(normal), DCM (dilated cardiomyopathy) and HCM (hypertrophic cardiomyopathy). Each row is a patient:
"patient" gives the name, "group" the group, "LVEF" the left ventricular ejection fraction in
percent, "LVEDVI" the left ventricular end-diastolic volume indexed to the body surface area in
mL/m², and "thickest wall" the thickest segment of the wall at end-diastole in mm. All were measured
on the contours of the experts.
Task: Apply the rules of ACDC to every patient: The patient is DCM if LVEF is below 40 and LVEDVI
above 100; otherwise HCM if the thickest wall is above 15 and LVEF is 50 or more; otherwise NOR.
Print a table that counts the patients by group and by rule, and compute the share of patients whose
rule equals their group.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the share with three decimals and keep it under the name "answer".
Test: The table must count 90 patients in total, and the share must lie between 0 and 1.
```

**Expected result:** "answer" = 0.967

## Stop 2: A first convolutional network

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html#stop-2) · The same result on the Python path: Sections 4 to 7*

The network of the course learns the three groups from the pixels of the middle slices, with the end-diastolic and the end-systolic frame of each slice as two channels. In this stop the slices are normalised, the network is built, trained with early stopping and judged patient by patient on the 30 test patients.

### Step 2.1: Normalising with the training slices

**Goal.** Prepare the inputs of the network with statistics that come from the training patients alone.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Before a network learns the groups of ACDC from cine MR slices, the cardiologist wants to
scale the pixels with numbers that come from the training patients alone.
Data: The notebook holds a table named "data" with 270 short-axis slices of cine MR, the three
middle slices of each of the 90 patients of ACDC. Each row is a slice: "patient" gives the patient,
"group" the group of the patient ("NOR", "DCM" or "HCM") and "set" the set of the patient
("training", 45 patients; "validation", 15 patients; "test", 30 patients). Each cell of the columns
"end-diastole" and "end-systole" holds an image of 64 × 64 pixels with values from 0 to 1; one pixel
is 2 mm.
Task: Compute the mean and the standard deviation of all pixels of both frames of the training
slices, those whose set is "training". Normalise the pixels of all slices with these two numbers:
Subtract the mean and divide by the standard deviation.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the mean and the standard deviation with four decimals, and keep the mean under the
name "answer".
Test: After the normalisation, the training pixels must have a mean of about 0 and a standard
deviation of about 1; the 135 training slices must keep their size of 64 × 64 pixels.
```

**Expected result:** "answer" = 0.2961

### Step 2.2: The network and its parameters

**Goal.** Build the network of the course and count its weights.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to build a small convolutional network for the groups of ACDC and to
know how many weights it learns.
Data: The notebook holds a table named "data" with 270 short-axis slices of cine MR, the three
middle slices of each of the 90 patients of ACDC. Each row is a slice: "patient" gives the patient,
"group" the group of the patient ("NOR", "DCM" or "HCM") and "set" the set of the patient
("training", 45 patients; "validation", 15 patients; "test", 30 patients). Each cell of the columns
"end-diastole" and "end-systole" holds an image of 64 × 64 pixels with values from 0 to 1; one pixel
is 2 mm.
Task: Build a small convolutional network that receives the two frames of a slice as two channels.
It has three blocks; each block has a convolution with 3 × 3 kernels that keeps the size of the
image, batch normalisation, ReLU and a 2 × 2 max pooling. The blocks have 8, 16 and 32 kernels.
After the blocks come flattening, dropout with a rate of 0.3 and one linear layer that gives a score
to each of the three groups. Count the weights that the network learns, its trainable parameters.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of trainable parameters and keep it under the name "answer".
Test: For the first four training slices, the network must return four rows of three scores.
```

**Expected result:** "answer" = 12,219

### Step 2.3: Training with early stopping and a decision per patient

**Goal.** Train the network and judge it as a clinic would: one decision for each patient.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to train a small convolutional network on the cine MR slices of ACDC
and to judge it on the test patients as a clinic would, with one decision for each patient.
Data: The notebook holds a table named "data" with 270 short-axis slices of cine MR, the three
middle slices of each of the 90 patients of ACDC. Each row is a slice: "patient" gives the patient,
"group" the group of the patient ("NOR", "DCM" or "HCM") and "set" the set of the patient
("training", 45 patients; "validation", 15 patients; "test", 30 patients). Each cell of the columns
"end-diastole" and "end-systole" holds an image of 64 × 64 pixels with values from 0 to 1; one pixel
is 2 mm.
Task: Normalise the pixels with the mean and the standard deviation of the training slices. Build a
small convolutional network that receives the two frames of a slice as two channels. It has three
blocks; each block has a convolution with 3 × 3 kernels that keeps the size of the image, batch
normalisation, ReLU and a 2 × 2 max pooling. The blocks have 8, 16 and 32 kernels. After the blocks
come flattening, dropout with a rate of 0.3 and one linear layer that gives a score to each of the
three groups. Train it on the training slices with the cross-entropy loss. After every epoch,
measure the loss on the validation slices without learning from them, and keep the weights of the
epoch with the lowest validation loss (early stopping). Make the random choices the same in every
run by using the number 2026 as the starting value. Then compute the probabilities of the three
groups for every test slice, average them over the three slices of each test patient, and take the
group with the largest mean as the decision for the patient.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the epoch with the lowest validation loss and the share of the 30 test patients whose
decision equals their group, with three decimals; keep the share under the name "answer".
Test: There must be 30 test patients, and the three mean probabilities of each patient must add up
to 1.
```

**Expected result:** "answer" = 0.933

### Step 2.4: The confusion matrix and the macro F1

**Goal.** Read the result class by class and find the patients that the network misses. The data cell trains the network of the course once, which takes about a minute.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: For the 30 test patients of ACDC, the cardiologist wants to read the decisions of a network
group by group and to find the patients that it misses.
Data: The notebook holds a table named "data". Each row is a test patient: "patient" gives the name,
"true group" the group given by the experts and "decision" the group chosen by the network; both are
"NOR", "DCM" or "HCM".
Task: Build the confusion matrix with the true groups in the rows and the decisions in the columns,
both in the order NOR, DCM, HCM, and print it. Compute the F1 score of each group and their plain
mean, the macro F1. Print the names of the patients whose decision differs from their true group.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the macro F1 with three decimals and keep it under the name "answer".
Test: The confusion matrix must add up to 30 patients, and each of its rows to 10.
```

**Expected result:** "answer" = 0.933

## Stop 3: Mini project: EchoNet-Dynamic, normal or abnormal (with your registration)

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html#stop-3) · The same result on the Python path: Sections 8 to 10*

The mini project of the session uses EchoNet-Dynamic, the echocardiography videos that each participant obtains through a personal registration at Stanford AIMI. Without a registration, follow the run of the instructor on the shared screen. With one, paste your personal download link into the first cell of this stop in the notebook, or put the zip file into the folder data/echonet of the course folder. The data stay in your Colab session or on your computer and never enter a prompt: The prompts describe only the table that the notebook prepares.

### Step 3.1: The videos and their sets

**Goal.** Check that the copy is complete before any analysis.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Before any analysis, the cardiologist wants to check that a copy of the echocardiography
data set EchoNet-Dynamic, obtained through a personal registration, is complete.
Data: The notebook holds a table named "data" with the videos of the cardiologist's own copy of
EchoNet-Dynamic, a data set of echocardiography videos. Each row is a video: "video" gives its name,
"EF" the ejection fraction in percent, and "set" the set chosen by the authors ("training",
"validation" or "test").
Task: Print the number of videos in each set and the total number of videos.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Keep the total number of videos under the name "answer".
Test: The set "training" must hold 7,465 videos, the set "validation" 1,288 and the set "test"
1,277.
```

**Expected result:** "answer": 10,030 for a complete copy

### Step 3.2: The share of abnormal EF

**Goal.** Know how common the abnormal class is before judging a model.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Before a model of EchoNet-Dynamic is judged, the cardiologist wants to know how common an
abnormal ejection fraction, below 50 percent, is among the test videos.
Data: The notebook holds a table named "data" with the videos of the cardiologist's own copy of
EchoNet-Dynamic, a data set of echocardiography videos. Each row is a video: "video" gives its name,
"EF" the ejection fraction in percent, and "set" the set chosen by the authors ("training",
"validation" or "test").
Task: Select the videos whose set is "test" and compute the share of them with an EF below 50
percent.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the share with three decimals and keep it under the name "answer".
Test: The share must lie between 0 and 1, and the number of test videos must be 1,277.
```

**Expected result:** "answer": the value of the ready code on your copy

### Step 3.3: The network of the course on echocardiography

**Goal.** Train the same network on the end-diastolic and end-systolic frames of the videos and measure how well it recognises an abnormal EF. The data cell reads 1,400 videos, which takes a few minutes.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how well a small convolutional network recognises an
ejection fraction below 50 percent from two frames of an echocardiography video, the end-diastolic
and the end-systolic one.
Data: The notebook holds a table named "data" with 1,000 training videos and 400 test videos of
EchoNet-Dynamic. Each row is a video: "set" says "training" or "test", and "abnormal" is 1 when the
EF is below 50 percent and 0 otherwise. Each cell of the columns "end-diastole" and "end-systole"
holds the traced frame of that phase as an image of 64 × 64 pixels with values from 0 to 1.
Task: Normalise the pixels with the mean and the standard deviation of the training videos. Build a
small convolutional network that receives the two frames of a video as two channels. It has three
blocks; each block has a convolution with 3 × 3 kernels that keeps the size of the image, batch
normalisation, ReLU and a 2 × 2 max pooling. The blocks have 8, 16 and 32 kernels. After the blocks
come flattening, dropout with a rate of 0.3 and one linear layer that gives two scores, one for a
normal and one for an abnormal EF. Train it on the training videos with the cross-entropy loss. Make
the random choices the same in every run by using the number 2026 as the starting value. Then
compute the probability of an abnormal EF for each test video and the area under the ROC curve
(AUC).
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the AUC with three decimals and keep it under the name "answer".
Test: There must be 1,000 training videos with two frames of 64 × 64 pixels, and the AUC must lie
between 0.5 and 1.
```

**Expected result:** "answer": a value between 0.6 and 1.0, which varies a little from computer to computer

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

### Ask for a review of a training loop

```text
Review the code below, which trains and evaluates a classifier of medical images. Check six points.
Is the split into training, validation and test sets made by patient? Does the normalisation use
statistics of the training images only? Is the network switched to training mode for learning and to
evaluation mode for measuring? Is the evaluation done without recording gradients? Does the output
layer fit the loss, with no extra softmax before a cross-entropy that applies its own? Does the
reported measure suit the classes and give one decision per patient? Answer with a short list, then
return the corrected code.

[paste the code here]
```

## Prompt path of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. The section *Weekly project on the prompt path* at the end of Part 1 of the Jupyter notebook prepares the table of each prompt. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Step 1: Train the network

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to train a small convolutional network on the cine MR slices of ACDC
with early stopping, and to see how the losses of the training and the validation slices develop.
Data: The notebook holds a table named "data" with 270 short-axis slices of cine MR, the three
middle slices of each of the 90 patients of ACDC. Each row is a slice: "patient" gives the patient,
"group" the group of the patient ("NOR", "DCM" or "HCM") and "set" the set of the patient
("training", 45 patients; "validation", 15 patients; "test", 30 patients). Each cell of the columns
"end-diastole" and "end-systole" holds an image of 64 × 64 pixels with values from 0 to 1; one pixel
is 2 mm.
Task: Normalise the pixels with the mean and the standard deviation of the training slices. Build a
small convolutional network that receives the two frames of a slice as two channels. It has three
blocks; each block has a convolution with 3 × 3 kernels that keeps the size of the image, batch
normalisation, ReLU and a 2 × 2 max pooling. The blocks have 8, 16 and 32 kernels. After the blocks
come flattening, dropout with a rate of 0.3 and one linear layer that gives a score to each of the
three groups. Train it on the training slices with the cross-entropy loss. Make the random choices
the same in every run by using the number 2026 as the starting value. After every epoch, measure the
loss on the validation slices without learning from them, and keep the weights of the epoch with the
lowest validation loss. Draw the training and the validation loss against the epochs.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the figure of the two losses, and keep the epoch with the lowest validation loss under
the name "answer".
Test: After the kept weights are loaded, the validation loss must again have its lowest value.
```

### Step 2: The confusion matrix of the network

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: For the 30 test patients of ACDC, the cardiologist wants to see the confusion matrix of a
network with one decision for each patient, and the precision, the recall and the F1 score of each
group.
Data: The notebook holds a table named "data" with the 90 test slices, three for each of the 30 test
patients. Each row is a slice: "patient" gives the patient, "true group" the group given by the
experts, and "NOR", "DCM" and "HCM" the probabilities of the three groups, from 0 to 1, that the
network of the course gives to the slice. The data cell trains this network once, which takes about
a minute.
Task: Average the probabilities over the slices of each patient and take the group with the largest
mean as the decision. Build the confusion matrix of the 30 patients with the true groups in the rows
and the decisions in the columns, both in the order NOR, DCM, HCM. Compute the precision, the recall
and the F1 score of each group, and the macro F1.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the matrix and a table of the three measures by group, and keep the macro F1 under the
name "answer".
Test: The matrix must add up to 30, and each of its rows to 10.
```

### Step 3: The rules on the same patients

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to compare the network with the measurement rules of ACDC on the
same 30 test patients.
Data: The notebook holds a table named "data" with the 30 test patients of ACDC in the groups NOR
(normal), DCM (dilated cardiomyopathy) and HCM (hypertrophic cardiomyopathy). Each row is a patient:
"patient" gives the name, "group" the group, "LVEF" the left ventricular ejection fraction in
percent, "LVEDVI" the left ventricular end-diastolic volume indexed to the body surface area in
mL/m², and "thickest wall" the thickest segment of the wall at end-diastole in mm. All were measured
on the contours of the experts.
Task: Apply the rules of ACDC: The patient is DCM if LVEF is below 40 and LVEDVI above 100;
otherwise HCM if the thickest wall is above 15 and LVEF is 50 or more; otherwise NOR. Build the
confusion matrix of group against rule, in the order NOR, DCM, HCM, and compute the accuracy.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the matrix and print the accuracy with three decimals, and keep the accuracy under the
name "answer".
Test: The matrix must add up to 30.
```

### Step 4: The errors

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: For the test patients that a network of ACDC misclassifies, the cardiologist wants to see
where the thickest wall of the left ventricle lies, from the base to the apex.
Data: The notebook holds a table named "data" with the misclassified test patients of the network of
the course. Each row is one short-axis slice of one of these patients at end-diastole: "patient"
gives the patient, "true group" and "decision" the group of the experts and the group of the
network, "slice" the number of the slice from the base (0) to the apex, "thickest wall" the thickest
segment of the wall in that slice in mm, and "seen by the network" says "yes" for the three middle
slices, the only ones that the network saw.
Task: For every patient, plot the thickest wall against the number of the slice and mark the slices
that the network saw. Print the slice with the thickest wall of the examination and whether the
network saw it.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show one figure for each patient, and keep the number of misclassified patients under the
name "answer".
Test: Each patient must have exactly three slices with "yes" in "seen by the network", and the
number of patients must equal the number of errors in the confusion matrix of project step 2.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
