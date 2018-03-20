# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_welcome.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_welcome(object):
    def setupUi(self, Dialog_welcome):
        Dialog_welcome.setObjectName("Dialog_welcome")
        Dialog_welcome.resize(570, 198)
        self.label_1_welcome = QtWidgets.QLabel(Dialog_welcome)
        self.label_1_welcome.setGeometry(QtCore.QRect(120, 20, 181, 51))
        self.label_1_welcome.setObjectName("label_1_welcome")
        self.label_2_welcome = QtWidgets.QLabel(Dialog_welcome)
        self.label_2_welcome.setGeometry(QtCore.QRect(30, 80, 491, 21))
        self.label_2_welcome.setObjectName("label_2_welcome")
        self.label_3_welcome = QtWidgets.QLabel(Dialog_welcome)
        self.label_3_welcome.setGeometry(QtCore.QRect(30, 100, 521, 21))
        self.label_3_welcome.setObjectName("label_3_welcome")
        self.line = QtWidgets.QFrame(Dialog_welcome)
        self.line.setGeometry(QtCore.QRect(10, 130, 551, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog_welcome)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 150, 241, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancel_welcome = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_cancel_welcome.setObjectName("btn_cancel_welcome")
        self.horizontalLayout.addWidget(self.btn_cancel_welcome)
        self.btn_next_welcome = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_next_welcome.setObjectName("btn_next_welcome")
        self.horizontalLayout.addWidget(self.btn_next_welcome)
        self.label_pic_welcome = QtWidgets.QLabel(Dialog_welcome)
        self.label_pic_welcome.setGeometry(QtCore.QRect(30, 10, 61, 61))
        self.label_pic_welcome.setText("")
        self.label_pic_welcome.setObjectName("label_pic_welcome")

        self.retranslateUi(Dialog_welcome)
        QtCore.QMetaObject.connectSlotsByName(Dialog_welcome)

    def retranslateUi(self, Dialog_welcome):
        _translate = QtCore.QCoreApplication.translate
        Dialog_welcome.setWindowTitle(_translate("Dialog_welcome", "Welcome"))
        self.label_1_welcome.setText(_translate("Dialog_welcome", "ウェルカム"))
        self.label_2_welcome.setText(_translate("Dialog_welcome", "このウィザードに従って、VRFシミュレーターのスキャンデータを作成することができます。"))
        self.label_3_welcome.setText(_translate("Dialog_welcome", "作成作業を行う場合、“次へ”ボタンを、キャンセルの場合“キャンセル”ボタンを押下してください。"))
        self.btn_cancel_welcome.setText(_translate("Dialog_welcome", "キャンセル"))
        self.btn_next_welcome.setText(_translate("Dialog_welcome", "次へ"))

