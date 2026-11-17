# Prompt library, Week 3

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 3](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-03/PROMPTLAR.md)

This library holds every prompt of Week 3, written on the prompt card of the course. Each prompt can be copied into an artificial intelligence (AI) assistant as it stands. The code that comes back goes into the Jupyter notebook, below the exercise or prompt challenge of the same name, and runs there. In the exercises, the line with `teach.check` tells at once whether the result is right. The [prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [The prompt cycle](#the-prompt-cycle)
2. [Prompts of the exercises](#prompts-of-the-exercises)
3. [Prompt challenges of the sections](#prompt-challenges-of-the-sections)
4. [Patterns for explaining, repairing and reviewing code](#patterns-for-explaining-repairing-and-reviewing-code)
5. [Prompt route of the weekly project](#prompt-route-of-the-weekly-project)

## The prompt cycle

| Step | What to do |
|---|---|
| 1. Describe | Copy the prompt card of the exercise, or write it with the seven fields: role, context, data, task, constraints, output and test. |
| 2. Generate | Send the prompt to an AI assistant. |
| 3. Run | Paste the code into the empty cell below the exercise and run it. |
| 4. Check | Read the result of `teach.check`, *correct* or *not yet*, and the test of the prompt. A result of *not yet* goes back to the assistant with the repair pattern. |
| 5. Explain | Ask the assistant for a line-by-line explanation, then explain the code once more in your own words. |
| 6. Log | Add the tool, the prompt, what was checked and what was changed to the AI usage log. |

## Prompts of the exercises

Each exercise of the Jupyter notebook has its prompt route in a folded cell right below it. The prompts below are the same. Paste the code from the assistant into the empty answer cell of the exercise and run it.

### Exercise 3.1: Numbers in a stack of frames

*Jupyter notebook, "Python step 3: Images as arrays"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `X12` is a NumPy array of shape (12, 64, 64): 12 frames of 64 × 64 pixels, values from 0 to 1.
Task: Count all the numbers that `X12` holds.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The count as an integer. Store it in a variable named `answer` and end the code with the
line `teach.check("Exercise 3.1", answer)`. Return only the code in one block, with a short comment
above each step.
Test: Check the method first on `np.zeros((2, 3, 4))`, which holds 24 numbers.
```

### Exercise 3.2: The mean of a frame read from a file

*Jupyter notebook, "Python step 3: Images as arrays"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `frame` is a NumPy array of shape (64, 64) read with `plt.imread` from the file VC-1212.png,
values from 0 to 1.
Task: Compute the mean value of all its pixels.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The mean, rounded to three decimals. Store it in a variable named `answer` and end the code
with the line `teach.check("Exercise 3.2", answer)`. Return only the code in one block, with a short
comment above each step.
Test: Print the minimum and the maximum as well; the mean must lie between them, and the maximum
must not exceed 1.
```

### Exercise 3.3: A smaller learning rate

*Jupyter notebook, "Python step 3: Images as arrays"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `Xs` is a NumPy array of shape (2000, 2) with the standardised lvedd_mm and ivs_mm of the 2000
patients (mean 0, SD 1). `target` is a NumPy array of 0 or 1 (1 abnormal).
Task: Train one logistic neuron by gradient descent: start from w = [0, 0] and b = 0, and make 200
updates with the learning rate 0.05. Each update computes p = sigmoid(Xs @ w + b), then subtracts
0.05 times the gradients Xs.T @ (p − target) / n and mean(p − target). After the 200 updates,
compute the mean binary cross-entropy.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The loss after the 200 updates, rounded to three decimals. Store it in a variable named
`answer` and end the code with the line `teach.check("Exercise 3.3", answer)`. Return only the code
in one block, with a short comment above each step.
Test: With the learning rate 0.5 of the Python step, the same loop must give the loss printed there
at step 200.
```

### Exercise A: The output of one neuron

*Jupyter notebook, Section 1, "A neuron and a network in NumPy"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: Two standardised measurements `x = [1.2, -0.5]`, the weights `w = [0.8, -1.5]` and the bias
`b = 0.1`.
Task: Compute the weighted sum z = w · x + b and the output of the sigmoid, 1 / (1 + e^(−z)).
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The output of the sigmoid, rounded to three decimals. Store it in a variable named `answer`
and end the code with the line `teach.check("Exercise A", answer)`. Return only the code in one
block, with a short comment above each step.
Test: With w = [0, 0] and b = 0 the output must be 0.5.
```

### Exercise B: A gradient from autograd

*Jupyter notebook, Section 2, "Learning: Loss, gradients and the training loop in PyTorch"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: One patient with `x = [1.0, 2.0]` and the label `y = 1`, and one neuron with the weights
`w = [0.5, -0.25]`, the bias 0 and the sigmoid. The loss is the binary cross-entropy.
Task: Make w a tensor with `requires_grad=True`, compute the loss with `F.binary_cross_entropy`,
call `backward()` and read the gradient of the loss with respect to the first weight.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The gradient with respect to w1, rounded to three decimals. Store it in a variable named
`answer` and end the code with the line `teach.check("Exercise B", answer)`. Return only the code in
one block, with a short comment above each step.
Test: Compare it with the formula (p − y) · x1; the two values must be equal.
```

### Exercise C: Abnormal frames in the test set

*Jupyter notebook, Section 3, "The frames of the echo laboratory"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `X` is a NumPy array of shape (2000, 64, 64) with one end-diastolic parasternal short-axis
frame per patient of the virtual clinic, pixel values from 0 to 1, one pixel = 2 mm. `y` holds the
report of the echo laboratory, 0 or 1 (1 abnormal: a left ventricular end-diastolic diameter above
58 mm or a septum of 13 mm or more). `echo_table` holds patient_id, lvedd_mm, ivs_mm and pw_mm (mm),
and dilated and thick_septum (0 or 1). `train_idx`, `val_idx` and `test_idx` are the indices of
1200, 400 and 400 frames, split with stratification by `y`. `Xtr`, `Xva` and `Xte` are float tensors
of shape (n, 1, 64, 64), normalised with the mean and the SD of the training frames; `ytr`, `yva`
and `yte` are tensors of labels, 0 or 1.
Task: Count the abnormal frames (label 1) of the test set.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The count as an integer. Store it in a variable named `answer` and end the code with the
line `teach.check("Exercise C", answer)`. Return only the code in one block, with a short comment
above each step.
Test: The training, validation and test sets must add up to 2000 frames, and the share of abnormal
frames must be about the same in the three sets.
```

### Exercise D: The size after a convolution

*Jupyter notebook, Section 4, "Convolution by hand and with PyTorch"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: A square input of 64 × 64 pixels with one channel.
Task: Compute the output size of a convolution with a 5 × 5 kernel, stride 2 and padding 1 with the
formula floor((n + 2p − k) / s) + 1, and check it with `F.conv2d` on `torch.zeros(1, 1, 64, 64)`.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The output size (one side) as an integer. Store it in a variable named `answer` and end the
code with the line `teach.check("Exercise D", answer)`. Return only the code in one block, with a
short comment above each step.
Test: With a 3 × 3 kernel, stride 1 and padding 1, the size must stay 64.
```

### Exercise E: Parameters of the network

*Jupyter notebook, Section 5, "A first convolutional network"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `EchoCNN` is the class of Section 5: three blocks of Conv2d (3 × 3, padding 1), BatchNorm2d,
ReLU and MaxPool2d(2) with 8, 16 and 32 channels, then Flatten, Dropout(0.3) and Linear(2048,
n_classes).
Task: Create `EchoCNN(n_classes=2)` and count its trainable parameters.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The number of parameters as an integer. Store it in a variable named `answer` and end the
code with the line `teach.check("Exercise E", answer)`. Return only the code in one block, with a
short comment above each step.
Test: Count the parameters of `nn.Conv2d(1, 8, 3)` as well; it must have 80.
```

### Exercise F: The scale of dropout

*Jupyter notebook, Section 6, "Overfitting: Dropout, batch normalisation and augmentation"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: A tensor of ten ones, `torch.ones(10)`.
Task: Apply `F.dropout` with p = 0.3 in training mode and find the value that the kept elements
take.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The value of a kept element, rounded to three decimals. Store it in a variable named
`answer` and end the code with the line `teach.check("Exercise F", answer)`. Return only the code in
one block, with a short comment above each step.
Test: With `training=False` the tensor must come back unchanged.
```

### Exercise G: The macro F1 of three classes

*Jupyter notebook, Section 7, "Reading the result: Precision, recall and F1"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: The confusion matrix of a network on 180 short-axis CMR slices, rows true and columns
predicted, in the order normal, DCM and HCM: [[51, 8, 1], [0, 60, 0], [6, 0, 54]].
Task: From the matrix, compute the precision, the recall and the F1 of each class, then their mean,
the macro F1.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The macro F1, rounded to three decimals. Store it in a variable named `answer` and end the
code with the line `teach.check("Exercise G", answer)`. Return only the code in one block, with a
short comment above each step.
Test: The F1 of DCM must be 0.938.
```

### Exercise H: Parameters of one convolution layer

*Jupyter notebook, Section 8, "Known architectures and skip connections"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: A convolution layer with 16 input channels, 32 output channels, a 3 × 3 kernel and a bias for
each output channel.
Task: Count its parameters with the formula c_in × c_out × k × k + c_out and check the result with
`nn.Conv2d`.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The number of parameters as an integer. Store it in a variable named `answer` and end the
code with the line `teach.check("Exercise H", answer)`. Return only the code in one block, with a
short comment above each step.
Test: `nn.Conv2d(1, 8, 3)` must have 80 parameters.
```

### Exercise I: Parameters of a residual block

*Jupyter notebook, Section 8, "Known architectures and skip connections"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: A basic block of ResNet with 64 channels: two 3 × 3 convolutions with padding 1 and without
bias, each followed by `nn.BatchNorm2d(64)`, ReLU after the first, and the input added to the output
before the last ReLU.
Task: Write the block as a subclass of `nn.Module` and count its trainable parameters.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The number of parameters as an integer. Store it in a variable named `answer` and end the
code with the line `teach.check("Exercise I", answer)`. Return only the code in one block, with a
short comment above each step.
Test: The output of the block for `torch.randn(1, 64, 16, 16)` must have the same shape as its
input.
```

### Exercise J: Evaluating the course model correctly

*Jupyter notebook, Section 9, "AI pair programming, part 3: Reviewing a training loop"*

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `course_model` is an `EchoCNN` with the weights of the course, loaded from
models/week03/echo_cnn.pt. `Xte` and `yte` are the 400 test frames and their labels (0 or 1, 40
abnormal).
Task: Switch the model to evaluation mode, predict the class with the largest output for every test
frame inside `torch.no_grad()`, and compute the F1 of the abnormal class with `f1_score`.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The F1, rounded to three decimals. Store it in a variable named `answer` and end the code
with the line `teach.check("Exercise J", answer)`. Return only the code in one block, with a short
comment above each step.
Test: Print the accuracy as well: It must be above 0.95, while the F1 is clearly lower.
```

## Prompt challenges of the sections

Each numbered section of the Jupyter notebook ends with a prompt challenge. It has a prompt but no prepared code and no `teach.check`. The checks below each prompt tell whether the result is right.

### Section 1: Activation functions and their slopes

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: No data: a grid of z values from −5 to 5.
Task: Draw the sigmoid, tanh and ReLU in one panel and their derivatives in a second panel.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure with two panels. Return only the code in one block, with a short comment above
each step.
Test: Print the largest value of each derivative.
```

**What to check.** The derivative of the sigmoid peaks at 0.25 at z = 0, that of tanh at 1; the derivative of ReLU is 0 for negative z and 1 for positive z.

### Section 2: Three learning rates

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `Xs` is a NumPy array of shape (2000, 2) with the standardised lvedd_mm and ivs_mm of the 2000
patients (mean 0, SD 1). `target` is a NumPy array of 0 or 1 (1 abnormal).
Task: Train the logistic neuron of the Python step for 300 updates with the learning rates 0.01, 0.1
and 1.0, starting each time from zero weights, and plot the loss against the update for the three
rates.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure with three lines and the final loss of each rate. Return only the code in one
block, with a short comment above each step.
Test: The losses must start at the same value, log(2) = 0.693.
```

**What to check.** The rate 0.01 ends well above the other two; 1.0 falls fastest. Too small a rate wastes steps.

### Section 3: Normal and abnormal frames side by side

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `X` is a NumPy array of shape (2000, 64, 64) with one end-diastolic parasternal short-axis
frame per patient of the virtual clinic, pixel values from 0 to 1, one pixel = 2 mm. `y` holds the
report of the echo laboratory, 0 or 1 (1 abnormal: a left ventricular end-diastolic diameter above
58 mm or a septum of 13 mm or more). `echo_table` holds patient_id, lvedd_mm, ivs_mm and pw_mm (mm),
and dilated and thick_septum (0 or 1).
Task: Show four normal and four abnormal frames in a grid of 2 × 4, each with its lvedd_mm and
ivs_mm in the title.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure. Return only the code in one block, with a short comment above each step.
Test: Print the label of each frame shown; the first row must be all 0 and the second all 1.
```

**What to check.** The abnormal frames show either a large cavity or a thick wall; some of the thick walls are hard to tell from normal ones by eye.

### Section 4: Two filters on a dilated ventricle

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `frame_d` is the frame of VC-1873, a NumPy array of shape (64, 64), values from 0 to 1.
Task: Apply a 3 × 3 averaging kernel (all values 1/9) and a 3 × 3 Laplacian kernel [[0, 1, 0], [1,
−4, 1], [0, 1, 0]] with `F.conv2d` and padding 1, and show the frame and the two results side by
side.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure with three panels. Return only the code in one block, with a short comment above
each step.
Test: Both results must have the shape (64, 64).
```

**What to check.** The averaging kernel smooths the speckle; the Laplacian lights up the borders of the myocardium.

### Section 5: Accuracy per epoch

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `train_idx`, `val_idx` and `test_idx` are the indices of 1200, 400 and 400 frames, split with
stratification by `y`. `Xtr`, `Xva` and `Xte` are float tensors of shape (n, 1, 64, 64), normalised
with the mean and the SD of the training frames; `ytr`, `yva` and `yte` are tensors of labels, 0 or
1. `EchoCNN` is the class of Section 5: three blocks of Conv2d (3 × 3, padding 1), BatchNorm2d, ReLU
and MaxPool2d(2) with 8, 16 and 32 channels, then Flatten, Dropout(0.3) and Linear(2048, n_classes).
Task: Train a new `EchoCNN` for 10 epochs with Adam (learning rate 0.003, batches of 32) and record
the accuracy on the training set and on the validation set after every epoch. Plot both against the
epoch.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure with two lines. Return only the code in one block, with a short comment above
each step.
Test: Compute the accuracy in evaluation mode and inside `torch.no_grad()`; both values must lie
between 0 and 1.
```

**What to check.** Both curves pass 0.9 after the first epochs, because 90 percent of the frames are normal. The F1 of Section 7 tells more.

### Section 6: Eight augmented copies of the case

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `frame` is the frame of VC-1212, a NumPy array of shape (64, 64), and `augment(x)` is the
function of Section 6, which takes a tensor of shape (n, 1, 64, 64).
Task: Make eight augmented copies of the frame with `augment` and show them in a grid of 2 × 4.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure. Return only the code in one block, with a short comment above each step.
Test: Each copy must keep the shape (64, 64) and values near the range of the frame.
```

**What to check.** The heart turns and shifts by a few pixels and the brightness changes, while the anatomy stays plausible. A left-right flip would move the right ventricle to the wrong side.

### Section 7: Precision and recall across thresholds

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `p_test`, the probabilities of the abnormal class for the 400 test frames, and `y_test`, their
labels (0 or 1).
Task: For the thresholds 0.1, 0.2, …, 0.9, compute the precision and the recall of the abnormal
class, and plot both against the threshold.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure and a table of the nine thresholds. Return only the code in one block, with a
short comment above each step.
Test: At the threshold 0.5 the table must show the values of the evaluation above it.
```

**What to check.** Recall falls and precision rises as the threshold grows; a lower threshold finds more thick septa at the price of more false alarms.

### Section 8: Parameters layer by layer

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `EchoCNN` is the class of Section 5: three blocks of Conv2d (3 × 3, padding 1), BatchNorm2d,
ReLU and MaxPool2d(2) with 8, 16 and 32 channels, then Flatten, Dropout(0.3) and Linear(2048,
n_classes).
Task: Build a table with one row for each layer of `EchoCNN(n_classes=2)` that has parameters: its
name, its type and its number of parameters.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: A pandas DataFrame. Return only the code in one block, with a short comment above each step.
Test: The column of the parameters must add up to the total of Exercise E.
```

**What to check.** The linear layer holds 4098 of the 10098 parameters; the three convolutions together hold 5888.

### Section 9: A function that evaluates a model

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `course_model`, the `EchoCNN` of the course, and the test tensors `Xte` and `yte`.
Task: Write a function `evaluate(model, X, y)` that switches the model to evaluation mode, predicts
inside `torch.no_grad()` and returns a dictionary with the accuracy, the precision, the recall and
the F1 of the abnormal class.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The function and its result for the course model, rounded to three decimals. Return only the
code in one block, with a short comment above each step.
Test: Calling the function twice must give the same numbers.
```

**What to check.** For the course model: accuracy 0.968, precision 0.909, recall 0.75 and F1 0.822.

## Patterns for explaining, repairing and reviewing code

These four patterns work with the code of any exercise. The parts in square brackets are replaced before the prompt is sent.

### Explain the code

```text
Explain the following Python code line by line for a physician who is new to Python. Then name two
ways in which it could return a wrong result without an error message.

[paste the code here]
```

### Repair code that does not pass the check

```text
The code below was written for this task: [paste the task of the prompt]. It runs, but the check of
the course prints "not yet". Find the error, explain it in two sentences and return the corrected
code. Keep the variable names and the line with teach.check.

[paste the code here]
```

### Understand an error message

```text
Running the cell below in a Jupyter notebook gives the error message that follows. Explain the cause
in plain language and return the corrected code.

[paste the code here]

[paste the error message here]
```

### Ask for a review of a training loop

```text
Review the PyTorch code below, which trains and evaluates an image classifier. Check five things:
whether the normalisation uses statistics of the training images only, whether model.train() and
model.eval() are called at the right places, whether the evaluation runs inside torch.no_grad(),
whether the output layer fits the loss (no softmax before CrossEntropyLoss), and whether the measure
reported suits a rare class. Answer with a short list, then return the corrected code.

[paste the code here]
```

## Prompt route of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. Each step builds on the one before it, so the test of a step must hold before the next prompt is sent. The report lists all four prompts in the AI usage log.

### Step 1: Prepare the slices

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: `Xc, yc, cmr_table = make_cmr_set(300)` gives 900 short-axis slices of cine cardiac magnetic
resonance (CMR), a NumPy array of shape (900, 64, 64) with values from 0 to 1 and one pixel = 2 mm.
`yc` is 0 for normal, 1 for dilated cardiomyopathy (DCM) and 2 for hypertrophic cardiomyopathy
(HCM). `cmr_table` holds study_id, lvedd_mm, septum_mm and posterior_mm (mm) and diagnosis.
Task: Split the 900 slices into training, validation and test sets of 60, 20 and 20 percent,
stratified by `yc` (random_state=RANDOM_STATE). Normalise every set with the mean and the SD of the
training slices and turn the sets into tensors of shape (n, 1, 64, 64).
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: Six tensors, Xc_tr, Xc_va, Xc_te, yc_tr, yc_va and yc_te, and a table of the class counts of
each set. Return only the code in one block, with a short comment above each step.
Test: The three sets must hold 540, 180 and 180 slices, with 60 slices of each class in the test
set.
```

### Step 2: Train a network for three classes

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: The tensors of step 1, the class `EchoCNN` of Section 5 and the function `augment(x)` of
Section 6.
Task: Train `EchoCNN(n_classes=3)` with Adam (learning rate 0.003, batches of 32) for up to 30
epochs, with augmentation of the training batches, and keep the weights of the epoch with the lowest
validation loss. Plot the training and validation loss.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The trained model and one figure of the two losses. Return only the code in one block, with
a short comment above each step.
Test: Print the epoch with the lowest validation loss; the validation loss of the kept weights must
be the smallest of the run.
```

### Step 3: Measure the network on the test slices

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: The model of step 2 and the test tensors Xc_te and yc_te.
Task: In evaluation mode and inside `torch.no_grad()`, predict the class of every test slice. Report
the confusion matrix, the precision, the recall and the F1 of each class, and the macro F1.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: The confusion matrix as a pandas DataFrame with the class names, and a table of the three
measures by class. Return only the code in one block, with a short comment above each step.
Test: The confusion matrix must add up to 180, and its rows to 60 each.
```

### Step 4: Look at the errors

```text
Role: You are helping a cardiologist who is learning Python.
Context: A Jupyter notebook in which NumPy is imported as np, pandas as pd and matplotlib.pyplot as
plt, PyTorch as torch with torch.nn as nn and torch.nn.functional as F, and scikit-learn is
installed. The course package vclinic with its modules teach and imaging is available, and
RANDOM_STATE = 2026.
Data: The predictions of step 3, `Xc` and `cmr_table`.
Task: Show every misclassified test slice with its true and predicted class and its lvedd_mm and
septum_mm in the title, and summarise the measurements of the errors in a table.
Constraints: Use only these packages and the variables named here. Do not load files and do not
install anything.
Output: One figure and one table. Return only the code in one block, with a short comment above each
step.
Test: The number of slices shown must equal the number of errors in the confusion matrix.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
