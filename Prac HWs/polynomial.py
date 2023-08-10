# -*- coding: utf-8 -*-


class Polynomial:
    def __init__(self, *args):
        self.args = list(args)

    def __call__(self, x):
        result = 0
        for power, coeff in zip(range(len(self.args)), self.args):
            result += x ** power * coeff
        return result
