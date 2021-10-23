from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cable_resistances


class widgets_1(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # VOLTAGE LEVEL
        voltage_level_lable = QLabel('Voltage (V)')
        self.voltage_level_value = QComboBox()
        self.voltage_level_value.setObjectName('voltage_level_value')
        self.voltage_level_value.addItems(['120', '208', '277', '480', 'Custom'])
        voltage_level_vbox = QVBoxLayout()
        voltage_level_vbox.addWidget(voltage_level_lable)
        voltage_level_vbox.addWidget(self.voltage_level_value)
        self.voltage_level_groupbox = QGroupBox()
        self.voltage_level_groupbox.setLayout(voltage_level_vbox)

        # PHASE CHOISE
        self.phase_3_radio_btn = QRadioButton('3-Phase')
        self.phase_3_radio_btn.setChecked(True)
        self.phase_1_radio_btn = QRadioButton('1-Phase')
        phase_vbox = QVBoxLayout()
        phase_vbox.addWidget(self.phase_3_radio_btn)
        phase_vbox.addWidget(self.phase_1_radio_btn)
        self.phase_groupbox = QGroupBox()
        self.phase_groupbox.setLayout(phase_vbox)

        # Conductor Type CHOISE
        self.cu_btn = QRadioButton('Copper')
        self.cu_btn.setChecked(True)
        self.al_btn = QRadioButton('Aluminum')
        conductor_type_vbox = QVBoxLayout()
        conductor_type_vbox.addWidget(self.cu_btn)
        conductor_type_vbox.addWidget(self.al_btn)
        self.conductor_type_groupbox = QGroupBox()
        self.conductor_type_groupbox.setLayout(conductor_type_vbox)

        # VOLTAGE DROP ALLOVANCE
        vd_allowance_lable = QLabel('VD Allowance (%)')
        self.vd_allowance_value = QComboBox()
        self.vd_allowance_value.addItems(['3%', '5%', 'Custom'])
        vd_allowance_vbox = QVBoxLayout()
        vd_allowance_vbox.addWidget(vd_allowance_lable)
        vd_allowance_vbox.addWidget(self.vd_allowance_value)
        self.vd_allowance_groupbox = QGroupBox()
        self.vd_allowance_groupbox.setLayout(vd_allowance_vbox)

        # PARALLEL SETS
        sets_lable = QLabel('Sets')
        self.sets_value = QSpinBox()
        self.sets_value.setMinimum(1)
        sets_vbox = QVBoxLayout()
        sets_vbox.addWidget(sets_lable)
        sets_vbox.addWidget(self.sets_value)
        self.sets_groupbox = QGroupBox()
        self.sets_groupbox.setLayout(sets_vbox)

        # CABLE SIZE
        cable_size_lable = QLabel('Cunductor Size')
        self.cable_size_value = QComboBox()
        self.cable_size_value.addItems(cable_resistances.cable_sizes)
        cable_size_vbox = QVBoxLayout()
        cable_size_vbox.addWidget(cable_size_lable)
        cable_size_vbox.addWidget(self.cable_size_value)
        self.cable_size_groupbox = QGroupBox()
        self.cable_size_groupbox.setLayout(cable_size_vbox)

        # CURRENT VALUE
        current_lable = QLabel('Current(A)')
        self.current_value = QLineEdit('0')
        current_vbox = QVBoxLayout()
        current_vbox.addWidget(current_lable)
        current_vbox.addWidget(self.current_value)
        self.current_groupbox = QGroupBox()
        self.current_groupbox.setLayout(current_vbox)

        # LENGTH OF THE RUN
        length_lable = QLabel('Length(Ft)')
        self.length_value = QLineEdit('0')
        length_vbox = QVBoxLayout()
        length_vbox.addWidget(length_lable)
        length_vbox.addWidget(self.length_value)
        self.length_groupbox = QGroupBox()
        self.length_groupbox.setLayout(length_vbox)

        # VOLTAGE DROP RESULT
        vd_percent_lable = QLabel('VD(%):')
        self.vd_percent_value = QLabel('0')
        vd_percent_hbox = QHBoxLayout()
        vd_percent_hbox.addWidget(vd_percent_lable)
        vd_percent_hbox.addWidget(self.vd_percent_value)
        vd_percent_groupbox = QGroupBox()
        vd_percent_groupbox.setLayout(vd_percent_hbox)

        vd_absolute_lable = QLabel('VD(V):')
        self.vd_absolute_value = QLabel('0')
        vd_absolute_hbox = QHBoxLayout()
        vd_absolute_hbox.addWidget(vd_absolute_lable)
        vd_absolute_hbox.addWidget(self.vd_absolute_value)
        vd_absolute_groupbox = QGroupBox()
        vd_absolute_groupbox.setLayout(vd_absolute_hbox)

        vd_result_vbox = QVBoxLayout()
        vd_result_vbox.addWidget(vd_percent_groupbox)
        vd_result_vbox.addWidget(vd_absolute_groupbox)
        self.vd_result_groupbox = QGroupBox()
        self.vd_result_groupbox.setLayout(vd_result_vbox)
