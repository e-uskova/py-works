import numpy as np
from math import *

x_0, y_0 = -2, 2

print("Введите формулу для x")
form_x = str(input())
print("Введите формулу для y")
form_y = str(input())

print("Введите значения следующих параметров:\nДиаметр разбиения ")
d = float(input())
print("a ")
a = float(input())
print("b ")
b = float(input())

N = int(4 / d)

print("Сохранять? (0/1)")
save = bool(int(input()))

def formula(x, y):
    return(eval(form_x), eval(form_y))

def get_num(x, y):
    y = np.where(x < -2, 3, y)
    x = np.where(x < -2, -3, x)
    
    y = np.where(x > 2, 3, y)
    x = np.where(x > 2, -3, x)
    
    x = np.where(y < -2, -3, x)
    y = np.where(y < -2, 3, y)
    
    x = np.where(y > 2, -3, x)
    y = np.where(y > 2, 3, y)
    
    i = ((y_0 - y) // d * N) + ((x - x_0) // d) + 1
    i = np.where(i < 0, 0, i)
    return i


graph = {}
pattern_x = np.ones((10, 10)) * np.array(range(1, 11)) * 0.1 * d - d / 20
pattern_y = pattern_x.copy().transpose()
n = 1
y_n = y_0
while(y_n > -y_0):
    x_n = x_0
    while(x_n < -x_0):
        s = set(np.unique(get_num(*formula(x_n + pattern_x, y_n - pattern_y))).astype('int32'))
        graph[n] = s
        x_n += d
        n += 1
    y_n -= d
    
if save:
    cntr = 0
    c = 1
    f = open('test.txt', 'w')
    f.write('a = {}, b = {}\n'.format(a, b))
    for k, v in graph.items():
        f.write(f'{k}: {v}\n')
        cntr += len(v)
        c += 1
    f.close()
    print("Количество рёбер: {}".format(cntr))
    print("Количество вершин: {}".format(c))
