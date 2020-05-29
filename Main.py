import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'Resource/')
import Home
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication([])
    home = Home.HomePage()
    home.show()
    conn = Home.contrl(home)
    sys.exit(app.exec_())