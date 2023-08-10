# -*- coding: utf-8 -*-
import numpy as np
import nearest_neighbors


def kfold(n, n_folds=3):
    all_idx = range(n)
    folds = np.array_split(all_idx, n_folds)
    res = []
    for k in range(n_folds):
        if k == 0:
            edu = np.hstack(folds[k+1:])
        elif k == n_folds - 1:
            edu = np.hstack(folds[:k])
        else:
            edu = np.hstack((np.hstack(folds[:k]), np.hstack(folds[k+1:])))
        val = folds[k]
        res.append((edu, val))
    return res


def knn_cross_val_score(X, y, k_list, score, cv, **kwargs):
    if cv is None:
        cv = kfold(X.shape[0], n_folds=3)
    dic = {}
    for k in k_list:
        acc = []
        if 'starategy' not in kwargs:
            cls = nearest_neighbors.KNNClassifier(k=k,
                                                  strategy='brute',
                                                  metric=kwargs['metric'],
                                                  weights=kwargs['weights'])
        else:
            cls = nearest_neighbors.KNNClassifier(k=k,
                                                  strategy=kwargs['strategy'],
                                                  metric=kwargs['metric'],
                                                  weights=kwargs['weights'])
        for fold in cv:
            X_train = np.array([X[i] for i in fold[0]])
            y_train = np.array([y[i] for i in fold[0]])
            X_test = np.array([X[i] for i in fold[1]])
            y_test = np.array([y[i] for i in fold[1]])
            cls.fit(X_train, y_train)
            y_predict = cls.predict(X_test)

            if score == 'accuracy':
                accuracy = np.sum(y_predict == y_test) / X_test.shape[0]
                acc.append(accuracy)
        dic[k] = np.array(acc)
    return dic
