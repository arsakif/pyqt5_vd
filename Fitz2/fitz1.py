from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Awesome App")

        layout = QStackedLayout()
        widget_magenta = Color('magenta')
        widget_blue = Color('blue')
        widget_red = Color('red')
        widget_white = Color('white')
        widget_yellow = Color('yellow')

        layout.addWidget(widget_yellow)
        layout.addWidget(widget_blue)
        layout.addWidget(widget_red)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()  # TODO IMPORTANT !!!
app.exec_()
