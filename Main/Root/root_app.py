import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox,QTimeEdit,QSpinBox
from root_dialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from operator import sub



class Root_Dialog(QDialog):
    def __init__(self):
        super(Root_Dialog,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        






def main():
    app = QApplication(sys.argv)
    dialog = Root_Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

