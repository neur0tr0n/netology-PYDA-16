# Задание 6 (необязательное)
# Напишите функцию, которая будет проверять номер сотового телефона на валидность,
# если он валиден, то переводить его в формат:
# +7-xxx-xxx-xx-xx
# Постарайтесь предусмотреть как можно больше адекватных форматов изначального ввода номера.
# +7 903 214-69-01
import re

test_phones = ['+7 955 555-55-55',
               '8(955)555-55-55',
               '+7 955 555 55 55',
               '7(955) 555-55-55',
               '423-555-55-5555',
               '123-456-789'
               ]


def check_phone_is_valid(phone_):
    reg_exp = re.compile(r'\+?(\d{1})\D{0,}(\d{3})\D{0,}(\d{3})\D?(\d{2})\D?(\d{2})')
    if reg_exp.search(phone_):
        return reg_exp.sub(r'+7-\2-\3-\4-\5', phone_)
    else:
        return 'Номер телефона не валиден!'


some_string = input('Введите номер телефона: ')
if some_string != '':
    print(check_phone_is_valid(some_string))
else:
    for phone in test_phones:
        print(check_phone_is_valid(phone))
