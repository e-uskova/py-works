import numpy as np


def grad_finite_diff(f, w, eps=1e-8):
    """
    Возвращает численное значение градиента, подсчитанное по следующией формуле:
        result_i := (f(w + eps * e_i) - f(w)) / eps,
        где e_i - следующий вектор:
        e_i = (0, 0, ..., 0, 1, 0, ..., 0)
                          >> i <<
    """
    e_i = np.zeros(len(w))
    grad = np.zeros(len(w))
    for i in range(len(w)):
        e_i[i] = 1
        result_i = (f(w + eps * e_i) - f(w)) / eps
        grad[i] += result_i[i]
        e_i[i] = 0
    return grad
