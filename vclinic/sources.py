"""Three sources of a data set: a Python library, the web and a file on this computer.

The Jupyter notebooks of the course offer the three sources wherever they
read a data set. A library reads the data from the site of the data set
(for example wfdb from PhysioNet, ucimlrepo from the UCI Machine Learning
Repository). The web source reads the file from its web address; the course
repository keeps a copy of every file that it may share. The computer source
reads a file that the participant downloaded: Jupyter looks for it in the
folder of the notebook, and Google Colab opens a window to upload it.
"""

import importlib
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

COURSE_RAW = ("https://raw.githubusercontent.com/utkukose/"
              "ai-cardiology-tkd-NB-lecture/main/")

_NAMES = {"library": "library", "kütüphane": "library", "kutuphane": "library",
          "web": "web", "computer": "computer", "bilgisayar": "computer"}

_TEXT = {
    "en": {
        "unknown": "Unknown data source {0!r}: choose \"library\", \"web\" or \"computer\".",
        "upload": "Choose the file(s) {0} on your computer in the window below.",
        "missing": ("The file(s) {0} are not in the folder of this Jupyter notebook ({1}). "
                    "Download them first, put them in this folder and run the cell again."),
        "installed": "{0}: installed now",
        "install_failed": "{0} could not be installed (no internet?)",
    },
    "tr": {
        "unknown": "Bilinmeyen veri kaynağı {0!r}: \"kütüphane\", \"web\" ya da \"bilgisayar\" yazınız.",
        "upload": "Aşağıdaki pencerede bilgisayarınızdaki {0} dosyasını (dosyalarını) seçiniz.",
        "missing": ("{0} dosyası (dosyaları) bu Jupyter Notebook'un klasöründe ({1}) yok. "
                    "Dosyayı önce indiriniz, bu klasöre koyunuz ve hücreyi yeniden çalıştırınız."),
        "installed": "{0}: şimdi kuruldu",
        "install_failed": "{0} kurulamadı (internet yok mu?)",
    },
}


def _t(key, *args):
    from . import teach
    return _TEXT[teach._STATE["lang"]][key].format(*args)


def source_name(source):
    """The source in English: "library", "web" or "computer" (Turkish names are accepted)."""
    name = _NAMES.get(str(source).strip().lower())
    if name is None:
        raise ValueError(_t("unknown", source))
    return name


def in_colab():
    return "google.colab" in sys.modules


def install(package, module=None):
    """Import a package and install it once with pip when it is missing."""
    module = module or package
    try:
        return importlib.import_module(module)
    except ImportError:
        result = subprocess.run([sys.executable, "-m", "pip", "install", "-q", package],
                                capture_output=True, text=True)
        importlib.invalidate_caches()
        if result.returncode != 0:
            raise ImportError(_t("install_failed", package))
        print(_t("installed", package))
        return importlib.import_module(module)


def local_files(*names):
    """Paths of files on this computer, in the current folder (the folder of the notebook).

    In Google Colab the missing files are asked for in an upload window. In
    Jupyter a missing file raises FileNotFoundError with the folder to use.
    """
    missing = [n for n in names if not Path(n).exists()]
    if missing and in_colab():
        from google.colab import files
        print(_t("upload", ", ".join(missing)))
        files.upload()
        missing = [n for n in names if not Path(n).exists()]
    if missing:
        raise FileNotFoundError(_t("missing", ", ".join(missing), Path.cwd()))
    return [str(Path(n).resolve()) for n in names]


def local_file(name):
    """Path of one file on this computer; see local_files."""
    return local_files(name)[0]


def web_files(url_folder, names, folder=None):
    """Download files from a web folder into a local folder and return their paths.

    Without a folder, the files go to a folder of the course in the temporary folder of the computer.
    """
    folder = Path(folder) if folder else Path(tempfile.gettempdir()) / "ai-cardiology-data"
    folder.mkdir(parents=True, exist_ok=True)
    paths = []
    for name in names:
        target = folder / name
        if not target.exists():
            urllib.request.urlretrieve(url_folder + name, target)
        paths.append(str(target))
    return paths
