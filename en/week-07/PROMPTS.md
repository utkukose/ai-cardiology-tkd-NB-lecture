# Prompt library, Week 7

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 7](README.md) · [Türkçe](../../tr/hafta-07/PROMPTLAR.md)

This library holds every prompt of the practice stops of Week 7, from the parts *Prompt and application* of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the Jupyter notebook, into the empty cell under the prompt of the same number, and runs there.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [Working with a prompt](#working-with-a-prompt)
2. [Stop 1: Transfer to echocardiography: A quality gate and the mini project](#stop-1-transfer-to-echocardiography-a-quality-gate-and-the-mini-project)
3. [Stop 2: Stenoses on synthetic and on real angiograms](#stop-2-stenoses-on-synthetic-and-on-real-angiograms)
4. [Stop 3: A convolutional network, a vision transformer and a hybrid](#stop-3-a-convolutional-network-a-vision-transformer-and-a-hybrid)
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

## Stop 1: Transfer to echocardiography: A quality gate and the mini project

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#stop-1) · Jupyter notebook: «Stop 1 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-07/NB07_vision_transformers.ipynb#scrollTo=stop-1-prompt)*

A vision transformer pretrained on photographs, ViT-B/16, turns every echocardiography frame of CAMUS into 768 numbers, and a logistic regression learns from them which frames the experts rated as poor. The same gate is built from four simple image statistics and from the convolutional network of Week 4, EfficientNet-B0, and Prompt 1.4 asks how sure the difference between the two networks is with 50 test patients. Prompt 1.5 is the mini project of the session: A mini vision transformer learns the photographs of CIFAR-10 and then a reduced ejection fraction from pairs of echocardiography frames of EchoNet-Dynamic or CAMUS.

### Prompt 1.1: A gate from four image statistics

**Goal.** Build a first quality gate from four numbers that describe the brightness, the contrast and the sharpness of a frame.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to flag echocardiography frames of poor quality before an automatic
measurement of the ejection fraction, and starts with four simple numbers of each frame.
Data: The notebook holds a table named "data" with 600 apical echocardiography frames of CAMUS, a
public data set: the end-diastolic frames of the two-chamber and of the four-chamber views of 300
patients. Each row is a frame: "set" gives the set of the patient ("training", 200 patients;
"validation", 50 patients; "test", 50 patients), "patient" the patient, "view" the view ("2CH" or
"4CH") and "quality" the image quality given by the experts of CAMUS ("good", "medium" or "poor").
Each cell of the column "frame" holds the frame as an image of 224 × 224 pixels with grey values
from 0 to 1.
Task: For every frame compute four numbers: the mean of its grey values, their standard deviation,
the mean absolute difference between vertically neighbouring pixels, and the share of pixels
brighter than half of the brightest pixel of the frame. The target is 1 for a frame of poor quality
and 0 otherwise. Standardise the features with the training frames. Fit a logistic regression on the
training frames with each of the inverse regularisation strengths 0.001, 0.01, 0.1 and 1, keep the
one with the largest area under the ROC curve (AUC) on the validation frames, and compute the AUC of
its probabilities on the test frames.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the chosen strength and the validation and test AUC, and keep the test AUC, with three
decimals, under the name "answer".
Test: The AUC must lie between 0 and 1, and the test frames must not be used before the last step.
```

**Expected result:** "answer" = 0.704

### Prompt 1.2: The class token of a vision transformer

**Goal.** Describe every frame by the 768 numbers of the class token of ViT-B/16, pretrained on ImageNet, and build the gate on them.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether a vision transformer that learned from millions of
photographs, and never saw an echocardiogram, can describe frames well enough to flag those of poor
quality.
Data: The notebook holds a table named "data" with 600 apical echocardiography frames of CAMUS, a
public data set: the end-diastolic frames of the two-chamber and of the four-chamber views of 300
patients. Each row is a frame: "set" gives the set of the patient ("training", 200 patients;
"validation", 50 patients; "test", 50 patients), "patient" the patient, "view" the view ("2CH" or
"4CH") and "quality" the image quality given by the experts of CAMUS ("good", "medium" or "poor").
Each cell of the column "frame" holds the frame as an image of 224 × 224 pixels with grey values
from 0 to 1.
Task: Use the vision transformer ViT-B/16 with its ImageNet weights, without its last layer, so that
it returns the class token of its last layer, 768 numbers for each frame. Give it every frame as an
image of 224 × 224 pixels with the same grey values in its three colour channels, scaled with the
mean and the standard deviation of ImageNet: Subtract 0.485, 0.456 and 0.406 from the three channels
and divide them by 0.229, 0.224 and 0.225. Pass the frames through the network in groups of 16, in
evaluation mode and without recording gradients. Then use the 768 numbers as the features of the
gate. The target is 1 for a frame of poor quality and 0 otherwise. Standardise the features with the
training frames. Fit a logistic regression on the training frames with each of the inverse
regularisation strengths 0.001, 0.01, 0.1 and 1, keep the one with the largest area under the ROC
curve (AUC) on the validation frames, and compute the AUC of its probabilities on the test frames.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the chosen strength and the validation and test AUC, and keep the test AUC, with three
decimals, under the name "answer".
Test: Every frame must give 768 numbers, and the AUC must lie between 0 and 1.
```

**Expected result:** "answer" = 0.862

### Prompt 1.3: The features of a convolutional network

**Goal.** Build the same gate on the 1,280 features of EfficientNet-B0, the network of Week 4.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to compare a vision transformer with the convolutional network used
in Week 4 as the source of features for a quality gate on echocardiography frames.
Data: The notebook holds a table named "data" with 600 apical echocardiography frames of CAMUS, a
public data set: the end-diastolic frames of the two-chamber and of the four-chamber views of 300
patients. Each row is a frame: "set" gives the set of the patient ("training", 200 patients;
"validation", 50 patients; "test", 50 patients), "patient" the patient, "view" the view ("2CH" or
"4CH") and "quality" the image quality given by the experts of CAMUS ("good", "medium" or "poor").
Each cell of the column "frame" holds the frame as an image of 224 × 224 pixels with grey values
from 0 to 1.
Task: Use the convolutional network EfficientNet-B0 with its ImageNet weights, without its last
layer, so that it returns the output of its average pooling, 1,280 numbers for each frame. Give it
every frame as an image of 224 × 224 pixels with the same grey values in its three colour channels,
scaled with the mean and the standard deviation of ImageNet: Subtract 0.485, 0.456 and 0.406 from
the three channels and divide them by 0.229, 0.224 and 0.225. Pass the frames through the network in
groups of 16, in evaluation mode and without recording gradients. Then use the 1,280 numbers as the
features of the gate. The target is 1 for a frame of poor quality and 0 otherwise. Standardise the
features with the training frames. Fit a logistic regression on the training frames with each of the
inverse regularisation strengths 0.001, 0.01, 0.1 and 1, keep the one with the largest area under
the ROC curve (AUC) on the validation frames, and compute the AUC of its probabilities on the test
frames.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the chosen strength and the validation and test AUC, and keep the test AUC, with three
decimals, under the name "answer".
Test: Every frame must give 1,280 numbers, and the AUC must lie between 0 and 1.
```

**Expected result:** "answer" = 0.782

### Prompt 1.4: How sure is the difference?

**Goal.** Draw the 50 test patients again and again with replacement and see how often the vision transformer wins.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether the difference between two quality gates for
echocardiography, measured on the frames of 50 test patients, would hold on other patients.
Data: The notebook holds a table named "data" with the 100 test frames of CAMUS, a public data set
of apical echocardiograms: the end-diastolic frames of the two-chamber and of the four-chamber views
of 50 patients. Each row is a frame: "patient" gives the patient, "view" the view ("2CH" or "4CH"),
"poor" is 1 when the experts of CAMUS rated the image quality as poor and 0 otherwise, and the two
columns "probability, ViT-B/16" and "probability, EfficientNet-B0" give the probability of poor
quality from two quality gates of the course, logistic regressions on the features of two networks
pretrained on ImageNet.
Task: Compute the AUC of both columns of probabilities against the column "poor". Then draw 2,000
bootstrap samples: Each sample draws 50 patients from the 50 test patients with replacement and
keeps both frames of every patient drawn. Fix the random seed to 2026 so that the result can be
repeated. In every sample that contains frames of both kinds, compute the AUC of both gates and the
difference, ViT-B/16 minus EfficientNet-B0. Report the mean difference, its 95 percent interval from
the 2.5th to the 97.5th percentile, and the share of samples in which the difference is above 0.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the two AUCs, the mean difference and its interval, and keep the share, with three
decimals, under the name "answer".
Test: The share must lie between 0 and 1, and the two frames of a patient must always be drawn
together.
```

**Expected result:** "answer" = 0.925

### Prompt 1.5: Mini project: A mini vision transformer from CIFAR-10 to echocardiography

**Goal.** Train a small vision transformer on the photographs of CIFAR-10, then fine-tune it on pairs of echocardiography frames to recognise a reduced ejection fraction, and compare it with the same network trained on the echocardiograms alone.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether a small vision transformer that first learned from
everyday photographs recognises a reduced ejection fraction on echocardiograms better than the same
network that learned from the echocardiograms alone.
Data: The notebook holds a table named "data" with two kinds of rows. The rows whose "source" is
"CIFAR-10" are the 60,000 colour photographs of CIFAR-10, a public data set of ten everyday classes
such as airplanes, cats and ships: "set" gives "training" (50,000 photographs) or "test" (10,000),
each cell of "image" holds a photograph as an array of 32 × 32 × 3 numbers from 0 to 255, and
"class" gives its class as a number from 0 to 9. The rows whose "source" is "echo" are pairs of
apical echocardiography frames of EchoNet-Dynamic or of CAMUS, two public data sets: "set" gives
"training", "validation" or "test", "patient" the patient or the video, each cell of "image" holds
an array of 32 × 32 × 3 numbers whose three channels are the end-diastolic frame and the
end-systolic frame, with values from 0 to 1, and their difference, with values from −1 to 1, and
"reduced EF" is 1 when the ejection fraction is below 50 percent and 0 otherwise.
Task: Build a small vision transformer for colour images of 32 × 32 pixels. Cut the image into 64
squares of 4 × 4 pixels and map every square to 64 numbers with the same learned linear map. Put a
learned class token of 64 numbers before the 64 tokens and add learned positions, one vector of 64
numbers for each of the 65 places, started from small random numbers with a standard deviation of
0.02. Pass the tokens through four transformer blocks. In each block, layer normalisation is
followed by self-attention with four heads, whose output is added to the input of the block; a
second layer normalisation is followed by a feed-forward network with a hidden layer of 128 units
and the GELU activation, whose output is added again. At the end, take the class token, apply layer
normalisation and a linear layer with ten outputs, the scores of the ten classes. Train it on the
CIFAR-10 rows of the training set: Divide the photographs by 255 and standardise each colour channel
with the mean and the standard deviation of the training photographs. Train for 5 epochs in shuffled
groups of 128 photographs with the cross-entropy loss and the AdamW optimiser with a learning rate
of 0.001 and a weight decay of 0.05. Move every group by a random shift of up to 4 pixels in each
direction, with the borders filled by reflection, and mirror it from left to right with a
probability of one half. Fix the random seed to 2026 so that the result can be repeated. Compute the
accuracy on the 10,000 test photographs. Then make two networks for the echocardiography rows, each
ending in a linear layer with one output, the logit of a reduced ejection fraction: one with the
same structure and new random weights, and one as a copy of the network trained on CIFAR-10 whose
last layer is replaced by a new layer with one output. Use the echocardiography images as they are.
Train each network for 30 epochs on the training rows in shuffled groups of 32 with the binary
cross-entropy loss on the logit and the Adam optimiser with a learning rate of 0.0005. After every
epoch, compute the AUC on the validation rows, and keep the weights of the epoch with the largest
validation AUC. Fix the random seed to 2026 so that the result can be repeated. Compute the test AUC
of both networks against the column "reduced EF".
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the accuracy on CIFAR-10 and the test AUC of both networks, and keep the test AUC of
the network that started from CIFAR-10, with three decimals, under the name "answer".
Test: The accuracy on CIFAR-10 must lie well above 0.1, which one class in ten gives by chance, and
the test rows must not be used before the end.
```

**Expected result:** "answer": a test AUC between 0.5 and 1.0, which varies from computer to computer and with the copy of the echocardiograms

## Stop 2: Stenoses on synthetic and on real angiograms

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#stop-2) · Jupyter notebook: «Stop 2 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-07/NB07_vision_transformers.ipynb#scrollTo=stop-2-prompt)*

A small convolutional network learns to recognise patches of 64 × 64 pixels centred on a significant stenosis, first on the synthetic angiograms of the virtual clinic. The same network is then tested on the real angiograms of ARCADE, without any change, and finally trained again on the training angiograms of ARCADE.

### Prompt 2.1: A small convolutional network on synthetic angiograms

**Goal.** Train a small convolutional network on patches of the synthetic angiograms and measure it on the patches of the test patients.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether a small network can learn from coronary angiograms
whether a small square of an image is centred on a significant stenosis.
Data: The notebook holds a table named "data" with patches of 64 × 64 pixels cut from the synthetic
coronary angiograms of the virtual clinic, two views for each of 500 patients (training 300
patients, validation 100, test 100). Each row is a patch: "set" gives its set ("training",
"validation" or "test"), "patient" the patient, and each cell of "patch" holds the patch as an image
of 64 × 64 pixels with grey values from 0 to 1. "stenosis" is 1 when the patch is centred within 6
pixels of a significant stenosis (50 percent or more in the left main coronary artery, 70 percent or
more elsewhere) and 0 when it lies on a vessel at least 48 pixels from every stenosis.
Task: Standardise every patch on its own: Subtract the mean of its grey values and divide by their
standard deviation plus 0.02. Build a small convolutional network for one patch of 64 × 64 pixels
with one channel: four blocks, each a convolution with filters of 3 × 3 pixels and a padding of one
pixel (16, 32, 64 and 64 filters), batch normalisation, ReLU and max pooling of 2 × 2; then the mean
of every channel over its positions and a linear layer with one output, the logit of a stenosis.
Train the network on the training patches for 8 epochs, in shuffled groups of 64 patches, with the
binary cross-entropy loss on the logit and the Adam optimiser with a learning rate of 0.001. As data
augmentation, turn every group by a random quarter turn and mirror it from left to right with a
probability of one half. After every epoch, compute the AUC of the probabilities of the validation
patches, and at the end keep the weights of the epoch with the largest validation AUC. Fix the
random seed to 2026 so that the result can be repeated. Then compute the probabilities of the test
patches and their AUC against the column "stenosis".
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of trainable weights and the validation AUC of every epoch, and keep the
test AUC, with three decimals, under the name "answer".
Test: The network must have 60,641 trainable weights, and the test patches must not be used before
the last step.
```

**Expected result:** "answer" = 0.965

### Prompt 2.2: The same network on real angiograms

**Goal.** Test a network that learned only from synthetic angiograms on the real angiograms of ARCADE.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how a network that learned to find stenoses on synthetic
angiograms does on real X-ray angiograms that it has never seen.
Data: The notebook holds a table named "data" with the test patches of two sources: 1,700 patches of
64 × 64 pixels from the synthetic coronary angiograms of the virtual clinic and 3,088 from the real
X-ray angiograms of ARCADE, a public data set. Each row is a patch: "source" gives its source
("synthetic" or "ARCADE"), "stenosis" is 1 for a patch centred on a stenosis and 0 for a patch on a
vessel far from every stenosis, and "probability" is the probability of a stenosis given by a small
convolutional network of the course that learned from the synthetic training patches only.
Task: Compute, for each source separately, the area under the ROC curve (AUC) of the column
"probability" against the column "stenosis", and the difference, synthetic minus ARCADE.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the two AUCs and their difference, and keep the AUC of the source "ARCADE", with three
decimals, under the name "answer".
Test: Each AUC must be computed from the patches of its own source only.
```

**Expected result:** "answer" = 0.538

### Prompt 2.3: Training on real angiograms

**Goal.** Train the same small network on the patches of the training angiograms of ARCADE.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how well a small convolutional network finds stenoses on
real coronary angiograms when it learns from real angiograms.
Data: The notebook holds a table named "data" with patches of 64 × 64 pixels cut from the 1,500
X-ray coronary angiograms of the stenosis set of ARCADE, a public data set (training 1,000
angiograms, validation 200, test 300). Each row is a patch: "set" gives its set ("training",
"validation" or "test"), "angiogram" the number of its angiogram, and each cell of "patch" holds the
patch as an image of 64 × 64 pixels with grey values from 0 to 1. "stenosis" is 1 when the patch is
centred within 6 pixels of the centre of a stenosis outlined by the experts and 0 when it lies on a
vessel at least 48 pixels from every outlined stenosis and from the border of the image.
Task: Standardise every patch on its own: Subtract the mean of its grey values and divide by their
standard deviation plus 0.02. Build a small convolutional network for one patch of 64 × 64 pixels
with one channel: four blocks, each a convolution with filters of 3 × 3 pixels and a padding of one
pixel (16, 32, 64 and 64 filters), batch normalisation, ReLU and max pooling of 2 × 2; then the mean
of every channel over its positions and a linear layer with one output, the logit of a stenosis.
Train the network on the training patches for 8 epochs, in shuffled groups of 64 patches, with the
binary cross-entropy loss on the logit and the Adam optimiser with a learning rate of 0.001. As data
augmentation, turn every group by a random quarter turn and mirror it from left to right with a
probability of one half. After every epoch, compute the AUC of the probabilities of the validation
patches, and at the end keep the weights of the epoch with the largest validation AUC. Fix the
random seed to 2026 so that the result can be repeated. Then compute the probabilities of the test
patches and their AUC against the column "stenosis".
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of trainable weights and the validation AUC of every epoch, and keep the
test AUC, with three decimals, under the name "answer".
Test: The network must have 60,641 trainable weights, and no patch of a test angiogram may be used
for training.
```

**Expected result:** "answer" = 0.81

## Stop 3: A convolutional network, a vision transformer and a hybrid

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#stop-3) · Jupyter notebook: «Stop 3 · Prompt and application», [open in Colab](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-07/NB07_vision_transformers.ipynb#scrollTo=stop-3-prompt)*

A small vision transformer and a hybrid of convolutions and attention learn the patches of ARCADE in the same way as the convolutional network of Stop 2, so that the three can be compared on the same test angiograms. The last step asks where the vision transformer looks: how much of the attention of its class token falls on the centre of the patch, where the stenosis is.

### Prompt 3.1: A small vision transformer

**Goal.** Train a small vision transformer, which cuts every patch into 64 squares and lets them attend to each other, on the patches of ARCADE.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to compare a small vision transformer with a small convolutional
network for finding stenoses on real coronary angiograms, both trained in the same way.
Data: The notebook holds a table named "data" with patches of 64 × 64 pixels cut from the 1,500
X-ray coronary angiograms of the stenosis set of ARCADE, a public data set (training 1,000
angiograms, validation 200, test 300). Each row is a patch: "set" gives its set ("training",
"validation" or "test"), "angiogram" the number of its angiogram, and each cell of "patch" holds the
patch as an image of 64 × 64 pixels with grey values from 0 to 1. "stenosis" is 1 when the patch is
centred within 6 pixels of the centre of a stenosis outlined by the experts and 0 when it lies on a
vessel at least 48 pixels from every outlined stenosis and from the border of the image.
Task: Standardise every patch on its own: Subtract the mean of its grey values and divide by their
standard deviation plus 0.02. Build a small vision transformer for one patch of 64 × 64 pixels with
one channel. Cut the patch into 64 squares of 8 × 8 pixels and map every square to 64 numbers with
the same learned linear map. Put a learned class token of 64 numbers before the 64 tokens and add
learned positions, one vector of 64 numbers for each of the 65 places, started from small random
numbers with a standard deviation of 0.02. Pass the tokens through four transformer blocks. In each
block, layer normalisation is followed by self-attention with four heads, whose output is added to
the input of the block; a second layer normalisation is followed by a feed-forward network with a
hidden layer of 128 units and the GELU activation, whose output is added again. At the end, take the
class token, apply layer normalisation and a linear layer with one output, the logit of a stenosis.
Train the network on the training patches for 8 epochs, in shuffled groups of 64 patches, with the
binary cross-entropy loss on the logit and the Adam optimiser with a learning rate of 0.001. As data
augmentation, turn every group by a random quarter turn and mirror it from left to right with a
probability of one half. After every epoch, compute the AUC of the probabilities of the validation
patches, and at the end keep the weights of the epoch with the largest validation AUC. Fix the
random seed to 2026 so that the result can be repeated. Then compute the probabilities of the test
patches and their AUC against the column "stenosis".
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of trainable weights and the validation AUC of every epoch, and keep the
test AUC, with three decimals, under the name "answer".
Test: The network must have 142,465 trainable weights, and no patch of a test angiogram may be used
for training.
```

**Expected result:** "answer" = 0.93

### Prompt 3.2: A hybrid of convolutions and attention

**Goal.** Train a hybrid model: three convolution blocks first, then two transformer blocks on the positions of their output.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether a network that first looks at small neighbourhoods
with convolutions and then relates the parts of the patch with attention finds stenoses on real
angiograms better than either kind alone.
Data: The notebook holds a table named "data" with patches of 64 × 64 pixels cut from the 1,500
X-ray coronary angiograms of the stenosis set of ARCADE, a public data set (training 1,000
angiograms, validation 200, test 300). Each row is a patch: "set" gives its set ("training",
"validation" or "test"), "angiogram" the number of its angiogram, and each cell of "patch" holds the
patch as an image of 64 × 64 pixels with grey values from 0 to 1. "stenosis" is 1 when the patch is
centred within 6 pixels of the centre of a stenosis outlined by the experts and 0 when it lies on a
vessel at least 48 pixels from every outlined stenosis and from the border of the image.
Task: Standardise every patch on its own: Subtract the mean of its grey values and divide by their
standard deviation plus 0.02. Build a hybrid network for one patch of 64 × 64 pixels with one
channel. Three convolution blocks, each a convolution with filters of 3 × 3 pixels and a padding of
one pixel (16, 32 and 64 filters), batch normalisation, ReLU and max pooling of 2 × 2, turn the
patch into 8 × 8 positions of 64 numbers. These 64 positions are the tokens of a small transformer:
Put a learned class token of 64 numbers before them, add learned positions for the 65 places,
started from small random numbers with a standard deviation of 0.02, and pass the tokens through two
transformer blocks. In each block, layer normalisation is followed by self-attention with four
heads, whose output is added to the input of the block; a second layer normalisation is followed by
a feed-forward network with a hidden layer of 128 units and the GELU activation, whose output is
added again. At the end, take the class token, apply layer normalisation and a linear layer with one
output, the logit of a stenosis. Train the network on the training patches for 8 epochs, in shuffled
groups of 64 patches, with the binary cross-entropy loss on the logit and the Adam optimiser with a
learning rate of 0.001. As data augmentation, turn every group by a random quarter turn and mirror
it from left to right with a probability of one half. After every epoch, compute the AUC of the
probabilities of the validation patches, and at the end keep the weights of the epoch with the
largest validation AUC. Fix the random seed to 2026 so that the result can be repeated. Then compute
the probabilities of the test patches and their AUC against the column "stenosis".
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of trainable weights and the validation AUC of every epoch, and keep the
test AUC, with three decimals, under the name "answer".
Test: The network must have 94,881 trainable weights, and no patch of a test angiogram may be used
for training.
```

**Expected result:** "answer" = 0.934

### Prompt 3.3: Where does the vision transformer look?

**Goal.** Measure how much of the attention of the class token of the vision transformer falls on the centre of the patch, where a stenosis lies.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether the attention of a vision transformer that finds
stenoses on angiograms falls where the stenosis is, before reading its attention maps as an
explanation.
Data: The notebook holds a table named "data" with the 3,088 test patches of 64 × 64 pixels of
ARCADE, a public data set of X-ray coronary angiograms. Each row is a patch: "angiogram" gives the
number of its angiogram, "stenosis" is 1 for a patch centred on a stenosis outlined by the experts
and 0 for a patch on a vessel far from every stenosis, and each cell of "attention" holds a table of
8 × 8 numbers that add up to 1: the attention that the class token of the small vision transformer
of the course pays to each of the 64 squares of 8 × 8 pixels of the patch, followed through its four
layers (attention rollout). The four central squares cover the central 16 × 16 pixels of the patch,
rows and columns 4 and 5 when they are counted from 1.
Task: For every patch, add up the attention of the four central squares. Compute the mean of this
share over the patches with a stenosis and over the others, and compare both with 4/64 = 0.0625, the
share of the four squares if the attention were spread evenly.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the two means, and keep the mean of the patches with a stenosis, with three decimals,
under the name "answer".
Test: Every share must lie between 0 and 1.
```

**Expected result:** "answer" = 0.153

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

### Ask for a review of an image pipeline

```text
Review the code below, which trains or tests a network on medical images and reports its accuracy.
Check six points. Are the sets split by patient, or at least by image, so that no patch or frame of
one patient or image lies on both sides? Are the normalisation, the thresholds and every other
choice learned on the training and validation sets only? Does every augmentation keep the meaning of
the label, for example no mirror when the label depends on the side? Is every image prepared at test
time exactly as in training, with the same size, range of values and scaling of a pretrained
network? Is the result reported at the level of the decision and at a realistic prevalence, for
example the lesion sensitivity and the false detections per image of a detector rather than the AUC
of curated patches? Could any image or header of a real patient leave the institution? For each
point, quote the line concerned, say whether it is right, and give the corrected code where it is
not.
```

## Prompts of the weekly project

The [weekly project](README.md#weekly-project) can be built with four prompts, one for each step. The section *Weekly project* at the end of the Jupyter notebook prepares the table of each prompt and opens on its own. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Project step 1: Three networks, one test

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to compare a convolutional network, a vision transformer and a
hybrid for finding stenoses on real coronary angiograms, trained in the same way and tested on the
same angiograms.
Data: The notebook holds a table named "data" with patches of 64 × 64 pixels cut from the 1,500
X-ray coronary angiograms of the stenosis set of ARCADE, a public data set (training 1,000
angiograms, validation 200, test 300). Each row is a patch: "set" gives its set ("training",
"validation" or "test"), "angiogram" the number of its angiogram, and each cell of "patch" holds the
patch as an image of 64 × 64 pixels with grey values from 0 to 1. "stenosis" is 1 when the patch is
centred within 6 pixels of the centre of a stenosis outlined by the experts and 0 when it lies on a
vessel at least 48 pixels from every outlined stenosis and from the border of the image.
Task: Standardise every patch on its own: Subtract the mean of its grey values and divide by their
standard deviation plus 0.02. Build three networks. First: Build a small convolutional network for
one patch of 64 × 64 pixels with one channel: four blocks, each a convolution with filters of 3 × 3
pixels and a padding of one pixel (16, 32, 64 and 64 filters), batch normalisation, ReLU and max
pooling of 2 × 2; then the mean of every channel over its positions and a linear layer with one
output, the logit of a stenosis. Second: Build a small vision transformer for one patch of 64 × 64
pixels with one channel. Cut the patch into 64 squares of 8 × 8 pixels and map every square to 64
numbers with the same learned linear map. Put a learned class token of 64 numbers before the 64
tokens and add learned positions, one vector of 64 numbers for each of the 65 places, started from
small random numbers with a standard deviation of 0.02. Pass the tokens through four transformer
blocks. In each block, layer normalisation is followed by self-attention with four heads, whose
output is added to the input of the block; a second layer normalisation is followed by a
feed-forward network with a hidden layer of 128 units and the GELU activation, whose output is added
again. At the end, take the class token, apply layer normalisation and a linear layer with one
output, the logit of a stenosis. Third: Build a hybrid network for one patch of 64 × 64 pixels with
one channel. Three convolution blocks, each a convolution with filters of 3 × 3 pixels and a padding
of one pixel (16, 32 and 64 filters), batch normalisation, ReLU and max pooling of 2 × 2, turn the
patch into 8 × 8 positions of 64 numbers. These 64 positions are the tokens of a small transformer:
Put a learned class token of 64 numbers before them, add learned positions for the 65 places,
started from small random numbers with a standard deviation of 0.02, and pass the tokens through two
transformer blocks. In each block, layer normalisation is followed by self-attention with four
heads, whose output is added to the input of the block; a second layer normalisation is followed by
a feed-forward network with a hidden layer of 128 units and the GELU activation, whose output is
added again. At the end, take the class token, apply layer normalisation and a linear layer with one
output, the logit of a stenosis. Train each network on the training patches for 8 epochs, in
shuffled groups of 64 patches, with the binary cross-entropy loss on the logit and the Adam
optimiser with a learning rate of 0.001. As data augmentation, turn every group by a random quarter
turn and mirror it from left to right with a probability of one half. After every epoch, compute the
AUC of the probabilities of the validation patches, and at the end keep the weights of the epoch
with the largest validation AUC. Fix the random seed to 2026 so that the result can be repeated.
Then compute the probabilities of the test patches and their AUC against the column "stenosis". Draw
2,000 bootstrap samples of the 300 test angiograms with replacement, keeping all patches of every
angiogram drawn, and give every AUC a 95 percent interval from the 2.5th to the 97.5th percentile.
Fix the random seed to 2026 so that the result can be repeated. In the same samples, compute the
difference of the AUC of the vision transformer and of the hybrid to that of the convolutional
network.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each network, its trainable weights, its training time and its
test AUC with the interval, and the two differences with their intervals; keep the largest test AUC,
with three decimals, under the name "answer".
Test: The three networks must have 60,641, 142,465 and 94,881 trainable weights, and the intervals
must come from angiograms, not from patches.
```

### Project step 2: A threshold for the laboratory

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know what the networks for stenoses on angiograms would give in
practice at a fixed threshold, among curated patches and among the windows of a whole angiogram,
where a stenosis is rare.
Data: The notebook holds a table named "data" with the 6,336 validation and test patches of 64 × 64
pixels of ARCADE, a public data set of X-ray coronary angiograms (validation 200 angiograms, test
300). Each row is a patch: "set" gives its set ("validation" or "test"), "angiogram" the number of
its angiogram, "stenosis" is 1 for a patch centred on a stenosis outlined by the experts and 0 for a
patch on a vessel far from every stenosis, and the three columns "convolutional network", "vision
transformer" and "hybrid" give the probability of a stenosis from the three small networks of the
course, trained on the training patches.
Task: For each of the three networks, choose on the patches of the set "validation" the threshold
that 90 percent of the patches with a stenosis reach. Apply it to the patches of the set "test" and
compute the sensitivity, the specificity and the positive predictive value. Then compute the
positive predictive value that the same sensitivity and specificity would give at a prevalence of 2
percent: the sensitivity times 0.02, divided by itself plus one minus the specificity times 0.98.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each network, its threshold and the four values, and keep the
positive predictive value of the hybrid at a prevalence of 2 percent, with three decimals, under the
name "answer".
Test: The thresholds must be chosen on the validation patches only, and every value must lie between
0 and 1.
```

### Project step 3: A detector for whole angiograms

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants a program that marks the stenoses on whole coronary angiograms, with
about one false detection per angiogram, and wants to know which share of the stenoses it finds.
Data: The notebook holds a table named "data" with the 1,500 X-ray coronary angiograms of the
stenosis set of ARCADE, a public data set (training 1,000, validation 200, test 300). Each row is an
angiogram: "set" gives its set ("training", "validation" or "test"), "angiogram" its number, each
cell of "image" holds the angiogram as an image of 512 × 512 pixels with grey values from 0 to 255,
and "stenoses" lists the centres of the stenoses outlined by the experts, each as (column, row) in
pixels counted from 0.
Task: Bring every image to grey values from 0 to 1. From every angiogram cut windows of 64 × 64
pixels: four for every stenosis, centred on it and shifted at random by up to 16 pixels in each
direction (label 1); and, for every stenosis, six windows centred on dark thin structures at least
48 pixels from the border of the image, among the pixels with the largest 3 percent of the values of
a black top-hat with a disk of radius 6, and six windows at random places, all at least 48 pixels
from every stenosis (label 0). Standardise every patch on its own: Subtract the mean of its grey
values and divide by their standard deviation plus 0.02. Build a hybrid network for one patch of 64
× 64 pixels with one channel. Three convolution blocks, each a convolution with filters of 3 × 3
pixels and a padding of one pixel (16, 32 and 64 filters), batch normalisation, ReLU and max pooling
of 2 × 2, turn the patch into 8 × 8 positions of 64 numbers. These 64 positions are the tokens of a
small transformer: Put a learned class token of 64 numbers before them, add learned positions for
the 65 places, started from small random numbers with a standard deviation of 0.02, and pass the
tokens through two transformer blocks. In each block, layer normalisation is followed by
self-attention with four heads, whose output is added to the input of the block; a second layer
normalisation is followed by a feed-forward network with a hidden layer of 128 units and the GELU
activation, whose output is added again. At the end, take the class token, apply layer normalisation
and a linear layer with one output, the logit of a stenosis. Train the network on the training
patches for 8 epochs, in shuffled groups of 64 patches, with the binary cross-entropy loss on the
logit and the Adam optimiser with a learning rate of 0.001. As data augmentation, turn every group
by a random quarter turn and mirror it from left to right with a probability of one half. After
every epoch, compute the AUC of the probabilities of the validation patches, and at the end keep the
weights of the epoch with the largest validation AUC. Fix the random seed to 2026 so that the result
can be repeated. Then scan every validation and test angiogram with windows of 64 × 64 pixels whose
centres lie every 16 pixels, starting at 8, with the image extended at its borders by reflection,
and compute the probability of every window. A detection is a window whose probability is at least
the threshold and is the largest among the windows of its neighbourhood of 5 × 5 centres. A stenosis
is found when a detection lies within 32 pixels of it, and every other detection is false. Choose
the smallest threshold from 0.50 to 0.99 in steps of 0.01 that gives at most one false detection per
angiogram on the validation angiograms, and apply it to the test angiograms.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the chosen threshold. Then show a table with one row for each of the thresholds 0.50,
0.70, 0.90 and the chosen one: the number of stenoses found out of all stenoses of the test
angiograms and the false detections per test angiogram. Keep the share of the stenoses found at the
chosen threshold, with three decimals, under the name "answer".
Test: The threshold must be chosen on the validation angiograms only, and the test angiograms must
hold 386 stenoses.
```

### Project step 4: The errors read by a cardiologist

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to see the stenoses that a detector misses and the places that it
marks wrongly, to judge what such a tool could do in the catheterisation laboratory.
Data: The notebook holds a table named "data" with the 300 test angiograms of ARCADE, a public data
set of X-ray coronary angiograms. Each row is an angiogram: "angiogram" gives its number, each cell
of "image" holds it as an image of 512 × 512 pixels with grey values from 0 to 255, "stenoses" lists
the centres of the stenoses outlined by the experts as (column, row) in pixels counted from 0, each
cell of "probabilities" holds a table of 32 × 32 probabilities of a stenosis from the detector of
the course, one for every window of 64 × 64 pixels whose centre lies at 8, 24, 40 and so on up to
504 pixels in each direction, and "threshold" holds the threshold of the detector, chosen on the
validation angiograms for at most one false detection per angiogram.
Task: A detection is a window whose probability is at least the threshold and is the largest among
the windows of its neighbourhood of 5 × 5 centres. A stenosis is found when a detection lies within
32 pixels of it, and every other detection is false. For every angiogram, list the missed stenoses
and the false detections with their probability. Then show five missed stenoses and the five false
detections with the largest probabilities, each as the window of 128 × 128 pixels around it with the
probabilities drawn over the image, the stenoses of the experts as circles and the detections as
squares.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show the ten windows, print the number of missed stenoses and of false detections, and keep
the number of missed stenoses under the name "answer".
Test: The missed stenoses and the found ones must add up to 386.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
