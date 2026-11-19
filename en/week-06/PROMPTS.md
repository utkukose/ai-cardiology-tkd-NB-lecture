# Prompt library, Week 6

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Week 6](README.md) · [Prompt path](../../PROMPT_PATH.md) · [Türkçe](../../tr/hafta-06/PROMPTLAR.md)

This library holds every prompt of the prompt path of Week 6, Part 1 of the Jupyter notebook, written on the prompt card of the course. Each prompt can be copied as it stands into an artificial intelligence (AI) assistant; GitHub shows a copy button in the corner of each box. The code that comes back goes into the notebook, into the empty cell of the step of the same number, and runs there. The [guide to the prompt path](../../PROMPT_PATH.md) explains the route as a whole.

No prompt of the course contains patient data, and none should be added. Real patient data never enter a prompt, a cloud notebook or an AI chat.

1. [How a step works](#how-a-step-works)
2. [Stop 1: Six diagnoses from discharge summaries: rules and a model](#stop-1-six-diagnoses-from-discharge-summaries-rules-and-a-model)
3. [Stop 2: Entities with a pretrained Turkish model](#stop-2-entities-with-a-pretrained-turkish-model)
4. [Stop 3: Angiography reports: the degree of stenosis and the vessel](#stop-3-angiography-reports-the-degree-of-stenosis-and-the-vessel)
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

## Stop 1: Six diagnoses from discharge summaries: rules and a model

*[Lecture page: practice stop 1](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-06/lecture.html#stop-1) · The same result on the Python path: Python step 6, Sections 1 to 5*

This stop is the mini project of the session. The six chronic diagnoses are read from the discharge summaries of the virtual clinic, first by searching for their words, then with the assertion of every mention, then with the drugs and two laboratory values, and finally by a model that learns from the training summaries. Every method is judged on the test set of hospital A, and the model also on the summaries of hospital B.

### Step 1.1: A keyword rule

**Goal.** Search the summaries for the words of six diagnoses and see where a search for words goes wrong.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how well a simple search for the words of a diagnosis finds
six chronic diagnoses in discharge summaries.
Data: The notebook holds a table named "data" with the 600 discharge summaries of the test set of
hospital A of the virtual clinic, a synthetic registry. Each row is a patient: "summary" holds the
discharge summary in Turkish, and the six columns "HF", "AF", "CAD", "HT", "DM" and "CKD" hold 0 or
1, with 1 when the registry records heart failure, atrial fibrillation, coronary artery disease,
hypertension, diabetes mellitus and chronic kidney disease, and 0 otherwise.
Task: Bring every text to small letters by the Turkish rules: First turn I into ı and İ into i, then
make the other letters small. Look for these words of each diagnosis as whole words, so that no word
is found inside a longer word: heart failure "kalp yetersizliği", "kalp yetmezliği", "konjestif kalp
yetmezliği", "ky" and "kky"; atrial fibrillation "atriyal fibrilasyon", "af" and "afib"; coronary
artery disease "koroner arter hastalığı", "kah", "iskemik kalp hastalığı", "miyokard enfarktüsü" and
"akut koroner sendrom"; hypertension "hipertansiyon" and "ht"; diabetes mellitus "diyabet",
"diyabetes mellitus" and "dm"; chronic kidney disease "kronik böbrek hastalığı", "kronik böbrek
yetmezliği", "kbh" and "kby". A diagnosis is present when at least one of its words is found
anywhere in the summary. Compare the six decisions with the six columns of the registry and compute,
for each diagnosis, the sensitivity, the positive predictive value and the F1 score (twice the true
positives divided by twice the true positives plus the false positives plus the false negatives),
and the mean of the six F1 scores, the macro F1.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print a table with one row for each diagnosis and the three values, and the macro F1. Keep
the positive predictive value of atrial fibrillation, with three decimals, under the name "answer".
Test: Every value must lie between 0 and 1, and the summary of patient VC-2444 must be called
positive for heart failure, atrial fibrillation and coronary artery disease.
```

**Expected result:** "answer" = 0.19

### Step 1.2: The assertion of every mention

**Goal.** Leave out the mentions that are negated, possible or in a relative.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how much a search for the words of six diagnoses in
discharge summaries improves when mentions that are negated, only suspected or about a relative are
left out.
Data: The notebook holds a table named "data" with the 600 discharge summaries of the test set of
hospital A of the virtual clinic, a synthetic registry. Each row is a patient: "summary" holds the
discharge summary in Turkish, and the six columns "HF", "AF", "CAD", "HT", "DM" and "CKD" hold 0 or
1, with 1 when the registry records heart failure, atrial fibrillation, coronary artery disease,
hypertension, diabetes mellitus and chronic kidney disease, and 0 otherwise.
Task: Bring every text to small letters by the Turkish rules: First turn I into ı and İ into i, then
make the other letters small. Look for these words of each diagnosis as whole words, so that no word
is found inside a longer word: heart failure "kalp yetersizliği", "kalp yetmezliği", "konjestif kalp
yetmezliği", "ky" and "kky"; atrial fibrillation "atriyal fibrilasyon", "af" and "afib"; coronary
artery disease "koroner arter hastalığı", "kah", "iskemik kalp hastalığı", "miyokard enfarktüsü" and
"akut koroner sendrom"; hypertension "hipertansiyon" and "ht"; diabetes mellitus "diyabet",
"diyabetes mellitus" and "dm"; chronic kidney disease "kronik böbrek hastalığı", "kronik böbrek
yetmezliği", "kbh" and "kby". A mention does not count when, after it and before the end of its
sentence or the next mention of another diagnosis, one of these words follows: "yok", "izlenmedi",
"saptanmadı", "tanımlamıyor", "dışlandı" or "(-)" (negated), or "şüphe", "olası" or "ön tanı"
(possible). It does not count either when, earlier in the same sentence, one of these words stands:
"babası", "annesi", "kardeşi", "babada", "annede" or "soygeçmiş" (a relative). A diagnosis is
present when at least one of its mentions counts. Compare the six decisions with the six columns of
the registry and compute, for each diagnosis, the sensitivity, the positive predictive value and the
F1 score (twice the true positives divided by twice the true positives plus the false positives plus
the false negatives), and the mean of the six F1 scores, the macro F1.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print a table with one row for each diagnosis and the three values, and keep the macro F1,
with three decimals, under the name "answer".
Test: The positive predictive value of atrial fibrillation must be higher than in step 1.1, and the
summary of patient VC-2444 must be positive only for heart failure.
```

**Expected result:** "answer" = 0.856

### Step 1.3: Drugs and laboratory values

**Goal.** Add the evidence that is not a word for the disease: drugs, eGFR and HbA1c.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to find six chronic diagnoses in discharge summaries also when the
summary does not name them but lists a drug that is given for them or a laboratory value that
defines them.
Data: The notebook holds a table named "data" with the 600 discharge summaries of the test set of
hospital A of the virtual clinic, a synthetic registry. Each row is a patient: "summary" holds the
discharge summary in Turkish, and the six columns "HF", "AF", "CAD", "HT", "DM" and "CKD" hold 0 or
1, with 1 when the registry records heart failure, atrial fibrillation, coronary artery disease,
hypertension, diabetes mellitus and chronic kidney disease, and 0 otherwise.
Task: Bring every text to small letters by the Turkish rules: First turn I into ı and İ into i, then
make the other letters small. Look for these words of each diagnosis as whole words, so that no word
is found inside a longer word: heart failure "kalp yetersizliği", "kalp yetmezliği", "konjestif kalp
yetmezliği", "ky" and "kky"; atrial fibrillation "atriyal fibrilasyon", "af" and "afib"; coronary
artery disease "koroner arter hastalığı", "kah", "iskemik kalp hastalığı", "miyokard enfarktüsü" and
"akut koroner sendrom"; hypertension "hipertansiyon" and "ht"; diabetes mellitus "diyabet",
"diyabetes mellitus" and "dm"; chronic kidney disease "kronik böbrek hastalığı", "kronik böbrek
yetmezliği", "kbh" and "kby". A mention does not count when, after it and before the end of its
sentence or the next mention of another diagnosis, one of these words follows: "yok", "izlenmedi",
"saptanmadı", "tanımlamıyor", "dışlandı" or "(-)" (negated), or "şüphe", "olası" or "ön tanı"
(possible). It does not count either when, earlier in the same sentence, one of these words stands:
"babası", "annesi", "kardeşi", "babada", "annede" or "soygeçmiş" (a relative). A diagnosis is
present when at least one of its mentions counts. A diagnosis is also present when the summary names
one of its drugs, as a whole word or the start of a word: heart failure "furosemid" or "sakubitril";
atrial fibrillation "apiksaban", "rivaroksaban", "edoksaban" or "dabigatran"; coronary artery
disease "klopidogrel", "tikagrelor", "pkg", "kabg" or "stent"; hypertension "amlodipin" or
"hidroklorotiyazid"; diabetes mellitus "metformin", "gliklazid", "insülin" or "sitagliptin". Chronic
kidney disease is present when the first number after "egfr" is below 60, and diabetes mellitus when
the first number after "hba1c" and an optional percent sign is 6.5 or more; these numbers use a
decimal comma. Compare the six decisions with the six columns of the registry and compute, for each
diagnosis, the sensitivity, the positive predictive value and the F1 score (twice the true positives
divided by twice the true positives plus the false positives plus the false negatives), and the mean
of the six F1 scores, the macro F1.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print a table with one row for each diagnosis and the three values, and keep the macro F1,
with three decimals, under the name "answer".
Test: The sensitivity of chronic kidney disease must be 1, and the summary of patient VC-2444 must
be positive for heart failure, hypertension and chronic kidney disease.
```

**Expected result:** "answer" = 0.98

### Step 1.4: A model that learns from the summaries: TF-IDF and logistic regression

**Goal.** Train a model on the summaries of hospital A and judge it on hospital A and on hospital B.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to train a model that finds six chronic diagnoses in discharge
summaries from examples, and to know how well it works in its own hospital and in another hospital
that writes in another style.
Data: The notebook holds a table named "data" with the 3,600 discharge summaries of the virtual
clinic, a synthetic registry. Each row is a patient: "set" gives the set of the summary ("training",
1,800 summaries; "validation", 600; "test", 600, all three from hospital A; "external", 600
summaries from hospital B, written in a short style with (+) and (-)), "summary" holds the discharge
summary in Turkish, and the six columns "HF", "AF", "CAD", "HT", "DM" and "CKD" hold 0 or 1, with 1
when the registry records heart failure, atrial fibrillation, coronary artery disease, hypertension,
diabetes mellitus and chronic kidney disease, and 0 otherwise.
Task: Bring every text to small letters by the Turkish rules: First turn I into ı and İ into i, then
make the other letters small. Turn every summary into a vector of TF-IDF weights of its words and of
its pairs of neighbouring words; a word is a run of letters and digits, and only the terms that
occur in at least two training summaries are kept. Learn the terms and their weights from the
training summaries only, use the logarithm of the count plus one as the frequency of a term, and
scale every vector to length 1. For each diagnosis, train a logistic regression with an inverse
regularisation strength of 10 on the training summaries. On the validation summaries, choose for
each diagnosis the threshold of the probability, from 0.05 to 0.95 in steps of 0.05, where its F1
score is highest. With these thresholds, compute the F1 score of each diagnosis and the macro F1 on
the test summaries and on the external summaries.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print a table with the F1 score of each diagnosis on the test and on the external summaries,
and keep the macro F1 on the external summaries, with three decimals, under the name "answer".
Test: The terms must come from the training summaries only, the thresholds from the validation
summaries only, and the macro F1 on the test summaries must be above 0.9.
```

**Expected result:** "answer" = 0.708

## Stop 2: Entities with a pretrained Turkish model

*[Lecture page: practice stop 2](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-06/lecture.html#stop-2) · The same result on the Python path: Sections 6 to 8*

A pretrained Turkish language model from the Hugging Face Hub reads the summaries here. Its tokenizer shows first what the capital letters of hospital B do to a model. The model is then fine-tuned to find diagnoses, drugs and procedures, and its entities, with the assertion rule and the drugs of Stop 1, give the six diagnoses of the summaries of hospital B.

### Step 2.1: The tokens of a pretrained Turkish model

**Goal.** See how a pretrained Turkish model cuts the summaries of hospital B into tokens, and what the case of the letters changes.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to use a pretrained Turkish language model on discharge summaries
written partly in capitals, and to know whether the model knows their words.
Data: The notebook holds a table named "data" with the 600 discharge summaries of hospital B of the
virtual clinic, a synthetic registry, written in Turkish in a short style with abbreviations in
capitals. Each row is a patient, and "summary" holds the discharge summary.
Task: Load the tokenizer of the model "ytu-ce-cosmos/turkish-tiny-bert-uncased" from the Hugging
Face Hub. Cut every summary into tokens three times: as it is written, after the usual lower case of
the programming language, and after the Turkish lower case (first I becomes ı and İ becomes i, then
the other letters become small). For each of the three, count the tokens without the special tokens
at the start and the end, and compute the percentage of them that are the unknown token. Also show
the tokens of the first summary in all three forms.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the number of tokens and the percentage of unknown tokens for the three forms, and
keep the percentage for the text as written, with one decimal, under the name "answer".
Test: The Turkish lower case must leave no unknown token, and the first summary must give more
tokens after the usual lower case than after the Turkish one or the same number.
```

**Expected result:** "answer" = 19.5

### Step 2.2: Fine-tuning the model for entities

**Goal.** Teach the pretrained model to tag diagnoses, drugs and procedures. The training takes a few minutes.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to adapt a small pretrained Turkish language model so that it finds
the diagnoses, drugs and procedures of discharge summaries, and to know how exactly it finds them in
summaries it has not seen.
Data: The notebook holds a table named "data" with 3,000 discharge summaries of the virtual clinic,
a synthetic registry. Each row is a patient: "set" gives the set ("training", 1,800 summaries of
hospital A; "test", 600 of hospital A; "external", 600 of hospital B), "summary" holds the discharge
summary in Turkish, and "entities" lists its annotated entities, each as (first character, last
character plus one, type), counted from 0, with the types "DIAG" for a diagnosis, "DRUG" for a drug
and "PROC" for a procedure; the six columns "HF", "AF", "CAD", "HT", "DM" and "CKD" hold 0 or 1,
with 1 when the registry records heart failure, atrial fibrillation, coronary artery disease,
hypertension, diabetes mellitus and chronic kidney disease, and 0 otherwise.
Task: Use the model "ytu-ce-cosmos/turkish-tiny-bert-uncased" from the Hugging Face Hub with a layer
that gives every token one of seven tags: outside an entity, or the beginning or the inside of a
diagnosis, a drug or a procedure. Bring every summary to the Turkish lower case (first I becomes ı
and İ becomes i), which keeps the positions of the characters, and cut it into at most 384 tokens. A
token gets the tag of the entity in which its first character lies: the beginning tag when it starts
the entity, the inside tag otherwise. Fine-tune the model on the training summaries for 4 epochs, in
shuffled groups of 16 summaries, with the optimiser AdamW and a learning rate of 0.0003. Then tag
the test summaries and the external summaries, join the tokens of every entity back into a stretch
of characters, and compute the precision, the recall and the F1 score of the entities, where a
predicted entity counts only when its type, its first character and its last character match an
annotated one. Fix the random seed to 2026 so that the result can be repeated.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the loss of every epoch and a table with the precision, the recall and the F1 score
for all entities and for each type, on the test and on the external summaries, and keep the F1 score
of all entities on the test summaries, with three decimals, under the name "answer".
Test: The loss must fall from the first to the last epoch, and the F1 score must lie between 0 and
1.
```

**Expected result:** "answer" = 0.981

### Step 2.3: From entities to the six diagnoses of hospital B

**Goal.** Turn the entities of the model into the six diagnoses of every summary of hospital B, with the assertion rule and the drugs of Stop 1.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to turn the diagnoses and drugs that a language model found in
discharge summaries of another hospital into the six chronic diagnoses of every patient, and to know
how well this works.
Data: The notebook holds a table named "data" with the 600 discharge summaries of hospital B of the
virtual clinic, a synthetic registry, written in Turkish in a short style. Each row is a patient:
"summary" holds the discharge summary; "entities" lists its annotated entities and "model entities"
the entities that the tiny Turkish language model of the course, fine-tuned on the training
summaries of hospital A, found in it, both as (first character, last character plus one, type),
counted from 0, with the types "DIAG" for a diagnosis, "DRUG" for a drug and "PROC" for a procedure;
the six columns "HF", "AF", "CAD", "HT", "DM" and "CKD" hold 0 or 1, with 1 when the registry
records heart failure, atrial fibrillation, coronary artery disease, hypertension, diabetes mellitus
and chronic kidney disease, and 0 otherwise.
Task: Use the column "model entities". Give every diagnosis entity to one of the six diagnoses by
its words, as in Stop 1, and decide its assertion with the rule of Stop 1; a diagnosis is present
when one of its entities is present. Add the diagnoses of the drug entities and of the values of
eGFR and HbA1c, as in Stop 1. Compare the six decisions with the six columns of the registry and
compute, for each diagnosis, the sensitivity, the positive predictive value and the F1 score (twice
the true positives divided by twice the true positives plus the false positives plus the false
negatives), and the mean of the six F1 scores, the macro F1.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print a table with one row for each diagnosis and the three values, and keep the macro F1,
with three decimals, under the name "answer".
Test: Every value must lie between 0 and 1, and a summary without any entity must be negative for
every diagnosis except chronic kidney disease and diabetes, which can come from the laboratory
values.
```

**Expected result:** "answer" = 0.754

## Stop 3: Angiography reports: the degree of stenosis and the vessel

*[Lecture page: practice stop 3](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-06/lecture.html#stop-3) · The same result on the Python path: Section 9*

The angiography reports of the virtual clinic are read here as a registry would read them. The pipeline of the lecture finds the arteries, the segments and the degrees of stenosis of a report, keeps the largest stenosis of every territory and counts the diseased vessels. It is applied first to one report, then to the test reports of hospital A and finally to the reports of hospital B, which are written in capitals.

### Step 3.1: One report, sentence by sentence

**Goal.** Read one angiography report as the pipeline of the lecture does.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants a program that reads a coronary angiography report written in
Turkish and gives the largest stenosis of every coronary territory and the number of diseased
vessels.
Data: The notebook holds a table named "data" with one row: "report" holds the coronary angiography
report of patient VC-2914 of the virtual clinic, a synthetic registry, written in Turkish.
Task: Read the report sentence by sentence; a sentence ends at a full stop that is followed by a
space and a capital letter or a digit. Bring every sentence to small letters by the Turkish rules
(first I becomes ı and İ becomes i). Skip the sentences that start with "endikasyon", "öykü", "sol
ventrikülografi", "sv:", "girişim" or "işlem". In every other sentence, find the first artery that
it names: the left main "sol ana koroner" or "lmca"; the LAD "sol ön inen" or "lad", with its
branches "birinci diyagonal", "1. diyagonal" or "d1" and "ikinci diyagonal", "2. diyagonal" or "d2";
the circumflex "sirkumfleks", "cx" or "lcx", with its branches "birinci obtus", "1. obtus" or "om1"
and "ikinci obtus", "2. obtus" or "om2"; the RCA "sağ koroner" or "rca", with "arka inen",
"posterior desendan" or "pda". Short names count only as whole words. A sentence without an artery
belongs to the artery of the sentence before. Read every degree of stenosis of the sentence: a
number after "%" or "yüzde " (a range such as "%70-80" counts as its upper end, 80), and the words
"total oklüzyon", "tam tıkanıklık" or "to" (100), "subtotal" (99), "kritik" (95), "ileri derecede"
(80), "orta derecede" (60), and "hafif", "plak" or "plaklı" (30). Give every value to the territory
of its artery (the branches belong to the territory of their main artery) and keep the largest value
of each territory; a territory without a value has 0. The number of diseased vessels counts the
territories LAD, LCX and RCA with 70 or more. Show every sentence with the artery it belongs to and
the values found in it.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the sentences, the largest stenosis of the four territories LM, LAD, LCX and RCA, and
the number of diseased vessels, and keep the number of diseased vessels under the name "answer".
Test: The sentence "Proksimal segmentinde ileri derecede darlık saptandı." must belong to the RCA,
and the number of the catheters, 6, must not appear as a stenosis.
```

**Expected result:** "answer" = 3

### Step 3.2: All test reports of hospital A

**Goal.** Apply the pipeline to every test report and compare it with the registry.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how often a program that reads coronary angiography reports
gives the same number of diseased vessels and the same degree of stenosis as the registry.
Data: The notebook holds a table named "data" with the 394 coronary angiography reports of the test
set of hospital A of the virtual clinic, a synthetic registry, written in Turkish. Each row is a
patient: "report" holds the report, the four columns "LM", "LAD", "LCX" and "RCA" give the largest
stenosis in percent of the territories of the left main coronary artery, the left anterior
descending artery with its diagonal branches, the left circumflex artery with its obtuse marginal
branches, and the right coronary artery with the posterior descending artery, as recorded in the
registry, and "diseased vessels" gives the number of the territories LAD, LCX and RCA with a
stenosis of 70 percent or more.
Task: Read the report sentence by sentence; a sentence ends at a full stop that is followed by a
space and a capital letter or a digit. Bring every sentence to small letters by the Turkish rules
(first I becomes ı and İ becomes i). Skip the sentences that start with "endikasyon", "öykü", "sol
ventrikülografi", "sv:", "girişim" or "işlem". In every other sentence, find the first artery that
it names: the left main "sol ana koroner" or "lmca"; the LAD "sol ön inen" or "lad", with its
branches "birinci diyagonal", "1. diyagonal" or "d1" and "ikinci diyagonal", "2. diyagonal" or "d2";
the circumflex "sirkumfleks", "cx" or "lcx", with its branches "birinci obtus", "1. obtus" or "om1"
and "ikinci obtus", "2. obtus" or "om2"; the RCA "sağ koroner" or "rca", with "arka inen",
"posterior desendan" or "pda". Short names count only as whole words. A sentence without an artery
belongs to the artery of the sentence before. Read every degree of stenosis of the sentence: a
number after "%" or "yüzde " (a range such as "%70-80" counts as its upper end, 80), and the words
"total oklüzyon", "tam tıkanıklık" or "to" (100), "subtotal" (99), "kritik" (95), "ileri derecede"
(80), "orta derecede" (60), and "hafif", "plak" or "plaklı" (30). Give every value to the territory
of its artery (the branches belong to the territory of their main artery) and keep the largest value
of each territory; a territory without a value has 0. The number of diseased vessels counts the
territories LAD, LCX and RCA with 70 or more. Apply this to every report. Put every largest
stenosis, of the program and of the registry, into one of five categories: below 50, 50 to 69, 70 to
89, 90 to 99 and 100 percent. Compute for each territory the share of reports in which the
categories agree, and the share of reports in which the number of diseased vessels agrees. Show the
reports in which the number of diseased vessels differs.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the four shares of the territories and the share for the number of diseased vessels,
and keep the last, with three decimals, under the name "answer".
Test: Every share must lie between 0 and 1, and the program must find 3 diseased vessels in the
report of patient VC-2914.
```

**Expected result:** "answer" = 0.959

### Step 3.3: The reports of hospital B, in capitals

**Goal.** Apply the same pipeline to the reports of another hospital, written in capitals and in a short style.

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know whether a program that reads the coronary angiography
reports of one hospital also reads those of another hospital, written in capitals and in a short
style.
Data: The notebook holds a table named "data" with the 373 coronary angiography reports of the
hospital B of the virtual clinic, a synthetic registry, written in Turkish in capital letters. Each
row is a patient: "report" holds the report, the four columns "LM", "LAD", "LCX" and "RCA" give the
largest stenosis in percent of the territories of the left main coronary artery, the left anterior
descending artery with its diagonal branches, the left circumflex artery with its obtuse marginal
branches, and the right coronary artery with the posterior descending artery, as recorded in the
registry, and "diseased vessels" gives the number of the territories LAD, LCX and RCA with a
stenosis of 70 percent or more.
Task: Read the report sentence by sentence; a sentence ends at a full stop that is followed by a
space and a capital letter or a digit. Bring every sentence to small letters by the Turkish rules
(first I becomes ı and İ becomes i). Skip the sentences that start with "endikasyon", "öykü", "sol
ventrikülografi", "sv:", "girişim" or "işlem". In every other sentence, find the first artery that
it names: the left main "sol ana koroner" or "lmca"; the LAD "sol ön inen" or "lad", with its
branches "birinci diyagonal", "1. diyagonal" or "d1" and "ikinci diyagonal", "2. diyagonal" or "d2";
the circumflex "sirkumfleks", "cx" or "lcx", with its branches "birinci obtus", "1. obtus" or "om1"
and "ikinci obtus", "2. obtus" or "om2"; the RCA "sağ koroner" or "rca", with "arka inen",
"posterior desendan" or "pda". Short names count only as whole words. A sentence without an artery
belongs to the artery of the sentence before. Read every degree of stenosis of the sentence: a
number after "%" or "yüzde " (a range such as "%70-80" counts as its upper end, 80), and the words
"total oklüzyon", "tam tıkanıklık" or "to" (100), "subtotal" (99), "kritik" (95), "ileri derecede"
(80), "orta derecede" (60), and "hafif", "plak" or "plaklı" (30). Give every value to the territory
of its artery (the branches belong to the territory of their main artery) and keep the largest value
of each territory; a territory without a value has 0. The number of diseased vessels counts the
territories LAD, LCX and RCA with 70 or more. Apply this to every report and compute the share of
reports in which the number of diseased vessels agrees with the registry. Then repeat it with the
usual lower case of the programming language instead of the Turkish one and compute the share again.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the two shares, and keep the share with the Turkish lower case, with three decimals,
under the name "answer".
Test: The share with the Turkish lower case must be higher than with the usual lower case.
```

**Expected result:** "answer" = 1.0

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

### Ask for a review of a text pipeline

```text
Review the code below, which reads clinical reports in Turkish and reports diagnoses, entities or
stenoses. Check six points. Is the text brought to small letters by the Turkish rules, with I
becoming ı and İ becoming i, and does the code keep the positions of the characters? Are the reports
of one patient and of the external hospital kept out of the training set, and are the vocabulary and
the thresholds learned on the training and validation sets only? Does every rule look for negation,
the relative and uncertainty, in the right direction for Turkish, where the negation usually follows
the disease? Are numbers read as numbers, with the decimal comma and ranges, and kept apart from
numbers of other kinds, such as a dose, a catheter size or an ejection fraction? Are the results
given per diagnosis, with sensitivity, positive predictive value and F1, and on an external test
set? Is any text of a real patient sent to a service outside the institution? For each point, quote
the line of the code that is wrong and propose the correction.

[paste the code here]
```

## Prompt path of the weekly project

The [weekly project](README.md#weekly-project) can be built on the prompt path with four prompts, one for each step. The section *Weekly project on the prompt path* at the end of Part 1 of the Jupyter notebook prepares the table of each prompt. The project has no check and no ready code, because its results go into the report. The test of a step must hold before the next prompt is sent, and the report lists all four prompts in the AI usage log.

### Step 1: Territory by territory in both hospitals

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to build a program that reads the coronary angiography reports of
two hospitals for a registry, and to know how often it gives the same degree of stenosis as the
registry in every coronary territory.
Data: The notebook holds a table named "data" with the 767 coronary angiography reports of the test
set of hospital A (394) and of hospital B (373) of the virtual clinic, a synthetic registry, written
in Turkish; hospital B writes in capitals and in a short style. Each row is a patient: "set" gives
the set ("test" or "external"), "patient" the patient, "report" the report, the four columns "LM",
"LAD", "LCX" and "RCA" the largest stenosis in percent of the four coronary territories as recorded
in the registry, and "diseased vessels" the number of the territories LAD, LCX and RCA with a
stenosis of 70 percent or more. "summary" holds the discharge summary of the same patient.
Task: Read the report sentence by sentence; a sentence ends at a full stop that is followed by a
space and a capital letter or a digit. Bring every sentence to small letters by the Turkish rules
(first I becomes ı and İ becomes i). Skip the sentences that start with "endikasyon", "öykü", "sol
ventrikülografi", "sv:", "girişim" or "işlem". In every other sentence, find the first artery that
it names: the left main "sol ana koroner" or "lmca"; the LAD "sol ön inen" or "lad", with its
branches "birinci diyagonal", "1. diyagonal" or "d1" and "ikinci diyagonal", "2. diyagonal" or "d2";
the circumflex "sirkumfleks", "cx" or "lcx", with its branches "birinci obtus", "1. obtus" or "om1"
and "ikinci obtus", "2. obtus" or "om2"; the RCA "sağ koroner" or "rca", with "arka inen",
"posterior desendan" or "pda". Short names count only as whole words. A sentence without an artery
belongs to the artery of the sentence before. Read every degree of stenosis of the sentence: a
number after "%" or "yüzde " (a range such as "%70-80" counts as its upper end, 80), and the words
"total oklüzyon", "tam tıkanıklık" or "to" (100), "subtotal" (99), "kritik" (95), "ileri derecede"
(80), "orta derecede" (60), and "hafif", "plak" or "plaklı" (30). Give every value to the territory
of its artery (the branches belong to the territory of their main artery) and keep the largest value
of each territory; a territory without a value has 0. The number of diseased vessels counts the
territories LAD, LCX and RCA with 70 or more. Apply this to every report. Put every largest
stenosis, of the program and of the registry, into one of five categories: below 50, 50 to 69, 70 to
89, 90 to 99 and 100 percent. For each set and each territory, compute the share of reports in which
the categories agree, and the share of reports in which all four territories agree.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Show a table with one row for each set and the five shares, and keep the share of reports of
the set "test" in which all four territories agree, with three decimals, under the name "answer".
Test: There must be 394 reports in the set "test" and 373 in the set "external", and every share
must lie between 0 and 1.
```

### Step 2: The left main coronary artery and the number of diseased vessels

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how well a program that reads coronary angiography reports
finds left main disease and the number of diseased vessels, the two findings that decide between
surgery and stents.
Data: The notebook holds a table named "data" with the 767 coronary angiography reports of the test
set of hospital A (394) and of hospital B (373) of the virtual clinic, a synthetic registry, written
in Turkish; hospital B writes in capitals and in a short style. Each row is a patient: "set" gives
the set ("test" or "external"), "patient" the patient, "report" the report, the four columns "LM",
"LAD", "LCX" and "RCA" the largest stenosis in percent of the four coronary territories as recorded
in the registry, and "diseased vessels" the number of the territories LAD, LCX and RCA with a
stenosis of 70 percent or more. "summary" holds the discharge summary of the same patient.
Task: Read the report sentence by sentence; a sentence ends at a full stop that is followed by a
space and a capital letter or a digit. Bring every sentence to small letters by the Turkish rules
(first I becomes ı and İ becomes i). Skip the sentences that start with "endikasyon", "öykü", "sol
ventrikülografi", "sv:", "girişim" or "işlem". In every other sentence, find the first artery that
it names: the left main "sol ana koroner" or "lmca"; the LAD "sol ön inen" or "lad", with its
branches "birinci diyagonal", "1. diyagonal" or "d1" and "ikinci diyagonal", "2. diyagonal" or "d2";
the circumflex "sirkumfleks", "cx" or "lcx", with its branches "birinci obtus", "1. obtus" or "om1"
and "ikinci obtus", "2. obtus" or "om2"; the RCA "sağ koroner" or "rca", with "arka inen",
"posterior desendan" or "pda". Short names count only as whole words. A sentence without an artery
belongs to the artery of the sentence before. Read every degree of stenosis of the sentence: a
number after "%" or "yüzde " (a range such as "%70-80" counts as its upper end, 80), and the words
"total oklüzyon", "tam tıkanıklık" or "to" (100), "subtotal" (99), "kritik" (95), "ileri derecede"
(80), "orta derecede" (60), and "hafif", "plak" or "plaklı" (30). Give every value to the territory
of its artery (the branches belong to the territory of their main artery) and keep the largest value
of each territory; a territory without a value has 0. The number of diseased vessels counts the
territories LAD, LCX and RCA with 70 or more. Apply this to every report. Left main disease is a
largest stenosis of 50 percent or more in the territory LM. For each set, compute the sensitivity
and the positive predictive value of the program for left main disease against the column "LM", and
show a table of the number of diseased vessels of the registry against that of the program.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the two values for each set and the two tables, and keep the positive predictive value
for left main disease in the set "test", with three decimals, under the name "answer".
Test: The numbers of the two tables must add up to the number of reports of the set.
```

### Step 3: The errors and their causes

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to see every report that a program for coronary angiography reports
reads wrongly, and to find the sentence that misled it.
Data: The notebook holds a table named "data" with the 767 coronary angiography reports of the test
set of hospital A (394) and of hospital B (373) of the virtual clinic, a synthetic registry, written
in Turkish; hospital B writes in capitals and in a short style. Each row is a patient: "set" gives
the set ("test" or "external"), "patient" the patient, "report" the report, the four columns "LM",
"LAD", "LCX" and "RCA" the largest stenosis in percent of the four coronary territories as recorded
in the registry, and "diseased vessels" the number of the territories LAD, LCX and RCA with a
stenosis of 70 percent or more. "summary" holds the discharge summary of the same patient.
Task: Read the report sentence by sentence; a sentence ends at a full stop that is followed by a
space and a capital letter or a digit. Bring every sentence to small letters by the Turkish rules
(first I becomes ı and İ becomes i). Skip the sentences that start with "endikasyon", "öykü", "sol
ventrikülografi", "sv:", "girişim" or "işlem". In every other sentence, find the first artery that
it names: the left main "sol ana koroner" or "lmca"; the LAD "sol ön inen" or "lad", with its
branches "birinci diyagonal", "1. diyagonal" or "d1" and "ikinci diyagonal", "2. diyagonal" or "d2";
the circumflex "sirkumfleks", "cx" or "lcx", with its branches "birinci obtus", "1. obtus" or "om1"
and "ikinci obtus", "2. obtus" or "om2"; the RCA "sağ koroner" or "rca", with "arka inen",
"posterior desendan" or "pda". Short names count only as whole words. A sentence without an artery
belongs to the artery of the sentence before. Read every degree of stenosis of the sentence: a
number after "%" or "yüzde " (a range such as "%70-80" counts as its upper end, 80), and the words
"total oklüzyon", "tam tıkanıklık" or "to" (100), "subtotal" (99), "kritik" (95), "ileri derecede"
(80), "orta derecede" (60), and "hafif", "plak" or "plaklı" (30). Give every value to the territory
of its artery (the branches belong to the territory of their main artery) and keep the largest value
of each territory; a territory without a value has 0. The number of diseased vessels counts the
territories LAD, LCX and RCA with 70 or more. Apply this to every report of the set "test". Put
every largest stenosis, of the program and of the registry, into one of five categories: below 50,
50 to 69, 70 to 89, 90 to 99 and 100 percent. A report is wrong when at least one territory
disagrees. For every wrong report, show the territories that disagree and the sentences that name no
artery known to the program but contain a degree of stenosis.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the wrong reports with their territories and sentences, and keep the number of wrong
reports under the name "answer".
Test: The number of wrong reports cannot be larger than 394.
```

### Step 4: The angiography and the discharge summary together

```text
Role: You are helping a cardiologist who does not write code. The code will be pasted into a Jupyter
notebook and run there.
Context: The cardiologist wants to know how many patients with a significant coronary stenosis on
angiography have no coronary artery disease in their discharge summary, as a search of discharge
summaries would find it.
Data: The notebook holds a table named "data" with the 767 coronary angiography reports of the test
set of hospital A (394) and of hospital B (373) of the virtual clinic, a synthetic registry, written
in Turkish; hospital B writes in capitals and in a short style. Each row is a patient: "set" gives
the set ("test" or "external"), "patient" the patient, "report" the report, the four columns "LM",
"LAD", "LCX" and "RCA" the largest stenosis in percent of the four coronary territories as recorded
in the registry, and "diseased vessels" the number of the territories LAD, LCX and RCA with a
stenosis of 70 percent or more. "summary" holds the discharge summary of the same patient.
Task: Read the report sentence by sentence; a sentence ends at a full stop that is followed by a
space and a capital letter or a digit. Bring every sentence to small letters by the Turkish rules
(first I becomes ı and İ becomes i). Skip the sentences that start with "endikasyon", "öykü", "sol
ventrikülografi", "sv:", "girişim" or "işlem". In every other sentence, find the first artery that
it names: the left main "sol ana koroner" or "lmca"; the LAD "sol ön inen" or "lad", with its
branches "birinci diyagonal", "1. diyagonal" or "d1" and "ikinci diyagonal", "2. diyagonal" or "d2";
the circumflex "sirkumfleks", "cx" or "lcx", with its branches "birinci obtus", "1. obtus" or "om1"
and "ikinci obtus", "2. obtus" or "om2"; the RCA "sağ koroner" or "rca", with "arka inen",
"posterior desendan" or "pda". Short names count only as whole words. A sentence without an artery
belongs to the artery of the sentence before. Read every degree of stenosis of the sentence: a
number after "%" or "yüzde " (a range such as "%70-80" counts as its upper end, 80), and the words
"total oklüzyon", "tam tıkanıklık" or "to" (100), "subtotal" (99), "kritik" (95), "ileri derecede"
(80), "orta derecede" (60), and "hafif", "plak" or "plaklı" (30). Give every value to the territory
of its artery (the branches belong to the territory of their main artery) and keep the largest value
of each territory; a territory without a value has 0. The number of diseased vessels counts the
territories LAD, LCX and RCA with 70 or more. Apply this to every report; a patient has a
significant stenosis when the program finds at least one diseased vessel or left main disease. Then
read the discharge summary of the same patient: Bring every text to small letters by the Turkish
rules: First turn I into ı and İ into i, then make the other letters small. Coronary artery disease
is present in the summary when "koroner arter hastalığı", "kah", "iskemik kalp hastalığı", "miyokard
enfarktüsü" or "akut koroner sendrom" occurs as a whole word and is not followed, before the end of
its sentence or the next mention of another diagnosis, by "yok", "izlenmedi", "saptanmadı",
"tanımlamıyor", "dışlandı", "(-)", "şüphe", "olası" or "ön tanı", and is not preceded in its
sentence by "babası", "annesi", "kardeşi", "babada", "annede" or "soygeçmiş", or when the summary
names "klopidogrel", "tikagrelor", "pkg", "kabg" or "stent". For each set, count the patients with a
significant stenosis whose summary has no coronary artery disease.
Constraints: Use only this table. The code must not read files, download anything from the internet
or install programs.
Output: Print the counts for each set and three of these summaries, and keep the count of the set
"test" under the name "answer".
Test: The count cannot be larger than the number of patients of the set with a significant stenosis.
```

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
