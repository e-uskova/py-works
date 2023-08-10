# -*- coding: utf-8 -*-
import numpy as np


def encode_rle(x):
    if x.size == 0:
        return None
    a = np.diff(x) != 0
    a = np.hstack((a, [False]))
    value = np.hstack((x[a], x[-1]))
    nonzero_index = (np.where(np.diff(x) != 0))[0]
    nonzero_index_l = np.hstack((nonzero_index, x.size - 1))
    nonzero_index_r = np.hstack(([-1], nonzero_index))
    number = nonzero_index_l - nonzero_index_r
    return value, number
