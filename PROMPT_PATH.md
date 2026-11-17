# Prompt path

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Course home](README.md) · [Python path](PYTHON_PATH.md) · [Türkçe](PROMPT_PATH.tr.md)

The course can be followed on three paths. All three lead to the same results, and the check of the course tests them in the same way. A participant can change the path at any exercise.

| Path | For whom | How an exercise is solved |
|---|---|---|
| Core path | Participants who are new to programming | The Python step and the exercises are typed by hand. Reference solutions sit in folded cells. |
| Prompt path | Participants who prefer to describe a task in words | A prompt on the prompt card goes to an artificial intelligence (AI) assistant. The code that comes back is run and checked. |
| Advanced path | Participants who already program | Cells marked *Advanced path* add optional extensions to the same notebook. |

The prompt path does not skip Python. It changes the order of learning. The participant first states exactly what the code must do and how its result will be checked. Then the participant reads, runs and explains code written by an assistant. Reading and explaining code are part of every exercise, so the language is learned along the way.

## The prompt card

Every prompt of the course has the same seven fields.

| Field | What it states |
|---|---|
| Role | Who the assistant should be, for example a helper of a cardiologist who is learning Python |
| Context | Where the code runs and what is ready: the Jupyter notebook, the imported packages and the course package `vclinic` |
| Data | Variable names, units and sampling frequency |
| Task | One clear task, with its formula if there is one |
| Constraints | Packages to use and things to avoid, such as loading files or installing packages |
| Output | Variable name, rounding and form of the answer. The prompts of the exercises end with the line `teach.check`. |
| Test | A case whose answer is known by hand |

## The prompt cycle

Each exercise on the prompt path follows six steps.

| Step | What to do |
|---|---|
| 1. Describe | Copy the prompt card of the exercise, or write it with the seven fields: role, context, data, task, constraints, output and test. |
| 2. Generate | Send the prompt to an AI assistant. |
| 3. Run | Paste the code into the empty cell below the exercise and run it. |
| 4. Check | Read the result of `teach.check`, *correct* or *not yet*, and the test of the prompt. A result of *not yet* goes back to the assistant with the repair pattern. |
| 5. Explain | Ask the assistant for a line-by-line explanation, then explain the code once more in your own words. |
| 6. Log | Add the tool, the prompt, what was checked and what was changed to the AI usage log. |

Code written by an assistant is accepted only when its result passes a check against a known answer and every line can be explained.

## Where the prompts are

| Week | Prompt library | Prompt routes | Prompt challenges | Interactive lab |
|---|---|---|---|---|
| 1 | [PROMPTS.md](en/week-01/PROMPTS.md) | 13, one below each exercise | 9, one at the end of each numbered section | Part F, prompt workshop |
| 2 | [PROMPTS.md](en/week-02/PROMPTS.md) | 13, one below each exercise | 9, one at the end of each numbered section | Part F, prompt workshop |
| 3 | [PROMPTS.md](en/week-03/PROMPTS.md) | 13, one below each exercise | 9, one at the end of each numbered section | Part F, prompt workshop |
| 4 to 11 | In preparation | | | |

In the Jupyter notebook, a *prompt route* is a folded cell below an exercise. It holds the prompt card of the exercise, ready to copy. A *prompt challenge* closes each numbered section. It gives a prompt but no prepared code, and the checks below it tell whether the result is right. The prompt library of the week collects all prompts, four patterns for explaining, repairing and testing code, and the prompt route of the weekly project. Part F of the interactive lab trains the prompt card with a quality meter and a privacy check.

## AI assistants

Any assistant that writes Python can be used, and the prompts of the course work with all of them. Three assistants work inside the notebook environments of the course.

| Assistant | Where it runs | What to know |
|---|---|---|
| [Jupyter AI](https://jupyter-ai.readthedocs.io/en/latest/) | JupyterLab in Anaconda | An open-source extension with a chat panel and the `%%ai` magic command. It needs the application programming interface (API) key of a model provider or a local model, for example through Ollama. Providers may charge for their use. |
| [Anaconda Assistant](https://docs.anaconda.com/anaconda-notebooks/local-assistant) | JupyterLab in Anaconda, through Anaconda Toolbox (`conda install anaconda-toolbox`) | It needs an Anaconda account. A free account has a limited number of requests. |
| [Gemini in Colab](https://developers.googleblog.com/en/new-ai-first-google-colab-now-available-to-everyone/) | Google Colab, the fallback environment of the course | Built into Colab. It generates code from a description and explains errors. The features may differ by account and region. |
| A general chat assistant | Web browser | The prompt is pasted into the chat, and the code is copied back into the notebook. |

The course does not depend on any one of these tools. Assistants change often, so the setup of each tool follows its own documentation.

## Privacy

No patient data enter a prompt. This includes names, dates of birth, national identity numbers, hospital and protocol numbers, dates of admission, free text from medical records and images that carry identifiers. The prompts of the course describe the structure of the data, such as column names, units and the sampling frequency, never a real patient. Real patient data stay on the participant's own computer, under the rules of the institution and of the Turkish Law on the Protection of Personal Data (KVKK) [1]. A local model keeps the text of a prompt on the computer, but the rule holds for every tool. The privacy check in Part F of the interactive lab warns about common identifiers, such as dates and long numbers. It sees only common patterns, and the responsibility stays with the participant.

## The AI usage log and assessment

Code from the prompt path counts like code typed by hand. A weekly project is scored on its results, its methods and their explanation, its discussion and its records, as the [syllabus](SYLLABUS.md#assessment-and-certificate) describes. The way the code was written does not change the score. Each weekly project adds an AI usage log with one row for each use of an assistant: the tool, the prompt, what was checked and what was changed. Prompts saved in the prompt workshop of the interactive lab go into the learning log of the week.

## References

1. Kişisel Verilerin Korunması Kanunu [Law on the Protection of Personal Data], Law No. 6698. (2016). *Resmî Gazete, 29677 (7 April 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
