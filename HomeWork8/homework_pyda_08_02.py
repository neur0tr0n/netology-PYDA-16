# Задание 2
# Напишите функцию, которая будет удалять все последовательные повторы
# слов из заданной строки при помощи регулярных выражений.
import re

some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений.'
reg_exp = re.compile(r'\b(\w+)(?:\s+\1\b)+')
new_string = reg_exp.sub(r'\1', some_string)
print(new_string)
