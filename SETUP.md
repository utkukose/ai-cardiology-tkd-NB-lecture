# Setup

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Course home](README.md) · [Türkçe](SETUP.tr.md)

The Jupyter notebooks of the course run in Jupyter on the participant's own computer, installed with Anaconda. The steps below take about 20 minutes and are done once, before Week 1. Google Colab is a fallback for computers on which Anaconda cannot be installed.

## 1. Install Anaconda

Download the Anaconda Distribution for the operating system of the computer from [anaconda.com/download](https://www.anaconda.com/download) and install it with the default options. Anaconda brings Python, Jupyter and the packages that Week 1 needs: NumPy, pandas, SciPy and Matplotlib.

## 2. Download the course folder

On the [GitHub page of the course](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture), choose **Code** and then **Download ZIP**, and unzip the file into a folder of your choice. A folder outside cloud synchronisation, for example `Documents/courses` rather than a OneDrive folder, avoids locked files. With git, the same folder is created with:

```bash
git clone https://github.com/utkukose/ai-cardiology-tkd-NB-lecture.git
```

## 3. Start Jupyter

Open **Anaconda Navigator** and launch **JupyterLab** or **Jupyter Notebook**, then move to the course folder in the file browser on the left. Alternatively, open **Anaconda Prompt** on Windows or **Terminal** on macOS and Linux, go to the course folder and start JupyterLab:

```bash
cd path/to/ai-cardiology-tkd-NB-lecture
jupyter lab
```

## 4. Check the computer with the start-here notebook

Open `en/start-here/NB00_start_here.ipynb` and run all its cells with **Run → Run All Cells**. The notebook checks the packages, finds the course folder, draws a first ECG and prints **Ready for Week 1** when everything works.

## 5. Open the notebook of the week

Open the Jupyter notebook in the folder of the week, for example `en/week-01/NB01_python_and_ecg_basics.ipynb`, and run Section 0 first. The first cell finds the course folder, and the second prints the version of the course package `vclinic`. **Kernel → Restart Kernel and Run All Cells** starts the notebook again from a clean state.

## 6. Optional packages

The notebooks use `wfdb` and `neurokit2` when they are installed and a built-in fallback when they are not. To install them, run in Anaconda Prompt or Terminal:

```bash
pip install wfdb neurokit2
```

A separate environment with all packages of the course can be created from the file `environment.yml` in the course folder:

```bash
conda env create -f environment.yml
conda activate ai-cardiology
jupyter lab
```

## 7. Update the course folder every week

New weeks are added to the repository during the course. With git, `git pull` in the course folder brings the new files. Without git, download the ZIP file again. Keep your own copies of the notebooks in a separate folder, so that an update does not overwrite your work.

## An AI assistant for the prompt path

An artificial intelligence (AI) assistant is optional. It is needed only on the [prompt path](PROMPT_PATH.md), and any assistant that writes Python can be used. In Anaconda, Anaconda Assistant comes with Anaconda Toolbox. Install it from the Anaconda Toolbox tile in Navigator or with the command below. Then open a notebook in JupyterLab and sign in with an Anaconda account. A free account has a limited number of requests.

```bash
conda install anaconda-toolbox
```

Jupyter AI is an open-source extension for JupyterLab that works with the application programming interface (API) key of a model provider or with a local model. In Google Colab, Gemini is built in. The section [AI assistants](PROMPT_PATH.md#ai-assistants) of the prompt path compares the options. No patient data enter any of them.

## Google Colab as a fallback

Each notebook has an **Open in Colab** badge. Colab needs a Google account and runs in the browser. Save a copy with **File → Save a copy in Drive** and run Section 0, which downloads the course package and the data files from GitHub. Colab sessions are temporary: Files created in a session disappear when it ends, unless they are saved to Drive or downloaded.

Real patient data never goes into Colab or any other cloud service. All data of the course notebooks are synthetic or public.

## Common problems

| Problem | What to do |
|---|---|
| `No module named 'vclinic'` without an internet connection | Open the notebook from inside the course folder. The first cell then finds the folder and needs no download. |
| The notebook opened outside the course folder | The first cell downloads the course package and the data into a folder named `ai-cardiology-course` next to the notebook. This needs an internet connection once. |
| An error after running cells out of order | Choose **Kernel → Restart Kernel and Run All Cells**, or run the *Catch-up* cell at the start of the section. |
| A notebook on GitHub shows no output | GitHub only displays the notebook. Download it with the course folder and run it in Jupyter. |
| Files locked or missing in a OneDrive folder | Move the course folder to a folder outside cloud synchronisation. |

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
