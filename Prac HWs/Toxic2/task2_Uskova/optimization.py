import numpy as np
import scipy as sc
from scipy import sparse
import time
import random
import oracles


class GDClassifier:
    
    def __init__(self, loss_function, step_alpha=1, step_beta=0, 
                 tolerance=1e-5, max_iter=1000, **kwargs):
        self.step_alpha = step_alpha
        self.step_beta = step_beta
        self.tolerance = tolerance
        self.max_iter = max_iter
        if loss_function == 'binary_logistic':
            self.oracle = oracles.BinaryLogistic(l2_coef=kwargs['l2_coef'])
            
    def fit(self, X, y, w_0=None, trace=False, acc=False, x_test=None, y_test=None):
        
        if w_0 is None:
            self.w = np.zeros(X.shape[1])
        else:
            self.w = w_0.copy()
        hist = {'time': [0], 'func': [self.oracle.func(X, y, self.w)]}
        if acc:
            hist['acc'] = [self.accuracy(x_test, y_test)]
        start = time.time()        
        for k in range(1, self.max_iter + 1):
            if (k > 2) and abs(hist['func'][-2] - hist['func'][-1]) < self.tolerance:
                break
            self.w -= self.step_alpha / (k ** self.step_beta) * self.oracle.grad(X, y, self.w)
            hist['time'].append(time.time() - start)
            hist['func'].append(self.oracle.func(X, y, self.w))
            if acc:
                hist['acc'].append(self.accuracy(x_test, y_test))
            start = time.time()
        if trace:
            return hist
        
    def predict(self, X):
        return np.where((expit(X.dot(self.w)) >= 0.5) == True, 1, -1)

    def predict_proba(self, X):
        return expit(X.dot(self.w))
        
    def get_objective(self, X, y):
        pass
        
    def get_gradient(self, X, y):
        return self.oracle.grad(X, y, self.w)
    
    def get_weights(self):
        return self.w
    
    def accuracy(self, X_test, y_test):
        return (self.predict(X_test) == y_test).mean()


class SGDClassifier(GDClassifier):
    
    def __init__(self, loss_function, batch_size, step_alpha=1, step_beta=0, 
                 tolerance=1e-5, max_iter=1000, random_seed=153, **kwargs):
        
        self.step_alpha = step_alpha
        self.step_beta = step_beta
        self.tolerance = tolerance
        self.max_iter = max_iter
        if loss_function == 'binary_logistic':
            self.oracle = oracles.BinaryLogistic(l2_coef=kwargs['l2_coef'])
        self.rand_seed = random_seed
        self.batch_size = batch_size
        
    def fit(self, X, y, w_0=None, trace=False, log_freq=1, acc=False, x_test=None, y_test=None):

        np.random.seed(self.rand_seed)
        if w_0 is None:
            self.w = np.zeros(X.shape[1])
        else:
            self.w = w_0.copy()
        w_l = self.w.copy()
        used_obj_c = 0
        epoch_num = 0
        if trace:
            history = {'time': [0], 'func': [self.oracle.func(X, y, self.w)],
                       'weights_diff': [0], 'epoch_num' : [0]}
            if acc:
                history['acc'] = [self.accuracy(x_test, y_test)]
        start = time.time()
        for k in range(1, self.max_iter + 1):
            ind = np.random.randint(X.shape[0], size=self.batch_size)
            used_obj_c += self.batch_size
            epoch_num = used_obj_c / X.shape[0]
#             print(k, used_obj_c, epoch_num)
            if trace and (used_obj_c / X.shape[0] > log_freq):
                history['epoch_num'].append(epoch_num * len(history['epoch_num']))
                history['time'].append(time.time() - start)
                history['weights_diff'].append(((w_l - self.w) ** 2).sum())
                history['func'].append(self.oracle.func(X, y, self.w))
                if (k>2) and np.abs(history['func'][-2] - history['func'][-1]) < self.tolerance:
                    break
                if acc:
                    history['acc'].append(self.accuracy(x_test, y_test))
                w_l = self.w.copy()
                used_obj_c = 0
                start = time.time()
            self.w -= self.step_alpha / (k ** self.step_beta) * self.oracle.grad(X[ind], y[ind], self.w)

        if trace:
            return history