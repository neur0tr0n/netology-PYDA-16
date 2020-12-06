# Задание 1
# Напишите функцию, которая возвращает название валюты (поле ‘Name’) с
# максимальным значением курса с помощью сервиса
# https://www.cbr-xml-daily.ru/daily_json.js
import requests


def get_max_value_cur():
    cur_lib = {}
    max_val = 0
    max_val_cur = ''
    req = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    cur_lib = req.json()['Valute']
    for cur, lib_ in cur_lib.items():
        if max_val <= lib_['Value']:
            max_val = lib_['Value']
            max_val_cur = cur
    return max_val_cur


def get_cur_values():
        req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return req.json()['Valute']


print(get_cur_values())
print(get_max_value_cur())




