# -*- coding: utf-8 -*-

import numpy as np


def get_nonzero_diag_product(input_smth):
    eye = np.eye(input_smth.shape[0], M=input_smth.shape[1])
    b = eye * input_smth
    b = b[np.nonzero(b)]
    if b.size == 0:
        return None
    else:
        return np.prod(b)
