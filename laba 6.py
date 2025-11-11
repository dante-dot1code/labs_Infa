import random

print('Задание №1')
while True:
    text = input('Введите текст: ')
    words = text.split()

    if words:
        break
    else:
        print('Вы ввели пустую строку или только пробелы :( Попробуйте еще раз!')

count = 0
vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'

for word in words:
    for i in range(len(word)-1):
        if word[i] == word[i+1] and word[i].isalpha():
            if word[i] not in vowels:
                count += 1
                break

print(f'Слов с удвоенной согласной: {count}')

print('Задание №2')

while True:
    try:
        N = int(input('Введите целое число N > 0: '))
        if N > 0:
            break
        else:
            print('Нужно было вести N > 0 :( Попробуйте еще раз, у вас обязательно получится!')
    except ValueError:
        print('Нужно ввести целое число :( Попробуйте еще раз, вы обязательно справитесь!')

S = input('Введите строку: ')

while len(S) != N:
    if len(S) > N:
        S = S[:-2]
    else:
        S = '*' + S

print(f'Итоговая строка S = {S}')

print('Задание №3')

while True:
    try:
        n = int(input('Введите размер списка: '))
        if n > 0:
            break
        else:
            print('Размер списка не может быть <= 0 :( Попробуйте еще раз, у вас обязательно получится!')
    except ValueError:
        print('Размером списка не может быть строка или вещественное значение :( Попробуйте еще раз, вы обязательно справитесь!')

o_list = []
for i in range(n):
    o_list.append(random.randint(-100, 100))

max_elem = o_list[0]
max_index = 0
for i in range(1, len(o_list)):
   if o_list[i] > max_elem:
       max_elem = o_list[i]
       max_index = i

sum_list = 0
for i in range(max_index):
    if o_list[i] > 0:
        sum_list += o_list[i]

r_list = o_list[::-1]

print(f'Изначальный список: {o_list}.\nСумма положительных элементов списка, расположенных до максимального элемента: {sum_list}.\nОбратный список: {r_list}')