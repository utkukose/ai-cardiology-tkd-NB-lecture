> **Türkçe:** Bu eğitim Türkçe yürütülmektedir. **[Bu haftanın Türkçe sayfasına geçin](../../tr/hafta-07/README.md)**

<div align="center">

# Week 7: Vision transformers

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology

*From attention and patches to stenoses on coronary angiograms and a quality gate for echocardiography*

[Course home](../../README.md) · [Syllabus](../../SYLLABUS.md) · [Setup](../../SETUP.md) · [Türkçe](../../tr/hafta-07/README.md)

</div>

## About the week

The catheterisation laboratory of the virtual clinic opens. Attention lets every part of an image look at every other part, and the vision transformer cuts an image into patches and treats them as the tokens of Week 6. A vision transformer pretrained on photographs, ViT-B/16, becomes a quality gate for the echocardiograms of CAMUS without ever having seen one (AUC 0.862 for poor frames, against 0.782 for EfficientNet-B0 and 0.704 for four image statistics). The second half looks for stenoses on coronary angiograms. A small convolutional network that learned on the synthetic angiograms of the virtual clinic reaches an AUC of 0.965 there and falls to 0.538 on the real angiograms of ARCADE. Trained on ARCADE, a convolutional network, a vision transformer and a hybrid of both reach 0.810, 0.930 and 0.936. Attention maps are read with their limits, a scan of whole angiograms shows why a patch classifier is not yet a detector, and the week closes with the review of an image pipeline written by an AI assistant.

4 hours in the session and about 3 hours for the weekly project.

## The route of the week

The lecture page is the main route of the week. It holds no code and no prompts, and it is read from top to bottom together with the interactive lab. At each practice stop, every participant chooses one of two paths in the Jupyter notebook: the **prompt path** (Part 1), on which an artificial intelligence (AI) assistant writes the code from ready prompts and the participant runs and checks it, or the **Python path** (Part 2), on which the participant writes the code. Both paths reach the same results. The notebook runs in Google Colab, with nothing to install, or in Jupyter on your own computer ([setup](../../SETUP.md)).

| Main route: lecture page and interactive lab | Practice stop | Prompt path (Part 1) | Python path (Part 2) |
|---|---|---|---|
| [Images of the catheterisation laboratory: The angiograms of the virtual clinic](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#images-of-the-catheterisation-laboratory-the-angiograms-of-the-virtual-clinic)<br>[From convolution to attention](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#from-convolution-to-attention)<br>[Self-attention with several heads and the transformer block](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#self-attention-with-several-heads-and-the-transformer-block)<br>[The vision transformer: An image as a sequence of patches](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#the-vision-transformer-an-image-as-a-sequence-of-patches)<br>[Inductive bias, data and pretraining](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#inductive-bias-data-and-pretraining)<br>[Transfer to echocardiography: A quality gate before the automatic EF](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#transfer-to-echocardiography-a-quality-gate) | **[Stop 1: A quality gate for echocardiography with a pretrained vision transformer](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#stop-1)** | Stop 1 | Python step 7 and Sections 1 to 4 |
| [Hybrid models: Convolutions first, attention after](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#hybrid-models-convolutions-first-attention-after)<br>[Finding stenoses on angiograms: Tasks and metrics](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#finding-stenoses-on-angiograms-tasks-and-metrics)<br>[Synthetic and real angiograms: A model in another world](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#synthetic-and-real-angiograms-a-model-in-another-world) | **[Stop 2: Stenoses on synthetic and on real angiograms](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#stop-2)** | Stop 2 | Sections 5 and 6 |
| [A convolutional network, a vision transformer and a hybrid compared](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#a-convolutional-network-a-vision-transformer-and-a-hybrid-compared)<br>[Attention maps read clinically, with their limits](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#attention-maps-read-clinically-with-their-limits)<br>[From patches to the whole angiogram](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#from-patches-to-the-whole-angiogram) | **[Stop 3: A convolutional network, a vision transformer and a hybrid](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#stop-3)** | Stop 3 | Sections 7 to 9 |
| [Working with an AI assistant, part 7: Reviewing an image pipeline](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#ai-pair-programming-part-7-reviewing-an-image-pipeline)<br>[The paper of the week](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#the-paper-of-the-week)<br>[The virtual clinic, stage 7: Catheterisation laboratory](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#the-virtual-clinic-stage-7-catheterisation-laboratory) | The section on your own data, the paper of the week and the virtual clinic | – | – |

## Materials

| Material | Open | What it holds |
|---|---|---|
| **Lecture page (main route)** | [Open the lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html) | The case, the concepts with worked examples, a three-dimensional (3D) scene of the attention of a patch, two animations, knowledge checks, three practice stops, the section on your own data, review cards and references. No code and no prompts. |
| **Interactive lab** | [Open the interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lab.html) | Parts A to F without code, including the prompt workshop of Part F, a self-assessment, a reflection and the learning log to export |
| **Jupyter notebook** | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-07/NB07_vision_transformers.ipynb)<br>[Download for Jupyter](NB07_vision_transformers.ipynb) | Part 1, the prompt path: three stops with ten steps, each with a ready prompt, a data cell for its table, a cell for the code of the AI assistant, an automatic check and ready code, and the weekly project in four prompts. Part 2, the Python path: Python step 7, Sections 1 to 10 with Exercises A to J and the challenges of seven fields. |
| **Prompt library** | [PROMPTS.md](PROMPTS.md) | All prompts of the prompt path with a copy button on GitHub, the prompts for repairing and reviewing code and the prompt path of the weekly project |
| **PDF notes** | [Week07_Lecture_Notes.pdf](Week07_Lecture_Notes.pdf) | The lecture page in print form, with its practice stops and the section on your own data |

<table>
<tr><td width="50%"><img src="screenshots/lab_part_a_attention.png" alt="Interactive lab, Part A: the attention of one query over four tokens, with the scores, the softmax weights and the output, and the effect of the scaling by the square root of the length of the keys." width="100%"></td><td width="50%"><img src="screenshots/notebook_quality_gate.png" alt="Jupyter notebook, Section 4: the ROC curves of the quality gate for poor echocardiography frames from four image statistics, EfficientNet-B0 and ViT-B/16." width="100%"></td></tr>
<tr><td>Interactive lab, Part A: the attention of one query over four tokens, with the scores, the softmax weights and the output, and the effect of the scaling by the square root of the length of the keys.</td><td>Jupyter notebook, Section 4: the ROC curves of the quality gate for poor echocardiography frames from four image statistics, EfficientNet-B0 and ViT-B/16.</td></tr>
<tr><td width="50%"><img src="screenshots/lab_part_c_thresholds.png" alt="Interactive lab, Part C: the threshold of a network of the course over its probabilities on the test patches of ARCADE, with the sensitivity, the specificity and the positive predictive value at two prevalences." width="100%"></td><td width="50%"><img src="screenshots/lecture_attention.png" alt="Lecture page: the attention of one query over four tokens of an angiogram, step by step." width="100%"></td></tr>
<tr><td>Interactive lab, Part C: the threshold of a network of the course over its probabilities on the test patches of ARCADE, with the sensitivity, the specificity and the positive predictive value at two prevalences.</td><td>Lecture page: the attention of one query over four tokens of an angiogram, step by step.</td></tr>
</table>

## The case of the week

Patient VC-2427, an 80-year-old man with heart failure and two diseased coronary vessels in the report of Week 6. Where are his stenoses on the angiograms, and can a convolutional network, a vision transformer or a hybrid find them on real angiograms?

## Learning outcomes

By the end of the week, participants are expected to explain attention with its queries, keys and values, to compute it by hand for a few tokens, and to describe how a vision transformer turns an image into a sequence of patches with a class token and positions. They should be able to explain the inductive bias of a convolutional network, why a vision transformer needs much data or pretraining, and how a hybrid combines the two. They should be able to use a pretrained vision transformer as a source of features for a clinical task, such as a quality gate for echocardiography, and to report its result with an interval from a bootstrap by patient. Finally, they should be able to compare a convolutional network, a vision transformer and a hybrid for stenoses on coronary angiograms, to recognise a domain shift between synthetic and real images, to read attention maps with their limits and to review an image pipeline.

## Study path

Participants who attend the session complete the main route and the practice stops there. Participants who follow the week on their own, for example after a missed session, can plan with the times below.

| Step | Activity | Prompt path | Python path |
|---|---|---|---|
| 1 | Read the case of the week and the lecture page up to Practice stop 1, with Parts A and B of the interactive lab, the 3D scene of the attention of a patch, the two animations and the knowledge checks | 1 hour 15 minutes | 1 hour 15 minutes |
| 2 | Practice stop 1, the mini project of the session: Part 1, Stop 1 on the prompt path, or Python step 7 and Sections 1 to 4 on the Python path | 35 minutes | 1 hour 35 minutes |
| 3 | Read on up to Practice stop 2: hybrid models, the tasks and metrics of stenosis detection, and synthetic and real angiograms, with Part C of the interactive lab | 35 minutes | 35 minutes |
| 4 | Practice stop 2: Part 1, Stop 2, or Sections 5 and 6 | 35 minutes | 50 minutes |
| 5 | Read on up to Practice stop 3: the three networks compared, attention maps and whole angiograms, with Part D of the interactive lab | 30 minutes | 30 minutes |
| 6 | Practice stop 3: Part 1, Stop 3, or Sections 7 to 9 | 35 minutes | 50 minutes |
| 7 | Read the review of an image pipeline with Parts E and F of the interactive lab, the paper of the week, the stage of the virtual clinic and the section on your own data; on the Python path, Section 10 as well | 40 minutes | 55 minutes |
| 8 | Take the self-assessment of the interactive lab (tab: Check yourself), write the reflection and export the learning log | 20 minutes | 20 minutes |
| | **Total without the weekly project** | **5 hours 5 minutes** | **6 hours 50 minutes** |
| 9 | Complete the weekly project, on either path | 3 hours | 3 hours |

## Training flow of the session

The four-hour session of the week follows the plan below. It is shared to show how the materials fit together in a live session.

| Time | Activity |
|---|---|
| 0:00 to 0:15 | The case of the week and the route of the week. Every participant opens the notebook in Google Colab or in Jupyter and runs Section 0. The first run downloads the frames of CAMUS (about 227 MB, if Week 4 did not), the ImageNet weights of ViT-B/16 (about 330 MB) and of EfficientNet-B0 (about 21 MB) and ARCADE (451.6 MB); the synthetic angiograms are drawn on the computer of the participant. |
| 0:15 to 1:00 | Main route: the angiograms of the virtual clinic, attention with Part A, the transformer block, the vision transformer with the 3D scene and Part B, inductive bias and pretraining, and the quality gate for echocardiography. |
| 1:00 to 1:35 | Mini project of the session, Practice stop 1, in two groups, the prompt path and the Python path: the quality gate from four image statistics, from ViT-B/16 and from EfficientNet-B0, and the bootstrap of the difference. |
| 1:35 to 1:50 | Break. |
| 1:50 to 2:35 | Main route: hybrid models, the tasks and metrics of stenosis detection, and synthetic and real angiograms with Part C. Practice stop 2: a small convolutional network on synthetic angiograms, on ARCADE without change and trained on ARCADE. |
| 2:35 to 3:20 | Main route: the three networks compared, attention maps with Part D and whole angiograms. Practice stop 3: the small vision transformer and the hybrid on ARCADE and the attention of the class token. |
| 3:20 to 4:00 | The review of an image pipeline with Parts E and F, the paper of the week, the catheterisation laboratory of the virtual clinic, the section on your own data and the weekly project. |

## Weekly project

**What to do.** Compare a convolutional network, a vision transformer and a hybrid for finding stenoses on the real coronary angiograms of ARCADE, and take the best of them from patches to whole angiograms. First, train the three small networks of the course on the patches of the training angiograms in the same way and give their test AUCs with 95 percent intervals from a bootstrap of the test angiograms, together with the difference of each to the convolutional network. Second, choose for each network the threshold that gives a sensitivity of 0.90 on the validation patches and report the sensitivity, the specificity and the positive predictive value on the test patches, at the prevalence of the patches and at a prevalence of 2 percent. Third, train the best network again with positive patches shifted by up to 16 pixels and with negatives cut from the vessels and from the background, scan the validation and test angiograms with windows every 16 pixels, keep the windows whose probability is the largest in their neighbourhood, choose the threshold on the validation angiograms for at most one false detection per angiogram, and give the share of the stenoses found and the false detections per angiogram on the test angiograms, at this threshold and at the thresholds 0.5, 0.7 and 0.9. Fourth, show five missed stenoses and five false detections with the heat map, and write half a page for a heart team on what such a tool could and could not do in the catheterisation laboratory.

**Where to look.** Lecture: sections "A convolutional network, a vision transformer and a hybrid compared" and "From patches to the whole angiogram". Interactive lab: Parts C and D. Jupyter notebook: Part 1, Stops 2 and 3, or Part 2, Sections 6 to 9.

**Prompt path.** The project can also be built with four prompts, one for each step, from the [prompt library](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/blob/main/en/week-07/PROMPTS.md#prompt-path-of-the-weekly-project). The section "Weekly project on the prompt path" at the end of Part 1 of the Jupyter notebook prepares the table of each prompt. The test of each prompt must hold before the next prompt is used.

**Example.** The detector of the course found 30 of the 386 stenoses of the test angiograms with 124 false detections over the 300 angiograms, and 30 of its detections lay on a stenosis. Its lesion sensitivity is $30/386 = 0.078$ with 0.41 false detections per angiogram, and the positive predictive value of a detection is $30/(30 + 124) = 0.195$. The same kind of network separates curated patches with an AUC of 0.936; on whole angiograms, at the threshold chosen for at most one false detection per validation angiogram, it misses most stenoses.

**What to submit.** A report of one to two pages in the [report template](../templates/Report_Template.docx), with the table of the three networks and their intervals, the table of the thresholds at both prevalences, the lesion sensitivity and the false detections per angiogram of the detector, the ten cases of the fourth step and the half page for the heart team. Add the AI usage log (tool, prompt, what was checked, what was changed) and the Jupyter notebook with its outputs.

**Submission.** The weekly project is submitted before the session of Week 8 by e-mail to utkukose@sdu.edu.tr or utkukose@gmail.com. The e-mail holds the items listed under What to submit and the learning log exported from the interactive lab. Weekly projects count for 40 percent of the assessment, and the rubric is in the syllabus.

## With your own data

The lecture page closes with a section on applying the methods of the week to your own data: which question fits which method, what to check first, the approval of the ethics committee, the Turkish Law on the Protection of Personal Data (KVKK) and where to compute. [Read it on the lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#with-your-own-data).

## Optional research assignment

Search PubMed for one study, published in 2020 or later, that used a vision transformer or a hybrid of convolutions and attention on cardiac images: angiograms, echocardiograms, cardiac magnetic resonance or computed tomography. Summarise it in half a page: the images, their number and their centres, the task and the reference, whether the network was pretrained and on what, the comparison with a convolutional network, whether the test came from another centre, and how attention maps were used. The three questions of [the paper of the week](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#the-paper-of-the-week) can guide the summary. The assignment is not graded, and it prepares the half page of the weekly project.

## The virtual clinic after this week

In Week 7 the virtual clinic opens its catheterisation laboratory. Every one of its 2,311 patients with an angiography has two synthetic angiograms with the stenoses of the registry, which the reports of Week 6 describe. Networks of the course look for stenoses on these images and on the real angiograms of ARCADE, and a pretrained vision transformer acts as a quality gate for the echocardiograms of CAMUS. The results are in the section [The virtual clinic, stage 7](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#the-virtual-clinic-stage-7-catheterisation-laboratory) of the lecture page.

## Next week

**Week 8: Multimodal artificial intelligence and data fusion.** The heart team: The ECG, the images, the reports and the laboratory values of the virtual clinic come together in a model for major adverse cardiovascular events. See the [plan of the course](../../README.md#the-eleven-weeks).

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
