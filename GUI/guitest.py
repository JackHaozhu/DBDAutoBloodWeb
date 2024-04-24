# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './GUI/gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.typeChoose = QtWidgets.QTabWidget(self.centralwidget)
        self.typeChoose.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.typeChoose.setStyleSheet("/* 设置QTabWidget的整体背景透明 */\n"
"QTabWidget {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* 设置Tab页面的样式 */\n"
"QTabWidget::QWidget {\n"
"    background: transparent; /* 设置Tab页面的背景为透明 */\n"
"    border: none;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border-top: 1px solid #CCCCCC; /* 添加一条1像素宽的灰色上边框（示例色值） */\n"
"}\n"
"\n"
"\n"
"/* 设置Tab项的样式 */\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    border: none;\n"
"    font-size: 30px;\n"
"    margin-right: 0px;\n"
"    width: 160px;\n"
"    height: 50px;\n"
"}\n"
"\n"
"/* 鼠标悬停时的样式 */\n"
"QTabBar::tab:hover {\n"
"    background: lightgray; /* 设置鼠标悬停时的背景色 */\n"
"}\n"
"\n"
"/* 选中Tab项的样式 */\n"
"QTabBar::tab:selected {\n"
"    margin-top: 0px; /* 设置选中Tab项不放大 */\n"
"    background-color: rgb(165, 165, 165);\n"
"    border-bottom: 1px solid #CCCCCC;\n"
"}\n"
"")
        self.typeChoose.setObjectName("typeChoose")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.killerCharacter = QtWidgets.QTabWidget(self.tab)
        self.killerCharacter.setGeometry(QtCore.QRect(50, 70, 551, 351))
        self.killerCharacter.setTabPosition(QtWidgets.QTabWidget.West)
        self.killerCharacter.setObjectName("killerCharacter")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.killerCharacter.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.killerCharacter.addTab(self.tab_4, "")
        self.typeChoose.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.typeChoose.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.typeChoose.setCurrentIndex(0)
        self.killerCharacter.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.killerCharacter.setTabText(self.killerCharacter.indexOf(self.tab_3), _translate("MainWindow", "test1"))
        self.typeChoose.setTabText(self.typeChoose.indexOf(self.tab), _translate("MainWindow", "杀手"))
        self.typeChoose.setTabText(self.typeChoose.indexOf(self.tab_2), _translate("MainWindow", "逃生者"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())