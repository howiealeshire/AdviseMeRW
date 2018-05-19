import sys
sys.path.insert(0,'/Users/howard/AdviseMeRW/Register')
import register_app as Register

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox,QTimeEdit,QSpinBox
from login_dialog import Ui_Dialog as ui_di
from PyQt5.QtCore import pyqtSlot
from operator import sub
from passlib.hash import pbkdf2_sha256



class Login_Dialog(QDialog):
    def __init__(self):
        super(Login_Dialog,self).__init__()
        self.ui = ui_di()
        self.ui.setupUi(self)
        self.user_input = open('/Users/howard/AdviseMeRW/Register/user_input','r')
        self.username = self.ui.username_line_edit.text()
        self.password = self.ui.password_line_edit.text()
        
   
        self.register = self.ui.register_btn
        self.sign_in = self.ui.sign_in_btn
        
        self.register.clicked.connect(self.goto_register)
        self.sign_in.clicked.connect(self.goto_root)
        
        #self.verify()

        
        
        
        
    @pyqtSlot()
    def goto_register(self):
        self.regf = Register.Register_Dialog()
        self.regf.show()
        self.close()
        

    @pyqtSlot()
    def goto_root(self):
        regl = Register.Register_Dialog()
        self.verify(regl.hash)
        



             
    def verify(self,hash):
        #self.regx = Register.Register_Dialog()
    
        password_verified = False
        username_verified = False
        with self.user_input as u:
            for i, line in enumerate(u):
                if i == 0:
                    if(self.username == line):
                        username_verified = True
                if i == 1:
                    password_verified = pbkdf2_sha256.verify(self.password, hash)
        print(password_verified)
        print(username_verified)
        return password_verified and username_verified


        



def main():
    app = QApplication(sys.argv)
    dialog = Login_Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

