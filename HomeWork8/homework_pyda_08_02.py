# Задание 2
# Напишите функцию, которая будет удалять все последовательные повторы
# слов из заданной строки при помощи регулярных выражений.
import re
some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений.'

reg_exp = re.compile(r'\w+')
new_line = ''
prev_item = ''
for item in reg_exp.findall(some_string):
    if item != prev_item:
        new_line = new_line + ' ' + item
    prev_item = item
new_line = new_line.strip()
print(new_line)


