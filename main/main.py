from gui import run_DAB
import sys


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = run_DAB.MainWindow()
    window.show()
    sys.exit(app.exec_())
