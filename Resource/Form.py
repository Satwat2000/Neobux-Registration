""" Made without using QtDesigner...
....Now used only as reference...
....Now Uiform, made using QtDesigner is being used instead""" 



import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
from PyQt5.QtWidgets import QFormLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtWidgets import QDialogButtonBox, QCheckBox ,QPushButton

# Font Start
font = QtGui.QFont()
font.setFamily("Algerian")
font.setPointSize(14)
font.setBold(True)
font.setWeight(50)
# Font End

        
class PyForm ( QDialog ):
    def __init__(self, Parent= None):
        super().__init__() 
        # '''Set View Property of MainWindow'''
        self.setWindowTitle("Neobux Registration")
        # '''Create Main Layout'''
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)
        self.createForm()
        self.setCapta()
        self.setButton()
        
    def createForm (self):
        _input = QLineEdit()
        _input.setFixedHeight(30)
        Layout = QFormLayout()
        Layout.setContentsMargins(10,5,10,10)
        Layout.addRow("Name: ", QLineEdit())
        Layout.addRow("Password: ",QLineEdit())
        Layout.addRow("Email: ", QLineEdit())
        Layout.addRow("Birth Year: ", QLineEdit())
        Layout.addRow("Verification Code: ", QLineEdit())
        self.mainLayout.addLayout(Layout)
    
    def setCapta(self):
        # pat = QWidget.palette()
        # pat.setColor()
        capLayout =  QHBoxLayout()
        capta = QLabel()
        path = "img/capta.png"))
        capta.setPixmap(QtGui.QPixmap(path))
        capLayout.addWidget(capta, alignment=QtCore.Qt.AlignHCenter)
        self.mainLayout.addLayout(capLayout)

    def setButton(self):
        # Font Start
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(50)
        # Font End
        btnLayout = QHBoxLayout()
        btnLayout.setContentsMargins(0,20,0,0)
        rbtn = QCheckBox("Confirm Submittion")
        rbtn.setFont(font)
        btn = QPushButton("Submit")
    
        btnLayout.addWidget(rbtn, alignment=QtCore.Qt.AlignLeft)
        btnLayout.addWidget(btn, alignment=QtCore.Qt.AlignRight)
        self.mainLayout.addLayout(btnLayout)
        
class controlPyform():
    def __init__(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    home = PyForm()
    home.show()
    sys.exit(app.exec_())