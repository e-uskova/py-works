# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(382, 390)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.x_formula = QLineEdit(self.centralwidget)
        self.x_formula.setObjectName(u"x_formula")
        self.x_formula.setGeometry(QRect(50, 30, 211, 20))
        self.y_formula = QLineEdit(self.centralwidget)
        self.y_formula.setObjectName(u"y_formula")
        self.y_formula.setGeometry(QRect(50, 60, 211, 20))
        self.a_value = QDoubleSpinBox(self.centralwidget)
        self.a_value.setObjectName(u"a_value")
        self.a_value.setGeometry(QRect(300, 30, 62, 22))
        self.a_value.setMinimum(-99.900000000000006)
        self.a_value.setSingleStep(0.100000000000000)
        self.a_value.setStepType(QAbstractSpinBox.DefaultStepType)
        self.d_value = QDoubleSpinBox(self.centralwidget)
        self.d_value.setObjectName(u"d_value")
        self.d_value.setGeometry(QRect(120, 90, 62, 22))
        self.d_value.setDecimals(3)
        self.d_value.setSingleStep(0.100000000000000)
        self.d_value.setValue(0.500000000000000)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(210, 90, 161, 21))
        self.checkBox.setChecked(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 320, 361, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 71, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 47, 21))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 60, 47, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 30, 47, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 60, 47, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 90, 91, 21))
        self.output_text = QTextBrowser(self.centralwidget)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setGeometry(QRect(95, 120, 271, 171))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 120, 47, 13))
        self.output_vertices = QLabel(self.centralwidget)
        self.output_vertices.setObjectName(u"output_vertices")
        self.output_vertices.setGeometry(QRect(20, 250, 61, 21))
        self.output_edges = QLabel(self.centralwidget)
        self.output_edges.setObjectName(u"output_edges")
        self.output_edges.setGeometry(QRect(20, 270, 81, 16))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 300, 111, 16))
        self.output_time = QLabel(self.centralwidget)
        self.output_time.setObjectName(u"output_time")
        self.output_time.setGeometry(QRect(130, 300, 81, 16))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(290, 300, 81, 16))
        self.b_value = QDoubleSpinBox(self.centralwidget)
        self.b_value.setObjectName(u"b_value")
        self.b_value.setGeometry(QRect(300, 60, 62, 22))
        self.b_value.setMinimum(-99.900000000000006)
        self.b_value.setSingleStep(0.100000000000000)
        self.b_value.setStepType(QAbstractSpinBox.DefaultStepType)
        self.b_value.setValue(-0.200000000000000)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 382, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.x_formula.setText(QCoreApplication.translate("MainWindow", u"x * x - y * y + a", None))
        self.y_formula.setText(QCoreApplication.translate("MainWindow", u"2 * x * y + b", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432\u044b\u0432\u043e\u0434 \u0432 \u0444\u0430\u0439\u043b", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"x ->", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"y ->", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"a = ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"b = ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u044f\u0447\u0435\u0439\u043a\u0438", None))
        self.output_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444:", None))
        self.output_vertices.setText(QCoreApplication.translate("MainWindow", u"0 \u0432\u0435\u0440\u0448\u0438\u043d", None))
        self.output_edges.setText(QCoreApplication.translate("MainWindow", u"0 \u0440\u0451\u0431\u0435\u0440", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f:", None))
        self.output_time.setText(QCoreApplication.translate("MainWindow", u"k \u0441", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0437\u044b\u043a: Python3", None))
    # retranslateUi

