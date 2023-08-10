import numpy as np
import scipy
import time
from scipy.special import expit, logsumexp


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
        self.loss_function = loss_function
        self.step_alpha = step_alpha
        self.step_beta = step_beta
        self.tolerance = tolerance
        self.max_iter = max_iter
        self.trashhold = 0.5
        if 'l2_coef' in kwargs.keys():
            self.l2_coef = kwargs.pop('l2_coef')
        else:
            self.l2_coef = 0
        if 'iter_acc' in kwargs.keys():
            self.iter_acc = kwargs.pop('iter_acc')
        else:
            self.iter_acc = 0
        if 'w_0' in kwargs.keys():
            self.w_0 = kwargs.pop('w_0')
            
    @staticmethod
    def softmax(X, w):
        alp = X.dot(w)
        #alp -= np.max(alp)
        #exp_l = np.exp(alp)
        exp_l = np.exp(alp - np.max(alp, axis=1)[:, np.newaxis])
        return exp_l / np.sum(exp_l, axis=1, keepdims=True)
   
    @staticmethod
    def loss_bc(X, y, w, l2_coef):
        loss = np.logaddexp(0, (-y*X.dot(w))).mean() + (l2_coef/2)*(w**2).sum()
        return loss

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
        if w_0 is None:
            w_0 = np.zeros(X.shape[1])
            
        self.w = w_0.copy()
        if trace == True:
            history = {'time': [0], 'func': [self.loss_bc(X, y, self.w, self.l2_coef)]}
            start_time = time.time()
        for k in range(1, self.max_iter+1):
            if k>2 and self.tolerance != 0:
                if np.abs(history['func'][-2] - history['func'][-1]) < self.tolerance:
                    break
            nu = self.step_alpha / (k**self.step_beta)
            gradient = self.get_gradient(X, y)
            self.w -= nu *gradient
            if trace == True:
                history['time'].append(time.time() - start_time)
                loss = self.loss_bc(X, y, self.w, self.l2_coef)
                history['func'].append(loss)
                start_time = time.time()
        if trace == True:
            return history
        
    def predict(self, X):
        """
        Получение меток ответов на выборке X
        
        X - scipy.sparse.csr_matrix или двумерный numpy.array
        
        return: одномерный numpy array с предсказаниями
        """
        return np.where((expit(X.dot(self.w)) >= self.trashhold) == True, 1, -1)

    def predict_proba(self, X):
        """
        Получение вероятностей принадлежности X к классу k
        
        X - scipy.sparse.csr_matrix или двумерный numpy.array
        
        return: двумерной numpy array, [i, k] значение соответветствует вероятности
        принадлежности i-го объекта к классу k 
        """
        return expit(X.dot(self.w))
        
    def get_objective(self, X, y):
        """
        Получение значения целевой функции на выборке X с ответами y
        
        X - scipy.sparse.csr_matrix или двумерный numpy.array
        y - одномерный numpy array
        
        return: float
        """
        pass
        
    def get_gradient(self, X, y):
        """
        Получение значения градиента функции на выборке X с ответами y
        
        X - scipy.sparse.csr_matrix или двумерный numpy.array
        y - одномерный numpy array
        
        return: numpy array, размерность зависит от задачи
        """
        grad = X.T.dot((expit(y*X.dot(self.w))-1)*y)/X.shape[0] + self.l2_coef * self.w
        return grad

    def get_weights(self):
        """
        Получение значения весов функционала
        """    
        return self.w


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
        self.loss_function = loss_function
        self.step_alpha = step_alpha
        self.step_beta = step_beta
        self.tolerance = tolerance
        self.max_iter = max_iter
        self.rand_seed = random_seed
        self.batch_size = batch_size
        self.l2_coef = kwargs.pop('l2_coef')
        self.trashhold = 0.5
        if 'l2_coef' in kwargs.keys():
            self.l2_coef = kwargs.pop('l2_coef')
        else:
            self.l2_coef = 0
        if 'iter_acc' in kwargs.keys():
            self.iter_acc = kwargs.pop('iter_acc')
        else:
            self.iter_acc = 0
        if 'w_0' in kwargs.keys():
            self.w_0 = kwargs.pop('w_0')
        
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
        np.random.seed(self.rand_seed)
        if w_0 is None:
            w_0 = np.zeros(X.shape[1])
        self.w = w_0.copy()
        w_l = self.w.copy()
        used_obj_c = 0
        epoch_num = 0
        if trace == True:
            history = {'time': [0], 'func': [self.loss_bc(X, y, self.w, self.l2_coef)],
                       'weights_diff': [0], 'epoch_num' : [0]}
        start_time = time.time()
        for k in range(1 , self.max_iter):
            ind = np.random.randint(X.shape[0], size = self.batch_size)
            used_obj_c += self.batch_size
            epoch_num = used_obj_c/X.shape[0]
            if (trace == True) and (used_obj_c/X.shape[0] > log_freq):
                history['epoch_num'].append(epoch_num*len(history['epoch_num']))
                history['time'].append(time.time() - start_time)
                history['weights_diff'].append(((w_l - self.w)**2).sum())
                loss = self.loss_bc(X, y, self.w, self.l2_coef)
                history['func'].append(loss)
                if np.abs(history['func'][-2] - history['func'][-1]) < self.tolerance:
                    break
                w_l = self.w
                used_obj_c = 0
                start_time = time.time()  
            nu = self.step_alpha / (k**self.step_beta) 
            gradient = self.get_gradient(X[ind], y[ind])
            self.w -= nu * gradient
        if trace == True:
            return history