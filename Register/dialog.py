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
        Dialog.resize(667, 468)
        self.username_lbl = QtWidgets.QLabel(Dialog)
        self.username_lbl.setGeometry(QtCore.QRect(30, 40, 71, 16))
        self.username_lbl.setObjectName("username_lbl")
        self.password_lbl = QtWidgets.QLabel(Dialog)
        self.password_lbl.setGeometry(QtCore.QRect(30, 70, 60, 16))
        self.password_lbl.setObjectName("password_lbl")
        self.institution_lbl = QtWidgets.QLabel(Dialog)
        self.institution_lbl.setGeometry(QtCore.QRect(30, 100, 60, 16))
        self.institution_lbl.setObjectName("institution_lbl")
        self.enter_completed_courses_lbl = QtWidgets.QLabel(Dialog)
        self.enter_completed_courses_lbl.setGeometry(QtCore.QRect(30, 240, 161, 16))
        self.enter_completed_courses_lbl.setObjectName("enter_completed_courses_lbl")
        self.username_line_edit = QtWidgets.QLineEdit(Dialog)
        self.username_line_edit.setGeometry(QtCore.QRect(120, 40, 113, 21))
        self.username_line_edit.setObjectName("username_line_edit")
        self.major_line_edit = QtWidgets.QLineEdit(Dialog)
        self.major_line_edit.setGeometry(QtCore.QRect(120, 130, 113, 21))
        self.major_line_edit.setObjectName("major_line_edit")
        self.institution_line_edit = QtWidgets.QLineEdit(Dialog)
        self.institution_line_edit.setGeometry(QtCore.QRect(120, 100, 113, 21))
        self.institution_line_edit.setObjectName("institution_line_edit")
        self.password_line_edit = QtWidgets.QLineEdit(Dialog)
        self.password_line_edit.setGeometry(QtCore.QRect(120, 70, 113, 21))
        self.password_line_edit.setObjectName("password_line_edit")
        self.course_line_edit = QtWidgets.QLineEdit(Dialog)
        self.course_line_edit.setGeometry(QtCore.QRect(30, 280, 113, 21))
        self.course_line_edit.setObjectName("course_line_edit")
        self.major_lbl = QtWidgets.QLabel(Dialog)
        self.major_lbl.setGeometry(QtCore.QRect(30, 130, 41, 16))
        self.major_lbl.setObjectName("major_lbl")
        self.register_btn = QtWidgets.QPushButton(Dialog)
        self.register_btn.setGeometry(QtCore.QRect(340, 240, 113, 32))
        self.register_btn.setObjectName("register_btn")
        self.add_btn = QtWidgets.QPushButton(Dialog)
        self.add_btn.setGeometry(QtCore.QRect(180, 280, 113, 32))
        self.add_btn.setObjectName("add_btn")
        self.course_text_edit = QtWidgets.QTextEdit(Dialog)
        self.course_text_edit.setGeometry(QtCore.QRect(50, 320, 321, 131))
        self.course_text_edit.setObjectName("course_text_edit")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 270, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.username_lbl.setText(_translate("Dialog", "Username"))
        self.password_lbl.setText(_translate("Dialog", "Password"))
        self.institution_lbl.setText(_translate("Dialog", "Institution"))
        self.enter_completed_courses_lbl.setText(_translate("Dialog", "Enter Completed Courses"))
        self.major_lbl.setText(_translate("Dialog", "Major"))
        self.register_btn.setText(_translate("Dialog", "Register"))
        self.add_btn.setText(_translate("Dialog", "Add"))

