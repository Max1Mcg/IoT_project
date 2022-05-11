from PyQt5 import  uic, QtGui, QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QDialogButtonBox, QWidget, QCheckBox

class params_settings(QWidget):
    def __init__(self, params):
        super(params_settings, self).__init__()
        uic.loadUi("params_settings.ui", self)

        self.pushButton.clicked.connect(lambda: self.update_params(params))

    def update_params(self, params):
        for i in range(len(self.verticalLayout)):
            params[self.verticalLayout.itemAt(i).widget().text()] = self.verticalLayout.itemAt(i).widget().isChecked()
        self.close()

