import os
import numpy as np
from datetime import datetime
from multiprocess import Process, Manager
# from multiprocessing import Process, Manager
from multiprocessing import Pool, TimeoutError, current_process

def printarr(arr):
    for row in arr:
        print(row)

def ad(arr, i, j):
    return np.delete(np.delete(np.copy(arr), (i), 0), (j), 1)

###############################################################################

def det4 (arr):
    res = []
    for i in range(4):
        res.append(arr[i][0] * det3(ad(arr, i, 0), i))
    return sum(res)

def det3 (arr, idx):
    res = []
    for i in range(3):
        res.append(arr[i][0] * det2(ad(arr, i, 0), i))
    return pow(-1, idx + 2) * sum(res)

def det2 (arr, idx):
    res = arr[0, 0] * arr[1, 1] - arr[1, 0] * arr[0, 1]
    return pow(-1, idx + 2) * res

###############################################################################

def det4p (arr):
    res4 = Manager().list()
    procs = []

    for i in range(4):
        args = (res4, ad(arr, i, 0), i, arr[i][0])
        proc = Process(target=det3p, args=args) # розовый
        proc.start()
        procs.append(proc)

    for proc in procs:
        proc.join()
    
    return sum(res4) # серый

def det3p (res, arr, idx, el):
    res3 = Manager().list()
    procs = []

    for i in range(3):
        args = (res3, ad(arr, i, 0), i, arr[i][0])
        proc = Process(target=det2p, args=args) # голубой
        proc.start()
        procs.append(proc)

    for proc in procs:
        proc.join()

    res.append(pow(-1, idx + 2) * el * sum(res3)) # фиолетовый
        
def det2p (res, arr, idx, el):  
    res2 = Manager().list()

    p1 = Process(target=mult, args=(res2, arr[0, 0], arr[1, 1], 0))
    p1.start()
    p2 = Process(target=mult, args=(res2, arr[0, 1], arr[1, 0], 1))
    p2.start()

    p1.join()
    p2.join()

    res.append(pow(-1, idx + 2) * el * sum(res2)) # зеленый

def mult(res, el1, el2, idx):
    res.append(pow(-1, idx + 2) * el1 * el2) # желтый
    
###############################################################################

def inv_count (m, k, i, j):
    return sum(((m > k), (m > i), (m > j), (k > i), (k > j), (i > j)))

# def inv_cnt (ind):
#     cnt = 0
#     for i in range(len(ind) - 1):
#         for j in range(i, len(ind)):
#             cnt += (ind[i] > ind[j])
#     return cnt

###############################################################################

def determ4 (arr):
    res = []
    args = [(m, k, i, j) for m in range(4) for k in range(4) for i in range(4) for j in range(4) 
            if (k != m)&(i != k)&(j != k)&(i != m)&(j != m)&(i != j)]

    def mult(m, k, i, j):
        return arr[m][0] * arr[k][1] * arr[i][2] * arr[j][3] * (-1) ** (inv_count (m, k, i, j))

    for i in range(24):
        res.append(mult(*args[i]))

    return sum(res)

###############################################################################

def determ4p (arr):
    procs = []
    res = Manager().list()
    args = [(m, k, i, j) for m in range(4) for k in range(4) for i in range(4) for j in range(4) 
            if (k != m)&(i != k)&(j != k)&(i != m)&(j != m)&(i != j)]

    def mult(m, k, i, j):
        res.append(arr[m][0] * arr[k][1] * arr[i][2] * arr[j][3] * (-1) ** (inv_count (m, k, i, j)))

    for i in range(24):
        proc = Process(target=mult, args=args[i])
        proc.start()
        procs.append(proc)

    for proc in procs:
        proc.join()

    return sum(res)

###############################################################################

def calc_time(func):
    time_start = datetime.now()
    det = func(arr)
    time_calc = datetime.now() - time_start
    return "result: {}\ttime: {}".format(det, time_calc)

if __name__ == '__main__':

    arr = np.array([[1, 2, 3, 4],
                    [5, 7, 9, 11],
                    [9, 3, 9, 8],
                    [7, 8, 5, 4]])
    # det = 12

    # np.random.seed(42)
    # arr = np.random.randint(-10, 10, (4, 4))
    # printarr(arr)

    print("Крамер последовательно\n{}".format(calc_time(det4)))
    print("Крамер параллельно\n{}".format(calc_time(det4p)))
    print("Перебор последовательно\n{}".format(calc_time(determ4)))
    print("Перебор параллельно\n{}".format(calc_time(determ4p)))
    print("Встроенная функция\n{}".format(calc_time(np.linalg.det)))
