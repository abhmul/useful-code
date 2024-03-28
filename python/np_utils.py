from typing import Sequence, cast

import numpy as np


def dynamic_slice(arr: np.ndarray, axis: int | Sequence, index: slice | int | Sequence):
    if isinstance(axis, int):
        axis = [axis]
        index = [index]
    index = cast(Sequence, index)
    slicer = [slice(None)] * arr.ndim
    for i, dim_ind in enumerate(axis):
        slicer[dim_ind] = index[i]
    return tuple(slicer)
