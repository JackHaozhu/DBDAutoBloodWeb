import dirInfo
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QRadioButton
from PyQt5.QtGui import QPixmap
from DAB import Ui_MainWindow  # 导入通过pyuic5转换生成的UI文件中的类

if dirInfo.get_program_install_location('黎明杀机') is not None:
    game_dir = dirInfo.get_program_install_location('黎明杀机')
ui_dir = game_dir + r'\DeadByDaylight\Content\UI\Icons'
char_dir = ui_dir + '\\CharPortraits\\'


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 链接槽与信号
        # 左侧主页、统计、设置按钮
        self.home.clicked.connect(self.homePage)
        self.statistics.clicked.connect(self.statisticsPage)
        self.radioButton.clicked.connect(self.settingsPage)
        # 初始化页面至 主页-杀手
        self.contentStackedWidget.setCurrentIndex(0)
        self.chooseType.setCurrentIndex(0)

        # 加载杀手图片
        self.loadKillerImgs(dirInfo.killer_key)
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

    def loadKillerImgs(self, killers):
        for name in killers:
            target_img_dir = char_dir + dirInfo.character[name]
            target_img_dir = target_img_dir.replace('\\', '/')
            print(name, target_img_dir)
            button = self.findChild(QRadioButton, name)
            if button:
                print('Button Found!')
                button.setStyleSheet(f'QRadioButton {{ border-image: url({target_img_dir}); }}')

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mouseMovePos.y() <= 50 and self.mouseMovePos.x() <= 1440:
            globalPos = event.globalPos()
            moved = globalPos - self.mouseMovePos
            self.move(moved)
        super().mouseMoveEvent(event)


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
