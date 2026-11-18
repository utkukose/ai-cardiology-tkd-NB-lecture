# Prompt library, Week 4

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 4](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-04/PROMPTLAR.md)

This library holds every prompt of the prompt path of Week 4, Part 1 of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the notebook, into the empty cell of the step of the same number, and runs there. The [guide to the prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [How a step works](#how-a-step-works)
2. [Stop 1: Learning from few patients with a network trained on photographs](#stop-1-learning-from-few-patients-with-a-network-trained-on-photographs)
3. [Stop 2: A U-Net on the echocardiograms of CAMUS](#stop-2-a-u-net-on-the-echocardiograms-of-camus)
4. [Stop 3: The ejection fraction by the method of discs](#stop-3-the-ejection-fraction-by-the-method-of-discs)
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

## Stop 1: Learning from few patients with a network trained on photographs

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-04/lecture.html#stop-1) · The same result on the Python path: Python step 4, Sections 1 to 4*

A network trained on more than a million photographs of ImageNet already knows edges, textures and shapes. In this stop EfficientNet-B0 is reused in two ways on the cardiomyopathy groups of ACDC: Its features feed a simple model, and the whole network is fine-tuned. Then only five patients per group are kept, to see how much the result depends on the patients that happen to be chosen.

### Step 1.1: Features of a network trained on photographs

**Goal.** Describe every slice with the 1280 features of EfficientNet-B0 and learn the three groups from them with a simple model.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: On the cine MR slices of the cardiomyopathy groups of ACDC, the cardiologist wants to know
how well the features of a network trained only on photographs separate normal hearts, dilated
cardiomyopathy and hypertrophic cardiomyopathy.
Data: The notebook holds a table named "data" with 270 short-axis slices of cine MR, the three
middle slices of each of the 90 patients of ACDC. Each row is a slice: "patient" gives the patient,
"group" the group of the patient ("NOR", "DCM" or "HCM") and "set" the set of the patient
("training", 45 patients, 15 of each group; "validation", 15 patients; "test", 30 patients). Each
cell of the column "image" holds the slice prepared for a network trained on photographs: three
colour channels (the end-diastolic frame, the end-systolic frame and their mean) of 128 × 128
pixels, normalised with the means and standard deviations of ImageNet.
Task: Use EfficientNet-B0 with its ImageNet weights, in evaluation mode. Pass the images of all
slices through the network in groups of 32, without recording gradients, and take the output of the
average pooling before its last layer: 1,280 numbers per slice, the features. Standardise the
features with the training slices and fit a logistic regression on the training slices. Then compute
the probabilities of the three groups for the test slices, average them over the three slices of
each test patient, and take the group with the largest mean as the decision for the patient.
Constraints: Use only this table. For the network, use only the ImageNet weights of EfficientNet-B0
that are already on this computer; no download is needed. The code must not read files, download
anything from the internet or install programs.
Output: Print the share of the 30 test patients whose decision equals their group with three
decimals, and keep it under the name "answer".
Test: The features must form a table of 270 rows and 1,280 columns, and there must be 30 test
patients.
```

**Expected result:** "answer" = 0.867

### Step 1.2: Fine-tuning the whole network

**Goal.** Let every layer of EfficientNet-B0 adapt to the slices, starting from the ImageNet weights. The training takes about a minute.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether adapting every layer of a network trained on
photographs to the cine MR slices of ACDC separates the three groups better than its features alone.
Data: The notebook holds a table named "data" with 270 short-axis slices of cine MR, the three
middle slices of each of the 90 patients of ACDC. Each row is a slice: "patient" gives the patient,
"group" the group of the patient ("NOR", "DCM" or "HCM") and "set" the set of the patient
("training", 45 patients, 15 of each group; "validation", 15 patients; "test", 30 patients). Each
cell of the column "image" holds the slice prepared for a network trained on photographs: three
colour channels (the end-diastolic frame, the end-systolic frame and their mean) of 128 × 128
pixels, normalised with the means and standard deviations of ImageNet.
Task: Start from EfficientNet-B0 with its ImageNet weights and replace its last layer with dropout
at a rate of 0.3 followed by a new linear layer with three outputs, one for each group. Train the
whole network on the training slices for 15 epochs, in shuffled groups of 16 slices, with a learning
rate of 0.001 and the cross-entropy loss. As data augmentation, turn every group of slices by a
random quarter turn. After every epoch, measure the loss on the validation slices without learning
from them, and keep the weights of the epoch with the lowest validation loss. Make the random
choices the same in every run by using the number 2026 as the starting value. Then decide for each
test patient as a clinic would: Average the probabilities of the three groups over the three slices
of the patient and take the group with the largest mean.
Constraints: Use only this table. For the network, use only the ImageNet weights of EfficientNet-B0
that are already on this computer; no download is needed. The code must not read files, download
anything from the internet or install programs.
Output: Print the epoch with the lowest validation loss and the share of the 30 test patients whose
decision equals their group, with three decimals; keep the share under the name "answer".
Test: After the kept weights are loaded, the validation loss must again have its lowest value.
```

**Expected result:** "answer" = 0.967

### Step 1.3: Five patients per group

**Goal.** See how much a result from few patients depends on which patients are chosen.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to see how much a result from only five patients per group depends
on which patients happen to be chosen.
Data: The notebook holds a table named "data" with 270 short-axis slices of cine MR, the three
middle slices of each of the 90 patients of ACDC. Each row is a slice: "patient" gives the patient,
"group" the group of the patient ("NOR", "DCM" or "HCM") and "set" the set of the patient
("training", 45 patients, 15 of each group; "validation", 15 patients; "test", 30 patients). The
other 1,280 columns, "f1" to "f1280", hold the features of the slice, the output of the average
pooling before the last layer of EfficientNet-B0, which was trained on the photographs of ImageNet.
Task: Choose five patients at random from each group of the training set, and repeat this choice
five times. Make the random choices the same in every run by using the number 2026 as the starting
value. For each choice, standardise the features with the slices of the 15 chosen patients only and
fit a logistic regression on these slices. Then compute the accuracy on the 30 test patients, with
one decision per patient: the group with the largest mean probability over the three slices of the
patient.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the five accuracies, and keep their mean, with three decimals, under the name
"answer".
Test: Every choice must hold 15 different patients, five of each group.
```

**Expected result:** "answer" = 0.62

## Stop 2: A U-Net on the echocardiograms of CAMUS

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-04/lecture.html#stop-2) · The same result on the Python path: Sections 5 to 7*

A segmentation network gives every pixel a label. In this stop the Dice coefficient is first computed by hand, on an outline shifted by a few pixels. Then a small U-Net learns the cavity of the left ventricle from 800 training frames of CAMUS and is measured on the 200 frames of the 50 test patients, by view and by phase.

### Step 2.1: The Dice coefficient by hand

**Goal.** See how much a small shift of an outline lowers the Dice coefficient.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to see how much a small shift of an outline lowers the Dice
coefficient, the usual measure of agreement between two outlines.
Data: The notebook holds a table named "data" with 96 rows and 96 columns: the expert outline of the
cavity of the left ventricle in the apical four-chamber frame at end-diastole of patient 201 of
CAMUS, resized to 96 × 96 pixels. Each cell is a pixel: 1 inside the cavity and 0 outside.
Task: Shift the cavity by 3 pixels to the right, that is, move every pixel 3 columns to the right.
Count the pixels of the original and of the shifted cavity and the pixels that the two share.
Compute the Dice coefficient: twice the shared pixels divided by the sum of the two counts.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the three counts, and keep the Dice coefficient, with three decimals, under the name
"answer".
Test: The Dice coefficient of the cavity with itself, without a shift, must be 1.
```

**Expected result:** "answer" = 0.877

### Step 2.2: Training the U-Net

**Goal.** Train a small U-Net to draw the cavity of the left ventricle and measure it on frames of patients it has never seen. The training takes about three minutes.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to train a small U-Net that outlines the cavity of the left
ventricle on the apical echocardiograms of CAMUS, and to measure it on patients that the network has
never seen.
Data: The notebook holds a table named "data" with 1,200 frames of CAMUS: the end-diastolic and
end-systolic frames of the apical two-chamber and four-chamber views of 300 patients. Each row is a
frame: "patient" gives the patient, "view" the view ("2CH" or "4CH"), "phase" the phase ("ED" or
"ES") and "set" the set of the patient ("training", 200 patients; "validation", 50 patients; "test",
50 patients). Each cell of the column "frame" holds the frame as an image of 96 × 96 pixels with
values from 0 to 1, and each cell of the column "cavity" the expert outline of the cavity of the
left ventricle at the same size: 1 inside the cavity and 0 outside.
Task: Build a small U-Net that gives two scores to every pixel, one for the cavity and one for the
rest. It has three levels down, a bottleneck and three levels up with skip connections. Every level
has two convolutions with 3 × 3 kernels that keep the size of the image, each followed by batch
normalisation and ReLU. On the way down, a 2 × 2 max pooling halves the image; on the way up, a 2 ×
2 transposed convolution doubles it, and the result is joined with the output of the same level on
the way down. The first level has 8 channels, and the number of channels doubles at every level
down, up to 64 in the bottleneck. A last 1 × 1 convolution gives the two scores. Train it on the
training frames for 15 epochs, in shuffled groups of 16 frames. The loss is the sum of the
cross-entropy and the soft Dice loss, which is one minus the Dice coefficient computed from the
probabilities of the cavity. Use a one-cycle learning rate with a highest value of 0.003. After
every epoch, compute the mean Dice coefficient of the validation frames, and keep the weights of the
epoch where it is highest. Make the random choices the same in every run by using the number 2026 as
the starting value. Then compute the probability of the cavity in every pixel of the test frames,
threshold it at 0.5 and compute the Dice coefficient of each test frame against its expert outline.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of trainable parameters, and keep the mean Dice coefficient of the 200 test
frames, with three decimals, under the name "answer".
Test: There must be 800 training frames and 200 test frames, and the network must have 121,394
trainable parameters.
```

**Expected result:** "answer" = 0.924

### Step 2.3: The Dice coefficient by view and phase

**Goal.** Find where the network draws worst, as an echocardiography laboratory would ask. The data cell trains the U-Net of the course once, which takes about three minutes.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: As an echocardiography laboratory would ask, the cardiologist wants to know in which view
and phase a U-Net outlines the cavity of the left ventricle worst.
Data: The notebook holds a table named "data" with the 200 test frames of CAMUS, the apical
two-chamber and four-chamber views of 50 patients at end-diastole and end-systole. Each row is a
frame: "patient" gives the patient, "view" the view ("2CH" or "4CH") and "phase" the phase ("ED" or
"ES"). Each cell of the column "probability" holds, for every pixel of the frame at 96 × 96 pixels,
the probability of the cavity of the left ventricle given by a U-Net, from 0 to 1. Each cell of the
column "cavity" holds the expert outline of the cavity at the same size: 1 inside the cavity and 0
outside.
Task: Threshold the probability of every frame at 0.5 and compute the Dice coefficient of the frame
against its expert cavity: twice the shared pixels divided by the sum of the pixels of the two.
Group the frames by view and phase, and print a small table with the number of frames and the mean
Dice coefficient of the four groups: 2CH ED, 2CH ES, 4CH ED and 4CH ES.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Keep the lowest of the four means, with three decimals, under the name "answer".
Test: Each of the four groups must hold 50 frames, and the mean of the four means must equal the
mean Dice coefficient of all 200 frames.
```

**Expected result:** "answer" = 0.908

## Stop 3: The ejection fraction by the method of discs

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-04/lecture.html#stop-3) · The same result on the Python path: Sections 8 and 9*

The outlines become numbers with the biplane method of discs, as in an echocardiography laboratory. In this stop the volumes and the ejection fraction (EF) of patient 201 are computed from the expert outlines, the network is compared with the expert on the 50 test patients with a Bland-Altman analysis, and the case is measured again with another convention for the thickness of the discs.

### Step 3.1: Patient 201 by the method of discs

**Goal.** Measure the case of the week from the outlines of the expert, as the reference of CAMUS does.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to compute the end-diastolic and end-systolic volumes and the
ejection fraction of patient 201 of CAMUS from the expert outlines by the biplane method of discs,
as in the reference of CAMUS.
Data: The notebook holds a table named "data" with the discs of the method of discs on the four
expert outlines of the cavity of the left ventricle of patient 201 of CAMUS: the apical two-chamber
(2CH) and four-chamber (4CH) views at end-diastole (ED) and end-systole (ES). Each outline is
divided into 20 discs perpendicular to its long axis, from the mitral annulus to the apex. Each row
is a disc: "view" and "phase" name the outline, "disc" gives its number from 1 to 20, "diameter" its
diameter in mm and "long axis" the length of the long axis of the outline in mm, the same for its 20
discs. The diameters and the lengths were measured at the original size of the frames, with the real
size of a pixel.
Task: Compute each volume by the biplane method of discs, V = π/4 × Σ (a_i × b_i) × h, where a_i is
the diameter of disc i in the 2CH outline, b_i that of the same disc in the 4CH outline of the same
phase, and h the thickness of a disc. As in the reference of CAMUS, use one thickness for both
phases, the longest of the four long axes divided by 20. Divide by 1,000 to turn mm³ into mL, round
each volume to a whole number of mL, and compute the EF from the rounded volumes as (EDV − ESV)/EDV
× 100.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print EDV and ESV in mL, and keep the EF, in percent with one decimal, under the name
"answer".
Test: EDV must be larger than ESV and lie between 50 and 300 mL.
```

**Expected result:** "answer" = 42.1

### Step 3.2: Agreement of the network with the expert

**Goal.** Compare the automatic EF with the expert's on the 50 test patients, as a laboratory would before using it. If the U-Net of the course is not yet in memory, the data cell trains it first, which takes about three minutes.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Before an automatic ejection fraction is used, the cardiologist wants to compare it with
the expert on the 50 test patients of CAMUS with a Bland-Altman analysis, as a laboratory would.
Data: The notebook holds a table named "data" with the 50 test patients of CAMUS. Each row is a
patient: "patient" gives the patient, "expert EF" the ejection fraction from the outlines of the
expert and "network EF" the ejection fraction from the outlines drawn by a U-Net, both in percent
and both by the biplane method of discs.
Task: Compute the difference of the EF for every patient, network minus expert, then the mean and
the standard deviation of the differences and the limits of agreement, the mean ± 1.96 standard
deviations. Draw a Bland-Altman plot: the difference against the mean of the two EFs, with
horizontal lines at the mean difference and at the two limits.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the standard deviation and the two limits of agreement, and keep the mean difference,
in percentage points with two decimals, under the name "answer".
Test: There must be 50 patients, and the expert EF of patient0201 must be 42.1 percent.
```

**Expected result:** "answer" = -4.24

### Step 3.3: Another convention for the thickness of the discs

**Goal.** See how much a convention of the software, not a border, changes the EF of the case.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to see how much the convention for the thickness of the discs, not a
border, changes the ejection fraction of patient 201.
Data: The notebook holds a table named "data" with the discs of the method of discs on the four
expert outlines of the cavity of the left ventricle of patient 201 of CAMUS: the apical two-chamber
(2CH) and four-chamber (4CH) views at end-diastole (ED) and end-systole (ES). Each outline is
divided into 20 discs perpendicular to its long axis, from the mitral annulus to the apex. Each row
is a disc: "view" and "phase" name the outline, "disc" gives its number from 1 to 20, "diameter" its
diameter in mm and "long axis" the length of the long axis of the outline in mm, the same for its 20
discs. The diameters and the lengths were measured at the original size of the frames, with the real
size of a pixel.
Task: Compute each volume by the biplane method of discs, V = π/4 × Σ (a_i × b_i) × h, where a_i is
the diameter of disc i in the 2CH outline, b_i that of the same disc in the 4CH outline of the same
phase, and h the thickness of a disc. This time, use a thickness for each phase, the longer of the
two long axes of that phase divided by 20. Divide by 1,000 to turn mm³ into mL, round each volume to
a whole number of mL, and compute the EF from the rounded volumes as (EDV − ESV)/EDV × 100. For
comparison, also compute EDV with one thickness for both phases, from the longest of the four long
axes.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print EDV and ESV in mL, and keep the EF, in percent with one decimal, under the name
"answer".
Test: The two EDVs must be equal, because at end-diastole both conventions use the same long axis.
```

**Expected result:** "answer" = 50.3

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

### Ask for a review of a measurement pipeline

```text
Review the code below, which measures volumes and an ejection fraction from echocardiograms. Check
six points. Are the training, validation and test sets split by patient? Are the masks resized
without creating new labels, with the nearest label or through probabilities? Do the volumes use the
real size of a pixel in mm? Is the Dice coefficient also given by view and by phase? Which rule
gives the volumes, and with which thickness of the discs? Is the agreement reported with the mean
difference and the limits of agreement, not with a correlation alone? For every problem, show the
line, explain the cause and give the corrected code.

[paste the code here]
```

## Prompt path of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. The section *Weekly project on the prompt path* at the end of Part 1 of the Jupyter notebook prepares the table of each prompt. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Step 1: Train the U-Net and measure its outlines

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to train a U-Net that outlines the cavity of the left ventricle on
the echocardiograms of CAMUS, and to see where it draws worse: by view, by phase and by image
quality.
Data: The notebook holds a table named "data" with 1,200 frames of CAMUS: the end-diastolic and
end-systolic frames of the apical two-chamber and four-chamber views of 300 patients. Each row is a
frame: "patient" gives the patient, "view" the view ("2CH" or "4CH"), "phase" the phase ("ED" or
"ES"), "set" the set of the patient ("training", 200 patients; "validation", 50 patients; "test", 50
patients) and "image quality" the quality of the view of the patient that the authors gave ("good",
"medium" or "poor"). Each cell of the column "frame" holds the frame as an image of 96 × 96 pixels
with values from 0 to 1, and each cell of the column "cavity" the expert outline of the cavity of
the left ventricle at the same size: 1 inside the cavity and 0 outside.
Task: Build a small U-Net that gives two scores to every pixel, one for the cavity and one for the
rest. It has three levels down, a bottleneck and three levels up with skip connections. Every level
has two convolutions with 3 × 3 kernels that keep the size of the image, each followed by batch
normalisation and ReLU. On the way down, a 2 × 2 max pooling halves the image; on the way up, a 2 ×
2 transposed convolution doubles it, and the result is joined with the output of the same level on
the way down. The first level has 8 channels, and the number of channels doubles at every level
down, up to 64 in the bottleneck. A last 1 × 1 convolution gives the two scores. Train it on the
training frames for 15 epochs, in shuffled groups of 16 frames. The loss is the sum of the
cross-entropy and the soft Dice loss, which is one minus the Dice coefficient computed from the
probabilities of the cavity. Use a one-cycle learning rate with a highest value of 0.003. After
every epoch, compute the mean Dice coefficient of the validation frames, and keep the weights of the
epoch where it is highest. Make the random choices the same in every run by using the number 2026 as
the starting value. Then threshold the probability of the cavity in the test frames at 0.5 and
compute the Dice coefficient of every test frame against its expert outline. Report its mean by view
and phase and by image quality.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table of the mean Dice coefficient by view and phase and a second table by image
quality, and keep the mean Dice coefficient of the 200 test frames, with three decimals, under the
name "answer".
Test: Each of the four groups of view and phase must hold 50 test frames, and the mean Dice
coefficient of the 200 test frames must lie between 0.85 and 0.97.
```

### Step 2: Volumes, EF and Bland-Altman

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: Before automatic volumes and an automatic ejection fraction are used, the cardiologist
wants to compare all three with the expert on the 50 test patients of CAMUS.
Data: The notebook holds a table named "data" with the 50 test patients of CAMUS. Each row is a
patient: "patient" gives the patient; "expert EDV" and "network EDV" give the end-diastolic volume
and "expert ESV" and "network ESV" the end-systolic volume in mL; "expert EF" and "network EF" give
the ejection fraction in percent. The values of the expert come from the outlines of the expert,
those of the network from the outlines drawn by a U-Net, all by the biplane method of discs.
Task: For each of the three measurements, EDV, ESV and the EF, compute the difference for every
patient, network minus expert, then the mean difference, the standard deviation of the differences
and the limits of agreement, the mean ± 1.96 standard deviations. Draw a Bland-Altman plot for each
measurement: the difference against the mean of the two values, with horizontal lines at the mean
difference and at the two limits.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row per measurement and the columns mean difference, standard
deviation, lower limit and upper limit, and the three Bland-Altman plots; keep the mean difference
of the EF, with two decimals, under the name "answer".
Test: There must be 50 patients, and the expert EF of patient0201 must be 42.1 percent.
```

### Step 3: The ranges of EF

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know for how many of the 50 test patients the network and the
expert place the ejection fraction in the same clinical range.
Data: The notebook holds a table named "data" with the 50 test patients of CAMUS. Each row is a
patient: "patient" gives the patient; "expert EDV" and "network EDV" give the end-diastolic volume
and "expert ESV" and "network ESV" the end-systolic volume in mL; "expert EF" and "network EF" give
the ejection fraction in percent. The values of the expert come from the outlines of the expert,
those of the network from the outlines drawn by a U-Net, all by the biplane method of discs.
Task: Sort each EF, that of the expert and that of the network, into three ranges: 40 percent or
less, above 40 and below 50 percent, and 50 percent or more. Make a cross table with the range of
the expert in the rows and the range of the network in the columns, in the order of the ranges, and
count the patients on its diagonal.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the cross table, and keep the number of patients on its diagonal under the name
"answer".
Test: The cross table must add up to 50 patients.
```

### Step 4: The largest errors

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: For the test patients whose automatic ejection fraction differs most from the expert, the
cardiologist wants to see the frames and the two outlines, to judge where the network went wrong.
Data: The notebook holds a table named "data" with the 200 test frames of CAMUS, four for each of
the 50 test patients. Each row is a frame: "patient" gives the patient, "view" the view ("2CH" or
"4CH"), "phase" the phase ("ED" or "ES") and "image quality" the quality of the view ("good",
"medium" or "poor"). Each cell of the column "frame" holds the frame as an image of 96 × 96 pixels;
"expert cavity" and "network cavity" hold the cavity of the left ventricle at the same size as drawn
by the expert and by a U-Net, 1 inside the cavity and 0 outside. "expert EF" and "network EF" give
the ejection fraction of the patient in percent, the same on the four rows of a patient.
Task: Find the three patients with the largest absolute difference between the two EFs. For each of
them, show its four frames with the outline of the expert cavity and that of the network cavity
drawn on the frame in two colours, and write the two EFs and the image quality in the title.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show one figure of four frames for each of the three patients, and keep the largest absolute
difference of the EF, in percentage points with one decimal, under the name "answer".
Test: The three patients shown must be those with the three largest absolute differences of the EF,
and each figure must hold four frames.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
