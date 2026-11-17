"""EchoNet-Dynamic: apical four-chamber echocardiography videos of Stanford Medicine.

EchoNet-Dynamic holds 10,030 apical four-chamber videos of 10,030 patients
examined at Stanford Medicine between 2016 and 2018, each 112 x 112 pixels,
with the ejection fraction, the end-diastolic and end-systolic volumes and the
expert tracings of the left ventricle at end-diastole and end-systole
[Ouyang et al., Nature 580:252-256, 2020, doi:10.1038/s41586-020-2145-8]. The
official split has 7,465 training, 1,288 validation and 1,277 test videos.

Every user registers at the Stanford AIMI shared data sets, accepts the
Research Use Agreement (non-commercial research) and downloads the data
personally. The data, and the personal download link, may not be passed on.
The course therefore never stores these files: the functions below read the
participant's own copy, either the zip file or its unpacked folder.
"""

import io
import pathlib
import tempfile
import urllib.request
import zipfile

import numpy as np
import pandas as pd

SPLITS = {"TRAIN": 7465, "VAL": 1288, "TEST": 1277}
CITATION = ("D. Ouyang, B. He, A. Ghorbani, N. Yuan, J. Ebinger, C. P. Langlotz, P. A. Heidenreich, R. A. Harrington, "
            "D. H. Liang, E. A. Ashley, J. Y. Zou. Video-based AI for beat-to-beat assessment of cardiac function. "
            "Nature 580:252-256, 2020. doi:10.1038/s41586-020-2145-8")


def default_folder():
    """The folder data/echonet of the course folder (next to the package vclinic)."""
    return pathlib.Path(__file__).resolve().parents[1] / "data" / "echonet"


class Source:
    """The participant's copy of EchoNet-Dynamic: an unpacked folder or the zip file."""

    def __init__(self, path):
        self.path = pathlib.Path(path)
        self.zip = None
        self.prefix = ""
        if self.path.is_file() and zipfile.is_zipfile(self.path):
            self.zip = zipfile.ZipFile(self.path)
            names = [n for n in self.zip.namelist() if n.endswith("FileList.csv")]
            if not names:
                raise FileNotFoundError(f"{self.path} holds no FileList.csv")
            self.prefix = names[0][: -len("FileList.csv")]

    def read(self, name):
        """The bytes of a file of the data set, for example "FileList.csv" or "Videos/0X1A0A263B22CCD966.avi"."""
        if self.zip is not None:
            return self.zip.read(self.prefix + name)
        return (self.path / name).read_bytes()

    def __repr__(self):
        return f"EchoNet-Dynamic in {self.path}"


def find(folder=None):
    """Find the participant's copy below folder (default data/echonet): a folder with FileList.csv or a zip file."""
    folder = pathlib.Path(folder) if folder else default_folder()
    if not folder.exists():
        raise FileNotFoundError(
            f"{folder} does not exist. Register for EchoNet-Dynamic at Stanford AIMI, download the data "
            "and put the zip file (or its unpacked folder) into this folder.")
    candidates = [p.parent for p in sorted(folder.rglob("FileList.csv"))]
    if candidates:
        return Source(candidates[0])
    for z in sorted(folder.rglob("*.zip")):
        try:
            return Source(z)
        except (FileNotFoundError, zipfile.BadZipFile):
            continue
    raise FileNotFoundError(f"No copy of EchoNet-Dynamic (FileList.csv or a zip file) was found in {folder}.")


def download(url, folder=None, name="EchoNet-Dynamic.zip"):
    """Download the zip file with the participant's personal download link into folder (default data/echonet)."""
    folder = pathlib.Path(folder) if folder else default_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / name
    with urllib.request.urlopen(url, timeout=120) as r, open(target, "wb") as f:
        total = int(r.headers.get("Content-Length") or 0)
        done, step = 0, max(total // 20, 1)
        while True:
            chunk = r.read(1 << 22)
            if not chunk:
                break
            f.write(chunk)
            done += len(chunk)
            if total and done // step != (done - len(chunk)) // step:
                print(f"  {done / 1e9:.2f} of {total / 1e9:.2f} GB")
    print("EchoNet-Dynamic saved to", target)
    return Source(target)


def file_list(source=None):
    """FileList.csv as a DataFrame: FileName, EF, ESV, EDV, FrameHeight, FrameWidth, FPS, NumberOfFrames, Split."""
    source = source or find()
    table = pd.read_csv(io.BytesIO(source.read("FileList.csv")))
    table["Split"] = table["Split"].str.upper()
    return table


def traced_frames(source=None):
    """The two traced frames of every video: {file name without .avi: (ED frame, ES frame)}.

    In VolumeTracings.csv the frames of a video are sorted by the traced area, so the
    first frame is the end-systolic one and the last the end-diastolic one. Videos
    with fewer than two traced frames are left out.
    """
    source = source or find()
    tr = pd.read_csv(io.BytesIO(source.read("VolumeTracings.csv")))
    out = {}
    for name, group in tr.groupby("FileName", sort=False):
        frames = list(dict.fromkeys(group["Frame"].tolist()))
        if len(frames) >= 2:
            out[pathlib.Path(name).stem] = (int(frames[-1]), int(frames[0]))
    return out


def _read_video(data):
    import cv2
    with tempfile.NamedTemporaryFile(suffix=".avi", delete=False) as f:
        f.write(data)
        path = f.name
    try:
        capture = cv2.VideoCapture(path)
        frames = []
        while True:
            ok, frame = capture.read()
            if not ok:
                break
            frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        capture.release()
    finally:
        pathlib.Path(path).unlink(missing_ok=True)
    return np.array(frames)


def frame_pairs(source=None, split="TEST", n=400, size=64, seed=2026, threshold=50.0):
    """End-diastolic and end-systolic frames of n videos of one split, as two channels.

    Returns a dictionary: images (n, 2, size, size) with values 0 to 1, ef, abnormal
    (1 when the ejection fraction is below threshold) and file (the video names).
    """
    import cv2
    source = source or find()
    table = file_list(source)
    traced = traced_frames(source)
    table = table[(table["Split"] == split.upper()) & table["FileName"].map(lambda f: pathlib.Path(f).stem in traced)]
    table = table.sample(n=min(n, len(table)), random_state=seed).reset_index(drop=True)
    images = []
    for name in table["FileName"]:
        stem = pathlib.Path(name).stem
        video = _read_video(source.read(f"Videos/{stem}.avi"))
        ed, es = traced[stem]
        pair = [cv2.resize(video[min(k, len(video) - 1)], (size, size), interpolation=cv2.INTER_AREA) for k in (ed, es)]
        images.append(np.stack(pair).astype(np.float32) / 255.0)
    return {"images": np.array(images, dtype=np.float32), "ef": table["EF"].to_numpy(float),
            "abnormal": (table["EF"] < threshold).astype(int).to_numpy(), "file": table["FileName"].tolist()}
