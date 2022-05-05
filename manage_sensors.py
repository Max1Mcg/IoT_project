from PyQt5 import  uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QWidget, QTextBrowser
import  sys
import requests
import urllib3
import json
import hashlib
import uuid
import time
from read_sensors import read_sensors

class manage_sensors(QWidget):
    temp_widget = ""
    def __init__(self, devices):
        super(manage_sensors, self).__init__()
        uic.loadUi("manage_sensors.ui", self)
        self.pushButton.clicked.connect(lambda: self.get_number_of_sensor_for_add(devices))
        self.pushButton_2.clicked.connect(lambda: self.get_number_of_sensor_for_delete(devices))
        self.pushButton_4.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(lambda: self.display_sensors(devices))
    def get_number_of_sensor_for_add(self, devices):
        self.temp_widget = read_sensors()
        self.temp_widget.pushButton.clicked.connect(lambda: self.add_sensors(devices))
    def get_number_of_sensor_for_delete(self, devices):
        self.temp_widget = read_sensors()
        self.temp_widget.pushButton.clicked.connect(lambda: self.delete_sensors(devices))
    def add_sensors(self, devices):
        for i in self.temp_widget.sensors_numbers:
            devices.append(int(i))
    def delete_sensors(self, devices):
        for i in self.temp_widget.sensors_numbers:
            devices.remove(int(i))
    def display_sensors(self, devices):
        self.temp_widget = QTextBrowser()
        str_for_display = ""
        for i in devices:
            str_for_display += 'D' + str(i) + ','
        str_for_display = str_for_display[0:-1]
        self.temp_widget.setText(str_for_display)
        self.temp_widget.setWindowTitle("Список отслеживаемых датчиков")
        self.temp_widget.setWindowModality(QtCore.Qt.ApplicationModal)
        self.temp_widget.show()
