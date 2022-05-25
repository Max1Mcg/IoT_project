from PyQt5 import  uic, QtGui, QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QLabel, QErrorMessage
import  sys
import requests
import urllib3
import json
import hashlib
import uuid
import time
from manage_sensors import manage_sensors
from get_info import get_info
from params_settings import params_settings
from ExitMessage import ExitMessage
from db_func import db_func
import sqlite3

class MWindow(QMainWindow):
    def __init__(self, payload, params, urll):
        super(MWindow, self).__init__()
        uic.loadUi("MWindow.ui", self)
        m_sensors = uic.loadUi("MWindow.ui")
        m_sensors.setGeometry(100, 100, 600, 600)
        self.wind = manage_sensors(payload)
        self.wind.parent = self
        self.ge = get_info(payload, params, urll)
        self.prm = params_settings(params)
        self.exitm = ExitMessage('Вы точно хотите выйти?')
        self.db_window = db_func(payload)
        self.pushButton_2.clicked.connect(self.slot_function)
        self.pushButton.clicked.connect(self.check_close)
        self.pushButton_4.clicked.connect(self.show_info_from_sensors)
        self.pushButton_3.clicked.connect(self.tune_data_from_sensors)
        self.pushButton_6.clicked.connect(self.out_and_find_in_db)
        self.show()
    def slot_function(self):
        self.wind.setWindowModality(QtCore.Qt.ApplicationModal)
        self.wind.show()
    def show_info_from_sensors(self):
        self.ge.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ge.show()
    def tune_data_from_sensors(self):
        self.prm.setWindowModality(QtCore.Qt.ApplicationModal)
        self.prm.show()
    def check_close(self):
        self.exitm.setWindowModality(QtCore.Qt.ApplicationModal)
        self.exitm.button.accepted.connect(self.close_app)
        self.exitm.show()
    def close_app(self):
        self.exitm.close()
        self.close()
    def out_and_find_in_db(self):
        self.db_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.db_window.show()
