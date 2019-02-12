# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1113, 850)
        Form.setWindowIcon(QIcon(r"img/Icon-100.png"))
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(290, 550, 91, 41))
        self.clearBtn.setObjectName("clearBtn")
        self.startBtn = QtWidgets.QPushButton(Form)
        self.startBtn.setGeometry(QtCore.QRect(290, 500, 91, 41))
        self.startBtn.setObjectName("startBtn")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 791, 481))
        self.groupBox.setObjectName("groupBox")
        self.resultText = QtWidgets.QTextEdit(self.groupBox)

        self.resultText.setGeometry(QtCore.QRect(10, 70, 361, 401))
        self.resultText.setObjectName("resultText")
        self.resultText.setStyleSheet(
            "QTextEdit{color:red(100,100,100,250);font-size:15px;font-weight:bold;font-family:Roman times;}")
        self.weatherComboBox = QtWidgets.QComboBox(self.groupBox)
        self.weatherComboBox.setGeometry(QtCore.QRect(40, 40, 111, 22))
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.label_versions = QtWidgets.QLabel(self.groupBox)

        self.label_versions.setGeometry(QtCore.QRect(10, 40, 31, 20))
        self.label_versions.setObjectName("label_versions")
        self.label_port = QtWidgets.QLabel(self.groupBox)
        self.label_port.setGeometry(QtCore.QRect(220, 40, 61, 20))
        self.label_port.setObjectName("label_port")
        self.portComboBox = QtWidgets.QComboBox(self.groupBox)
        self.portComboBox.setGeometry(QtCore.QRect(270, 40, 69, 22))
        self.portComboBox.setObjectName("portComboBox")
        self.portComboBox.addItem("")
        self.portComboBox.addItem("")
        self.portComboBox.addItem("")
        self.portComboBox.addItem("")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(430, 70, 351, 401))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_port_2 = QtWidgets.QLabel(self.groupBox)
        self.label_port_2.setGeometry(QtCore.QRect(430, 40, 101, 20))
        self.label_port_2.setObjectName("label_port_2")

        self.retranslateUi(Form)
        self.clearBtn.clicked.connect(Form.clearResult)
        self.startBtn.clicked.connect(Form.startService)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.clearBtn.setText(_translate("Form", "重置数据"))
        self.startBtn.setText(_translate("Form", "重启服务器"))
        self.groupBox.setTitle(_translate("Form", "服务器做牌工具"))
        self.groupBox.setStyleSheet("QGroupBox{color:rgb(100,100,100,250);font-size:15px;font-weight:bold;font-family:Roman times;}" )
        self.weatherComboBox.setItemText(0, _translate("Form", "本地麻将"))
        self.weatherComboBox.setItemText(1, _translate("Form", "本地跑胡子"))
        self.weatherComboBox.setItemText(2, _translate("Form", "本地跑得快"))
        self.weatherComboBox.setItemText(3, _translate("Form", "测试服麻将"))
        self.weatherComboBox.setItemText(4, _translate("Form", "测试服跑胡子"))
        self.weatherComboBox.setItemText(5, _translate("Form", "测试服跑得快"))
        self.label_versions.setText(_translate("Form", "版本"))
        self.label_port.setText(_translate("Form", "端口"))
        self.portComboBox.setItemText(0, _translate("Form", "9037"))
        self.portComboBox.setItemText(1, _translate("Form", "9011"))
        self.portComboBox.setItemText(2, _translate("Form", "9010"))
        self.portComboBox.setItemText(3, _translate("Form", "9007"))
        self.label_port_2.setText(_translate("Form", "做牌json格式"))
