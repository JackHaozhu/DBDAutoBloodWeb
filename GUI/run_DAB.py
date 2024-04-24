import sys

from PyQt5 import QtWidgets

import DAB
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DAB.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
