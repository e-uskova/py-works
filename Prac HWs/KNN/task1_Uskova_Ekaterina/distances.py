# -*- coding: utf-8 -*-
import numpy as np


def euclidean_distance(X, Y):
    X_sq_sum = np.sum(X ** 2, axis=1)
    Y_sq_sum = np.sum(Y ** 2, axis=1)
    return np.sqrt(np.array([X_sq_sum[i] + Y_sq_sum[j] - 2 * np.dot(X[i], Y[j])
                             for i in range(X.shape[0])
                             for j in range(Y.shape[0])
                             ])).reshape(X.shape[0], Y.shape[0])


def cosine_distance(X, Y):
    X_n = np.linalg.norm(X, axis=1)
    Y_n = np.linalg.norm(Y, axis=1)
    return np.array([1 - np.dot(X[i], Y[j])/(X_n[i] * Y_n[j])
                     for i in range(X.shape[0]) for j in
                     range(Y.shape[0])]).reshape(X.shape[0], Y.shape[0])
