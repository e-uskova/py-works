# -*- coding: utf-8 -*-
import numpy as np
import distances
import sklearn.neighbors


class KNNClassifier:

    def __init__(self, k, strategy='my_own', metric='euclidean', weights=False,
                 test_block_size=100):

        if metric in ['euclidean', 'cosine']:
            self.metric = metric
        else:
            raise TypeError

        self.k = k
        self.weights = weights

        if strategy in ['my_own', 'brute', 'kd_tree', 'ball_tree']:
            self.strategy = strategy
            if strategy != 'my_own':
                self.other = sklearn.neighbors.NearestNeighbors(
                        algorithm=self.strategy, metric=self.metric)
        else:
            raise TypeError

    def fit(self, X, y):

        self.X_train = X
        self.y_train = y

        if self.strategy != 'my_own':
            self.other.fit(X, y)

    def find_kneighbors(self, X, return_distance):

        if self.metric == 'euclidean':
            dist_func = distances.euclidean_distance
        elif self.metric == 'cosine':
            dist_func = distances.cosine_distance

        if self.strategy == 'my_own':
            ret_dist = np.zeros((X.shape[0], self.k))
            ret_ind = np.zeros((X.shape[0], self.k))

            max_size_of_X = 100

            if X.shape[0] > max_size_of_X:

                ret_dist, ret_ind = [], []

                for X_for_predict in np.array_split(X, X.shape[0] //
                                                    (max_size_of_X - 1) + 1):
                    dist = []
                    if return_distance:
                        dist, ind = self.find_kneighbors(
                                X_for_predict, return_distance=return_distance)
                    else:
                        ind = self.find_kneighbors(
                                X_for_predict, return_distance=return_distance)

                    ret_dist += list(dist)
                    ret_ind += list(ind)

                print(ret_dist, ret_ind)

                if return_distance:
                    return (np.array(ret_dist), np.array(ret_ind))
                else:
                    return (np.array(ret_ind))

            else:
                ret_dist = np.zeros((X.shape[0], self.k))
                ret_ind = np.zeros((X.shape[0], self.k))

                dist = dist_func(X, self.X_train)

                for i in range(X.shape[0]):
                    one_dist = dist[i]
                    ind = range(self.X_train.shape[0])
                    res = list(zip(ind, one_dist))
                    res = sorted(res, key=lambda d: d[1])
                    res = res[:self.k]
                    ind, one_dist = zip(*res)

                    ind = np.array(ind)
                    one_dist = np.array(one_dist)

                    ret_dist[i] = np.array(one_dist)
                    ret_ind[i] = np.array(ind)

                if return_distance:
                    return (np.array(ret_dist), np.array(ret_ind).astype('int'))
                else:
                    return (np.array(ret_ind).astype('int'))

        else:
            return self.other.kneighbors(
                    X, n_neighbors=self.k, return_distance=return_distance)

    def predict(self, X):
        if self.weights:
            dist, ind = self.find_kneighbors(X, return_distance=True)

            el_weights = 1 / (dist + 10 ** -5)

            res = []
            for i in range(ind.shape[0]):
                indeces = ind[i]
                w = el_weights[i]
                ind_list = []
                for index in indeces:
                    index = int(index)
                    ind_list.append(self.y_train[index])
                counts = np.bincount(ind_list, weights=w)
                y = np.argmax(counts)
                res.append(y)
        else:
            ind = self.find_kneighbors(X, return_distance=False)
            res = []
            for indeces in ind:
                ind_list = []
                for index in indeces:
                    index = int(index)
                    ind_list.append(self.y_train[index])
                counts = np.bincount(ind_list)
                y = np.argmax(counts)
                res.append(y)
        return np.array(res)
