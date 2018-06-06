import sys
sys.path.insert(0, '/Users/howard/AdviseMeRW/Schedule')
import ScheduleApp as Schedule
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox,QTimeEdit,QSpinBox
from dialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot
from operator import sub
import constraints


class Preferences_Dialog(QDialog):
    def __init__(self):
        super(Preferences_Dialog,self).__init__()
        #list that will store all info from preferences
        #to be written to file
        #must use set() function after apply
        
        #info = []

        #self.out_file = open('workfile','w')

        
        
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.buttons = self.ui.buttonBox.buttons()
        self.apply_button = self.buttons[2]
        self.cancel_button = self.buttons[1]
        self.ok_button = self.buttons[0]
        
        self.remove_cat_btn = self.ui.remove_cat_btn
        self.remove_loc_btn = self.ui.remove_loc_btn
        self.remove_prof_btn = self.ui.remove_prof_btn
        self.remove_subj_btn = self.ui.remove_sub_btn

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.apply_button.clicked.connect(self.apply_changes)

        

        self.all_chk = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"all_days_chk")
        self.all_chk.clicked.connect(self.check_all_days)
    
        self.time_from_edit =  self.get_child_widget(self.ui.time_available_grpbox,QTimeEdit,"available_from_time_edit")
        self.time_to_edit =  self.get_child_widget(self.ui.time_available_grpbox,QTimeEdit,"available_to_time_edit")

        self.cat_list = self.ui.cat_list
        self.loc_list = self.ui.loc_list
        self.prof_list = self.ui.prof_list
        self.subj_list = self.ui.sub_list 
    
        self.remove_cat_btn.clicked.connect(lambda: self.remove_item(self.cat_list))
        self.remove_loc_btn.clicked.connect(lambda: self.remove_item(self.loc_list))
        self.remove_prof_btn.clicked.connect(lambda: self.remove_item(self.prof_list))
        self.remove_subj_btn.clicked.connect(lambda: self.remove_item(self.subj_list))





    
    @pyqtSlot()
    def apply_changes(self):
        
        
        #need to write categories, locations, professors, subjects
        category = self.get_category()
        location = self.get_location()
        professor = self.get_professor()
        subject = self.get_subject()
        
        if category not in self.get_all_from_list(self.cat_list):
            self.cat_list.addItem(category)
        if location not in self.get_all_from_list(self.loc_list):
            self.loc_list.addItem(location)
        if professor not in self.get_all_from_list(self.prof_list):
            self.prof_list.addItem(professor)
        if subject not in self.get_all_from_list(self.subj_list):
            self.subj_list.addItem(subject)

        
        
    @pyqtSlot()
    def remove_item(self,input_list):
        item = input_list.takeItem(input_list.currentRow())
        item = None


    @pyqtSlot()
    def accept(self):
        #loc = self.get_location()
        #cat = self.get_category()
        #prof = self.get_professor()
        days = self.get_days()
        
        locs = self.get_all_from_list(self.loc_list)
        cats = self.get_all_from_list(self.cat_list)
        profs = self.get_all_from_list(self.prof_list)
        subjects = self.get_all_from_list(self.subj_list)
    
        time_to = self.get_time_to()
        time_from = self.get_time_from()
        time_interval = self.get_time_available()
        #subjects = self.get_subject()
        num_courses = self.get_num_course_interval()
    
            
        
        
        final_courses_list = constraints.main(locs,cats,profs,days,time_to,time_from,time_interval,subjects,num_courses)
        #print(final_courses_list)
            

        self.sched = Schedule.Schedule_Dialog(final_courses_list)
        self.close()
        self.sched.show()    

 #       sched = Schedule.main()
#        self.close()
    
    #method essentially taken from user @delnan from Stack Overflow: https://stackoverflow.com/questions/4629584/pyqt4-how-do-you-iterate-all-items-in-a-qlistwidget    
    def get_all_from_list(self,list_w):
        list_items = []
        for i in range(list_w.count()):
            list_items.append(list_w.item(i).text())
        return list_items

    
        


    def get_time_available(self):
        return tuple(map(sub,self.get_time_to(), self.get_time_from()))
    def get_time_from(self):
        time_from =  self.get_child_widget(self.ui.time_available_grpbox,QTimeEdit,"available_from_time_edit")
        return (time_from.time().hour(),time_from.time().minute())
        #print(time_from.time().hour())
        #print(str(time_to.time().hour()))
    def get_time_to(self):
        time_to =  self.get_child_widget(self.ui.time_available_grpbox,QTimeEdit,"available_to_time_edit")
        return (time_to.time().hour(),time_to.time().minute())

    
    def get_category(self):
       # category = self.ui.category_grpbox.findChild(QComboBox,"category_comb")
       # category_text = str(category.currentText())
        #cat_list = []
        return self.get_cwtext(self.ui.category_grpbox,QComboBox,"category_comb")
        #return cat_list

    def get_location(self):
        #loc_list = []
        return self.get_cwtext(self.ui.location_grpbox,QComboBox,"location_comb")
        #return loc_list
        
    
    def get_days(self):
        
        return (self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"all_days_chk"),
        self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"monday_chk") ,
        self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"tues_chk"),
        self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"wed_chk"),
        self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"thurs_chk"),
        self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"fri_chk"))
    
    @pyqtSlot()
    def check_all_days(self):
        all_is_checked = self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"all_days_chk")
        if all_is_checked:
            self.check_rest()
        
    def check_rest(self):
        monday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"monday_chk")
        tuesday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"tues_chk")
        wednesday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"wed_chk")
        thursday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"thurs_chk")
        friday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"fri_chk")
        
        monday.setChecked(True)
        tuesday.setChecked(True)
        wednesday.setChecked(True)
        thursday.setChecked(True)
        friday.setChecked(True)
        
        #immediately update gui to reflect changes
        #note: choice of monday is arbitrary
        monday.repaint()
        
    def get_subject(self):
        #subject_list = []
        return self.get_cwtext(self.ui.subject_grpbox,QComboBox,"subject_comb")
        #return subject_list

    def get_num_course_interval(self):
        min_course_w = self.ui.min_courses_grpbox.findChild(QSpinBox,"min_courses_spin")
        min_num_course = min_course_w.value()
        max_course_w = self.ui.max_courses_grpbox.findChild(QSpinBox,"max_courses_spin")
        max_num_course = max_course_w.value()
        return (min_num_course,max_num_course)


    def get_child_widget(self,parent,child_widget_type,child_name):
        child = parent.findChild(child_widget_type,child_name)
        return child

        

    def get_checkbox_helper(self,parent,child_widget_type,child_name):
        child = parent.findChild(child_widget_type,child_name)
        child_is_checked = child.isChecked()
        return child_is_checked

    def get_professor(self):
        #prof_list = []
        return self.get_cwtext(self.ui.professor_grpbox,QComboBox,"professor_comb")
        #return prof_list

    def get_cwtext(self,parent,child_widget_type,child_name):
        child = parent.findChild(child_widget_type,child_name)
        child_text = str(child.currentText())
        return child_text


def main():
    app = QApplication(sys.argv)
    dialog = Preferences_Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
