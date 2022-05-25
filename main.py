from PyQt5 import  uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox
import  sys
import requests
import urllib3
import json
import hashlib
import uuid
import time
from MWindow import MWindow
import sqlite3

#global variables
urll = 'http://narodmon.ru/api'
app_id = str(uuid.getnode())
md5_app_id = hashlib.md5(app_id.encode()).hexdigest()
payload = {
        'cmd': 'sensorsOnDevice',
        'devices': [],
        'uuid': md5_app_id,
        'api_key': 'TTyEvZaZ92G7b',
        'lang': 'ru'
}

#on/off params
params_new = {'id':True, 'name':True, 'my':True, 'owner':True, 'mac':True, 'cmd':True,
'location':True, 'distance':True, 'time':True, 'liked':True, 'uptime':True,'site':True, 'photo':True, 'info':True, 'sensors':True}

"""Creating database module"""
try:
    #  Connecting to the database
    sqlite_connection = sqlite3.connect('iot.db')
    cursor = sqlite_connection.cursor()

    sqlite_create_table_requests = '''CREATE TABLE requests (
                                        id INT NOT NULL PRIMARY KEY,
                                        date TIMESTAMP NOT NULL);'''

    sqlite_create_table_values = '''CREATE TABLE vals (
                                        id INT NOT NULL PRIMARY KEY,
                                        sensors_id INT NOT NULL,
                                        requests_id INT NOT NULL,
                                        val VARCHAR(150) NOT NULL,
                                        parameter VARCHAR(150) NOT NULL,
                                        FOREIGN KEY (requests_id) REFERENCES requests (id),
                                        FOREIGN KEY (sensors_id) REFERENCES sensors (id));'''

    sqlite_create_table_sensors = '''CREATE TABLE sensors (
                                        id INT NOT NULL PRIMARY KEY,
                                        id_owner INT NOT NULL);'''

    cursor.execute(sqlite_create_table_requests)
    cursor.execute(sqlite_create_table_values)
    cursor.execute(sqlite_create_table_sensors)
    sqlite_connection.commit()
    cursor.close()

except sqlite3.Error as error:
    pass

finally:
    if sqlite_connection:
        sqlite_connection.close()

#инициализация списка значениями из БД
sqlite_connection = sqlite3.connect('iot.db')
cursor = sqlite_connection.cursor()
cursor.execute('select * from sensors')
res = cursor.fetchall()
for i in res:
    payload['devices'].append(i[0])
cursor.close()
sqlite_connection.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = MWindow(payload, params_new, urll)
    app.exec_()

