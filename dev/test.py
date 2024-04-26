from PyQt5.QtWidgets import QApplication, QListWidget, QVBoxLayout, QWidget


class DragDropListWidget(QListWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.source() == self:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            super().dragEnterEvent(event)

    def dropEvent(self, event):
        if event.source() == self:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            super().dropEvent(event)


app = QApplication([])

# 创建一个 QWidget 作为窗口
window = QWidget()

# 创建 targetList 和 sortList
target_list = DragDropListWidget()
sort_list = DragDropListWidget()

# 向 targetList 添加一些项目
target_items = ["Item 1", "Item 2", "Item 3"]
target_list.addItems(target_items)

# 创建一个垂直布局管理器
layout = QVBoxLayout()

# 将 targetList 和 sortList 添加到布局中
layout.addWidget(target_list)
layout.addWidget(sort_list)

# 设置窗口的布局
window.setLayout(layout)

# 显示窗口
window.show()

app.exec_()
