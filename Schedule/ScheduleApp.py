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
        #print(self.courses)
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

        i = 0
        while i < 1:

            #handle time
            unparsed_time = str(self.courses[i]['Time'])
            unparsed_time = unparsed_time.split('-')
        
            if unparsed_time[0] != 'nan':
                p_time_from = int(unparsed_time[0])
            else:
                p_time_from = int('1100')
            if unparsed_time[1] != 'nan':
                p_time_to = int(unparsed_time[1])
            else:
                p_time_to = int('1200')
            p_time_to = int(unparsed_time[1])
            
            i_row = int('0800')
            j = 0
            while i_row < p_time_from:
                i_row += 100
                j += 1
            print(j)
            print(i_row)
            print(p_time_from)

            #handle days
            u_days = self.courses[i]['Days']
            for day in u_days:
                print('^^^^')
                print(day)
                print('^^^^')
                if day == 'M':
                    self.tbl.setItem(j,0, QTableWidgetItem(self.courses[i]['Title']))
                if day == 'T':
                    self.tbl.setItem(j,1, QTableWidgetItem(self.courses[i]['Title']))
                if day == 'W':
                    self.tbl.setItem(j,2, QTableWidgetItem(self.courses[i]['Title']))
                if day == 'R':
                    self.tbl.setItem(j,3, QTableWidgetItem(self.courses[i]['Title']))
                if day == 'F':
                    self.tbl.setItem(j,4, QTableWidgetItem(self.courses[i]['Title']))
            
            i += 1
        
    
    
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
