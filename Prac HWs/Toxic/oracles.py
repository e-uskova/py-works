import numpy as np
import scipy as sc
from scipy import sparse
from scipy.special import expit


class BaseSmoothOracle:
    """
    Базовый класс для реализации оракулов.
    """
    def func(self, w):
        """
        Вычислить значение функции в точке w.
        """
        raise NotImplementedError('Func oracle is not implemented.')

    def grad(self, w):
        """
        Вычислить значение градиента функции в точке w.
        """
        raise NotImplementedError('Grad oracle is not implemented.')


class BinaryLogistic(BaseSmoothOracle):
    """
    Оракул для задачи двухклассовой логистической регрессии.

    Оракул должен поддерживать l2 регуляризацию.
    """

    def __init__(self, l2_coef):
        """
        Задание параметров оракула.

        l2_coef - коэффициент l2 регуляризации
        """
        self.l2_coef = l2_coef
        pass

    def func(self, X, y, w):
        """
        Вычислить значение функционала в точке w на выборке X с ответами y.

        X - scipy.sparse.csr_matrix или двумерный numpy.array

        y - одномерный numpy array

        w - одномерный numpy array
        """
        if sc.sparse.issparse(X):
            sp_mtr = sparse.csr_matrix(-y).multiply(sparse.csr_matrix(w).dot(X.transpose()))
            return 1 / y.size *\
                (np.sum(np.log(np.exp(sp_mtr.data) + 1)) + (sp_mtr.shape[1] - sp_mtr.data.shape[0]) * np.log(2))+\
                self.l2_coef / 2 * np.linalg.norm(w) ** 2
        else:
            return 1 / y.size *\
                np.sum(np.log(1 + np.exp(-y.reshape(1, -1) *
                                         np.dot(w, X.T)))) +\
                self.l2_coef / 2 * np.linalg.norm(w) ** 2
        return super().func(w)

    def grad(self, X, y, w):
        """
        Вычислить градиент функционала в точке w на выборке X с ответами y.

        X - scipy.sparse.csr_matrix или двумерный numpy.array

        y - одномерный numpy array

        w - одномерный numpy array
        """
        if sc.sparse.issparse(X):
            margin = sparse.csr_matrix(y).multiply(sparse.csr_matrix(w).dot(X.transpose()))
            niz = margin.copy()
            niz.data = expit(margin.data)
            margin.data = np.exp(-margin.data)
            if np.count_nonzero(w):
                return - 1 / y.size * \
                    np.array((margin.multiply(sparse.csr_matrix(y)).multiply(X.transpose()).multiply(niz)).sum(axis=1)).ravel() +\
                    self.l2_coef * w
            else:
                return - 1 / y.size * \
                    (np.array((margin.multiply(sparse.csr_matrix(y)).multiply(X.transpose()).multiply(niz)).sum(axis=1)).ravel() +
                    0.5 * np.array(sparse.csr_matrix(y).multiply(X.transpose()).sum(axis=1)).ravel()) +\
                    self.l2_coef * w
        else:
            return - 1 / y.size * \
                np.sum(np.exp(-y * np.dot(w, X.T)).reshape(-1, 1) *
                       y.reshape(-1, 1) * X /
                       np.array(1 + np.exp(-y * np.dot(w, X.T))).reshape(-1, 1),
                       axis=0) + self.l2_coef * w
        return super().grad(w)
