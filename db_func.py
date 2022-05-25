from PyQt5 import  uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QWidget, QTextBrowser
import sqlite3

class db_func(QWidget):
    def __init__(self, payload):
        temp_widget = ""
        super(db_func, self).__init__()
        uic.loadUi("db_func.ui", self)
        self.pushButton_6.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(lambda: self.db_clear(payload))
        self.pushButton_4.clicked.connect(self.db_show)
    def db_clear(self, payload):
        payload['devices'] = []
        sqlite_connection = sqlite3.connect('iot.db')
        cursor = sqlite_connection.cursor()
        cursor.execute('delete from sensors')
        cursor.execute('delete from requests')
        cursor.execute('delete from vals')
        sqlite_connection.commit()
        cursor.close()
        sqlite_connection.close()
    def db_show(self):
        self.temp_widget = QTextBrowser()
        str_for_display = ""
        sqlite_connection = sqlite3.connect('iot.db')
        cursor = sqlite_connection.cursor()
        data = cursor.execute('select * from sensors')
        str_for_display += "DB sensors: " + "\n"
        for i in data:
            for j in range(len(i)):
                if j == 0:
                    str_for_display += 'id = '
                else:
                    str_for_display += 'id_owner = '
                str_for_display += str(i[j]) + ' '
            str_for_display += '\n'
        data = cursor.execute('select * from requests')
        str_for_display += "DB requests: " + "\n"
        for i in data:
            for j in range(len(i)):
                if j == 0:
                    str_for_display += 'id = '
                else:
                    str_for_display += 'date = '
                str_for_display += str(i[j]) + ' '
            str_for_display += '\n'
        data = cursor.execute('select * from vals')
        str_for_display += "DB vals: " + "\n"
        for i in data:
            for j in range(len(i)):
                if j == 0:
                    str_for_display += 'id = '
                elif j == 1:
                    str_for_display += 'sensors_id = '
                elif j == 2:
                    str_for_display += 'requests_id = '
                elif j == 3:
                    str_for_display += 'val = '
                else:
                    str_for_display += 'parameter = '
                str_for_display += str(i[j]) + ' '
            str_for_display += '\n'
        self.temp_widget.setText(str_for_display)
        self.temp_widget.setWindowTitle("Значения из используемых баз данных")
        self.temp_widget.setWindowModality(QtCore.Qt.ApplicationModal)
        self.temp_widget.show()
