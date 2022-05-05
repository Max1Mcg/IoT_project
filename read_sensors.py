from PyQt5 import  uic, QtGui, QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QWidget

class read_sensors(QWidget):
    sensors_numbers = []
    def __init__(self):
        super(read_sensors, self).__init__()
        uic.loadUi("read_sensors.ui", self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.show()
        self.pushButton.clicked.connect(self.read_data)
    def read_data(self):
        str = self.lineEdit.text()
        self.sensors_numbers = str.split(" ")
        self.hide()
