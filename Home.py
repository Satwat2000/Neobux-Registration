import sys
import process
from Uiform import Ui_Dialog
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton

# Font Start
font = QtGui.QFont()
font.setFamily("Algerian")
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
        self.opened = False

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
        self.btn = QPushButton('REGISTER YOURSELF',self)
        self.btn.setFont(font)
        self.btn.move(500,600)
        self.btn.setFixedSize(250,50)
        

class contrl():
    def __init__(self,view):
        self.Do = process.func()
        self.view = view
        self.connectSignal()
    
    def connectSignal(self):
        self.view.btn.clicked.connect(self.doit)
    
    def doit(self):
        if not self.view.opened:
            self.view.opened = True
            print("button clicked")
            path = self.Do.open_url()
            Dialog = QDialog()
            self.ui = Ui_Dialog()
            self.ui.setupUi(Dialog, path)
            Dialog.show()
            Dialog.exec_()
            
        print ("i returned")
       


if __name__ == '__main__':
    app = QApplication([])
    home = HomePage()
    home.show()
    conn = contrl(home)
    sys.exit(app.exec_())
        