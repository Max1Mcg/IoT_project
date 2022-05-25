from PyQt5 import  uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QWidget, QTextBrowser, QErrorMessage
import sys
import requests
import urllib3
import json
import hashlib
import uuid
import time
import datetime
import sqlite3

class get_info(QWidget):
    id = 0
    values = 1
    def __init__(self, payload, params, urll):
        super(get_info, self).__init__()
        uic.loadUi("get_info.ui", self)
        self.pushButton.clicked.connect(lambda: self.show_info_from_sensors(payload, params, urll))
        self.pushButton_2.clicked.connect(self.hide)
    def show_info_from_sensors(self, payload, params, urll):
        self.id += 1
        current_time = datetime.datetime.now()

        '''table requests'''
        sqlite_connection = sqlite3.connect('iot.db')
        cursor = sqlite_connection.cursor()
        cursor.execute('INSERT INTO requests(id, date) VALUES(?, ?)', (self.id, current_time))
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
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
                temp = response.json()
                for j in params.keys():
                    if params[j]:
                        result += j + " = " + str(temp['devices'][0][j]) + "\n"

                '''sql vals'''
                sqlite_connection = sqlite3.connect('iot.db')
                cursor = sqlite_connection.cursor()
                for j in temp['devices'][0]['sensors']:
                    cursor.execute('INSERT INTO vals(id, sensors_id, requests_id, val, parameter) VALUES(?, ?, ?, ?, ?)', (self.values, payload['devices'][i], self.id, str(j['value']), str(j['name'])))
                    self.values += 1
                sqlite_connection.commit()
                cursor.close()
                sqlite_connection.close()
                result += "\n"
            self.textBrowser.setText(result)
        except Exception:
            self.em = QErrorMessage(self)
            self.em.setWindowModality(QtCore.Qt.ApplicationModal)
            self.em.setWindowTitle('Ошибка')
            self.em.showMessage('Ошибка при попытке получить данные. Проверьте правильность введённых данных и наличие подключения к интернету.')
            self.em.show()
