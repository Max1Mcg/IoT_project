from PyQt5 import  uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QWidget, QTextBrowser
import sys
import requests
import urllib3
import json
import hashlib
import uuid
import time

class get_info(QWidget):
    def __init__(self, payload, params, urll):
        super(get_info, self).__init__()
        uic.loadUi("get_info.ui", self)
        self.pushButton.clicked.connect(lambda: self.show_info_from_sensors(payload, params, urll))
    def show_info_from_sensors(self, payload, params, urll):
        result = ""
        response = requests.post(url=urll, json=payload)
        temp = response.json()
        print(len(temp['devices']))
        for i in params:
            result += str(i) + " = " + str(temp['devices'][0][i]) + "\n"
        self.textBrowser.setText(result)
