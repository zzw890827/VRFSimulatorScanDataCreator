# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_finish.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_finish(object):
    def setupUi(self, Dialog_finish):
        Dialog_finish.setObjectName("Dialog_finish")
        Dialog_finish.resize(396, 145)
        self.progressBar = QtWidgets.QProgressBar(Dialog_finish)
        self.progressBar.setGeometry(QtCore.QRect(10, 80, 381, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_finish = QtWidgets.QLabel(Dialog_finish)
        self.label_finish.setGeometry(QtCore.QRect(100, 40, 251, 16))
        self.label_finish.setObjectName("label_finish")
        self.btn_finish = QtWidgets.QPushButton(Dialog_finish)
        self.btn_finish.setGeometry(QtCore.QRect(160, 110, 75, 23))
        self.btn_finish.setObjectName("btn_finish")
        self.label_pic_finish = QtWidgets.QLabel(Dialog_finish)
        self.label_pic_finish.setGeometry(QtCore.QRect(20, 10, 61, 61))
        self.label_pic_finish.setText("")
        self.label_pic_finish.setObjectName("label_pic_finish")

        self.retranslateUi(Dialog_finish)
        QtCore.QMetaObject.connectSlotsByName(Dialog_finish)

    def retranslateUi(self, Dialog_finish):
        _translate = QtCore.QCoreApplication.translate
        Dialog_finish.setWindowTitle(_translate("Dialog_finish", "作成中"))
        self.label_finish.setText(_translate("Dialog_finish", "ただいま作成中です、しばらくお待ちください。"))
        self.btn_finish.setText(_translate("Dialog_finish", "完了"))

