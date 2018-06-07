import sys
sys.path.insert(0,'/Users/howard/AdviseMeRW/Preferences')
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox,QTimeEdit
from ScheduleDialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from operator import sub




class Schedule_Dialog(QDialog):
    def __init__(self,courses):
        super(Schedule_Dialog,self).__init__()
        

        self.courses = courses
        print(self.courses)
        print("goodbye")
 #      self.courses = courses
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.tbl = self.ui.schedule_tbl
        
 #       self.preferences = (self.preference_string,)
        
        pref_btn = self.ui.preferences_btn
        rec_btn = self.ui.recommendations_btn
        make_btn = self.ui.create_schedule_btn
        lkahd_btn = self.ui.look_ahead_btn
        
        pref_btn.clicked.connect(self.gt_prefs)
        rec_btn.clicked.connect(self.gt_rec)
        make_btn.clicked.connect(self.mk_sched)
        lkahd_btn.clicked.connect(self.lkahd)


        
        unparsed_time = self.courses[1]['Time']
        unparsed_time = unparsed_time.split('-')
        p_time_from = int(unparsed_time[0])
        p_time_to = int(unparsed_time[1])
        
        i_row = int('0800')
        i = 0
        while i_row < p_time_from:
            i_row += 100
            i += 1
        print(i)
        print(i_row)
        print(p_time_from)
        self.tbl.setItem(i,0, QTableWidgetItem(self.courses[1]['Title']))
        

        
        
    
    
    @pyqtSlot()
    def gt_prefs(self):
        self.pref = Preferences.Preferences_Dialog()
        self.close()
        self.pref.show()

        
   
    @pyqtSlot()
    def gt_rec(self):
        pass
        
    @pyqtSlot()
    def mk_sched(self):
        pass
        
        
    @pyqtSlot()
    def lkahd(self):
        pass





def main():
    app = QApplication(sys.argv)
    dialog = Schedule_Dialog()















    
    dialog.show()
    #print(dialog.courses)

    #print(dialog.preference_string)
   # print('\n')
    #print(dialog.emp)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
