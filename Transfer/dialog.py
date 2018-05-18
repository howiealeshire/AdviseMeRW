# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(671, 463)
        self.register_btn = QtWidgets.QPushButton(Dialog)
        self.register_btn.setGeometry(QtCore.QRect(440, 430, 113, 32))
        self.register_btn.setObjectName("register_btn")
        self.sign_in_btn = QtWidgets.QPushButton(Dialog)
        self.sign_in_btn.setGeometry(QtCore.QRect(550, 430, 113, 32))
        self.sign_in_btn.setObjectName("sign_in_btn")
        self.password_line_edit = QtWidgets.QLineEdit(Dialog)
        self.password_line_edit.setGeometry(QtCore.QRect(200, 120, 113, 21))
        self.password_line_edit.setObjectName("password_line_edit")
        self.username_line_edit = QtWidgets.QLineEdit(Dialog)
        self.username_line_edit.setGeometry(QtCore.QRect(200, 80, 113, 21))
        self.username_line_edit.setObjectName("username_line_edit")
        self.password_lbl = QtWidgets.QLabel(Dialog)
        self.password_lbl.setGeometry(QtCore.QRect(110, 120, 61, 16))
        self.password_lbl.setObjectName("password_lbl")
        self.username_lbl = QtWidgets.QLabel(Dialog)
        self.username_lbl.setGeometry(QtCore.QRect(110, 80, 71, 16))
        self.username_lbl.setObjectName("username_lbl")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.register_btn.setText(_translate("Dialog", "Register"))
        self.sign_in_btn.setText(_translate("Dialog", "Sign In"))
        self.password_lbl.setText(_translate("Dialog", "Password"))
        self.username_lbl.setText(_translate("Dialog", "Username"))

