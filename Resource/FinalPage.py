# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'done.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

   

class Ui_Dialog(object):
    
    def setVesibality(self,vesibal):
        labels=[
            self.label,
            self.label_2,
            self.label_3,
            self.pushButton,
            self.line
            ]
        for l in labels:
            l.setVisible(vesibal)
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(801, 674)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 677))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/page2.png"))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 181, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/Neo_logo.png"))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QLabel(Dialog)
        self.line.setGeometry(QtCore.QRect(270, 330, 431, 31))
        self.line.setText("")
        self.line.setPixmap(QtGui.QPixmap("img/line.png"))
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 250, 581, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("img/done.png"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(491, 480, 221, 61))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(221, 61))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        
        
        # Define functionality
        def yesClick():
            Dialog.close()
        
        
        
        # Set Functionality
        self.pushButton.clicked.connect(yesClick)
        
        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

