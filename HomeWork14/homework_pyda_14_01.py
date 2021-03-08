# Задание 1. Базовое изучение
# Изучить представленный набор данных на основе описания его столбцов и выбрать 8 столбцов для дальнейшего изучения
# (среди них должны быть как числовые, так и категориальные). Провести расчет базовых метрик для них,
# кратко описать результаты.
import pandas as pd
import re

file_path = '/Users/neur0tr0n/Downloads/homework_14/horse_data.csv'
header_file_path = '/Users/neur0tr0n/Downloads/homework_14/horse_data.names'
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
df = pd.read_csv(file_path, names=headers, usecols=col_show, na_values='?')
print(df.head())

# ВЫВОДЫ
print(df.describe())
# 1. 75% лошадей составляют лошади возрастной категории 1, то есть старше 6 мес
# 2. В 50% наблюдений имело место хирургическое поражение (surgical lesion)
s = pd.to_numeric(df['1:  surgery?'])
print(s.describe())
# 3. В более чем 50% случаев, исследованные лошади подвергались хирургическому вмешательству (surgery?).
s = pd.to_numeric(df['23: outcome'])
print(s.describe())
