import numpy as np
import sys
import time
# import PySide2
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from math import *
from test2 import Ui_MainWindow

# create application
app = QApplication(sys.argv)

#create form and init ui
Form = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(Form)
Form.show()

#hook logic

x_0, y_0 = -2, 2

def formula(form_x, form_y, x, y):
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

def func():
    global form_x, form_y, a, b, d, N
    
    form_x = ui.x_formula.text()
    form_y = ui.y_formula.text()

    d = ui.d_value.value()
    a = ui.a_value.value()
    b = ui.b_value.value()

    N = int(4 / d)

    save = ui.checkBox.isChecked()
    
    graph = {}
    pattern_x = np.ones((10, 10)) * np.array(range(1, 11)) * 0.1 * d - d / 20
    pattern_y = pattern_x.copy().transpose()
    n = 1
    y_n = y_0
    cntr = 0
    c = 1
    
    start = time.time()
    
    while(y_n > -y_0):
        x_n = x_0
        while(x_n < -x_0):
            s = set(np.unique(get_num(*formula(form_x, form_y, x_n + pattern_x, y_n - pattern_y))).astype('int32'))
            graph[n] = s
            cntr += len(s)
            c += 1
            x_n += d
            n += 1
        y_n -= d
        
    t = round(time.time() - start, 3)

    if save:       
        f = open('test2.txt', 'w')
        for k, v in graph.items():
            f.write(f'{k}: {v}\n')
        f.close()
        
    text = ''
    for n, s in graph.items():
        text += f'{n}: {s}' + '\n'
    
    ui.output_text.setText(text)    
    
    ui.output_vertices.setText("{} вершин".format(c))
    ui.output_edges.setText("{} рёбер".format(cntr))
    ui.output_time.setText("{} c".format(t))

ui.pushButton.clicked.connect(func)

#run main loop
sys.exit(app.exec_())
