# Задание 6 (необязательное)
number_string = input('Введите числа через пробел: ')
num_list = number_string.split(' ')
unique_num = []
for num in num_list:
    if num not in unique_num:
        unique_num.append(num)
for num in unique_num:
    if num_list.count(num) > 1:
        print(num, end=' ')