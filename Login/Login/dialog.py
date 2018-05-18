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
        Dialog.resize(262, 222)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.username_horiz_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.username_horiz_layout.setContentsMargins(11, 11, 11, 11)
        self.username_horiz_layout.setSpacing(6)
        self.username_horiz_layout.setObjectName("username_horiz_layout")
        self.username_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.username_lbl.setObjectName("username_lbl")
        self.username_horiz_layout.addWidget(self.username_lbl)
        self.username_line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.username_line_edit.setObjectName("username_line_edit")
        self.username_horiz_layout.addWidget(self.username_line_edit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 181, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.password_horiz_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.password_horiz_layout.setContentsMargins(11, 11, 11, 11)
        self.password_horiz_layout.setSpacing(6)
        self.password_horiz_layout.setObjectName("password_horiz_layout")
        self.password_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.password_lbl.setObjectName("password_lbl")
        self.password_horiz_layout.addWidget(self.password_lbl)
        self.password_line_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.password_line_edit.setObjectName("password_line_edit")
        self.password_horiz_layout.addWidget(self.password_line_edit)
        self.register_btn = QtWidgets.QPushButton(Dialog)
        self.register_btn.setGeometry(QtCore.QRect(130, 150, 113, 32))
        self.register_btn.setObjectName("register_btn")
        self.sign_in_btn = QtWidgets.QPushButton(Dialog)
        self.sign_in_btn.setGeometry(QtCore.QRect(10, 150, 113, 32))
        self.sign_in_btn.setObjectName("sign_in_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.username_lbl.setText(_translate("Dialog", "Username"))
        self.password_lbl.setText(_translate("Dialog", "Password"))
        self.register_btn.setText(_translate("Dialog", "Register"))
        self.sign_in_btn.setText(_translate("Dialog", "Sign In"))

