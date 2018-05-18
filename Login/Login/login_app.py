import sys
sys.path.insert(0,'/Users/howard/AdviseMeRW/Register')
import register_app as Register

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox,QTimeEdit,QSpinBox
from login_dialog import Ui_Dialog as ui_di
from PyQt5.QtCore import pyqtSlot
from operator import sub



class Login_Dialog(QDialog):
    def __init__(self):
        super(Login_Dialog,self).__init__()
        self.ui = ui_di()
        self.ui.setupUi(self)



def main():
    app = QApplication(sys.argv)
    dialog = Login_Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

