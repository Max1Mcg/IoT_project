# This Python file uses the following encoding: utf-8
from PyQt5 import  uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QWidget, QTextBrowser

class ExitMessage(QWidget):
    def __init__(self, text):
        super(ExitMessage, self).__init__()
        uic.loadUi("ExitMessage.ui", self)
        self.label.setText(text)
        self.button.rejected.connect(self.close_message)
        self.setWindowTitle(' ')
    def close_message(self):
        self.close()
