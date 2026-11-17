# Prompt library, Week 3

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 3](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-03/PROMPTLAR.md)

This library holds every prompt of the prompt path of Week 3, Part 1 of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the notebook, into the cell below the step of the same number, and runs there. The [guide to the prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [How a step works](#how-a-step-works)
2. [Stop 1: Cine MR as numbers](#stop-1-cine-mr-as-numbers)
3. [Stop 2: A first convolutional network](#stop-2-a-first-convolutional-network)
4. [Stop 3: EchoNet-Dynamic: normal or abnormal (with your registration)](#stop-3-echonet-dynamic-normal-or-abnormal-with-your-registration)
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

## Stop 1: Cine MR as numbers

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html#stop-1) · The same result on the Python path: Python step 3, Sections 1 to 3*

The expert contours of ACDC turn each examination into numbers: volumes, the ejection fraction (EF) and the thickness of the walls. In this stop the three groups are described with these numbers, the EF of patient 134 is computed from the voxels of the contours, and the rules of ACDC are applied to every patient.

### Step 1.1: The ejection fraction of the three groups

**Goal.** See how the EF separates the three groups of ACDC.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: `acdc_table` is a table with the 90 patients of ACDC in the groups NOR (normal), DCM (dilated
cardiomyopathy) and HCM (hypertrophic cardiomyopathy), one row per patient. The columns used here
are group; split ("training" or "testing"); lv_ef, the left ventricular ejection fraction (%);
lv_edvi, the left ventricular end-diastolic volume indexed to the body surface area (mL/m²); and
max_wall_mm, the thickest segment of the wall at end-diastole (mm). All were measured on the expert
contours.
Task: Compute the mean ejection fraction, lv_ef, of each group and print the three means, rounded to
one decimal.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the mean EF of the group DCM, rounded to one decimal. Keep the result under the name
`mean_ef_dcm` and print it with a short label. Return only the code, as one block, with a short
comment above each step.
Test: The mean EF of the group DCM must be below 40 percent and that of the group HCM above 50
percent.
```

**Expected result:** `mean_ef_dcm` = 19.8

### Step 1.2: The ejection fraction of patient 134 from the voxels

**Goal.** Compute volumes and the EF from the expert contours, as the software of a CMR laboratory does.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: `gt_ed` and `gt_es` hold the expert contours of patient 134 at end-diastole and at
end-systole, one label for every voxel: 0 background, 1 cavity of the right ventricle, 2 myocardium,
3 cavity of the left ventricle. `spacing` holds the size of one voxel in mm in its three directions.
Task: Count the voxels of the cavity of the left ventricle, the label 3, in gt_ed and in gt_es.
Multiply each count by the volume of one voxel, the product of the three sizes in spacing in mm³,
and divide by 1000 to get mL. This gives the end-diastolic volume EDV and the end-systolic volume
ESV. The EF is (EDV − ESV)/EDV × 100.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the EF in percent, rounded to one decimal, and also print EDV and ESV in mL. Keep the
result under the name `ef_case` and print it with a short label. Return only the code, as one block,
with a short comment above each step.
Test: EDV must be larger than ESV and lie between 50 and 300 mL.
```

**Expected result:** `ef_case` = 62.2

### Step 1.3: The rules of ACDC on every patient

**Goal.** Classify the 90 patients with the definitions of ACDC and see where the measurements alone go wrong.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: `acdc_table` is a table with the 90 patients of ACDC in the groups NOR (normal), DCM (dilated
cardiomyopathy) and HCM (hypertrophic cardiomyopathy), one row per patient. The columns used here
are group; split ("training" or "testing"); lv_ef, the left ventricular ejection fraction (%);
lv_edvi, the left ventricular end-diastolic volume indexed to the body surface area (mL/m²); and
max_wall_mm, the thickest segment of the wall at end-diastole (mm). All were measured on the expert
contours.
Task: Apply the rules of ACDC to every patient. A patient is DCM if lv_ef is below 40 and lv_edvi
above 100; otherwise HCM if max_wall_mm is above 15 and lv_ef is 50 or more; otherwise NOR. Write
the result into a new column named rule, print a table that counts the patients by group and by
rule, and compute the share of patients whose rule equals their group.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the share, rounded to three decimals. Keep the result under the name `rule_accuracy`
and print it with a short label. Return only the code, as one block, with a short comment above each
step.
Test: The table must count 90 patients in total, and the share must lie between 0 and 1.
```

**Expected result:** `rule_accuracy` = 0.967

## Stop 2: A first convolutional network

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html#stop-2) · The same result on the Python path: Sections 4 to 7*

The network of the course learns the three groups from the pixels of the middle slices, with the end-diastolic and the end-systolic frame of each slice as two channels. In this stop the slices are normalised, the network is built, trained with early stopping and judged patient by patient on the 30 test patients.

### Step 2.1: Normalising with the training slices

**Goal.** Prepare the inputs of the network with statistics that come from the training patients alone.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: `X` holds 270 slices: the three middle short-axis slices of each of the 90 patients. Every
slice has two frames of 64 × 64 pixels, the end-diastolic and the end-systolic one, with values from
0 to 1 and 2 mm per pixel. `y` holds the group of each slice (0 NOR, 1 DCM, 2 HCM), `patients` its
patient and `sets` its set: "train" (45 patients), "val" (15 patients) or "test" (30 patients).
Task: Compute the mean and the standard deviation of all pixels of the training slices, those whose
set is "train". Normalise all slices with these two numbers: Subtract the mean and divide by the
standard deviation. Then turn the slices and the groups of the three sets into the form that PyTorch
reads, under the names X_train, X_val and X_test for the slices and y_train, y_val and y_test for
the groups.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the mean of the training pixels, rounded to four decimals. Keep the six prepared
arrays, because the next steps use them. Keep the result under the name `train_mean` and print it
with a short label. Return only the code, as one block, with a short comment above each step.
Test: X_train must hold 135 slices of two frames of 64 × 64 pixels, and the normalised training
pixels must have a mean of about 0 and a standard deviation of about 1.
```

**Expected result:** `train_mean` = 0.2961

### Step 2.2: The network and its parameters

**Goal.** Build the network of the course and count its weights.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: The prepared slices of step 2.1: `X_train`, `X_val` and `X_test` hold the slices of the three
sets, normalised with the mean and the standard deviation of the training pixels, and `y_train`,
`y_val` and `y_test` their groups. `patients` and `sets` hold the patient and the set of each slice.
Task: Build the network of the course as a class named CmrCNN. It has three blocks; each block has a
convolution with 3 × 3 kernels that keeps the size of the image, batch normalisation, ReLU and a 2 ×
2 max pooling. The blocks have 8, 16 and 32 kernels, and the input has two channels, the two frames.
After the blocks come flattening, dropout with a rate of 0.3 and one linear layer that gives a score
to each of the three groups. Fix the randomness with RANDOM_STATE, create one network named model
and count its trainable parameters.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the number of trainable parameters as a whole number. Keep the class CmrCNN and the
network model. Keep the result under the name `n_params` and print it with a short label. Return
only the code, as one block, with a short comment above each step.
Test: For the first four training slices, the network must return four rows of three scores.
```

**Expected result:** `n_params` = 12219

### Step 2.3: Training with early stopping and a decision per patient

**Goal.** Train the network and judge it as a clinic would: one decision for each patient.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: The prepared slices of step 2.1: `X_train`, `X_val` and `X_test` hold the slices of the three
sets, normalised with the mean and the standard deviation of the training pixels, and `y_train`,
`y_val` and `y_test` their groups. `patients` and `sets` hold the patient and the set of each slice.
`model` is the network of step 2.2, not yet trained.
Task: Train the network with the training slices for 40 epochs. In every epoch, shuffle the slices
and use them in small batches of 16. Use the Adam method with a learning rate of 0.003 and the
cross-entropy loss. After every epoch, measure the loss on the validation slices without learning
from them, and keep a copy of the weights of the epoch with the lowest validation loss. When the
training ends, return to these weights. Then compute the probabilities of the three groups for the
test slices, average them over the slices of each test patient, and take the group with the highest
mean probability as the decision for that patient. Fix the randomness with RANDOM_STATE, so that the
training can be repeated.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the share of test patients whose decision equals their group, rounded to three
decimals. Keep the mean probabilities of the patients under the name patient_prob, their groups
under patient_true and the decisions under patient_pred, in the order of the sorted names of the
patients. Keep the result under the name `patient_accuracy` and print it with a short label. Return
only the code, as one block, with a short comment above each step.
Test: There must be 30 test patients, and the three probabilities of each patient must add up to 1.
```

**Expected result:** `patient_accuracy` = 0.933

### Step 2.4: The confusion matrix and the macro F1

**Goal.** Read the result class by class and find the patients that the network misses.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: patient_true and patient_pred of step 2.3: the groups and the decisions of the 30 test
patients (0 NOR, 1 DCM, 2 HCM), and patient_prob, their mean probabilities.
Task: Build the confusion matrix of the groups and the decisions, with the true groups in the rows
and the decisions in the columns, both in the order NOR, DCM, HCM, and print it with these names.
Compute the F1 score of each group and their plain mean, the macro F1.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the macro F1, rounded to three decimals. Keep the result under the name `macro_f1` and
print it with a short label. Return only the code, as one block, with a short comment above each
step.
Test: The confusion matrix must add up to 30 patients.
```

**Expected result:** `macro_f1` = 0.933

## Stop 3: EchoNet-Dynamic: normal or abnormal (with your registration)

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html#stop-3) · The same result on the Python path: Sections 8 to 10*

The mini project of the session uses EchoNet-Dynamic, the echocardiography videos that each participant obtains through a personal registration at Stanford AIMI. Without a registration, follow the run of the instructor on the shared screen. With one, paste your personal download link into the first cell below, or put the zip file into the folder data/echonet of the course folder. The data stay in your Colab session or on your computer and are never uploaded elsewhere.

### Step 3.1: The videos and their sets

**Goal.** Check that the copy is complete before any analysis.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: `echo` is the participant's own copy of EchoNet-Dynamic, which the course package reads with
two tools. The reading tool `echonet.file_list` receives the copy and gives the table of the videos,
one row per video, with the columns FileName, EF (ejection fraction, %) and Split ("TRAIN", "VAL" or
"TEST"). The frame tool `echonet.frame_pairs` receives the copy, the name of a set, the number of
videos, the size of the images in pixels and a seed for the random choice of the videos. For every
chosen video it gives the traced end-diastolic and end-systolic frames as two channels with values
from 0 to 1 (images), and abnormal, which is 1 when the EF is below 50 percent.
Task: Get the table of the videos with the reading tool of the course package. Print the number of
videos in each set of the column Split and the total number of videos.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the total number of videos as a whole number. Keep the result under the name `n_videos`
and print it with a short label. Return only the code, as one block, with a short comment above each
step.
Test: The three sets must hold 7465, 1288 and 1277 videos.
```

**Expected result:** `n_videos`: 10030 for a complete copy

### Step 3.2: The share of abnormal EF

**Goal.** Know how common the abnormal class is before judging a model.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: `echo` is the participant's own copy of EchoNet-Dynamic, which the course package reads with
two tools. The reading tool `echonet.file_list` receives the copy and gives the table of the videos,
one row per video, with the columns FileName, EF (ejection fraction, %) and Split ("TRAIN", "VAL" or
"TEST"). The frame tool `echonet.frame_pairs` receives the copy, the name of a set, the number of
videos, the size of the images in pixels and a seed for the random choice of the videos. For every
chosen video it gives the traced end-diastolic and end-systolic frames as two channels with values
from 0 to 1 (images), and abnormal, which is 1 when the EF is below 50 percent.
Task: Select the videos whose Split is "TEST" and compute the share of them with an EF below 50
percent.
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the share, rounded to three decimals. Keep the result under the name `share_low_ef` and
print it with a short label. Return only the code, as one block, with a short comment above each
step.
Test: The share must lie between 0 and 1, and the number of test videos must be 1277.
```

**Expected result:** `share_low_ef`: the value of the ready code on your copy

### Step 3.3: The network of the course on echocardiography

**Goal.** Train the same network on the end-diastolic and end-systolic frames of the videos and measure how well it recognises an abnormal EF.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: `echo` is the participant's own copy of EchoNet-Dynamic, which the course package reads with
two tools. The reading tool `echonet.file_list` receives the copy and gives the table of the videos,
one row per video, with the columns FileName, EF (ejection fraction, %) and Split ("TRAIN", "VAL" or
"TEST"). The frame tool `echonet.frame_pairs` receives the copy, the name of a set, the number of
videos, the size of the images in pixels and a seed for the random choice of the videos. For every
chosen video it gives the traced end-diastolic and end-systolic frames as two channels with values
from 0 to 1 (images), and abnormal, which is 1 when the EF is below 50 percent.
Task: With the frame tool of the course package, load the two traced frames of 1000 training videos
and of 400 test videos at 64 × 64 pixels, with RANDOM_STATE for the choice of the videos. Normalise
both sets with the mean and the standard deviation of the training pixels. Fix the randomness with
RANDOM_STATE and train the network of the course, CmrCNN, with two groups, normal and abnormal, for
15 epochs on shuffled batches of 32 training videos, with the Adam method, a learning rate of 0.003
and the cross-entropy loss. Then compute the probability of an abnormal EF for each test video and
the area under the ROC curve (AUC).
Constraints: Use only the data and the tools named here. The code must not read files, download
anything or install packages.
Output: Give the AUC, rounded to three decimals. Keep the result under the name `auc_echo` and print
it with a short label. Return only the code, as one block, with a short comment above each step.
Test: The training frames must be 1000 pairs of 64 × 64 pixels, and the AUC must lie between 0.5 and
1.
```

**Expected result:** `auc_echo`: a value between 0.6 and 1.0, which varies a little from computer to computer

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

### Ask for a review of a training loop

```text
Review the code below, which trains and evaluates a classifier of medical images. Check six points.
Is the split into training, validation and test sets made by patient? Does the normalisation use
statistics of the training images only? Is the network switched to training mode for learning and to
evaluation mode for measuring? Is the evaluation done without recording gradients? Does the output
layer fit the loss, with no softmax before a cross-entropy that applies its own? Does the reported
measure suit the classes and give one decision per patient? Answer with a short list, then return
the corrected code.

[paste the code here]
```

## Prompt path of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. Each step builds on the one before it, so the test of a step must hold before the next prompt is sent. The report lists all four prompts in the AI usage log.

### Step 1: Train the network

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: `X` holds 270 slices: the three middle short-axis slices of each of the 90 patients, each with
two frames of 64 × 64 pixels, the end-diastolic and the end-systolic one, with values from 0 to 1
and 2 mm per pixel. `y` holds the group of each slice (0 NOR, 1 DCM, 2 HCM), `patients` its patient
and `sets` its set: "train" (45 patients), "val" (15) or "test" (30). `CmrCNN` is the network of
Section 5: three blocks, each with a 3 × 3 convolution that keeps the size, batch normalisation,
ReLU and a 2 × 2 max pooling, with 8, 16 and 32 kernels on an input of two channels; then
flattening, dropout with a rate of 0.3 and a linear layer that turns 2048 values into 3 scores.
Task: Normalise X with the mean and the standard deviation of the training pixels, those whose set
is "train", and prepare the three sets for PyTorch. Fix the randomness with RANDOM_STATE and train
CmrCNN for 40 epochs with the Adam method, a learning rate of 0.003, the cross-entropy loss and
shuffled batches of 16 training slices. After each epoch, measure the validation loss without
learning from it and keep a copy of the weights with the lowest validation loss. Draw the training
and the validation loss against the epochs.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: The trained network with the kept weights and one figure of the two losses. Return only the
code, as one block, with a short comment above each step.
Test: Print the epoch with the lowest validation loss; after the kept weights are loaded, the
validation loss must have this lowest value again.
```

### Step 2: The confusion matrix of the network

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: The network of step 1, the prepared test slices of step 1, and y and patients of the slices;
the test slices are those whose set is "test".
Task: In evaluation mode and without recording gradients, compute the probabilities of the three
groups for the test slices, average them over the slices of each patient and take the group with the
largest mean as the decision. Report the confusion matrix of the 30 test patients with the groups
NOR, DCM and HCM, the precision, the recall and the F1 score of each group, and the macro F1.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: The confusion matrix as a table and a table of the three measures by group. Return only the
code, as one block, with a short comment above each step.
Test: The matrix must add up to 30, and each of its rows to 10.
```

### Step 3: The rules on the same patients

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: `acdc_table` is a table with the 90 patients of ACDC in the groups NOR (normal), DCM (dilated
cardiomyopathy) and HCM (hypertrophic cardiomyopathy), one row per patient. The columns used here
are group; split ("training" or "testing"); lv_ef, the left ventricular ejection fraction (%);
lv_edvi, the left ventricular end-diastolic volume indexed to the body surface area (mL/m²); and
max_wall_mm, the thickest segment of the wall at end-diastole (mm). All were measured on the expert
contours.
Task: Apply the rules of ACDC to the patients of acdc_table whose split is "testing": DCM if lv_ef
is below 40 and lv_edvi above 100; otherwise HCM if max_wall_mm is above 15 and lv_ef is 50 or more;
otherwise NOR. Report the confusion matrix of group against rule, in the order NOR, DCM, HCM, and
the accuracy.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: The confusion matrix as a table and the accuracy, rounded to three decimals. Return only the
code, as one block, with a short comment above each step.
Test: The matrix must add up to 30; on all 90 patients, the same rules must give the accuracy of
step 1.3.
```

### Step 4: The errors

```text
Role: You are helping a cardiologist who is new to programming.
Context: The code runs in the Jupyter notebook of Week 3, where the data below are already loaded.
The usual packages for tables, calculations and plots (pandas, NumPy and Matplotlib), the deep
learning package PyTorch, the machine learning package scikit-learn and the course package vclinic,
with its modules acdc and echonet, are available. RANDOM_STATE holds the fixed value that the
notebook uses wherever chance plays a part.
Data: The decisions of step 2 with the names of the test patients, acdc_table, and S, which holds
the three middle slices of every patient, their images of 64 × 64 pixels, their patients and their
phases ("ED" or "ES"); The tool acdc.slices of the course package prepared S for the groups NOR, DCM
and HCM. Another tool of the package, acdc.walls, receives the name of a patient and gives the
thickest wall of every slice at end-diastole in mm, from the base, slice 0, to the apex.
Task: For every test patient whose decision differs from the group, show the three end-diastolic
slices that the network saw, with the group, the decision and max_wall_mm in the title. Then print
the thickest wall of every slice of the examination, from the base to the apex.
Constraints: Use only the data and the tools named here. The code must not read files or install
packages.
Output: One figure for each misclassified patient and a list of the thickest wall by slice. Return
only the code, as one block, with a short comment above each step.
Test: The number of patients shown must equal the number of errors in the confusion matrix of step
2.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
