import numpy as np
import scipy as sc
from scipy import sparse
import time
import random
import oracles


class GDClassifier:
    """
    Реализация метода градиентного спуска для произвольного
    оракула, соответствующего спецификации оракулов из модуля oracles.py
    """

    def __init__(self, loss_function, step_alpha=1, step_beta=0, 
                 tolerance=1e-5, max_iter=1000, **kwargs):
        """
        loss_function - строка, отвечающая за функцию потерь классификатора. 
        Может принимать значения:
        - 'binary_logistic' - бинарная логистическая регрессия

        step_alpha - float, параметр выбора шага из текста задания

        step_beta- float, параметр выбора шага из текста задания

        tolerance - точность, по достижении которой, необходимо прекратить оптимизацию.
        Необходимо использовать критерий выхода по модулю разности соседних значений функции:
        если |f(x_{k+1}) - f(x_{k})| < tolerance: то выход 

        max_iter - максимальное число итераций     

        **kwargs - аргументы, необходимые для инициализации   
        """
        if loss_function == 'binary_logistic':
            self.oracle = oracles.BinaryLogistic(l2_coef=kwargs['l2_coef'])
        self.alpha = step_alpha
        self.beta = step_beta
        self.tolerance = tolerance
        self.max_iter = max_iter
        pass

    def fit(self, X, y, w_0=None, trace=False):
        """
        Обучение метода по выборке X с ответами y

        X - scipy.sparse.csr_matrix или двумерный numpy.array

        y - одномерный numpy array

        w_0 - начальное приближение в методе

        trace - переменная типа bool

        Если trace = True, то метод должен вернуть словарь history, содержащий информацию 
        о поведении метода. Длина словаря history = количество итераций + 1 (начальное приближение)

        history['time']: list of floats, содержит интервалы времени между двумя итерациями метода
        history['func']: list of floats, содержит значения функции на каждой итерации
        (0 для самой первой точки)
        """
        self.w = w_0.copy()
        w_k = w_0.copy()
        history = {'time': [0], 'func': [self.oracle.func(X, y, w_0)]}
        start = time.time()
        for k in range(1, self.max_iter):
            w_k1 = w_k - self.alpha / (k ** self.beta) * self.oracle.grad(X, y,
                                                                          w_k)

            if trace:
                history['func'].append(self.oracle.func(X, y, w_k1))
                history['time'].append(time.time() - start)
                start = time.time()
            if np.absolute(self.oracle.func(X, y, w_k1) -
                           self.oracle.func(X, y, w_k)) < self.tolerance:
                break
            w_k = w_k1.copy()
        self.w = w_k.copy()
        if trace:
            return history
        pass

    def predict(self, X):
        """
        Получение меток ответов на выборке X

        X - scipy.sparse.csr_matrix или двумерный numpy.array

        return: одномерный numpy array с предсказаниями
        """
        if sc.sparse.issparse(X):
            return np.sign(np.dot(self.w, X.todense().T))
        else:
            return np.sign(np.dot(self.w, X.T))
        pass

    def predict_proba(self, X):
        """
        Получение вероятностей принадлежности X к классу k

        X - scipy.sparse.csr_matrix или двумерный numpy.array

        return: двумерной numpy array, [i, k] значение соответветствует вероятности
        принадлежности i-го объекта к классу k 
        """
        if sc.sparse.issparse(X):
            return np.vstack((np.log(1 + np.exp(np.dot(self.w,
                                                       X.todense().T))),
                              np.log(1 + np.exp(-np.dot(self.w,
                                                        X.todense().T)))))
        else:
            return np.vstack((np.log(1 + np.exp(np.dot(self.w, X.T))),
                              np.log(1 + np.exp(-np.dot(self.w, X.T)))))
        pass

    def get_objective(self, X, y):
        """
        Получение значения целевой функции на выборке X с ответами y

        X - scipy.sparse.csr_matrix или двумерный numpy.array
        y - одномерный numpy array

        return: float
        """
        return self.oracle.func(X, y, self.w)
        pass

    def get_gradient(self, X, y):
        """
        Получение значения градиента функции на выборке X с ответами y

        X - scipy.sparse.csr_matrix или двумерный numpy.array
        y - одномерный numpy array

        return: numpy array, размерность зависит от задачи
        """
        return self.oracle.grad(X, y, self.w)
        pass

    def get_weights(self):
        """
        Получение значения весов функционала
        """ 
        return self.w
        pass


class SGDClassifier(GDClassifier):
    """
    Реализация метода стохастического градиентного спуска для произвольного
    оракула, соответствующего спецификации оракулов из модуля oracles.py
    """

    def __init__(self, loss_function, batch_size, step_alpha=1, step_beta=0, 
                 tolerance=1e-5, max_iter=1000, random_seed=153, **kwargs):
        """
        loss_function - строка, отвечающая за функцию потерь классификатора. 
        Может принимать значения:
        - 'binary_logistic' - бинарная логистическая регрессия

        batch_size - размер подвыборки, по которой считается градиент

        step_alpha - float, параметр выбора шага из текста задания

        step_beta- float, параметр выбора шага из текста задания

        tolerance - точность, по достижении которой, необходимо прекратить оптимизацию
        Необходимо использовать критерий выхода по модулю разности соседних значений функции:
        если |f(x_{k+1}) - f(x_{k})| < tolerance: то выход 


        max_iter - максимальное число итераций (эпох)

        random_seed - в начале метода fit необходимо вызвать np.random.seed(random_seed).
        Этот параметр нужен для воспроизводимости результатов на разных машинах.

        **kwargs - аргументы, необходимые для инициализации
        """
        super().__init__(loss_function=loss_function, step_alpha=step_alpha,
                         step_beta=step_beta, tolerance=tolerance,
                         max_iter=max_iter, l2_coef=kwargs['l2_coef'])
        self.batch_size = batch_size
        self.random_seed = random_seed
        pass

    def fit(self, X, y, w_0=None, trace=False, log_freq=1):
        """
        Обучение метода по выборке X с ответами y

        X - scipy.sparse.csr_matrix или двумерный numpy.array

        y - одномерный numpy array

        w_0 - начальное приближение в методе

        Если trace = True, то метод должен вернуть словарь history, содержащий информацию 
        о поведении метода. Если обновлять history после каждой итерации, метод перестанет 
        превосходить в скорости метод GD. Поэтому, необходимо обновлять историю метода лишь
        после некоторого числа обработанных объектов в зависимости от приближённого номера эпохи.
        Приближённый номер эпохи:
            {количество объектов, обработанных методом SGD} / {количество объектов в выборке}

        log_freq - float от 0 до 1, параметр, отвечающий за частоту обновления. 
        Обновление должно проиходить каждый раз, когда разница между двумя значениями приближённого номера эпохи
        будет превосходить log_freq.

        history['epoch_num']: list of floats, в каждом элементе списка будет записан приближённый номер эпохи:
        history['time']: list of floats, содержит интервалы времени между двумя соседними замерами
        history['func']: list of floats, содержит значения функции после текущего приближённого номера эпохи
        history['weights_diff']: list of floats, содержит квадрат нормы разности векторов весов с соседних замеров
        (0 для самой первой точки)
        """
#        if sc.sparse.issparse(X):
#            X = np.array(X.todense())
#
#        random.seed(self.random_seed)
#
#        ind = list(range(X.shape[0]))
#        random.shuffle(ind)
#        batches = [ind[i:i + self.batch_size] for i in range(0, len(ind),
#                   self.batch_size)]
#
#        self.w = w_0
#        w_k = w_0
#        history = {'epoch_num': [0], 'time': [0],
#                   'func': [self.oracle.func(X, y, w_0)], 'weights_diff': [0]}
#        old_epoch = 0
#        start = time.time()
#
#        for i in range(len(batches)):
#            batch = batches[i]
#            X_b = np.array([X[j] for j in batch])
#            y_b = np.array([y[j] for j in batch])
#            epoch_num = self.batch_size * i / X.shape[0]
#            for k in range(self.max_iter):
#                w_k1 = w_k - self.alpha / (k ** self.beta) *\
#                    self.oracle.grad(X_b, y_b, w_k)
#
#                if round(epoch_num - old_epoch, 8) > log_freq:
#                    old_epoch = epoch_num
#                    if trace:
#                        history['func'].append(self.oracle.func(X_b, y_b,
#                                                                w_k1))
#                        history['epoch_num'].append(epoch_num)
#                        history['weights_diff'].append(np.linalg.norm(
#                                                       w_k1 - w_k) ** 2)
#                        history['time'].append(time.time() - start)
#                        start = time.time()
#                if np.absolute(self.oracle.func(X_b, y_b, w_k1) -
#                               self.oracle.func(X_b, y_b, w_k)) <\
#                   self.tolerance:
#                    break
#                w_k = w_k1.copy()
#            self.w = w_k
#        if trace:
#            return history
        pass
