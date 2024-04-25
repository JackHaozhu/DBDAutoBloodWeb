from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from main.gui.DAB import Ui_MainWindow  # 导入通过pyuic5转换生成的UI文件中的类

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.home.clicked.connect(self.homePage)
        self.statistics.clicked.connect(self.statisticsPage)
        self.radioButton.clicked.connect(self.settingsPage)
        # 鼠标按下事件处理函数
        self.mousePressPos = None
        self.mouseMovePos = None


    def homePage(self):
        self.contentStackedWidget.setCurrentIndex(0)

    def statisticsPage(self):
        self.contentStackedWidget.setCurrentIndex(1)

    def settingsPage(self):
        self.contentStackedWidget.setCurrentIndex(2)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # mousePressPos -> 鼠标全局位置
            # mouseMovePos -> 鼠标窗口相对位置
            self.mousePressPos = event.globalPos()
            self.mouseMovePos = event.globalPos() - self.pos()
            # print(self.mousePressPos, self.mouseMovePos)
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mouseMovePos.y() <= 50 and self.mouseMovePos.x() <= 1400:
            globalPos = event.globalPos()
            moved = globalPos - self.mouseMovePos
            self.move(moved)
        super().mouseMoveEvent(event)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
