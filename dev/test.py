import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QListWidget 示例')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        # 创建 QListWidget 和提示标签
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet("QListWidget::item { height: 30px; }")
        self.list_widget.setFixedWidth(200)
        self.list_widget.setFixedHeight(100)

        self.label = QLabel('没有项目')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.list_widget)
        layout.addWidget(self.label)

        self.setLayout(layout)

        # 检测列表是否为空，显示或隐藏提示信息
        self.list_widget.itemChanged.connect(self.checkEmptyList)

    def checkEmptyList(self):
        if self.list_widget.count() == 0:
            self.label.setVisible(True)
        else:
            self.label.setVisible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = MyWidget()
    my_widget.show()
    sys.exit(app.exec_())
