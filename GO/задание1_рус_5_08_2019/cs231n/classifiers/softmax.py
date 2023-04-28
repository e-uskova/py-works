import numpy as np
from random import shuffle


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax фнкция потерь, наивная реализация (с циклами)

    Число пикселей изображения - D, число классов - С, мы оперируем миниблоками по N примеров


    Входы:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
      that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Возвращает кортеж:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Инициализация потерь и градиентов.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # ЗАДАНИЕ: Вычислите softmax  потери и  градиенты, используя явные циклы.   #
    # Сохраните потери в переменной loss, а градиенты в dW.  Не забывайте о     #
    # регуляризации!                                                            #
    #############################################################################
    
    num_classes = W.shape[1]
    num_train = X.shape[0]

    for i in range(num_train):
        scores = X[i].dot(W)
        correct_class_score = scores[y[i]]

        sum_j = 0.0
        for j in range(num_classes):
            sum_j += np.exp(scores[j]) #1

        for j in range(num_classes):
            dW[:, j] += (np.exp(scores[j]) * X[i]) / sum_j
            if (j == y[i]):
                dW[:, y[i]] -= X[i]

    dW /= num_train #3
    dW += W * reg
    
    #############################################################################
    #                          КОНЕЦ ВАШЕГО КОДА                                #
    #############################################################################

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax функция потерь, векторизованная версия.

    Входы и выходы те же, что и у функции softmax_loss_naive.
    """
    # Инициализация потерь и градиентов.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # ЗАДАНИЕ: Вычислите softmax  потери и  градиенты без использования циклов. #
    # Сохраните потери в переменной loss, а градиенты в dW.  Не забывайте о     #
    # регуляризации!                                                            #
    #############################################################################
    pass
    #############################################################################
    #                         КОНЕЦ ВАШЕГО КОДА                                 #
    #############################################################################

    return loss, dW
