import os
import json

from PyQt5 import QtCore

from . import dirInfo

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QRadioButton, QListView, QFileDialog, QListWidgetItem, QListWidget
from PyQt5.QtGui import QIcon
from .DAB import Ui_MainWindow  # 导入通过pyuic5转换生成的UI文件中的类
from PyQt5.QtCore import pyqtSignal

if dirInfo.get_program_install_location('黎明杀机') is not None:
    auto_game_dir = dirInfo.get_program_install_location('黎明杀机')
auto_ui_dir = auto_game_dir + r'\DeadByDaylight\Content\UI\Icons'
auto_char_dir = auto_ui_dir + '\\CharPortraits\\'
auto_offering_dir = auto_ui_dir + '\\Favors\\'
QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(r'.\icon_resources\escapeCake.png'))
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 初始化config.json
        self.initializeConfig()

        self.setupUi(self)
        # 链接槽与信号
        # 左侧主页、统计、设置按钮
        self.home.clicked.connect(self.homePage)
        self.statistics.clicked.connect(self.statisticsPage)
        self.radioButton.clicked.connect(self.settingsPage)
        # 统计页面彩蛋
        self.developingButton.clicked.connect(self.devButtonEasterEgg)

        # 切换杀手
        for killerRadioButton in self.killerList.findChildren(QRadioButton):
            killerRadioButton.toggled.connect(self.killerToggled)
        # 拖动杀手Item事件
        self.killerChooseList.itemDropped.connect(self.killerItemMoved)
        self.killerTargetList.itemDropped.connect(self.killerTargetMoved)
        # 初始化页面至 主页-杀手
        self.contentStackedWidget.setCurrentIndex(0)
        self.chooseType.setCurrentIndex(0)
        # 加载杀手图片
        self.loadKillerImgs(dirInfo.killer_key)
        # 初始化QComboBox样式
        self.gameDirComboBox.setView(QListView())
        self.killerTargetType.setView(QListView())
        # 初始化下拉菜单中自动选择目录
        self.initChooseDir()
        # 检测下拉菜单切换项目事件
        self.gameDirComboBox.activated.connect(self.chooseGameDir)
        # 鼠标按下事件处理函数
        self.mousePressPos = None
        self.mouseMovePos = None

    # 初始化config.json
    def initializeConfig(self):
        if os.path.exists('config.json'):
            pass
        else:
            write_config = {
                'game_dir': {
                    'index': 0,
                    'dir': ''
                },
                'killer_config': {
                },
                'human_config': {
                }
            }
            with open('config.json', 'w') as write:
                json.dump(write_config, write, indent=4)

    # 切换至主页
    def homePage(self):
        self.contentStackedWidget.setCurrentIndex(0)

    # 切换至统计页，初始化彩蛋
    def statisticsPage(self):
        self.contentStackedWidget.setCurrentIndex(1)
        self.developingButton.setText('这里什么也没有')

    # 切换至设置页
    def settingsPage(self):
        self.contentStackedWidget.setCurrentIndex(2)
        self.initChooseDir()

    # 彩蛋
    def devButtonEasterEgg(self):
        current_text = self.developingButton.text()
        new_text = dirInfo.easter_egg[current_text]
        self.developingButton.setText(new_text)

    # 加载杀手图标
    def loadKillerImgs(self, killers):
        data = json.load(open('config.json', 'r'))
        if data['game_dir']['index'] == 0:
            char_dir = auto_game_dir
        else:
            char_dir = data['game_dir']['dir']
        char_dir = char_dir + r'\DeadByDaylight\Content\UI\Icons\CharPortraits\\'
        for name in killers:
            target_img_dir = char_dir + dirInfo.character_path[name]
            target_img_dir = target_img_dir.replace('\\', '/')
            button = self.findChild(QRadioButton, name)
            if button:
                button.setStyleSheet(f'QRadioButton {{ border-image: url({target_img_dir}); }}')

    # 加载杀手祭品与配件，读config
    def loadKillerItems(self, killer_name):
        data = json.load(open('config.json', 'r'))
        if data['game_dir']['index'] == 0:
            offering_path = auto_offering_dir
        else:
            offering_path = data['game_dir']['dir']
        common_offering_list = list(dirInfo.offerings['killers'].keys())
        self.killerChooseList.clear()
        self.killerTargetList.clear()
        for offering_name in common_offering_list:
            # print(killer_name)
            # print(offering_name)
            item = QListWidgetItem(offering_name)
            if killer_name in data['killer_config'] and offering_name not in data['killer_config'][killer_name]:
                self.killerChooseList.addItem(item)
            file_name = 'iconFavors_' + offering_name + '.png'
            icon_path = offering_path + file_name
            item.setIcon(QIcon(icon_path))  # todo 叠加稀有度背景
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(dirInfo.offerings['killers'][offering_name]['name'][0])
        for chosen_offering in data['killer_config'][killer_name]:
            item = QListWidgetItem(chosen_offering)
            self.killerTargetList.addItem(item)
            file_name = 'iconFavors_' + chosen_offering + '.png'
            icon_path = offering_path + file_name
            item.setIcon(QIcon(icon_path))
            item.setTextAlignment(Qt.AlignCenter)
            item.setText(dirInfo.offerings['killers'][chosen_offering]['name'][0])

    # 杀手物品列表拖动事件，刷新列表，写入config
    def killerItemMoved(self, item, source):
        item2bDeleted = self.killerChooseList.findItems(item.text(), Qt.MatchExactly)[0]
        new_item = self.killerChooseList.takeItem(self.killerChooseList.row(item2bDeleted))
        print('Signal Connected!')  # debug
        print('Source Item:', item.text())  # debug
        print('Source List:', source.objectName())  # debug
        current_items_list = []
        for i in range(self.killerChooseList.count()):
            item_name = self.killerChooseList.item(i).text()
            current_items_list.append(item_name)
        print('Current Item List', current_items_list)  # debug
        killers_offerings_list = list(dirInfo.offerings['killers'].keys())
        position = 0
        for index, key in enumerate(killers_offerings_list):
            if index < len(current_items_list):
                if current_items_list[index] != dirInfo.offerings['killers'][key]['name'][0]:
                    current_items_list.insert(index, 'temp')
            else:
                current_items_list.append('temp')
            if item.text() == dirInfo.offerings['killers'][key]['name'][0]:
                position = index
        temp_list = current_items_list
        temp_list[position] = item.text()
        print('Temp List:', temp_list)  # debug
        current_items_list = [item for item in current_items_list if item != 'temp']
        print('Processed Current Item List:', current_items_list)  # debug
        insert_index = current_items_list.index(item.text())
        self.killerChooseList.insertItem(insert_index, new_item)

        # data = json.load(open('config.json', 'r'))
        # current_item_list = []
        # print('count', self.killerTargetList.count())
        # killers_offerings_list = list(dirInfo.offerings['killers'].keys())
        # for i in range(self.killerTargetList.count()):
        #     item_name = self.killerTargetList.item(i).text()
        #     print(item_name)
        #     for index, key in enumerate(killers_offerings_list):
        #         if item_name == dirInfo.offerings['killers'][key]['name'][0]:
        #             item_name = key
        #             break
        #     current_item_list.append(item_name)
        # print(current_item_list)
        # current_killer = self.getCurrentKiller()
        # data['killer_config'][current_killer] = current_item_list
        # print(data['killer_config'][current_killer])
        # json.dump(data, open('config.json', 'w'), indent=4)

    def killerTargetMoved(self, item, source):
        data = json.load(open('config.json', 'r'))
        current_item_list = []
        print('count', self.killerTargetList.count())
        killers_offerings_list = list(dirInfo.offerings['killers'].keys())
        for i in range(self.killerTargetList.count()):
            item_name = self.killerTargetList.item(i).text()
            print(item_name)
            for index, key in enumerate(killers_offerings_list):
                if item_name == dirInfo.offerings['killers'][key]['name'][0]:
                    item_name = key
                    break
            current_item_list.append(item_name)
        print('unprocessed list:', current_item_list)
        # temp_list = current_item_list
        # current_item_list = []
        # for item in temp_list:
        #     if item not in current_item_list:
        #         current_item_list.append(item)
        print('processed list:', current_item_list)
        current_killer = self.getCurrentKiller()
        data['killer_config'][current_killer] = current_item_list
        json.dump(data, open('config.json', 'w'), indent=4)

    def getCurrentKiller(self):
        for button in self.killerList.findChildren(QRadioButton):
            if button.isChecked():
                current_killer = button.objectName()
                print('current_killer', current_killer)
                break
        return current_killer

    # 切换杀手，加载其配件与祭品，读取config
    def killerToggled(self, checked):
        toggledButton = self.sender()
        if checked:
            print(f'{toggledButton.objectName()} is checked!')
            self.loadKillerItems(toggledButton.objectName())
        else:
            print(f'{toggledButton.objectName()} is unchecked!')
    # 初始化选择目录下拉菜单
    def initChooseDir(self):
        data = json.load(open('config.json', 'r'))
        self.gameDirComboBox.setItemText(0, '自动选择目录：' + auto_game_dir)
        if data['game_dir']['dir'] != '' and self.gameDirComboBox.count() == 2:
            self.gameDirComboBox.insertItem(1, data['game_dir']['dir'])
        self.gameDirComboBox.setCurrentIndex(data['game_dir']['index'])
        self.checkGameDir()

    # 选择游戏目录
    def chooseGameDir(self):
        # 读取config.json
        data = json.load(open('config.json', 'r'))
        if self.gameDirComboBox.currentIndex() == 0:
            # 传递参数至config.json
            data['game_dir']['index'] = 0
        elif self.gameDirComboBox.currentIndex() == (self.gameDirComboBox.count() - 1):
            # todo 传递参数至config.json
            options = QFileDialog.Options()
            path = QFileDialog.getExistingDirectory(self, options=options)
            if path:
                path = path.replace('/', '\\')
                data['game_dir']['dir'] = path
                data['game_dir']['index'] = 1
                if self.gameDirComboBox.count() == 2:
                    self.gameDirComboBox.insertItem(1, path)
                else:
                    self.gameDirComboBox.setItemText(1, path)
                self.gameDirComboBox.setCurrentIndex(1)
                self.checkGameDir()
        elif self.gameDirComboBox.currentIndex() == 1 and self.gameDirComboBox.count() == 3:
            data['game_dir']['index'] = 1
        json.dump(data, open('config.json', 'w'), indent=4)
        self.loadKillerImgs(dirInfo.killer_key)

    # 游戏目录检查
    def checkGameDir(self):
        if self.gameDirComboBox.currentIndex() == 0:
            path = auto_game_dir
        else:
            path = self.gameDirComboBox.currentText()
        if os.path.exists(path + r'\DeadByDaylight'):
            self.dirErrorHint.setText('')
        else:
            self.dirErrorHint.setText('当前路径无效，请重新选择。\n正确路径应以\"\\common\\Dead by Daylight\"结束')

    # 点击鼠标
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # mousePressPos -> 鼠标全局位置
            # mouseMovePos -> 鼠标窗口相对位置
            self.mousePressPos = event.globalPos()
            self.mouseMovePos = event.globalPos() - self.pos()
        super().mousePressEvent(event)

    # 拖动鼠标
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.mouseMovePos.y() <= 50 and self.mouseMovePos.x() <= 1440:
            globalPos = event.globalPos()
            moved = globalPos - self.mouseMovePos
            self.move(moved)
        super().mouseMoveEvent(event)

# if __name__ == "__main__":
#     from PyQt5.QtWidgets import QApplication
#
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
