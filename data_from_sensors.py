from PyQt5 import  uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QWidget, QTextBrowser

class data_from_sensors(QWidget):
    def __init__(self, params):
        super(data_from_sensors, self).__init__()
        uic.loadUi("data_from_sensors.ui", self)

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(lambda: self.show_params(params))
    def show_params(self, params):
        result = ""
        for i in params:
            pass
