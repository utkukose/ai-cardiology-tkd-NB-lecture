# Python path

**Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists**<br>
Turkish Society of Cardiology · First version: November 2026

[Course home](README.md) · [Türkçe](PYTHON_PATH.tr.md)

The Python path is Part 2 of every Jupyter notebook, for participants who want to learn to write the code themselves. The course assumes no programming experience. Part 2 starts with a Python step that teaches the language the week needs, and *Python note* cells explain every new construct where it first appears. The numbered sections reach the results of the practice stops of the lecture page, with exercises that check their answers at once. The table lists the Python steps of the weeks; the steps of later weeks are linked when each week is published.

Before Week 1, the [start-here notebook](en/start-here/NB00_start_here.ipynb) checks the computer and introduces cells, values, printing and a first plot.

Participants who do not want to write code follow the [prompt path](PROMPT_PATH.md) in Part 1 of the same notebook, where an artificial intelligence (AI) assistant writes the code from ready prompts. Both paths reach the same results, and the path can be changed at any practice stop.

| Week | Python step | Topics | Notebook |
|---|---|---|---|
| 1 | Python step 1: Values, lists, dictionaries, decisions, loops and functions | Variables and types, arithmetic with clinical values, lists and indexing, dictionaries, if and else, for loops, functions with arguments and return values, NumPy arrays, pandas DataFrames and Matplotlib plots | [NB01_python_and_ecg_basics.ipynb](en/week-01/NB01_python_and_ecg_basics.ipynb) |
| 2 | Python step 2: Data for models | Selecting columns and rows, missing values, dummy variables, splitting data by patient, the fit and predict pattern of scikit-learn, pipelines | [NB02_machine_learning_fundamentals.ipynb](en/week-02/NB02_machine_learning_fundamentals.ipynb) |
| 3 | Python step 3: Images as arrays | Arrays with two and three dimensions, slicing, normalisation, loading images, the training loop of a neural network | [NB03_deep_learning_and_cnns.ipynb](en/week-03/NB03_deep_learning_and_cnns.ipynb) |
| 4 | Python step 4: Reusing trained models | Loading pretrained weights, freezing layers, masks as arrays, functions that measure areas and volumes | [NB04_transfer_learning.ipynb](en/week-04/NB04_transfer_learning.ipynb) |
| 5 | Python step 5: Signals in batches | Windows of a signal, arrays of many recordings, labels with several classes, reading a large data set step by step | [NB05_time_series_and_ecg_ai.ipynb](en/week-05/NB05_time_series_and_ecg_ai.ipynb) |
| 6 | Python step 6: Working with text | Strings and their methods, regular expressions, tokens, calling a pretrained model from the Hugging Face Hub | [NB06_clinical_text_mining.ipynb](en/week-06/NB06_clinical_text_mining.ipynb) |
| 7 | Python step 7: Classes and modules | Reading and writing a small class, importing code from modules, building a model from parts | [NB07_vision_transformers.ipynb](en/week-07/NB07_vision_transformers.ipynb) |
| 8 | Python step 8: Joining data | Merging tables, aligning signals and images of one patient, dealing with missing parts | [NB08_multimodal_ai_and_data_fusion.ipynb](en/week-08/NB08_multimodal_ai_and_data_fusion.ipynb) |
| 9 | Python step 9: Explaining a model in code | Groups and orders of variables with itertools, dictionaries with tuples as keys, the factorials of the Shapley formula, functions handed to other functions, charts of contributions | [NB09_reliability_and_explainable_ai.ipynb](en/week-09/NB09_reliability_and_explainable_ai.ipynb) |
| 10 | Python step 10: From notebook to application | Scripts, a small web interface with Streamlit, saving and loading a model | In preparation |
| 11 | Python step 11: A project of one's own | Organising a project folder, documenting code, making results reproducible | In preparation |

---

*Prof. Dr. Utku Kose · Süleyman Demirel University · [utkukose.com](https://www.utkukose.com) · Content CC BY 4.0, code MIT.*
