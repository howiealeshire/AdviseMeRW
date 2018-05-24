import sys
sys.path.insert(0,'/Users/howard/AdviseMeRW/Register')
import register_app as Register
sys.path.insert(0,'/Users/howard/AdviseMeRW/Main/Root')
import root_app as Root

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox,QTimeEdit,QSpinBox,QLabel
from login_dialog import Ui_Dialog as ui_di
from PyQt5.QtCore import pyqtSlot
from operator import sub
from passlib.hash import pbkdf2_sha256



class Login_Dialog(QDialog):
    def __init__(self,username,password):
        super(Login_Dialog,self).__init__()
        self.ui = ui_di()
        self.ui.setupUi(self)
        self.username = username 
        
        self.password = password 
        self.curr_pass = self.ui.password_line_edit.text()
       
   
        self.register = self.ui.register_btn
        self.sign_in = self.ui.sign_in_btn
        

        self.register.clicked.connect(self.goto_register)
        self.sign_in.clicked.connect(self.goto_root)
        
        

        
        
        
        
    @pyqtSlot()
    def goto_register(self):
        self.regf = Register.Register_Dialog()
        self.regf.show()
        self.close()
        

    @pyqtSlot()
    def goto_root(self):
        if self.verify() == True:
            self.r_dialog = Root.Root_Dialog()
            
            self.r_dialog.show()
            self.close()
        else:
            self.user_incorrect_lbl = QLabel("Username or password incorrect",self)
            self.user_incorrect_lbl.move(19,190)
            self.user_incorrect_lbl.resize(201,20)
            self.user_incorrect_lbl.setStyleSheet("QLabel {color: red;}")
            self.user_incorrect_lbl.show()


            


    def verify(self):
        self.curr_user = self.ui.username_line_edit.text()
        self.curr_pass = self.ui.password_line_edit.text()

        print('*******')
        print(self.username)
        print(self.curr_user)
        print(self.password)
        print(self.curr_pass)
        print('******')
        password_verified = False
        username_verified = False
        if self.username == self.curr_user:
            username_verified = True
            print('here')
        
        
        #this block takes care of the case where the password provided is blank
        try:
            if pbkdf2_sha256.verify(self.curr_pass, self.password):
                password_verified = True
                print('there')
        except ValueError:
            pass
            

        print('username_verified: ' + str(username_verified))
        print('password_verified: ' + str(password_verified))
        print(str(password_verified and username_verified))
        return password_verified and username_verified


        



def main():
    app = QApplication(sys.argv)
    dialog = Login_Dialog('a','b')
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

