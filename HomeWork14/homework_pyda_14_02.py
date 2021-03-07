# Задание 2. Работа с выбросами
# В выбранных числовых столбцах найти выбросы, выдвинуть гипотезы об их причинах и
# проинтерпретировать результаты. Принять и обосновать решение о дальнейшей работе с ними.
import pandas as pd
import re

header_file_path = '/Users/neur0tr0n/Downloads/homework_14/horse_data.names'
file_path = '/Users/neur0tr0n/Downloads/homework_14/horse_data.csv'
pd.options.display.max_columns = 8

reg_exp = re.compile(r'\d{1,}:.+')
headers_file = open(header_file_path, 'r')
df = pd.DataFrame()
headers = reg_exp.findall(headers_file.read())
# Можно вывести список всех полей полученных из файла horse_data.names
#print(headers)
# Заполняем датафрейм полями:
col_show = [
    '1:  surgery?',
    '2:  Age',
    '4:  rectal temperature',
    '5:  pulse',
    '6:  respiratory rate',
    '7:  temperature of extremities',
    '8:  peripheral pulse',
    '9:  mucous membranes',
    '10: capillary refill time',
    '23: outcome',
    '24: surgical lesion?'
]

df = pd.read_csv(file_path, names=headers, usecols=col_show)
df = pd.DataFrame.replace(df, '?', value=None)
#print(df.head(10))
for header in headers:
    s = pd.to_numeric(df['23: outcome'])
    print(type(s))

