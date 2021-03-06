# Задание 1
# Напишите функцию, которая принимает на вход строку и проверяет является ли она валидным
# транспортным номером (1 буква, 3 цифры, 2 буквы, 2-3 цифры).
# Обратите внимание, что не все буквы кириллического алфавита используются в транспортных номерах.
# Если номер валиден, то функция должна возвращать отдельно номер и регион.
import re

user_input = input('Введите регистрационный номер транстпортного стредства: ').upper()
reg_exp = re.compile(r'([РОМСТУХНАВЕК]{1}\d{3}[РОМСТУХНАВЕК]{2})(\d{2,3})')
if reg_exp.search(user_input):
    reg_num = reg_exp.search(user_input)
    print(f'Номер {reg_num.group(1)} валиден. Регион: {reg_num.group(2)}')
else:
    print('Номер не валиден.')