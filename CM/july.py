import numpy as np
from math import *

def init():
    global x_0, y_0, form_x, form_y, d, N
    
    x_0, y_0 = -2, 2
    print("Введите формулу для x")
    form_x = str(input())
    print("Введите формулу для y")
    form_y = str(input())
    print("Диаметр разбиения ")
    d = float(input())
    N = int(4 / d)

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

def main(graph=None, save=False):
    
    if graph == None:
        init()
        graph = dict.fromkeys(range(1, N * N + 1))
        
    print(x_0, y_0, form_x, form_y, d, N)
    
    pattern_x = np.ones((10, 10)) * np.array(range(1, 11)) * 0.1 * d - d / 20
    pattern_y = pattern_x.copy().transpose()
    
    e_cntr = 0
    
    for n in graph.keys():
        y_n = round(y_0 - ((n - 1) // N) * d, 4)
        x_n = round(x_0 + ((n - 1) % N) * d, 4)
        s = set(np.unique(get_num(*formula(x_n + pattern_x, y_n - pattern_y))).astype('int32'))
        graph[n] = s
        e_cntr += len(s)
            
    if save:
        print('Введите название файла для сохранения')
        file = str(input())
        save_graph(file, graph)
    return graph
    
def save_graph(file, graph):
    f = open(file, 'w')
    for k, v in graph.items():
        f.write(f'{k}: {v}\n')
    f.close()
