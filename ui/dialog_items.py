# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_items.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_items(object):
    def setupUi(self, Dialog_items):
        Dialog_items.setObjectName("Dialog_items")
        Dialog_items.resize(572, 242)
        self.label = QtWidgets.QLabel(Dialog_items)
        self.label.setGeometry(QtCore.QRect(50, 50, 50, 12))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_1_items = QtWidgets.QLabel(Dialog_items)
        self.label_1_items.setGeometry(QtCore.QRect(90, 20, 431, 20))
        self.label_1_items.setObjectName("label_1_items")
        self.label_2_items = QtWidgets.QLabel(Dialog_items)
        self.label_2_items.setGeometry(QtCore.QRect(90, 40, 431, 20))
        self.label_2_items.setObjectName("label_2_items")
        self.label_3_items = QtWidgets.QLabel(Dialog_items)
        self.label_3_items.setGeometry(QtCore.QRect(90, 60, 431, 20))
        self.label_3_items.setObjectName("label_3_items")
        self.label_pic_items = QtWidgets.QLabel(Dialog_items)
        self.label_pic_items.setGeometry(QtCore.QRect(10, 20, 61, 61))
        self.label_pic_items.setText("")
        self.label_pic_items.setObjectName("label_pic_items")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog_items)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 100, 431, 51))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.radio_1_items = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radio_1_items.setObjectName("radio_1_items")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radio_1_items)
        self.radio_2_items = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radio_2_items.setObjectName("radio_2_items")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radio_2_items)
        self.label_1_radio_items = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_1_radio_items.setObjectName("label_1_radio_items")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_1_radio_items)
        self.label_2_radio_items = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2_radio_items.setObjectName("label_2_radio_items")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2_radio_items)
        self.line = QtWidgets.QFrame(Dialog_items)
        self.line.setGeometry(QtCore.QRect(10, 170, 551, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog_items)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 200, 361, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancel_items = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_cancel_items.setObjectName("btn_cancel_items")
        self.horizontalLayout.addWidget(self.btn_cancel_items)
        self.btn_detail_items = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_detail_items.setObjectName("btn_detail_items")
        self.horizontalLayout.addWidget(self.btn_detail_items)
        self.btn_create_items = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_create_items.setObjectName("btn_create_items")
        self.horizontalLayout.addWidget(self.btn_create_items)

        self.retranslateUi(Dialog_items)
        QtCore.QMetaObject.connectSlotsByName(Dialog_items)

    def retranslateUi(self, Dialog_items):
        _translate = QtCore.QCoreApplication.translate
        Dialog_items.setWindowTitle(_translate("Dialog_items", "Items"))
        self.label_1_items.setText(_translate("Dialog_items", "以下、試験をしたい項目を選び、“作成ボタン”を押下してください。"))
        self.label_2_items.setText(_translate("Dialog_items", "また、詳細を設定する場合、“詳細”ボタンを押下してください。"))
        self.label_3_items.setText(_translate("Dialog_items", "キャンセルの場合、“キャンセル”ボタンを押下してください。"))
        self.radio_1_items.setText(_translate("Dialog_items", "表示試験"))
        self.radio_2_items.setText(_translate("Dialog_items", "親子機試験"))
        self.label_1_radio_items.setText(_translate("Dialog_items", "モニタ画面や運転設定画面における要素の表示試験"))
        self.label_2_radio_items.setText(_translate("Dialog_items", "親機と子機混在の時に機能の有無試験"))
        self.btn_cancel_items.setText(_translate("Dialog_items", "キャンセル"))
        self.btn_detail_items.setText(_translate("Dialog_items", "詳細"))
        self.btn_create_items.setText(_translate("Dialog_items", "作成"))

