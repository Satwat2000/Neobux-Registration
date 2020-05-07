import sys
import Form, Home
from PyQt5.QtWidgets import QApplication





if __name__ == '__main__':
    app = QApplication([])
    home = Home.HomePage()
    home.show()
    conn = Home.contrl(home)
    sys.exit(app.exec_())