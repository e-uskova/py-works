# -*- coding: utf-8 -*-
import numpy as np


def calc_expectations(h, w, X, Q):
    a = np.copy(Q)
    a = np.vstack((np.zeros((h - 1, a.shape[1])), a))
    a = np.hstack((np.zeros((a.shape[0], w - 1)), a))
    sub_shape = (h, w)
    view_shape = tuple(np.subtract(a.shape, sub_shape) + 1) + sub_shape
    strides = a.strides + a.strides
    sub_matrices = np.lib.stride_tricks.as_strided(a, view_shape, strides)
    veroyaynosti = np.sum(np.sum(sub_matrices, axis=3), axis=2)
    return veroyaynosti * X

# https://stackoverflow.com/questions/43086557/convolve2d-just-by-using-numpy
