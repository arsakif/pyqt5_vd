from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Custom Dialog')
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.windowTitleChanged.connect(lambda x: self.a_custom_func())
        self.setWindowTitle("My Awesome App")

        label = QLabel('This is Awesome')
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('My Main Toolbar')
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('icons/bug.png'), 'Your button', self)
        button_action.setStatusTip('This is your button')
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        button_action.setShortcut(QKeySequence('Ctrl+p'))
        toolbar.addAction(button_action)
        toolbar.setIconSize(QSize(16, 16))

        toolbar.addSeparator()

        button_action2 = QAction(QIcon('icons/bug.png'), 'Your button', self)
        button_action2.setStatusTip('This is your Second button')
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        button_action2.setShortcut(QKeySequence('Ctrl+v'))
        toolbar.addAction(button_action2)
        toolbar.setIconSize(QSize(16, 16))

        toolbar.addWidget(QLabel('Hello'))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()
        menu.setNativeMenuBar(False)

        file_menu = menu.addMenu('&File')
        file_menu.addAction(button_action)

        file_menu.addSeparator()
        file_submenu = file_menu.addMenu('Submenu')
        file_submenu.addAction(button_action2)
    def onWindowTitleChange(self, s):
        print(s)

    def a_custom_func(self, a='Hello', b=5, c='hella'):
        print(a, b, c)

    def onMyToolBarButtonClick(self, my_signal):
        print('click', not my_signal)

        dlg = CustomDialog()
        if dlg.exec_():
            print('Success!')


app = QApplication(sys.argv)

window = MainWindow()
window.show()  # TODO IMPORTANT !!!
app.exec_()
