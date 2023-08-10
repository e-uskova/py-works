# -*- coding: utf-8 -*-
import numpy as np


def replace_nan_to_means(x):
    mask = np.isnan(x)
    x_new = x.copy()
    mask2 = np.all(mask, axis=0)
    np.transpose(x_new)[mask2] = 0
    x_new[mask] = np.nanmean(x_new, axis=0)[np.where(mask)[1]]
    return x_new
