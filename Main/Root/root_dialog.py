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
        Dialog.resize(397, 252)
        self.email_advisor_btn = QtWidgets.QPushButton(Dialog)
        self.email_advisor_btn.setGeometry(QtCore.QRect(130, 140, 113, 32))
        self.email_advisor_btn.setObjectName("email_advisor_btn")
        self.transfer_credit_btn = QtWidgets.QPushButton(Dialog)
        self.transfer_credit_btn.setGeometry(QtCore.QRect(130, 100, 113, 32))
        self.transfer_credit_btn.setObjectName("transfer_credit_btn")
        self.adviseme_btn = QtWidgets.QPushButton(Dialog)
        self.adviseme_btn.setGeometry(QtCore.QRect(130, 60, 113, 32))
        self.adviseme_btn.setObjectName("adviseme_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.email_advisor_btn.setText(_translate("Dialog", "Email Advisor"))
        self.transfer_credit_btn.setText(_translate("Dialog", "Tranfer Credit"))
        self.adviseme_btn.setText(_translate("Dialog", "AdviseMe"))

