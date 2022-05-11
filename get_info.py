from PyQt5 import  uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QWidget, QTextBrowser, QErrorMessage
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
        self.pushButton_2.clicked.connect(self.hide)
    def show_info_from_sensors(self, payload, params, urll):
        result = ""
        payload_temp = {}#возможность есть возможность за один запрос получить сразу все требуемые датчики!
        payload_temp['cmd'] = payload['cmd']
        payload_temp['uuid'] = payload['uuid']
        payload_temp['api_key'] = payload['api_key']
        payload_temp['lang'] = payload['lang']
        try:
            for i in range(len(payload['devices'])):
                payload_temp['devices'] = payload['devices'][i]
                response = requests.post(url=urll, json=payload_temp)
                print(response)
                temp = response.json()
                for j in params.keys():
                    if params[j]:
                        result += j + " = " + str(temp['devices'][0][j]) + "\n"
                result += "\n"
            self.textBrowser.setText(result)
        except Exception:
            self.em = QErrorMessage(self)
            self.em.setWindowModality(QtCore.Qt.ApplicationModal)
            self.em.setWindowTitle('Ошибка')
            self.em.showMessage('Ошибка при попытке получить данные. Проверьте правильность введённых данных и наличие подключения к интернету.')
            self.em.show()
