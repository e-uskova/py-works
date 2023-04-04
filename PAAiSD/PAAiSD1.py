import os
import numpy as np
from datetime import datetime
from multiprocessing import Process

def printarr(arr):
    for row in arr:
        print(row)

def ad(arr, i, j):
    return np.delete(np.delete(np.copy(arr), (i), 0), (j), 1)
        
# def doubler(number):
#     """
#     Функция умножитель на два
#     """
#     result = number * 2
#     proc = os.getpid()
#     print('{0} doubled to {1} by process id: {2}'.format(
#         number, result, proc))
    
def y1 (op1, op2) :
    return op1 * op2

def y2 (op1, op2, op3) :
    return op1 * (op2 - op3)

def y3 (op1, op2, op3, op4) :
    return op1 * (op2 - op3 + op4)

def y4 (op1, op2, op3, op4) :
    return op1 - op2 + op3 - op4

def calc (arr) :
    for i in range(4):
        for j in range(4):
            pass

def det4 (arr):
    res = []
    for i in range(4):
        res.append(-pow(-1, i + 1) * arr[i][0] * det3(ad(arr, i, 0)))
    return sum(res)

def det3 (arr):
    res = []
    for i in range(3):
        res.append(pow(-1, i + 2) * arr[i][0] * det2(ad(arr, i, 0)))
    return sum(res)

def det2 (arr):
    res = arr[0, 0] * arr[1, 1] - arr[1, 0] * arr[0, 1]
    return res

if __name__ == '__main__':
    # numbers = [5, 10, 15, 20, 25]
    # procs = []

    # for index, number in enumerate(numbers):
    #     proc = Process(target=doubler, args=(number,))
    #     procs.append(proc)
    #     proc.start()

    # for proc in procs:
    #     proc.join()
    arr = np.array([[1, 2, 3, 4],
                    [5, 7, 9, 11],
                    [9, 3, 9, 8],
                    [7, 8, 5, 4]])
    
    # det = 12

    # printarr(arr)

    # time_start = datetime.now()
    det = det4(arr)
    # time_calc = datetime.now() - time_start
    print(det)
    # print(time_calc)


