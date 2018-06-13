import sys
sys.path.insert(0,'/Users/howard/AdviseMeRW/Transfer')
import transfer_app as Transfer
sys.path.insert(0,'/Users/howard/AdviseMeRW/Preferences')
import PreferencesApp as Preferences
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
        self.advise = self.ui.adviseme_btn
        self.transfer = self.ui.transfer_credit_btn
        self.email = self.ui.email_advisor_btn

        self.advise.clicked.connect(self.goto_preferences)
        self.transfer.clicked.connect(self.goto_transfer)
        self.email.clicked.connect(self.goto_email)
        
        
        

    @pyqtSlot()
    def goto_preferences(self):
        self.pref = Preferences.Preferences_Dialog()
        self.pref.show()
        self.close()
    @pyqtSlot()
    def goto_transfer(self):
        self.tran = Transfer.Dialog()
        self.tran.show()
        self.close
    
    @pyqtSlot()
    def goto_email(self):
        pass








def main():
    app = QApplication(sys.argv)
    dialog = Root_Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

