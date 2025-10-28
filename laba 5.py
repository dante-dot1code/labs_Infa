from math import acos, degrees, sin

print("Задание №1")

x = 4.5
y = [2, 2.2, 2.4, 2.6, 2.8, 3]
a = []

for y in y:
    a.append(round(degrees(acos(y/x))))

print(f"Ответ на Задание №1: a = {a} градусов")

print("Задание №2")

while True:
    try:
        N = int(input("Введите натуральное число N: "))
        if N >= 1:
            break
        else:
            print('Нужно ввести натуральное число 0_0 Попробуйте еще раз!')
    except ValueError:
        print("Вы ввели не число:( Попробуйте еще раз!")

currentSum = 0
totalSum = 0

for i in range(1, N + 1):
    currentSum += sin(i)
    totalSum += 1 / currentSum

print(f"Ответ на Задание №2: {totalSum}")

print("Задание №3")

while True:
    try:
        A = float(input("Введите число A: "))
        if A > 1:
            break
        else:
            print('Нужно ввести что бы A > 1 (0_0) Попробуйте еще раз!')
    except ValueError:
        print("Вы ввели не число:( Попробуйте еще раз!")

Sum = 0
K = 0

while Sum < A:
    K += 1
    Sum += 1 / K

print(f"Ответ на Задание №2: наименьшее K = {K}, Сумма = {Sum}")