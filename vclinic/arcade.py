"""ARCADE: X-ray coronary angiograms with expert outlines of stenoses.

ARCADE (Automatic Region-based Coronary Artery Disease diagnostics using
x-ray angiography imagEs) holds two sets of 1,500 coronary angiograms of
512 x 512 pixels, one with the 26 segments of the SYNTAX score and one with
the outlines of the stenoses, each split into 1,000 images for training,
200 for validation and 300 for the test. The course uses the set with the
stenoses. The data set is published on Zenodo under the Creative Commons
CC0 1.0 dedication and is downloaded by every participant from there; no
image of it is stored in the course repository.

The images carry no patient identifiers, so two images of one patient can
fall into two sets.
"""
import hashlib
import json
import pathlib
import urllib.request
import zipfile

import numpy as np

URL = "https://zenodo.org/records/10390295/files/arcade.zip?download=1"
SIZE = 451573813
MD5 = "c5b1973ade06f7dff210f878161e1a76"
DOI = "10.5281/zenodo.10390295"
SPLITS = ("train", "val", "test")
CREDIT = "ARCADE, Popov et al. 2024, CC0"


def default_folder():
    """The folder data/arcade of the course folder (next to the package vclinic)."""
    return pathlib.Path(__file__).resolve().parents[1] / "data" / "arcade"


def _ready(folder):
    return all((folder / "stenosis" / s / "annotations" / f"{s}.json").exists() for s in SPLITS)


def download(folder=None, keep_zip=False, verbose=True):
    """Download ARCADE from Zenodo (451.6 MB) and unpack the set with the stenoses into data/arcade/stenosis.

    The archive is checked against the MD5 checksum published on Zenodo, and only the files of the set with
    the stenoses are unpacked. Nothing is downloaded when the files are already there. Returns the folder.
    """
    folder = pathlib.Path(folder) if folder else default_folder()
    if _ready(folder):
        if verbose:
            print("ARCADE: the set with the stenoses is already in", folder)
        return folder
    folder.mkdir(parents=True, exist_ok=True)
    zpath = folder / "arcade.zip"
    if not (zpath.exists() and zpath.stat().st_size == SIZE):
        part = zpath.with_suffix(".zip.part")
        md5, done, step = hashlib.md5(), 0, SIZE // 10
        with urllib.request.urlopen(URL, timeout=120) as r, open(part, "wb") as f:
            while True:
                chunk = r.read(1 << 20)
                if not chunk:
                    break
                f.write(chunk)
                md5.update(chunk)
                done += len(chunk)
                if verbose and done // step != (done - len(chunk)) // step:
                    print(f"  {done / 1e6:.0f} of {SIZE / 1e6:.0f} MB")
        if done != SIZE or md5.hexdigest() != MD5:
            raise IOError(f"ARCADE: the download is incomplete or damaged ({done} bytes); please run download() again.")
        part.replace(zpath)
    with zipfile.ZipFile(zpath) as z:
        for name in z.namelist():
            parts = pathlib.PurePosixPath(name).parts
            if name.endswith("/") or ".." in parts or name.startswith("/") or parts[:2] != ("arcade", "stenosis"):
                continue
            target = folder.joinpath(*parts[1:])
            target.parent.mkdir(parents=True, exist_ok=True)
            with z.open(name) as src, open(target, "wb") as dst:
                dst.write(src.read())
    if not keep_zip:
        zpath.unlink()
    if verbose:
        print("ARCADE: the set with the stenoses is in", folder / "stenosis")
    return folder


def annotations(split, folder=None):
    """The images of a split and their stenoses: a list of dicts with id, file, stenoses (box, polygon, centre)."""
    folder = pathlib.Path(folder) if folder else default_folder()
    d = json.loads((folder / "stenosis" / split / "annotations" / f"{split}.json").read_text())
    by = {}
    for a in d["annotations"]:
        x, y, w, h = a["bbox"]
        poly = np.array(a["segmentation"][0], dtype=float).reshape(-1, 2) if a.get("segmentation") else None
        by.setdefault(a["image_id"], []).append(dict(box=[float(x), float(y), float(w), float(h)], polygon=poly,
                                                     x=float(x + w / 2), y=float(y + h / 2)))
    return [dict(id=im["id"], file=im["file_name"], stenoses=by.get(im["id"], [])) for im in sorted(d["images"], key=lambda i: i["id"])]


def load(split, file, folder=None):
    """One angiogram as grey values from 0 to 1, 512 x 512."""
    from PIL import Image
    folder = pathlib.Path(folder) if folder else default_folder()
    return np.asarray(Image.open(folder / "stenosis" / split / "images" / file).convert("L"), dtype=np.float32) / 255


def vessel_points(img, radius=6, share=0.03, margin=48):
    """Pixels that look like a vessel: the brightest share of the black top-hat, which marks thin dark structures,
    at least `margin` pixels from the border of the image, where the dark frame of the X-ray field lies."""
    from skimage.morphology import black_tophat, disk
    th = black_tophat(img, disk(radius))[margin:-margin, margin:-margin]
    return np.argwhere(th > np.quantile(th, 1 - share)) + margin


def patches(split, size=64, per_stenosis=2, neg_per_pos=3, away=48, folder=None, seed=2026, limit=None, jitter=6, background=0):
    """Patches of size x size pixels: `per_stenosis` positives centred near every stenosis (shifted by up to `jitter`
    pixels); `neg_per_pos` negatives for every positive on vessels at least `away` pixels from every stenosis; and,
    with background > 0, `background` more negatives for every positive at random places of the image at least `away`
    pixels from every stenosis. Returns (X of shape n x size x size, y, image ids)."""
    rng = np.random.default_rng(seed)
    X, y, ids = [], [], []
    h = size // 2
    for im in annotations(split, folder)[:limit]:
        g = load(split, im["file"], folder)
        pad = np.pad(g, size, mode="reflect")
        cut = lambda r, c: pad[r + size - h:r + size + h, c + size - h:c + size + h]
        for s in im["stenoses"]:
            for _ in range(per_stenosis):
                dx, dy = rng.integers(-jitter, jitter + 1, size=2)
                X.append(cut(int(s["y"]) + dy, int(s["x"]) + dx)); y.append(1); ids.append(im["id"])
        far_of = lambda cand: [c for c in cand if all(np.hypot(c[1] - s["x"], c[0] - s["y"]) > away for s in im["stenoses"])]
        cand = vessel_points(g)
        cand = cand[rng.permutation(len(cand))[:400]]
        n_pos = per_stenosis * max(1, len(im["stenoses"]))
        chosen = far_of(cand)[:int(round(neg_per_pos * n_pos))]
        if background:
            chosen += far_of(rng.integers(0, g.shape[0], size=(400, 2)))[:int(round(background * n_pos))]
        for r, c in chosen:
            X.append(cut(int(r), int(c))); y.append(0); ids.append(im["id"])
    return np.stack(X).astype(np.float32), np.array(y, dtype=np.int64), np.array(ids)
