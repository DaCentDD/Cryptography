import math
import random
import sys

from PyQt5 import QtWidgets, QtCore
from RSA_UI import Ui_MainWindow  # Импорт GUI


encrypted = []
e, d, n = 0, 0, 0
dim = 64  # Размерность генерируемого ключа в битах.


def is_prime(num, r):  # Проверка на простоту Миллера-Рабина
    for i in range(r):
        s = 2
        while True:
            t = (num - 1) / 2 ** s
            if int(t) == 0:
                s, t = 3, 1
            if t % int(t) == 0 and t % 2 == 1:
                t = int(t)
                break
            s += 1
        a = random.randint(2, num - 2)
        x = pow(a, t, num)
        if x == 1 or x == (num - 1):
            continue
        for i in range(s - 1):
            x = pow(x, 2, num)
            if x == 1:
                return False
            if x == (num - 1):
                continue
        return False
    return True


def prime_num():  # Генератор простого числа
    while True:
        num = random.randint(2 ** (dim/2 - 1), 2 ** (dim/2) - 1)  # Генерируем число указанной размерности / 2
        r = math.ceil(math.log2(num)) // 4  # Выбираем количество раундов равным порядку log2(n)//4
        if is_prime(num, r):  # Проверяем простое ли оно
            return num


def opened_exp(euler):  # Вычисление открытой экспоненты
    ferms = [3, 5, 17, 527, 65537]  # Числа Ферма
    for ferm in ferms:
        if math.gcd(euler, ferm) == 1:  # Если НОД равен единице, то числа взаимно простые
            return ferm


def bezout_recursive(a, b):  # Вычисление коэффициенов Безу
    if not b:
        return 1, 0, a
    y, x, g = bezout_recursive(b, a % b)
    return x, y - (a // b) * x, g


def closed_exp(e, euler):  # Вычисление закрытой экспоненты с помощью Расширенной теоремы Евклида и соотношения Безу
    x = bezout_recursive(e, euler)
    return x[0] + euler if x[0] < 0 else x[0]


class GenKey(QtCore.QThread):  # Генерация ключей в потоке-воркере
    set_key_text = QtCore.pyqtSignal(int, int)
    set_enc_text = QtCore.pyqtSignal(list)
    finish = QtCore.pyqtSignal()

    def __init__(self, coded_message):
        QtCore.QThread.__init__(self)
        self.coded_message = coded_message

    def run(self):
        global e, d, n, encrypted
        p = prime_num()  # Выбираются два простых числа p и q
        q = prime_num()
        n = p * q
        euler = (p - 1) * (q - 1)  # Определяется φ(n)=(p – 1)( q – 1)
        e = opened_exp(euler)  # Выбор числа e, взаимно простого с φ(n), причем e < φ(n)
        d = closed_exp(e, euler)  # Выбор числа d, отвечающего тождеству e*d = 1 (mod φ(n))
        self.set_key_text.emit(e, n)
        encrypted = [pow(x, e, n) for x in self.coded_message]
        self.set_enc_text.emit(encrypted)
        self.finish.emit()

    @QtCore.pyqtSlot(int, int)
    def set_key(self):
        application.ui.label_key.setText(f'Public key: {e, n}')

    @QtCore.pyqtSlot(list)
    def set_enc(self):
        application.ui.label_encrypt.setText(f'{encrypted}')

    @QtCore.pyqtSlot()
    def return_but():
        application.ui.button_encrypt.setEnabled(True)
        application.gen.exit()


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_encrypt.clicked.connect(self.encrypt)
        self.ui.button_decrypt.clicked.connect(self.decrypt)

    def encrypt(self):  # Шифрование
        message, coded_message = list(self.ui.text_input.toPlainText()), []  # Считывание сообщения
        if not len(message):
            return
        for letter in message:
            coded_message.append(ord(letter))
        self.ui.label_key.setText("Generating new keys for you")
        self.ui.button_encrypt.setEnabled(False)
        self.gen = GenKey(coded_message)
        self.gen.set_key_text.connect(GenKey.set_key)
        self.gen.set_enc_text.connect(GenKey.set_enc)
        self.gen.finish.connect(GenKey.return_but)
        self.gen.start()

    def decrypt(self):  # Расшифровка
        decoded_message = []
        decrypted = [pow(x, d, n) for x in encrypted]  # Расшифрование
        for letter in decrypted:
            decoded_message.append(chr(letter))
        result = "".join(decoded_message)
        self.ui.label_decrypt.setText(result)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())



