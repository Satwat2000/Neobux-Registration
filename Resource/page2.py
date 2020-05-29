# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reg_p2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from FinalPage import Ui_Dialog as finalui
import Db

class Ui_Dialog(object):
    
    def setVesibality(self,vesibal):
        labels=[
            self.label,
            self.label_2,
            self.label_3,
            self.code,
            self.label_4,
            self.Email,
            self.label_6,
            self.Cshow,
            self.capta,
            self.label_8,
            self.pushButton,
            self.line
            ]
        for l in labels:
            l.setVisible(vesibal)
        
        
    def setupUi(self, Dialog, browserob):
        
        # load This page 
        Dialog.setObjectName("Dialog")
        Dialog.resize(801, 674)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 677))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/page2.png"))
        # self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(360, 30, 561, 221))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/page2 im1.png"))
        # self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 181, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/Neo_logo.png"))
        # self.label_3.setObjectName("label_3")
        self.code = QtWidgets.QTextEdit(Dialog)
        self.code.setGeometry(QtCore.QRect(310, 310, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.code.setFont(font)
        self.code.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.code.setPlaceholderText("")
        # self.code.setObjectName("code")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(310, 270, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        # self.label_4.setObjectName("label_4")
        self.Email = QtWidgets.QLabel(Dialog)
        self.Email.setGeometry(QtCore.QRect(460, 270, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.Email.setFont(font)
        # self.Email.setObjectName("Email")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(320, 400, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        # self.label_6.setObjectName("label_6")
        self.Cshow = QtWidgets.QLabel(Dialog)
        self.Cshow.setGeometry(QtCore.QRect(630, 410, 121, 31))
        self.Cshow.setText("")
        self.Cshow.setPixmap(QtGui.QPixmap("img/capta.png"))
        # self.Cshow.setObjectName("Cshow")
        self.capta = QtWidgets.QTextEdit(Dialog)
        self.capta.setGeometry(QtCore.QRect(480, 410, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        self.capta.setFont(font)
        # self.capta.setObjectName("capta")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(330, 500, 431, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("img/line.png"))
        # self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(490, 550, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        # self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(530, 590, 131, 41))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line.setObjectName("line")
        self.only_cap = QtWidgets.QLabel(Dialog)
        self.only_cap.setGeometry(QtCore.QRect(270, 190, 311, 31))
        self.only_cap.setText("")
        self.only_cap.setPixmap(QtGui.QPixmap("img/errcap.png"))
        self.only_cap.setVisible(False)
        # self.only_cap.setObjectName("only_cap")
        self.only_code = QtWidgets.QLabel(Dialog)
        self.only_code.setGeometry(QtCore.QRect(270, 190, 471, 61))
        self.only_code.setText("")
        self.only_code.setPixmap(QtGui.QPixmap("img/Vcodeerr.png"))
        self.only_code.setVisible(False)
        # self.only_code.setObjectName("only_code")
        self.both = QtWidgets.QLabel(Dialog)
        self.both.setGeometry(QtCore.QRect(270, 190, 481, 81))
        self.both.setText("")
        self.both.setPixmap(QtGui.QPixmap("img/botherr.png"))
        self.both.setVisible(False)
        # self.both.setObjectName("both")
        # load Final ui
        self.FP = finalui()
        self.FP.setupUi(Dialog)
        self.FP.setVesibality(False)   # make Final Page invisable
        

        # # Def Connections        
        def yesClick():
            # Assign I/p's in Dict
            values={"Vcode": self.code.toPlainText(),
                    "Vcap": self.capta.toPlainText()}
            # Update Dict in Db
            Db.update('page2',values)
            #Fill in browser
            rdata = browserob.fill_page2()
            #Check for any error
            if rdata['pass']:
                browserob.getSnap('Final snap')
                self.FP.setVesibality(True)
            print("Rdata returned")
            self.only_code.setVisible(rdata['OnlyV'])
            self.only_cap.setVisible(rdata['OnlyC'])
            self.both.setVisible(rdata['Both'])
            self.Cshow.setPixmap(QtGui.QPixmap(browserob.get_capta()))
        
        # # Set Connections
        self.pushButton.clicked.connect(yesClick)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Validation code for"))
        self.Email.setText(_translate("Dialog", "TextLabel"))
        self.label_6.setText(_translate("Dialog", "Verification Code :"))
        self.capta.setPlaceholderText(_translate("Dialog", "Capta"))
        self.pushButton.setText(_translate("Dialog", "Finish Registration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, '')
    Dialog.show()
    sys.exit(app.exec_())
