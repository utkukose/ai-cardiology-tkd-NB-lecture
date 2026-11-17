"""A small reader for NIfTI-1 files (.nii and .nii.gz) with NumPy only.

The cardiac magnetic resonance files of ACDC are NIfTI-1 volumes. This reader
covers what they need: the dimensions, the voxel size and the data, without
an extra package. nibabel reads the same files with many more options.
"""

import gzip
import struct

import numpy as np

_DTYPES = {2: "u1", 4: "i2", 8: "i4", 16: "f4", 64: "f8", 256: "i1", 512: "u2", 768: "u4"}


def read_nifti(path):
    """Return (data, spacing): the voxel array (x, y, z[, t]) and the voxel size in mm."""
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rb") as f:
        raw = f.read()
    endian = "<" if struct.unpack("<i", raw[:4])[0] == 348 else ">"
    if struct.unpack(endian + "i", raw[:4])[0] != 348:
        raise ValueError(f"{path} is not a NIfTI-1 file")
    dim = struct.unpack(endian + "8h", raw[40:56])
    datatype = struct.unpack(endian + "h", raw[70:72])[0]
    pixdim = struct.unpack(endian + "8f", raw[76:108])
    vox_offset = int(struct.unpack(endian + "f", raw[108:112])[0])
    slope, inter = struct.unpack(endian + "2f", raw[112:120])
    if datatype not in _DTYPES:
        raise ValueError(f"NIfTI data type {datatype} is not supported")
    shape = tuple(int(d) for d in dim[1:1 + dim[0]])
    offset = max(vox_offset, 352)
    count = int(np.prod(shape))
    data = np.frombuffer(raw, dtype=endian + _DTYPES[datatype], count=count, offset=offset)
    data = data.reshape(shape, order="F")
    if slope not in (0.0, 1.0) and np.isfinite(slope):
        data = data * slope + (inter if np.isfinite(inter) else 0.0)
    spacing = tuple(float(p) for p in pixdim[1:1 + len(shape)])
    return np.array(data), spacing
