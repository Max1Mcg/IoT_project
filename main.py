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

params = ['id', 'name', 'my', 'owner', 'mac', 'cmd', 'location', 'distance', 'time', 'liked', 'uptime',
'site', 'photo', 'info', 'sensors']

#on/off params
params_new = {'id':1, 'name':1, 'my':1, 'owner':1, 'mac':1, 'cmd':1, 'location':1, 'distance':1, 'time':1, 'liked':1, 'uptime':1,
'site':1, 'photo':1, 'info':1, 'sensors':1}

#menu
def menu():
    """
    some test text for docs
    """
    work = True
    while(work):
        print('выберите действие')
        print('0 - завершение работы')
        print('1 - настройка получаемой информации с датчиков')
        print('2 - управление датчиками')
        print('3 - получение информации с датчиков')
        move = input()
        if(move == '0'):
            print('Спасибо за использование!!!')
            work = False
        elif(move == '1'):
            getting_info()
        elif(move == '2'):
            sensors()
        elif(move == '3'):
            get_values()
        else:
            print("Действие введено неверно, попробуйте ещё раз")

def getting_info():
    print("0 - вернуться назад")
    print("1 - вывод всех параметров")
    print("2 - удаление параметров настроек вывода с датчиков")
    print("3 - добавление параметров настроек вывода с датчиков")
    move = -1
    move = input()
    if move == 0:
        return
    elif move == 1:
        print("Введите через пробел номера параметров, которые вы хотите видеть при выводе информации")
    elif move == 2:
        print()#
    elif move == 3:
        print()#
    else:
        print("Действие введено неверно, попробуйте ещё раз")

#add/remove sensors
def sensors():
    while(True):
        move = 0
        print('0 - вернуться назад')
        print('1 - вывести номера датчиков')
        print('2 - удалить датчик')
        print('3 - добавить датчик')
        move = input()
        number = -1
        lst = []  # номера удаляемых датчиков
        if(move == '0'):
            break
        elif (move == '1'):
            if len(payload['devices']) != 0:
                print("список датчиков для считывания информации:")
                for i in payload['devices']:
                    print(i, sep=" ")  # в одну строку сделать
                continue
            print("Список пуст!")
        elif (move == '2'):
            print("Введите датчик или список датчиков для удаления через пробел")
            numbers = input()
            lst = numbers.split()
            for i in range(len(lst)):
                lst[i] = int(lst[i])
            try:
                for i in range(len(lst)):
                    payload['devices'].remove(lst[i])
            except Exception:
                print("Ошибка! Список датчиков пуст или введённый номера нет в списке!")
        elif (move == '3'):
            print("введите номер датчика")#добавить проверку на существования датчика на nm
            number = input()
            number = int(number)
            payload['devices'].append(number)
        else:
            print("Действие введено неверно, попробуйте ещё раз")

#work with [] of sensors
def get_values():#infinity
    move = "move"
    while(True):
        try:
            response = requests.post(url=urll, json=payload)
            print(response)
            temp = response.json()
            for i in params:
                print(temp['devices'][0][i])
            print('введите end для окончания сбора информации или любой другой символ для продолжения')
            move = input()
            if (move == "end"):
                return
            print("ждите 30 секунд до следующего получения информации с датчика")
            time.sleep(10)
            for i in range(10, 21, 10):
                print("прошло " + str(i) + " секунд")
                time.sleep(10)
        except Exception:
            print("error!!!")
            break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = MWindow(payload, params, urll)
    app.exec_()

