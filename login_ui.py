# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1150, 850)
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(590, 480, 80, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.enter.setFont(font)
        self.enter.setObjectName("enter")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(720, 480, 80, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 150, 451, 81))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 300, 80, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 380, 80, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.account = QtWidgets.QLineEdit(self.centralwidget)
        self.account.setGeometry(QtCore.QRect(630, 300, 150, 25))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(14)
        self.account.setFont(font)
        self.account.setText("")
        self.account.setObjectName("account")
        self.word = QtWidgets.QLineEdit(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(630, 380, 150, 25))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.word.setFont(font)
        self.word.setObjectName("word")
        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setGeometry(QtCore.QRect(590, 540, 231, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.prompt.setFont(font)
        self.prompt.setText("")
        self.prompt.setObjectName("prompt")
        self.logoo = QtWidgets.QLabel(self.centralwidget)
        self.logoo.setGeometry(QtCore.QRect(0, 0, 1150, 850))
        self.logoo.setText("")
        self.logoo.setObjectName("logoo")
        self.logoo.raise_()
        self.enter.raise_()
        self.exit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.account.raise_()
        self.word.raise_()
        self.prompt.raise_()
        login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 26))
        self.menubar.setObjectName("menubar")
        login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "登录"))
        self.enter.setText(_translate("login", "登录"))
        self.exit.setText(_translate("login", "退出"))
        self.label.setText(_translate("login", "人脸采集系统登录"))
        self.label_2.setText(_translate("login", "账号"))
        self.label_3.setText(_translate("login", "密码"))
        self.label.setStyleSheet("color:yellow;")
        self.label_2.setStyleSheet("color:yellow;")
        self.label_3.setStyleSheet("color:yellow;")
        self.prompt.setStyleSheet("color:white;")