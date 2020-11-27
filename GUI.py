# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:26:01 2020

@author: cttc
"""

from PyQt5 import uic,QtWidgets
from dbms import Student
 
def gotostudent():
  frontpage.close()
  studentpage.show()
  
def backfromstudentPage():
  studentpage.close()
  frontpage.show()
  
def gotofaculty():
  frontpage.close()
  facultylogin.show()
  
def backfromfacultylogin():
  facultylogin.close()
  frontpage.show()
def gotoadminlogin():
  frontpage.close()
  adminlogin.show()
  
def backfromadminlogin():
  adminlogin.close()
  frontpage.show()
  
def gotofacultydashboard():
  facultylogin.close()
  facultydashboard.show()
  
def backfromfacultydashboard():
   facultydashboard.close()
   facultylogin.show()
def resisterstudent():
  facultydashboard.close()
  registerstudent.show()
  
def backfromregisterstudent():
   registerstudent.close()
   frontpage.show()

def capturedata():
    Sid = registerstudent.lineEdit_2.text()
    Sname = registerstudent.lineEdit.text()
    Sclass_id = registerstudent.lineEdit_3.text()
    Sphone_no = registerstudent.lineEdit_4.text()
    Spassword =  registerstudent.lineEdit_6.text()
    URL    =  registerstudent.lineEdit_7.text()
    s = Student()
    s.register(URL,Sid,Sname,Sclass_id,Sphone_no,Spassword)

       
app = QtWidgets.QApplication([])

frontpage = uic.loadUi('uifiles/FrontPage.ui') 
studentpage = uic.loadUi('uifiles/student_Login.ui')
facultylogin = uic.loadUi('uifiles/Faculty Login.ui')
adminlogin = uic.loadUi('uifiles/Admin_login.ui')
facultydashboard =  uic.loadUi('uifiles/Faculty_dashboard1.ui')
registerstudent =  uic.loadUi('uifiles/sTUDENT REGISTER.ui')

frontpage.show()

frontpage.Student_Login.clicked.connect(gotostudent)
studentpage.pushButton_2.clicked.connect(backfromstudentPage)

frontpage.Faculty_Login.clicked.connect(gotofaculty)
facultylogin.pushButton_2.clicked.connect(backfromfacultylogin)
frontpage.pushButton_3.clicked.connect(gotoadminlogin)
adminlogin.pushButton_2.clicked.connect(backfromadminlogin)
facultylogin.pushButton.clicked.connect(gotofacultydashboard)
facultydashboard.pushButton_3.clicked.connect(backfromfacultydashboard)
facultydashboard.Resister.clicked.connect(resisterstudent)
registerstudent.pushButton_2.clicked.connect(backfromregisterstudent)
registerstudent.pushButton.clicked.connect(capturedata)


app.exec()


