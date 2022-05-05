from PyQt5 import  uic, QtGui, QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox
import  sys
import requests
import urllib3
import json
import hashlib
import uuid
import time
from manage_sensors import manage_sensors
from get_info import get_info
from data_from_sensors import data_from_sensors

class MWindow(QMainWindow):
    def __init__(self, payload, params, urll):
        super(MWindow, self).__init__()
        uic.loadUi("MWindow.ui", self)
        #oImage = QtGui.QImage("back.jpg")
        #oImage = oImage.scaled(QtCore.QSize(440, 280))
        #palette = QtGui.QPalette()
        #palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(oImage))
        m_sensors = uic.loadUi("MWindow.ui")
        m_sensors.setGeometry(100,100,600,600)
        self.wind = manage_sensors(payload['devices'])
        self.wind.parent = self
        self.ge = get_info(payload, params, urll)
        self.dfs = data_from_sensors(params)
        #self.setPalette(palette)
        self.pushButton_2.clicked.connect(self.slot_function)
        self.pushButton.clicked.connect(self.close)
        self.pushButton_4.clicked.connect(self.show_info_from_sensors)
        self.pushButton_3.clicked.connect(self.tune_data_from_sensors)
        self.show()
    def slot_function(self):
        self.wind.setWindowModality(QtCore.Qt.ApplicationModal)
        self.wind.show()
    def show_info_from_sensors(self):
        self.ge.show()
    def tune_data_from_sensors(self):
        self.dfs.setWindowModality(QtCore.Qt.ApplicationModal)
        self.dfs.show()
