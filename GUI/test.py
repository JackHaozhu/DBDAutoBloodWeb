import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QPropertyAnimation, QRect

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        self.button = QPushButton("Click Me", self)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.startAnimation)

    def startAnimation(self):
        # 创建动画对象，将按钮从当前位置平移100像素
        self.animation = QPropertyAnimation(self.button, b"geometry")
        self.animation.setDuration(1000)  # 动画持续时间为1秒
        self.animation.setStartValue(QRect(self.button.x(), self.button.y(), self.button.width(), self.button.height()))
        self.animation.setEndValue(QRect(self.button.x() + 100, self.button.y(), self.button.width(), self.button.height()))
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
