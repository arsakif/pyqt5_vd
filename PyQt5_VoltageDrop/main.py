from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

import cable_resistances
import calculate_vd

from widgets_1 import widgets_1
from calculate_vd import calculate_vd


class ToolBar(QToolBar):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.toolbar = QToolBar('VD Toolbar')


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.setMinimumSize(500, 400)
        self.toolbar = ToolBar().toolbar
        self.addToolBar(self.toolbar)

        # --------First Grid--------------------------------------
        self.grid_layout1 = QGridLayout()
        self.grid_layout1.setObjectName('grid_layout1')
        self.grid_layout1.addWidget(widgets_1().voltage_level_groupbox, 0, 0)
        self.grid_layout1.addWidget(widgets_1().phase_groupbox, 0, 1)
        self.grid_layout1.addWidget(widgets_1().conductor_type_groupbox, 0, 2)
        self.grid_layout1.addWidget(widgets_1().vd_allowance_groupbox, 0, 3)

        self.grid_layout1.addWidget(widgets_1().sets_groupbox, 1, 0)
        self.grid_layout1.addWidget(widgets_1().cable_size_groupbox, 1, 1)
        self.grid_layout1.addWidget(widgets_1().current_groupbox, 1, 2)
        self.grid_layout1.addWidget(widgets_1().length_groupbox, 1, 3)

        # --------Second Grid--------------------------------------

        # --------Third Grid--------------------------------------
        self.grid_layout3 = QGridLayout()

        self.grid_layout3.addWidget(widgets_1().vd_result_groupbox, 0, 0, 2, 1)

        # ________Button________
        self.run_button = QPushButton('Run')
        self.run_button.clicked.connect(self.run_button_click)

        # -------------------------------------------
        self.vboxlayout_1 = QVBoxLayout()
        # self.vboxlayout_1.addStretch()
        self.vboxlayout_1.addLayout(self.grid_layout1)
        self.vboxlayout_1.addLayout(self.grid_layout3)
        self.vboxlayout_1.addWidget(self.run_button)

        # --------------------------------------------

        self.widget = QWidget()
        self.widget.setLayout(self.vboxlayout_1)
        self.setCentralWidget(self.widget)

        # CHANGE EVENTS -- COMBOBOX
        self.findChildren(QComboBox)[0].currentTextChanged.connect(self.run_button_click)
        self.findChildren(QComboBox)[1].currentTextChanged.connect(self.run_button_click)
        self.findChildren(QComboBox)[2].currentTextChanged.connect(self.run_button_click)

        # CHANGE EVENTS -- RADIO BUTTON
        self.findChildren(QRadioButton)[0].clicked.connect(self.run_button_click)
        self.findChildren(QRadioButton)[1].clicked.connect(self.run_button_click)
        self.findChildren(QRadioButton)[2].clicked.connect(self.run_button_click)
        self.findChildren(QRadioButton)[3].clicked.connect(self.run_button_click)

        # CHANGE EVENTS -- QLINEEDIT
        self.findChildren(QSpinBox)[0].valueChanged.connect(self.run_button_click)
        self.findChildren(QLineEdit)[1].textEdited.connect(self.run_button_click)
        self.findChildren(QLineEdit)[2].textChanged.connect(self.run_button_click)

    def run_button_click(self):
        voltage_level = self.findChildren(QComboBox)[0].currentText()
        vd_allowance = self.findChildren(QComboBox)[1].currentText()
        conductor_size = self.findChildren(QComboBox)[2].currentText()

        phase_3 = self.findChildren(QRadioButton)[0].isChecked()
        copper = self.findChildren(QRadioButton)[2].isChecked()

        sets = self.findChildren(QLineEdit)[0].text()
        current = self.findChildren(QLineEdit)[1].text()
        length = self.findChildren(QLineEdit)[2].text()
        print(sets)

        vd_percent = self.findChildren(QLabel)[7]
        vd_absolute = self.findChildren(QLabel)[9]

        vd_percent.setText(calculate_vd(voltage_level, phase_3, copper,
                                        vd_allowance, sets, conductor_size,
                                        current, length).vd_percent)

        vd_absolute.setText(calculate_vd(voltage_level, phase_3, copper,
                                         vd_allowance, sets, conductor_size,
                                         current, length).vd_absolute)

        print(self.grid_layout1.itemAtPosition(0, 0).layout())
        print(self.grid_layout1.itemAtPosition(0, 0).widget().findChild(QComboBox, name='voltage_level_value').currentText())
        print(self.findChild(QComboBox, name='voltage_level_value').currentText())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
