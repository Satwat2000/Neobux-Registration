import sys,os
import process
import Uiform, error
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMessageBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from page2 import Ui_Dialog as pg2ui


# Font Start
font = QtGui.QFont()
font.setFamily("Informal Roman")
font.setPointSize(14)
font.setBold(True)
font.setWeight(50)
# Font End

        
class HomePage ( QWidget ):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Neobux")
        self.homeLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget = self._centralWidget
        self._centralWidget.setLayout(self.homeLayout)
        self.addLabel()
        self.add_btn()
        # Make instance of Process class
        self.Do = process.func()
        #load 2nd page ui
        self.S2 = pg2ui()
        self.S2.setupUi(self, self.Do)
        self.S2.setVesibality(False)   # make 2nd page ui invisable
        
       
    def addLabel(self):
        bg = QLabel(self)
        path = "img\main.png"
        pic = QtGui.QPixmap(path)
        bg.setPixmap(pic)
        self.setGeometry(240,200,pic.width(),pic.height())
        
        logo = QLabel(self)
        path_ = "img\logo.png"
        pic = QtGui.QPixmap(path_)
        logo.setPixmap(pic)
        logo.move(620,10)
        
    def add_btn(self):
        self.btn = QPushButton('',self)
        self.btn.setFont(font)
        self.btn.move(490,600)
        self.btn.setFixedSize(253,66)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/register.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn.setIcon(icon)
        self.btn.setIconSize(QtCore.QSize(243, 56))

# Class To give functionaluities to the buttons
class contrl():
    def __init__(self,view):
        self.Do = view.Do
        self.view = view
        self.connectSignal()
    
    def connectSignal(self):
        self.view.btn.clicked.connect(self.doit)
    
    def doit(self):
        print("button clicked")
        path = self.Do.open_url()
        self.Do.getSnap("Opening url")
        if path:
            Dialog = QDialog()
            # Make object of Form class
            self.fillui = Uiform.Ui_Dialog()
            #make the form class
            self.fillui.setupUi(Dialog, self.Do, self.Do.get_capta())
            # Dialog.show()   #---> Modeless Dialog
            Dialog.exec_()    #--->Mode Dialog
            
            print('Returned form Uiform')
            # Show up the 2nd page
            if self.fillui.compFillup :
                self.Do.getSnap('Email Verification')
                self.view.S2.setVesibality(True)
                self.view.S2.Email.setText(self.Do.get_email() )
                self.view.S2.Cshow.setPixmap(QtGui.QPixmap(self.Do.get_capta()))
                print ("Form Fill up completed")
            
        else:
            Dialog = QDialog()
            self.noui = error.Ui_Dialog()
            self.noui.setupUi(Dialog)
            Dialog.exec_()
        print ("Returned from page2 returned")
            
       


if __name__ == '__main__':
    app = QApplication([])
    home = HomePage()
    home.show()
    conn = contrl(home)
    sys.exit(app.exec_())
        