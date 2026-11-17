# Prompt path

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Course home](README.md) · [Python path](PYTHON_PATH.md) · [Your own data](OWN_DATA.md) · [Türkçe](PROMPT_PATH.tr.md)

The course has one main route, the lecture page of each week, and two paths of practice in the Jupyter notebook of the week. The **prompt path** is Part 1 of every notebook. It is meant for participants who do not write code and who may never have used an artificial intelligence (AI) assistant. An AI assistant writes the code from a ready prompt, a written instruction; the participant runs the code and checks the result. The **Python path**, Part 2 of the notebook, reaches the same results by writing the code ([PYTHON_PATH.md](PYTHON_PATH.md)). The path can be changed at any practice stop.

## What happens at a practice stop

The lecture page has two or three practice stops each week. At a stop, the button **Prompt path** opens Part 1 of the notebook at the same stop, in Google Colab or in Jupyter on your own computer. A stop has two to four steps, and every step looks the same.

| Step | What to do |
|---|---|
| 1. Read | Read the goal of the step in the notebook. |
| 2. Copy and send | Copy the prompt and send it to an AI assistant: Gemini in Google Colab, or ChatGPT, Claude, Copilot or Gemini in another browser tab. |
| 3. Run | Paste the code of the assistant into the cell below the prompt and run it. |
| 4. Check | Run the check cell. It prints *correct* or *not yet* and the value of the result. |
| 5. Repair | If the check prints *not yet*, send the repair prompt with the code. If the result is still wrong, run the *Ready code* cell, which gives the correct result. |
| 6. Explain and log | Ask the assistant to explain the code in plain language, and write the tool, the prompt and what was checked in the AI usage log. |

Every stop starts with a preparation cell that loads the data of the stop, so a stop can also be started on another day. The *Ready code* cell of each step always gives the correct result: Nobody gets stuck, and the next step can always start.

## Which assistant?

Any assistant that writes Python can be used, and the prompts of the course work with all of them.

| Assistant | Where it runs | What to know |
|---|---|---|
| [Gemini in Colab](https://developers.googleblog.com/en/new-ai-first-google-colab-now-available-to-everyone/) | Google Colab | Built into Colab and opened with its button at the top of the window. It writes code from a description and explains errors. The features may differ by account and region. |
| A chat assistant such as ChatGPT, Claude, Copilot or Gemini | A second tab of the web browser | The prompt is pasted into the chat, and the code is copied back into the notebook. |
| [Anaconda Assistant](https://docs.anaconda.com/anaconda-notebooks/local-assistant) | JupyterLab in Anaconda, through Anaconda Toolbox (`conda install anaconda-toolbox`) | It needs an Anaconda account. A free account has a limited number of requests. |
| [Jupyter AI](https://jupyter-ai.readthedocs.io/en/latest/) | JupyterLab in Anaconda | An open-source extension with a chat panel. It needs the application programming interface (API) key of a model provider or a local model. Providers may charge for their use. |

The course does not depend on any one of these tools. Assistants change often, so the setup of each tool follows its own documentation.

## The prompt card

Every prompt of the course has the same seven fields, and reading them teaches how to write a good request to an assistant.

| Field | What it states |
|---|---|
| Role | Who the assistant should be: a helper of a cardiologist who does not write code |
| Context | Where the code runs and what is ready: the Jupyter notebook, the imported packages and the course package `vclinic` |
| Data | The names of the variables, their units and, for signals, the sampling frequency |
| Task | One clear task, with its formula if there is one |
| Constraints | What the code may not do, such as reading files or installing packages |
| Output | The name of the variable that holds the result and its rounding |
| Test | A case whose answer is known, so that the result can be checked |

An assistant can write code that runs without an error and still gives a wrong number. The check of every step is therefore the most important part of the prompt path.

## Where the prompts are

| Week | Prompt library | Prompt path | Interactive lab |
|---|---|---|---|
| 1 | [PROMPTS.md](en/week-01/PROMPTS.md) | 3 stops with 10 steps | Part F, prompt workshop |
| 2 | [PROMPTS.md](en/week-02/PROMPTS.md) | 3 stops with 9 steps | Part F, prompt workshop |
| 3 | [PROMPTS.md](en/week-03/PROMPTS.md) | 3 stops with 10 steps | Part F, prompt workshop |
| 4 to 11 | In preparation | | |

The prompt library of the week holds every prompt of Part 1 with a copy button on GitHub, the prompts for repairing code and the prompt path of the weekly project. Part F of the interactive lab trains the prompt card with a quality meter and a privacy check.

## Privacy

No patient data enter a prompt. This includes names, dates of birth, national identity numbers, hospital and protocol numbers, dates of admission, free text from medical records and images that carry identifiers. The prompts of the course describe the structure of the data, such as column names, units and the sampling frequency, never a real patient. Real patient data stay on a computer of the institution, under its rules and those of the Turkish Law on the Protection of Personal Data (KVKK) [1]. [OWN_DATA.md](OWN_DATA.md) explains how the prompt path is used with one's own data: The prompt describes the columns, and the data never leave the computer.

## The AI usage log and assessment

Code from the prompt path counts like code typed by hand. A weekly project is scored on its results, its methods and their explanation, its discussion and its records, as the [syllabus](SYLLABUS.md#assessment-and-certificate) describes. Each weekly project adds an AI usage log with one row for each use of an assistant: the tool, the prompt, what was checked and what was changed.

## References

1. Kişisel Verilerin Korunması Kanunu [Law on the Protection of Personal Data], Law No. 6698. (2016). *Resmî Gazete, 29677 (7 April 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
