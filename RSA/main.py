import math
import random


def is_prime(num, r):  # Проверка на простоту Миллера-Рабина
    for i in range(r):
        s = 2
        while True:
            t = (num - 1)/2**s
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
        num = random.randint(2 ** (dim - 1), 2 ** dim - 1)  # Генерируем число указанной размерности
        r = math.ceil(math.log2(num))//4  # Выбираем количество раундов равным порядку log2(n)//4
        if is_prime(num, r):  # Проверяем простое ли оно
            return num


def opened_exp(euler):  # Вычисление открытой экспоненты
    ferms = [3, 5, 17, 527, 65537]  # Числа Ферма
    for ferm in ferms:
        if math.gcd(euler, ferm) == 1:  # Если НОД равен единице, то числа взаимно простые
            return ferm


def bezout_recursive(a, b):
    if not b:
        return 1, 0, a
    y, x, g = bezout_recursive(b, a % b)
    return x, y - (a // b) * x, g


def closed_exp(e, euler):  # Вычисление закрытой экспоненты с помощью Расширенной теоремы Евклида и соотношения Безу
    x = bezout_recursive(e, euler)
    return x[0] + euler if x[0] < 0 else x[0]


message, coded_message, decoded_message = list(input("Enter a message:\n")), [], []
for letter in message:
    coded_message.append(ord(letter))
dim = int(input("Укажите размерность: \n"))
print("Generating a new keys for you")
p = prime_num()  # Выбираются два простых числа p и q
q = prime_num()
n = p * q
euler = (p - 1) * (q - 1)  # Определяется φ(n)=(p – 1)( q – 1)
e = opened_exp(euler)  # Выбор числа e, взаимно простого с φ(n), причем e < φ(n)
d = closed_exp(e, euler)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')
encrypted = [pow(x, e, n) for x in coded_message]
print(encrypted)
decrypted = [pow(x, d, n) for x in encrypted]
print(decrypted)
for letter in decrypted:
    decoded_message.append(chr(letter))
print("".join(decoded_message))
