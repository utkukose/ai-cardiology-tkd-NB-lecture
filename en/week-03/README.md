<div align="center">

# Week 3: Deep learning and convolutional neural networks

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology

*From one neuron to a network that reads echocardiograms*

[Course home](../../README.md) · [Syllabus](../../SYLLABUS.md) · [Setup](../../SETUP.md) · [Türkçe](../../tr/hafta-03/README.md)

</div>

## About the week

Neural networks from one neuron to a deep network: the loss, the gradients and the training loop in PyTorch, images as arrays, convolution and pooling, and a convolutional neural network (CNN) that reads the parasternal short-axis frames of the new echo laboratory of the virtual clinic. Overfitting is met with dropout, batch normalisation, augmentation and early stopping, and the results are read with precision, recall and the F1 score, class by class. The known architectures from LeNet to ResNet follow, and a review of a training loop written by an AI assistant closes the week.

4 hours in the session and about 3 hours for the weekly project.

## Materials

| Material | Open | What it holds |
|---|---|---|
| **Lecture page** | [Open the lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html) | Concepts, formulas with worked examples, a three-dimensional (3D) scene of the network, two animations, knowledge checks, review cards and references |
| **Interactive lab** | [Open the interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lab.html) | Parts A to F, including the prompt workshop of Part F, a self-assessment, a reflection and the learning log to export |
| **Jupyter notebook** | [NB03_deep_learning_and_cnns.ipynb](NB03_deep_learning_and_cnns.ipynb)<br>[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-03/NB03_deep_learning_and_cnns.ipynb) (fallback) | Python step 3, Sections 0 to 10 with Exercises A to J, a prompt route below each exercise, a prompt challenge at the end of each section, an application key and the challenges of seven fields |
| **Prompt library** | [PROMPTS.md](PROMPTS.md) | All prompts of the week on the prompt card: 13 exercises, 9 prompt challenges, 4 patterns for explaining, repairing and reviewing code and the prompt route of the weekly project |
| **PDF notes** | [Week03_Lecture_Notes.pdf](Week03_Lecture_Notes.pdf) | Python step 3 and the whole lecture, ready to print |

<table>
<tr><td width="50%"><img src="screenshots/lab_part_b_convolution.png" alt="Interactive lab, Part B: a 3 × 3 kernel slides over a frame of the echo laboratory, with the products of one position and the feature map that grows." width="100%"></td><td width="50%"><img src="screenshots/notebook_learning_curves.png" alt="Jupyter notebook, Section 6: the training and validation loss of the network on 300 frames, without and with augmentation." width="100%"></td></tr>
<tr><td>Interactive lab, Part B: a 3 × 3 kernel slides over a frame of the echo laboratory, with the products of one position and the feature map that grows.</td><td>Jupyter notebook, Section 6: the training and validation loss of the network on 300 frames, without and with augmentation.</td></tr>
<tr><td width="50%"><img src="screenshots/lab_part_c_overfitting.png" alt="Interactive lab, Part C: the learning curves of four settings against overfitting and the augmented copies of one frame." width="100%"></td><td width="50%"><img src="screenshots/lab_part_f_prompt_workshop.png" alt="Interactive lab, Part F: the prompt workshop with the seven fields of the prompt card, a quality meter and a privacy check." width="100%"></td></tr>
<tr><td>Interactive lab, Part C: the learning curves of four settings against overfitting and the augmented copies of one frame.</td><td>Interactive lab, Part F: the prompt workshop with the seven fields of the prompt card, a quality meter and a privacy check.</td></tr>
</table>

## The case of the week

**VC-1212, 70 years, woman**, has diabetes and hypertension and comes with breathlessness on exertion. The new echo laboratory of the virtual clinic records her parasternal short-axis view. Its convolutional network reads the frame as normal, with a probability of an abnormal frame of 0.012. The echocardiographer measures a septum of 13.8 mm. The [lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html) opens with her case, and the laboratory answers it in its last section.

## Learning outcomes

By the end of the week, participants are expected to explain how a neuron, a layer and a network compute their outputs, and how a loss, its gradients and the update of the weights make a network learn. They should be able to treat a stack of echocardiographic frames as an array, to normalise it with the statistics of the training frames only and to follow a convolution and a pooling step by hand. They should be able to train a small convolutional network in PyTorch, to recognise overfitting in its learning curves and to use dropout, batch normalisation, augmentation and early stopping against it. Finally, they should be able to read the result with precision, recall and the F1 score for each class, to place the network among the known architectures and to review a training loop written by an AI assistant with five questions.

## Study path

Participants who attend the session complete steps 1 to 5 there. Participants who follow the week on their own, for example after a missed session, can plan with the times below. Steps 1 to 7 take about 6 hours 40 minutes, and the weekly project takes about 3 hours. On the [prompt path](../../PROMPT_PATH.md), steps 2 and 4 use the prompt routes below the exercises and the prompt challenges of the sections. The [prompt library](PROMPTS.md) holds every prompt of the week, and the times stay about the same.

| Step | Activity | Time |
|---|---|---|
| 1 | Read the case of the week and the lecture page, and answer its knowledge checks | 1 hour 15 minutes |
| 2 | Run Python step 3 in the Jupyter notebook, right after Section 0 | 40 minutes |
| 3 | Work through Parts A to F of the interactive lab | 1 hour 10 minutes |
| 4 | Work through Sections 1 to 9 of the Jupyter notebook and solve the exercises | 2 hours 15 minutes |
| 5 | Use the application key of Section 10 and solve the challenge of your field | 30 minutes |
| 6 | Read the paper of the week with its three questions | 30 minutes |
| 7 | Take the self-assessment in the interactive lab (tab: Check yourself), write the reflection and export the learning log | 20 minutes |
| 8 | Complete the weekly project | 3 hours |

## Training flow of the session

The four-hour session of the week follows the plan below. It is shared to show how the materials fit together in a live session.

| Time | Activity |
|---|---|
| 0:00 to 0:15 | The case of the week, VC-1212. Participants open the Jupyter notebook and run Section 0, which also checks that PyTorch is installed. |
| 0:15 to 0:50 | Python step 3 in pairs: one participant who writes code and one who does not. The second participant may solve the exercises on the prompt path. |
| 0:50 to 1:45 | Mini project, first half: a neuron and a network (Section 1), the training loop by hand and in PyTorch (Part A of the interactive lab, Section 2), the frames of the echo laboratory (Section 3) and convolution by hand (Part B, Section 4). |
| 1:45 to 2:00 | Break. |
| 2:00 to 2:40 | Mini project, second half: the network of the echo laboratory in three dimensions and in code (Section 5), then overfitting and the tools against it (Part C, Section 6). |
| 2:40 to 3:30 | Reading the result class by class: precision, recall and the F1 score for two and three classes (Part D, Section 7), then the known architectures from LeNet to ResNet (Section 8). |
| 3:30 to 4:00 | AI pair programming, part 3: the review of a training loop and the prompt workshop (Section 9, Parts E and F), the paper of the week and the weekly project. |

## Weekly project

**What to do.** Train the network of the echo laboratory on the short-axis slices of the cardiomyopathy clinic, with three classes: normal, dilated cardiomyopathy (DCM) and hypertrophic cardiomyopathy (HCM). First, split the 900 slices of `make_cmr_set(300)` into training, validation and test sets of 60, 20 and 20 percent, and normalise them with the training slices. Second, train `EchoCNN(n_classes=3)` with augmentation for up to 30 epochs and keep the weights of the epoch with the lowest validation loss. Third, report the confusion matrix, the precision, the recall and the F1 of each class, and the macro F1. Fourth, show every misclassified test slice with its measurements, and write which errors would matter most in the clinic and why.

**Where to look.** Lecture: sections "A convolutional network for the echo laboratory", "Overfitting: Dropout, batch normalisation and augmentation" and "Reading the result: Precision, recall and F1". Interactive lab: Parts C, D and F. Jupyter notebook: Sections 5, 6, 7 and 10.

**Prompt route.** The project can also be built with four prompts, one for each step, from the [prompt library](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-03/PROMPTS.md#prompt-route-of-the-weekly-project). The test of each prompt must hold before the next prompt is used.

**Example.** Suppose the network calls 68 test slices DCM, 60 of them rightly, and misses none of the 60 slices with DCM: $TP = 60$, $FP = 8$, $FN = 0$. The precision of DCM is $60/68 = 0.882$ and its recall $60/60 = 1.000$. Its F1 is $2TP/(2TP + FP + FN)$, here $120/128 = 0.938$. The macro F1 is the plain mean of the F1 of the three classes.

**What to submit.** A report of one to two pages in the [report template](../templates/Report_Template.docx), with the figure of the two losses, the confusion matrix, the table of the measures by class and the figure of the errors. Add the AI usage log (tool, prompt, what was checked, what was changed) and the Jupyter notebook with its outputs.

**Submission.** The weekly project is submitted before the session of Week 4 by e-mail to utkukose@sdu.edu.tr or utkukose@gmail.com. The e-mail holds the items listed under What to submit and the learning log exported from the interactive lab. Weekly projects count for 40 percent of the assessment, and the rubric is in the syllabus.

## Optional research assignment

Search PubMed for one study, published in 2020 or later, that trained a deep learning model on echocardiograms or on cardiac magnetic resonance images to detect a disease. Summarise it in half a page: the images and how many patients they came from, the labels and who gave them, the network, the measures reported for each class and how the model was tested on patients from another hospital, if at all. The three questions of [the paper of the week](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html#the-paper-of-the-week) can guide the summary. The assignment is not graded, and it prepares the discussion of transfer learning in Week 4.

## The virtual clinic after this week

In Week 3 the virtual clinic opens its echo laboratory. Every patient of the registry gets an end-diastolic frame of the parasternal short-axis view, drawn from the patient's own measurements. A convolutional network learns the report of the laboratory from the pixels. The cardiomyopathy clinic adds short-axis slices of cardiac magnetic resonance with three classes. The results are in the section [The virtual clinic, stage 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html#the-virtual-clinic-stage-3-the-echo-laboratory-opens) of the lecture page.

## Next week

**Week 4: Transfer learning.** The echo laboratory starts to measure: transfer learning adapts a network trained on millions of other images, a U-Net outlines the left ventricle, and the ejection fraction is computed from the outlines with the method of discs. See the [plan of the course](../../README.md#the-eleven-weeks).

---

<div align="center">

**Prof. Dr. Utku Kose**

Full Professor, Department of Computer Engineering, Süleyman Demirel University, Isparta, Türkiye<br>
Founding Director, AI Application and Research Center (YAZEM), Süleyman Demirel University<br>
Head of the Computer Science Division, Department of Computer Engineering, Süleyman Demirel University<br>
Additional affiliations: University of North Dakota (USA), Universidad Panamericana (Mexico City, Mexico), Vel Tech University (Chennai, India)<br>
IEEE Senior Member, ACM Professional Member

[ORCID 0000-0002-9652-6415](https://orcid.org/0000-0002-9652-6415) | [utkukose.com](https://www.utkukose.com) | [github.com/utkukose](https://github.com/utkukose)

[utkukose@sdu.edu.tr](mailto:utkukose@sdu.edu.tr) | [utku.kose@und.edu](mailto:utku.kose@und.edu) | [ukose@up.edu.mx](mailto:ukose@up.edu.mx) | [utkukose@gmail.com](mailto:utkukose@gmail.com)

*First version: November 2026. Content CC BY 4.0, code MIT.*

</div>
