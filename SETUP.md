# Setup

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Course home](README.md) · [Türkçe](SETUP.tr.md)

Every Jupyter notebook of the course runs in two places, with the same data and the same results. Choose the one you prefer; switching from one week to the next is possible. In Part 1 of a notebook, an artificial intelligence (AI) assistant writes the code from a ready prompt; in Part 2, the participant writes the code in Python.

| | Google Colab | Jupyter on your own computer (Anaconda) |
|---|---|---|
| What you need | A Google account and a web browser | A computer with Windows, macOS or Linux and about 5 GB of free space |
| Installation | None | About 20 minutes, once, before Week 1 |
| Opening a notebook | The **Open in Colab** button of a practice stop, of the week page or of the course site | **Download for Jupyter**, or the whole course folder |
| AI assistant for the prompt path | Gemini is built in | Any assistant in the browser; Anaconda Assistant or Jupyter AI inside Jupyter |
| Data of real patients | Never | Only on a computer of the institution, under its rules |

## Option A: Google Colab

1. On the lecture page of the week, press **Open in Colab** at a practice stop. The week page and the course site have the same button.
2. Sign in with a Google account and keep your own copy with **File → Save a copy in Drive**, so that your changes are not lost.
3. Run **Section 0**. Its first cell downloads the course package `vclinic` and the data files of the week from GitHub in a few seconds.
4. Continue in **Part 1, the prompt path**, or in **Part 2, the Python path**. Gemini, the AI assistant of Colab, opens with its button at the top of the window.

Colab sessions are temporary: Files created in a session disappear when it ends, while the notebook saved in Drive stays. Colab already includes most packages of the course, PyTorch among them. The two ECG packages `wfdb` and `neurokit2` are installed by Section 0 of the Week 1 notebook.

## Option B: Jupyter on your own computer

The steps below install Anaconda, which brings Python and Jupyter, and download the course folder. They take about 20 minutes and are done once. This is also the environment for later work with the data of your own clinic.

### 1. Install Anaconda

Download the Anaconda Distribution for the operating system of the computer from [anaconda.com/download](https://www.anaconda.com/download) and install it with the default options. Anaconda brings Python, Jupyter and most packages that Week 1 needs: NumPy, pandas, SciPy, Matplotlib and Seaborn.

### 2. Download the course folder

On the [GitHub page of the course](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture), choose **Code** and then **Download ZIP**, and unzip the file into a folder of your choice. A folder outside cloud synchronisation, for example `Documents/courses` rather than a OneDrive folder, avoids locked files. With git, the same folder is created with:

```bash
git clone https://github.com/utkukose/ai-cardiology-tkd-NB-lecture.git
```

### 3. Start Jupyter

Open **Anaconda Navigator** and launch **JupyterLab** or **Jupyter Notebook**, then move to the course folder in the file browser on the left. Alternatively, open **Anaconda Prompt** on Windows or **Terminal** on macOS and Linux, go to the course folder and start JupyterLab:

```bash
cd path/to/ai-cardiology-tkd-NB-lecture
jupyter lab
```

### 4. Check the computer with the start-here notebook

Open `en/start-here/NB00_start_here.ipynb` and run all its cells with **Run → Run All Cells**. The notebook checks the packages, finds the course folder, draws a first ECG and prints **Ready for Week 1** when everything works.

### 5. Open the notebook of the week

Open the Jupyter notebook in the folder of the week, for example `en/week-01/NB01_python_and_ecg_basics.ipynb`, and run Section 0 first. The first cell finds the course folder, and the second prints the version of the course package `vclinic`. **Kernel → Restart Kernel and Run All Cells** starts the notebook again from a clean state.

### 6. Packages of later weeks

From Week 3, the notebooks use PyTorch, the deep learning package of the course. Anaconda does not include it, and it is installed once with pip. Run in Anaconda Prompt on Windows or in Terminal on macOS:

```bash
pip install torch torchvision
```

On Linux, the default package also holds libraries for NVIDIA graphics cards and is large. The notebooks of the course need no graphics card, so the smaller version for the processor is enough:

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

For other systems, the selector at [pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/) gives the command. Restart the kernel of an open notebook after the installation. Colab includes PyTorch.

Week 3 also builds a first model with Keras, a high-level interface for deep learning. Colab includes it; elsewhere, `pip install keras` installs it, and the notebook runs it on PyTorch, so TensorFlow is not needed. Without Keras, the notebook skips this one cell.

From Week 4, the notebooks also use scikit-image for the outlines of the echocardiograms. Anaconda and Colab include it; in another Python environment, `pip install scikit-image` installs it.

From Week 6, the notebooks also use transformers, the package of Hugging Face for pretrained language models. On first use, it downloads the tokenizer and the weights of the tiny Turkish model of the course, about 19 MB, from the Hugging Face Hub. Colab includes the package; elsewhere, `pip install transformers` installs it.

Week 7 needs no new package. On first use, its notebook downloads the ImageNet weights of the vision transformer ViT-B/16, about 330 MB, through torchvision and the stenosis set of the ARCADE angiograms, about 452 MB, from Zenodo; both are kept on the computer for later runs.

Week 8 needs no new package and downloads nothing: The course package draws all its data on the computer.

Week 9 needs no new package. Its notebook uses the 300 patients of CAMUS of Week 4 and downloads them again, about 250 MB, only when they are missing. The optional package shap, installed with `pip install shap`, computes the Shapley values of the logistic regression a second way; without it, the notebook uses the closed form.

Week 10 needs one new package, Streamlit, for the web interface of the prototype; `pip install streamlit` installs it. Section 8 of the notebook writes the interface as the file `app_af.py` in the folder of the week. The Anaconda Prompt, opened in that folder, starts it with `streamlit run app_af.py`, and the browser shows it at http://localhost:8501. On first use, the notebook downloads the header and annotation files of the 25 records of the MIT-BIH Atrial Fibrillation Database and the signal files of three of them, about 86 MB, from PhysioNet; no registration is needed. The notebook also runs in Colab, but the web interface needs a computer of one's own.

Week 11 needs no new package and downloads nothing: The Cleveland data of its worked final project come with the course folder. The notebook writes the folder `final_project` next to itself, with the results, a figure and the toolbox of the final project, `final_project/code/project_tools.py`.

Week 1 reads and processes ECGs with the packages `wfdb` and `neurokit2`, which neither Anaconda nor Colab includes. Section 0 of the Week 1 notebook installs them when they are missing and the computer is online. Without them, the notebooks use a built-in fallback. They can also be installed beforehand:

```bash
pip install wfdb neurokit2
```

A separate environment with all packages of the course, PyTorch included, can be created from the file `environment.yml` in the course folder:

```bash
conda env create -f environment.yml
conda activate ai-cardiology
jupyter lab
```

### 7. Update the course folder every week

New weeks are added to the repository during the course. With git, `git pull` in the course folder brings the new files. Without git, download the ZIP file again. Keep your own copies of the notebooks in a separate folder, so that an update does not overwrite your work.

## An AI assistant for the prompt path

An AI assistant is optional. It is needed only on the [prompt path](PROMPT_PATH.md), and any assistant that writes Python can be used. In Anaconda, Anaconda Assistant comes with Anaconda Toolbox. Install it from the Anaconda Toolbox tile in Navigator or with the command below. Then open a notebook in JupyterLab and sign in with an Anaconda account. A free account has a limited number of requests.

```bash
conda install anaconda-toolbox
```

Jupyter AI is an open-source extension for JupyterLab that works with the application programming interface (API) key of a model provider or with a local model. In Google Colab, Gemini is built in. The section [AI assistants](PROMPT_PATH.md#which-assistant) of the prompt path compares the options. No patient data enter any of them.

Real patient data never go into Colab or any other cloud service. All data of the course notebooks are synthetic or public.

## Common problems

| Problem | What to do |
|---|---|
| `No module named 'vclinic'` without an internet connection | Open the notebook from inside the course folder. The first cell then finds the folder and needs no download. |
| `No module named 'torch'` | Install PyTorch as step 6 describes, then restart the kernel. |
| `No module named 'skimage'` | Install scikit-image with `pip install scikit-image`, then restart the kernel. |
| `No module named 'transformers'` | Install it with `pip install transformers`, then restart the kernel. |
| The notebook opened outside the course folder | The first cell downloads the course package and the data into a folder named `ai-cardiology-course` next to the notebook. This needs an internet connection once. |
| An error after running cells out of order | Choose **Kernel → Restart Kernel and Run All Cells**, or run the *Catch-up* cell at the start of the section. |
| A notebook on GitHub shows no output | GitHub only displays the notebook. Download it with the course folder and run it in Jupyter. |
| Files locked or missing in a OneDrive folder | Move the course folder to a folder outside cloud synchronisation. |

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
