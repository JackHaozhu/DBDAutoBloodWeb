import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hidden Title Bar')
        self.setGeometry(100, 100, 300, 200)

        # 设置窗口属性，隐藏标题栏但保留边框
        self.setWindowFlags(Qt.FramelessWindowHint)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
