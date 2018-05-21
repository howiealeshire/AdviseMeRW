import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox,QTimeEdit,QSpinBox
from transfer_dialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from operator import sub



class Dialog(QDialog):
    def __init__(self):
        super(Dialog,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.uni_from = self.ui.uni_from_box.currentText()
        self.uni_to = self.ui.courses_to_box.currentText()
        
        '''
        Things needed:
        1.) Determine what the courses from a university correspond to
        2.) Once mapping from 1.) is done, intersect the objects mapped to with the university transferring to's courses
        3.) Print in box
        '''
        



def main():
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

