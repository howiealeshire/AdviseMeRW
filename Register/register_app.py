import sys
sys.path.insert(0,'/Users/howard/AdviseMeRW/Login/Login')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox,QTimeEdit,QSpinBox
from register_dialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from operator import sub
from passlib.hash import pbkdf2_sha256
import login_app as Login
import os

'''maybe implement login as an observer, so that way we don't have to pass 'user' and 'password' directly to it'''

class Register_Dialog(QDialog):
    def __init__(self):
        super(Register_Dialog,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.username = self.ui.username_line_edit
        self.password = self.ui.password_line_edit
        self.institution = self.ui.institution_line_edit
        self.major = self.ui.major_line_edit

        self.course_to_add = self.ui.course_line_edit
        self.added_courses = self.ui.courses_list_widget
        
        self.add = self.ui.add_btn
        self.register = self.ui.register_btn
        
        self.remove = self.ui.remove_btn
        
        self.add.clicked.connect(self.add_course)
        self.remove.clicked.connect(self.remove_course)

        
        
        self.register.clicked.connect(self.on_register)
    


 
        
    
    
    @pyqtSlot()
    def add_course(self):
        course = self.course_to_add.text()
        self.added_courses.addItem(course)
    
    @pyqtSlot()
    def remove_course(self):
        course = self.added_courses.takeItem(self.added_courses.currentRow())
        item = None
        
    @pyqtSlot()
    def on_register(self):
        
        self.goto_login()
        
       
    
    
        
        
        
    

    def goto_login(self):
        self.hash = pbkdf2_sha256.hash(self.password.text())

        self.close()
        self.logf = Login.Login_Dialog(self.username.text(),self.hash)
        self.logf.show()
        

        
def main():
    app = QApplication(sys.argv)
    dialog = Register_Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
