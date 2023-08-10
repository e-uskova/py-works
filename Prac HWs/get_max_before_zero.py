# -*- coding: utf-8 -*-

import numpy as np


def get_max_before_zero(x):
    after_zero_index_list = list(np.where(x == 0)[0] + 1)
    if x.size in after_zero_index_list:
        after_zero_index_list.remove(x.size)
    if len(after_zero_index_list) == 0:
        return None
    return np.max(x[after_zero_index_list])
