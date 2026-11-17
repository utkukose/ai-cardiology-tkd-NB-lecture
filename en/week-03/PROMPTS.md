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
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: `acdc_table` is a pandas DataFrame with the 90 patients of ACDC in the groups NOR (normal),
DCM (dilated cardiomyopathy) and HCM (hypertrophic cardiomyopathy), one row per patient. The columns
used here: group, split ("training" or "testing"), lv_ef (left ventricular ejection fraction, %),
lv_edvi (left ventricular end-diastolic volume indexed to body surface area, mL/m²) and max_wall_mm
(thickest wall segment at end-diastole, mm), all measured on the expert contours.
Task: Compute the mean of lv_ef for each group with groupby and print the three means, rounded to
one decimal.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The mean EF of the group DCM, rounded to one decimal. Save it in a variable named
`mean_ef_dcm` and print it with a short label. Return only the code, in one block, with a short
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
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: `gt_ed` and `gt_es` are NumPy arrays with the expert contours of patient 134 at end-diastole
and at end-systole, one value per voxel: 0 background, 1 right ventricular cavity, 2 myocardium, 3
left ventricular cavity. `spacing` holds the size of one voxel in mm as (x, y, z).
Task: Count the voxels with the value 3 in gt_ed and in gt_es. Multiply each count by the volume of
one voxel, the product of the three values of spacing in mm³, and divide by 1000 to get mL. Compute
the end-diastolic volume EDV, the end-systolic volume ESV and the EF as (EDV − ESV)/EDV × 100.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The EF in percent, rounded to one decimal; print EDV and ESV in mL as well. Save it in a
variable named `ef_case` and print it with a short label. Return only the code, in one block, with a
short comment above each step.
Test: EDV must be larger than ESV and lie between 50 and 300 mL.
```

**Expected result:** `ef_case` = 62.2

### Step 1.3: The rules of ACDC on every patient

**Goal.** Classify the 90 patients with the definitions of ACDC and see where the measurements alone go wrong.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: `acdc_table` is a pandas DataFrame with the 90 patients of ACDC in the groups NOR (normal),
DCM (dilated cardiomyopathy) and HCM (hypertrophic cardiomyopathy), one row per patient. The columns
used here: group, split ("training" or "testing"), lv_ef (left ventricular ejection fraction, %),
lv_edvi (left ventricular end-diastolic volume indexed to body surface area, mL/m²) and max_wall_mm
(thickest wall segment at end-diastole, mm), all measured on the expert contours.
Task: Apply the rules of ACDC to every row: DCM if lv_ef < 40 and lv_edvi > 100; otherwise HCM if
max_wall_mm > 15 and lv_ef >= 50; otherwise NOR. Store the result in a new column rule, print the
crosstab of group and rule, and compute the share of patients whose rule equals their group.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The share, rounded to three decimals. Save it in a variable named `rule_accuracy` and print
it with a short label. Return only the code, in one block, with a short comment above each step.
Test: The crosstab must hold 90 patients in total, and the share must lie between 0 and 1.
```

**Expected result:** `rule_accuracy` = 0.967

## Stop 2: A first convolutional network

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html#stop-2) · The same result on the Python path: Sections 4 to 7*

The network of the course learns the three groups from the pixels of the middle slices, with the end-diastolic and the end-systolic frame of each slice as two channels. In this stop the slices are normalised, the network is built, trained with early stopping and judged patient by patient on the 30 test patients.

### Step 2.1: Normalising with the training slices

**Goal.** Prepare the tensors of the network with statistics that come from the training patients alone.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: `X` is a NumPy array of shape (270, 2, 64, 64): the three middle short-axis slices of each of
the 90 patients, with values from 0 to 1 and 2 mm per pixel. Channel 0 is the end-diastolic and
channel 1 the end-systolic frame of the slice. `y` holds the class of each slice (0 NOR, 1 DCM, 2
HCM), `patients` the patient of each slice and `sets` its set: "train" (45 patients), "val" (15
patients) or "test" (30 patients).
Task: Compute the mean and the SD of all pixels of the training slices (sets == "train"). Normalise
all slices with them, as (X − mean)/SD. Make the float tensors X_train, X_val and X_test and the
long tensors y_train, y_val and y_test for the three sets.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The mean of the training pixels, rounded to four decimals. Keep the six tensors, because the
next steps use them. Save it in a variable named `train_mean` and print it with a short label.
Return only the code, in one block, with a short comment above each step.
Test: X_train must have the shape (135, 2, 64, 64), and the normalised training pixels must have a
mean of about 0 and an SD of about 1.
```

**Expected result:** `train_mean` = 0.2961

### Step 2.2: The network and its parameters

**Goal.** Build the network of the course and count its weights.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: The float tensors `X_train`, `X_val` and `X_test` and the long tensors `y_train`, `y_val` and
`y_test` of step 2.1: the slices normalised with the mean and the SD of the training pixels, and
their classes. `patients` and `sets` hold the patient and the set of each slice.
Task: Define a class CmrCNN(nn.Module) with three blocks. Each block is nn.Conv2d with a 3 × 3
kernel and padding 1, nn.BatchNorm2d, nn.ReLU and nn.MaxPool2d(2); the channels go from 2 to 8, 16
and 32. After the blocks come nn.Flatten(), nn.Dropout(0.3) and nn.Linear(32 * 8 * 8, 3). Create
model = CmrCNN() and count its trainable parameters.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The number of trainable parameters as an integer. Keep the class CmrCNN and the object
model. Save it in a variable named `n_params` and print it with a short label. Return only the code,
in one block, with a short comment above each step.
Test: The model applied to X_train[:4] must return a tensor of shape (4, 3).
```

**Expected result:** `n_params` = 12219

### Step 2.3: Training with early stopping and a decision per patient

**Goal.** Train the network and judge it as a clinic would: one decision for each patient.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: The float tensors `X_train`, `X_val` and `X_test` and the long tensors `y_train`, `y_val` and
`y_test` of step 2.1: the slices normalised with the mean and the SD of the training pixels, and
their classes. `patients` and `sets` hold the patient and the set of each slice.
Task: After torch.manual_seed(RANDOM_STATE), train model for 40 epochs with
torch.optim.Adam(model.parameters(), lr=0.003, weight_decay=1e-4), F.cross_entropy and mini-batches
of 16 shuffled training slices. After each epoch, compute the loss on X_val and y_val in evaluation
mode without gradients, and keep a copy of the weights of the epoch with the lowest validation loss.
At the end, load these weights, compute the softmax probabilities of X_test in evaluation mode,
average them over the slices of each test patient and take the class with the highest mean
probability as the decision for the patient.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The share of test patients whose decision equals their class, rounded to three decimals.
Save the mean probabilities of the patients in patient_prob, their classes in patient_true and the
decisions in patient_pred, as NumPy arrays in the order of sorted patient names. Save it in a
variable named `patient_accuracy` and print it with a short label. Return only the code, in one
block, with a short comment above each step.
Test: There must be 30 test patients, and each row of patient_prob must add up to 1.
```

**Expected result:** `patient_accuracy` = 0.933

### Step 2.4: The confusion matrix and the macro F1

**Goal.** Read the result class by class and find the patients that the network misses.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: `patient_true` and `patient_pred` of step 2.3: the classes and the decisions of the 30 test
patients (0 NOR, 1 DCM, 2 HCM), and `patient_prob`, their mean probabilities.
Task: Compute the confusion matrix of patient_true and patient_pred with confusion_matrix(...,
labels=[0, 1, 2]) and print it with the row and column names NOR, DCM and HCM. Compute the macro F1
with f1_score(..., average="macro").
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The macro F1, rounded to three decimals. Save it in a variable named `macro_f1` and print it
with a short label. Return only the code, in one block, with a short comment above each step.
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
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: `echo` is the participant's own copy of EchoNet-Dynamic. `echonet.file_list(echo)` returns
FileList.csv as a pandas DataFrame with one row per video; the columns used here: FileName, EF
(ejection fraction, %) and Split ("TRAIN", "VAL" or "TEST").
`echonet.frame_pairs(echo, split=..., n=..., size=64, seed=...)` returns a dictionary: images, an
array of shape (n, 2, 64, 64) with the traced end-diastolic and end-systolic frames of n videos of
the split as two channels and values from 0 to 1, and abnormal, 1 when the EF is below 50 percent.
Task: Get the table of the videos with echonet.file_list(echo), print the number of videos in each
value of Split and the total number of videos.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The total number of videos as an integer. Save it in a variable named `n_videos` and print
it with a short label. Return only the code, in one block, with a short comment above each step.
Test: The three sets must hold 7465, 1288 and 1277 videos.
```

**Expected result:** `n_videos`: 10030 for a complete copy

### Step 3.2: The share of abnormal EF

**Goal.** Know how common the abnormal class is before judging a model.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: `echo` is the participant's own copy of EchoNet-Dynamic. `echonet.file_list(echo)` returns
FileList.csv as a pandas DataFrame with one row per video; the columns used here: FileName, EF
(ejection fraction, %) and Split ("TRAIN", "VAL" or "TEST").
`echonet.frame_pairs(echo, split=..., n=..., size=64, seed=...)` returns a dictionary: images, an
array of shape (n, 2, 64, 64) with the traced end-diastolic and end-systolic frames of n videos of
the split as two channels and values from 0 to 1, and abnormal, 1 when the EF is below 50 percent.
Task: Select the videos whose Split is "TEST" and compute the share of them with an EF below 50.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The share, rounded to three decimals. Save it in a variable named `share_low_ef` and print
it with a short label. Return only the code, in one block, with a short comment above each step.
Test: The share must lie between 0 and 1, and the number of test videos must be 1277.
```

**Expected result:** `share_low_ef`: the value of the ready code on your copy

### Step 3.3: The network of the course on echocardiography

**Goal.** Train the same network on the end-diastolic and end-systolic frames of the videos and measure how well it recognises an abnormal EF.

```text
Role: You are helping a cardiologist who does not write code. The code you write will be pasted into
a cell of a Jupyter notebook and run there.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: `echo` is the participant's own copy of EchoNet-Dynamic. `echonet.file_list(echo)` returns
FileList.csv as a pandas DataFrame with one row per video; the columns used here: FileName, EF
(ejection fraction, %) and Split ("TRAIN", "VAL" or "TEST").
`echonet.frame_pairs(echo, split=..., n=..., size=64, seed=...)` returns a dictionary: images, an
array of shape (n, 2, 64, 64) with the traced end-diastolic and end-systolic frames of n videos of
the split as two channels and values from 0 to 1, and abnormal, 1 when the EF is below 50 percent.
Task: Load the frame pairs of 1000 training videos and 400 test videos with
echonet.frame_pairs(echo, split="TRAIN", n=1000, size=64, seed=RANDOM_STATE) and the same with
split="TEST" and n=400. Normalise both with the mean and the SD of the training pixels. After
torch.manual_seed(RANDOM_STATE), train CmrCNN(n_classes=2) for 15 epochs with torch.optim.Adam (lr
0.003), F.cross_entropy and mini-batches of 32 shuffled training videos, with abnormal as the label.
Then compute the softmax probability of the class 1 on the test videos in evaluation mode without
gradients and its AUC with roc_auc_score.
Constraints: Use only the packages and the variables named here. Do not read files, do not download
anything and do not install packages.
Output: The AUC, rounded to three decimals. Save it in a variable named `auc_echo` and print it with
a short label. Return only the code, in one block, with a short comment above each step.
Test: The training images must have the shape (1000, 2, 64, 64), and the AUC must lie between 0.5
and 1.
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
Review the PyTorch code below, which trains and evaluates a classifier of medical images. Check six
things: whether the split into training, validation and test sets is made by patient, whether the
normalisation uses statistics of the training images only, whether model.train() and model.eval()
are called at the right places, whether the evaluation runs inside torch.no_grad(), whether the
output layer fits the loss (no softmax before F.cross_entropy), and whether the measure reported
suits the classes and gives one decision per patient. Answer with a short list, then return the
corrected code.

[paste the code here]
```

## Prompt path of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. Each step builds on the one before it, so the test of a step must hold before the next prompt is sent. The report lists all four prompts in the AI usage log.

### Step 1: Train the network

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: `X` is a NumPy array of shape (270, 2, 64, 64): the three middle short-axis slices of each of
the 90 patients, with the ED frame in channel 0 and the end-systolic (ES) frame in channel 1, values
from 0 to 1, 2 mm per pixel. `y` holds the class of each slice (0 NOR, 1 DCM, 2 HCM), `patients` its
patient and `sets` its set: "train" (45 patients), "val" (15) or "test" (30). `CmrCNN` is the class
of Section 5: three blocks of Conv2d (3 × 3, padding 1), BatchNorm2d, ReLU and MaxPool2d(2) with 8,
16 and 32 channels on an input of 2 channels, then Flatten, Dropout(0.3) and Linear(2048, 3).
Task: Normalise `X` with the mean and the SD of the training pixels (`sets == "train"`) and turn the
three sets into float tensors of shape (n, 2, 64, 64) with long tensors of their classes. After
`torch.manual_seed(RANDOM_STATE)`, train `CmrCNN()` for 40 epochs with Adam (learning rate 0.003),
`F.cross_entropy` and mini-batches of 16 shuffled training slices. After each epoch, compute the
validation loss in evaluation mode without gradients and keep a copy of the weights with the lowest
validation loss. Plot the training and the validation loss per epoch.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The trained model with the kept weights and one figure of the two losses. Return only the
code in one block, with a short comment above each step.
Test: Print the epoch with the lowest validation loss; after the kept weights are loaded, the
validation loss must have that lowest value again.
```

### Step 2: The confusion matrix of the network

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: The model of step 1, the test tensor of step 1, and `y` and `patients` of the slices, where
`sets == "test"` marks the test slices.
Task: In evaluation mode and inside `torch.no_grad()`, compute the softmax probabilities of the test
slices, average them over the slices of each patient and take the class with the largest mean as the
decision. Report the confusion matrix of the 30 test patients with the classes NOR, DCM and HCM, the
precision, the recall and the F1 of each class and the macro F1.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The confusion matrix as a pandas DataFrame and a table of the three measures by class.
Return only the code in one block, with a short comment above each step.
Test: The matrix must add up to 30, and each of its rows to 10.
```

### Step 3: The rules on the same patients

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: `acdc_table` is a pandas DataFrame with the 90 patients of ACDC in the groups NOR (normal),
DCM (dilated cardiomyopathy) and HCM (hypertrophic cardiomyopathy), one row per patient. The columns
used here: group, split ("training" or "testing"), lv_ef (left ventricular ejection fraction, %),
lv_edvi (left ventricular end-diastolic volume indexed to body surface area, mL/m²) and max_wall_mm
(thickest wall segment at end-diastole, mm), all measured on the expert contours.
Task: Apply the rules of ACDC to the rows of `acdc_table` whose split is "testing": DCM if lv_ef <
40 and lv_edvi > 100; otherwise HCM if max_wall_mm > 15 and lv_ef >= 50; otherwise NOR. Report the
confusion matrix of group against rule with the classes in the order NOR, DCM, HCM, and the
accuracy.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The confusion matrix as a pandas DataFrame and the accuracy, rounded to three decimals.
Return only the code in one block, with a short comment above each step.
Test: The matrix must add up to 30; on all 90 patients, the same rules must give the accuracy of
Step 1.3.
```

### Step 4: The errors

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd, matplotlib.pyplot as
plt, torch, torch.nn as nn and torch.nn.functional as F, and copy. From scikit-learn, these are
imported: confusion_matrix, f1_score, accuracy_score and roc_auc_score. The course package vclinic
is imported with its modules acdc and echonet, and read_nifti from vclinic.nifti. RANDOM_STATE =
2026.
Data: The decisions of step 2 with the names of the test patients, `acdc_table` and
`S = acdc.slices(("NOR", "DCM", "HCM"))`, a dictionary with the arrays images (n, 64, 64), patient
and phase ("ED" or "ES") of the three middle slices of every patient. `acdc.walls(name)` returns a
dictionary with the thickest wall of every slice of the patient at ED in mm, from the base (slice 0)
to the apex.
Task: For every test patient whose decision differs from the class, show the three ED slices that
the network saw, with the class, the decision and max_wall_mm in the title. Then print the thickest
wall of every slice of the examination, from the base to the apex.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure for each misclassified patient and a list of the thickest wall per slice. Return
only the code in one block, with a short comment above each step.
Test: The number of patients shown must equal the number of errors in the confusion matrix of step
2.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
