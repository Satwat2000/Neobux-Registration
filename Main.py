import sys
sys.path.insert(1, 'Resource/')
from PyQt5.QtWidgets import QApplication
import Home


if __name__ == '__main__':
    app = QApplication([])
    home = Home.HomePage()
    home.show()
    conn = Home.contrl(home)
    sys.exit(app.exec_())
