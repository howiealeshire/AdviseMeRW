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
        Dialog.resize(809, 474)
        self.schedule_tbl = QtWidgets.QTableWidget(Dialog)
        self.schedule_tbl.setGeometry(QtCore.QRect(70, 80, 541, 257))
        self.schedule_tbl.setObjectName("schedule_tbl")
        self.schedule_tbl.setColumnCount(5)
        self.schedule_tbl.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.schedule_tbl.setItem(2, 3, item)
        self.look_ahead_btn = QtWidgets.QPushButton(Dialog)
        self.look_ahead_btn.setGeometry(QtCore.QRect(620, 190, 141, 31))
        self.look_ahead_btn.setObjectName("look_ahead_btn")
        self.create_schedule_btn = QtWidgets.QPushButton(Dialog)
        self.create_schedule_btn.setGeometry(QtCore.QRect(620, 160, 141, 31))
        self.create_schedule_btn.setObjectName("create_schedule_btn")
        self.schedule_me_lbl = QtWidgets.QLabel(Dialog)
        self.schedule_me_lbl.setGeometry(QtCore.QRect(330, 50, 81, 16))
        self.schedule_me_lbl.setObjectName("schedule_me_lbl")
        self.recommendations_btn = QtWidgets.QPushButton(Dialog)
        self.recommendations_btn.setGeometry(QtCore.QRect(620, 130, 141, 31))
        self.recommendations_btn.setObjectName("recommendations_btn")
        self.preferences_btn = QtWidgets.QPushButton(Dialog)
        self.preferences_btn.setGeometry(QtCore.QRect(620, 100, 141, 31))
        self.preferences_btn.setObjectName("preferences_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.schedule_tbl.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "8 am"))
        item = self.schedule_tbl.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "8"))
        item = self.schedule_tbl.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "9"))
        item = self.schedule_tbl.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "10"))
        item = self.schedule_tbl.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "11"))
        item = self.schedule_tbl.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "12 pm"))
        item = self.schedule_tbl.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "1"))
        item = self.schedule_tbl.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "2"))
        item = self.schedule_tbl.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "3"))
        item = self.schedule_tbl.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "4"))
        item = self.schedule_tbl.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "5"))
        item = self.schedule_tbl.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "6"))
        item = self.schedule_tbl.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "7"))
        item = self.schedule_tbl.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "8"))
        item = self.schedule_tbl.verticalHeaderItem(14)
        item.setText(_translate("Dialog", "9"))
        item = self.schedule_tbl.verticalHeaderItem(15)
        item.setText(_translate("Dialog", "11"))
        item = self.schedule_tbl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Monday"))
        item = self.schedule_tbl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Tuesday"))
        item = self.schedule_tbl.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Wednesday"))
        item = self.schedule_tbl.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Thursday"))
        item = self.schedule_tbl.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Friday"))
        __sortingEnabled = self.schedule_tbl.isSortingEnabled()
        self.schedule_tbl.setSortingEnabled(False)
        item = self.schedule_tbl.item(0, 0)
        item.setText(_translate("Dialog", "Princpls of Biology I Lab"))
        item = self.schedule_tbl.item(0, 1)
        item.setText(_translate("Dialog", "Moleculr Bio Apprch in Resrch"))
        item = self.schedule_tbl.item(0, 2)
        item.setText(_translate("Dialog", "General Chemistry Lab I"))
        item = self.schedule_tbl.item(2, 1)
        item.setText(_translate("Dialog", "Approach to Literature"))
        item = self.schedule_tbl.item(2, 3)
        item.setText(_translate("Dialog", "Tpc Nonwest Lit:Postcolnl Dev"))
        item.setText(_translate("Dialog", "course1"))
        item = self.schedule_tbl.item(0, 1)
        item.setText(_translate("Dialog", "course2"))
        item = self.schedule_tbl.item(0, 2)
        item.setText(_translate("Dialog", "course1"))
        item = self.schedule_tbl.item(2, 1)
        item.setText(_translate("Dialog", "course3"))
        item = self.schedule_tbl.item(2, 3)
        item.setText(_translate("Dialog", "course3"))
        self.schedule_tbl.setSortingEnabled(__sortingEnabled)
        self.look_ahead_btn.setText(_translate("Dialog", "Look Ahead"))
        self.create_schedule_btn.setText(_translate("Dialog", "Create Schedule"))
        self.schedule_me_lbl.setText(_translate("Dialog", "ScheduleMe"))
        self.recommendations_btn.setText(_translate("Dialog", "Recommendations"))
        self.preferences_btn.setText(_translate("Dialog", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

