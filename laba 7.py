import random

print('Задание №1')

while True:
    try:
        M = int(input('Введите число столбцов матрицы: '))
        N = int(input('Введите количество строк матрицы: '))
        if M > 0 and N > 0:
            break
        else:
            print('Число столбцов или строк не может быть отрицательным или равным нулю!')
    except ValueError:
        print('Нужно ввести целочисленно число!')


def Matrix(M, N):
    matrix = []
    for i in range(M):
        st = [random.randint(-100, 100) for _ in range(N)]
        matrix.append(st)
    return matrix

o_matrix = Matrix(M,N)


def MaxSumElem(matrix):
    max_sum = float('-inf')
    max_col_index = 0

    for col in range(len(matrix[0])):  # Идем по столбцам
        col_sum = 0
        for row in range(len(matrix)):
            col_sum += matrix[row][col]

        if col_sum > max_sum:
            max_sum = col_sum
            max_col_index = col

    return max_col_index

print('Исходная матрица:\n')

for st in o_matrix:
    print(st)

col_index = MaxSumElem(o_matrix)

print(f'\nСтолбец с наибольшей суммой элементов: №{col_index + 1}')

print('Задание №2')

while True:
    try:
        x = float(input('Введите вещественное число x: '))
        n = int(input('Введите степень n: '))
        k = int(input('Введите целочисленное число k: '))
        a = int(input('Введите целочисленное число a: '))
        if a != -1:
            break
        else:
            print('При a = -1 будет деление на ноль!')
    except ValueError:
        print('Вы ввели неправильный тип числа!')


def stepen(x: float, n: int) -> float:
    res = 1.0
    for _ in range(abs(n)):
        res *= x
    return res if n >= 0 else 1.0 / res

def F(k, a):
    return stepen(2.7, k) + stepen((a + 1), -5)

print(f'F(k,a) = {F(k, a)}')

print('Задание №3')

while True:
    try:
        length = int(input('Введите длину последовательности: '))
        if length > 0:
            break
        else:
            print('Длина должна быть положительным числом!')
    except ValueError:
        print('Нужно ввести целое число!')

def generate_sequence(length):
    return [random.randint(0, 9) for _ in range(length)]

def count_numbers(sequence):
    count_dict = {}
    for num in sequence:
        count_dict[num] = count_dict.get(num, 0) + 1
    return count_dict

def get_user_number():
    while True:
        try:
            num = int(input('Введите цифру от 0 до 9: '))
            if 0 <= num <= 9:
                return num
            else:
                print('Ошибка: цифра должна быть от 0 до 9!')
        except ValueError:
            print('Ошибка: нужно ввести целое число!')


sequence = generate_sequence(length)
count_dict = count_numbers(sequence)
search_num = get_user_number()
count = count_dict.get(search_num, 0)

print(f'Изначальная последовательность: {sequence}')
if count > 0:
    print(f'Цифра {search_num} встречается {count} раз(а)')
else:
    print(f'Цифра {search_num} не встречается в последовательности')
