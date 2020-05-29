# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import Db, datetime, re
from PyQt5 import QtCore, QtGui, QtWidgets
now = datetime.datetime.now()       # year
now = now.year

class Ui_Dialog(object):
    def __init__(self):
        self.compFillup = False
    def setupUi(self, Dialog, browserob, path=""):
        Dialog.setObjectName("Dialog")
        Dialog.resize(516, 576)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 561, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/Neo.png"))
        self.label.setObjectName("label")
        self.Vefrify_C = QtWidgets.QLabel(Dialog)
        self.Vefrify_C.setGeometry(QtCore.QRect(80, 410, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Vefrify_C.setFont(font)
        self.Vefrify_C.setObjectName("Vefrify_C")
        self.info1 = QtWidgets.QLabel(Dialog)
        self.info1.setGeometry(QtCore.QRect(220, 10, 271, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.info1.setFont(font)
        self.info1.setObjectName("info1")
        self.username = QtWidgets.QTextEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(240, 160, 251, 31))
        self.username.setObjectName("username")
        self.password = QtWidgets.QTextEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(240, 230, 251, 31))
        self.password.setObjectName("password")
        self.Username = QtWidgets.QLabel(Dialog)
        self.Username.setGeometry(QtCore.QRect(130, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.info3 = QtWidgets.QLabel(Dialog)
        self.info3.setGeometry(QtCore.QRect(270, 60, 201, 21))
        self.info3.setObjectName("info3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 470, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.enter_cap = QtWidgets.QTextEdit(Dialog)
        self.enter_cap.setGeometry(QtCore.QRect(240, 410, 111, 31))
        self.enter_cap.setObjectName("enter_cap")
        self.dob = QtWidgets.QTextEdit(Dialog)
        self.dob.setGeometry(QtCore.QRect(240, 360, 111, 31))
        self.dob.setObjectName("dob")
        self.DOB = QtWidgets.QLabel(Dialog)
        self.DOB.setGeometry(QtCore.QRect(130, 360, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.DOB.setFont(font)
        self.DOB.setObjectName("DOB")
        self.Neo_icon = QtWidgets.QLabel(Dialog)
        self.Neo_icon.setGeometry(QtCore.QRect(10, 10, 171, 61))
        self.Neo_icon.setText("")
        self.Neo_icon.setPixmap(QtGui.QPixmap("img/Neo_logo.png"))
        self.Neo_icon.setObjectName("Neo_icon")
        self.email = QtWidgets.QTextEdit(Dialog)
        self.email.setGeometry(QtCore.QRect(240, 300, 251, 31))
        self.email.setObjectName("email")
        self.info2 = QtWidgets.QLabel(Dialog)
        self.info2.setGeometry(QtCore.QRect(190, 30, 311, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.info2.setFont(font)
        self.info2.setObjectName("info2")
        self.info6 = QtWidgets.QLabel(Dialog)
        self.info6.setGeometry(QtCore.QRect(30, 540, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Typewriter")
        font.setPointSize(6)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.info6.setFont(font)
        self.info6.setObjectName("info6")
        self.Password = QtWidgets.QLabel(Dialog)
        self.Password.setGeometry(QtCore.QRect(130, 230, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Password.setFont(font)
        self.Password.setObjectName("Password")
        self.info4 = QtWidgets.QLabel(Dialog)
        self.info4.setGeometry(QtCore.QRect(10, 90, 511, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.info4.setFont(font)
        self.info4.setObjectName("info4")
        self.Email = QtWidgets.QLabel(Dialog)
        self.Email.setGeometry(QtCore.QRect(170, 300, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Email.setFont(font)
        self.Email.setObjectName("Email")
        self.info5 = QtWidgets.QLabel(Dialog)
        self.info5.setGeometry(QtCore.QRect(70, 110, 261, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.info5.setFont(font)
        self.info5.setObjectName("info5")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(240, 480, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(370, 410, 121, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(path))
        self.label_2.setObjectName("label_2")
        self.btncheck_err = QtWidgets.QLabel(Dialog)
        self.btncheck_err.setGeometry(QtCore.QRect(250, 510, 231, 21))
        self.btncheck_err.setText("")
        self.btncheck_err.setPixmap(QtGui.QPixmap("img/warning totle.png"))
        self.btncheck_err.setObjectName("btncheck_err")
        self.user_err = QtWidgets.QLabel(Dialog)
        self.user_err.setGeometry(QtCore.QRect(200, 190, 291, 21))
        self.user_err.setText("")
        self.user_err.setPixmap(QtGui.QPixmap("img/user_error2.png"))
        self.user_err.setObjectName("user_err")
        self.pass_err = QtWidgets.QLabel(Dialog)
        self.pass_err.setGeometry(QtCore.QRect(200, 260, 291, 21))
        self.pass_err.setText("")
        self.pass_err.setPixmap(QtGui.QPixmap("img/pass_len_err.png"))
        self.pass_err.setObjectName("pass_err")
        self.email_err = QtWidgets.QLabel(Dialog)
        self.email_err.setGeometry(QtCore.QRect(200, 330, 201, 21))
        self.email_err.setText("")
        self.email_err.setPixmap(QtGui.QPixmap("img/email_err.png"))
        self.email_err.setObjectName("email_err")
        self.capta_err = QtWidgets.QLabel(Dialog)
        self.capta_err.setGeometry(QtCore.QRect(200, 440, 201, 21))
        self.capta_err.setText("")
        self.capta_err.setPixmap(QtGui.QPixmap("img/capta_err.png"))
        self.capta_err.setObjectName("capta_err")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 290, 501, 241))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/billi.png"))
        self.label_3.setObjectName("label_3")
        self.label_3.setVisible(False)
        self.check_err = QtWidgets.QLabel(Dialog)
        self.check_err.setGeometry(QtCore.QRect(250, 510, 231, 21))
        self.check_err.setText("")
        self.check_err.setPixmap(QtGui.QPixmap("img/check_sub.png"))
        self.check_err.setObjectName("check_err")
        self.doberr = QtWidgets.QLabel(Dialog)
        self.doberr.setGeometry(QtCore.QRect(360, 365, 30, 25))
        self.doberr.setText("")
        self.doberr.setPixmap(QtGui.QPixmap("img/doberr.png"))
        self.doberr.setObjectName("doberr")
        self.doberr.setVisible(False)
        # Password length Constrain
        def checkpass():
            s = self.password.toPlainText()
            n = len(s)
            print(s,"-->",n)
            if n >= 8:
                self.pass_err.setVisible(False)
            else:
                self.pass_err.setVisible(True)
        # Email Constrain
        def checkmail():
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if not re.search(regex,self.email.toPlainText()):
                print("email flag")
                self.email_err.setVisible(True)
            else:
                self.email_err.setVisible(False)
        # Checkbox Constrain
        def checkbtbn():
            if self.checkBox.isChecked():
                self.btncheck_err.setVisible(False)
                
       
        # DOB Constrain
        def doberr():
            string = self.dob.toPlainText()
            if len(string)>4:
                print("DOB flag")
                self.errdob = True
                self.doberr.setVisible(True)
        
            else:
                dif = now - int(string)
                if dif < 10:
                    self.errdob = True
                    self.doberr.setVisible(True)
                else:
                    self.errdob = False
                    self.doberr.setVisible(False)
        
        # Username Constrain
        def checkuser():
            string = self.username.toPlainText()
            if len(string) > 14:
                print(string[:-1])
                self.username.setText(string[:-1])
                     
        # error..fields....!!!!
        user_err, pass_err, email_err, capta_err, btncheck_err, check_err = (False, False, False, False, False, False)
        self.user_err.setVisible(user_err)
        self.username.textChanged.connect(checkuser)
        self.pass_err.setVisible(pass_err)
        self.password.textChanged.connect(checkpass)
        self.email_err.setVisible(email_err)
        self.email.textChanged.connect(checkmail)
        self.capta_err.setVisible(capta_err)
        self.btncheck_err.setVisible(btncheck_err)
        self.check_err.setVisible(check_err)
        self.checkBox.clicked.connect(checkbtbn)
        self.dob.textChanged.connect(doberr)
        print ()


        # add actions...
        def clickyes():
            if not self.pass_err.isVisible() and not self.email_err.isVisible() and not self.errdob :
                if self.checkBox.isChecked():
                    # All constrains checked to proceed
                    print("sleep over")
                    values = {
                        "user": self.username.toPlainText(),
                        "pswd": self.password.toPlainText(),
                        "mail": self.email.toPlainText(),
                        "year": self.dob.toPlainText(),
                        "code": self.enter_cap.toPlainText()
                    }
                    Db.update('page1',values)
                    #fill info in browswe
                    rdata = browserob.fill_info()
                    #chek to proceed
                    if rdata['pass']:
                        browserob.getSnap('Form Filled')
                        Dialog.close()
                        self.compFillup = True
                    print("Rdata returned")
                    self.user_err.setVisible(rdata['usr'])
                    self.capta_err.setVisible(rdata['capt'])
                    self.email_err.setVisible(rdata['mail'])
                    self.label_2.setPixmap(QtGui.QPixmap(browserob.get_capta()))
                else:
                    self.btncheck_err.setVisible(True)
            else:
                self.check_err.setVisible(True)
                self.btncheck_err.setVisible(False)
    
        self.pushButton.clicked.connect(clickyes)
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Vefrify_C.setText(_translate("Dialog", "Verification Code :"))
        self.info1.setText(_translate("Dialog", "You are just a minute away from changing "))
        self.Username.setText(_translate("Dialog", "Username :"))
        self.info3.setText(_translate("Dialog", "!! ~ Trusted sinsce 2006"))
        self.pushButton.setText(_translate("Dialog", "Continue"))
        self.DOB.setText(_translate("Dialog", "Birth Year :"))
        self.info2.setText(_translate("Dialog", "the way you make maoney online forever."))
        self.info6.setText(_translate("Dialog", "Please enter a valid email address for recieving the email confirmation mail"))
        self.Password.setText(_translate("Dialog", "Password :"))
        self.info4.setText(_translate("Dialog", "Unlike many other sites, we will always offer the best possible rewards for your"))
        self.Email.setText(_translate("Dialog", "Email :"))
        self.info5.setText(_translate("Dialog", "for your activities in a safe, accomodating and multi-language enviroment."))
        self.checkBox.setText(_translate("Dialog", "Confirm Submission"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog," ")
    Dialog.show()
    sys.exit(app.exec_())
