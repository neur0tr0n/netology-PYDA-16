# Задание 1. Базовое изучение
# Изучить представленный набор данных на основе описания его столбцов и выбрать 8 столбцов для дальнейшего изучения
# (среди них должны быть как числовые, так и категориальные). Провести расчет базовых метрик для них,
# кратко описать результаты.
import pandas as pd
import re
reg_exp = re.compile(r'\d{1,}:.+')
headers_file = open('/Users/neur0tr0n/Downloads/homework_14/horse_data.names', 'r')
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
    '24: surgical lesion?',
    '28: cp_data'
]

df = pd.read_csv('/Users/neur0tr0n/Downloads/homework_14/horse_data.csv', names=headers, usecols=col_show)
df = pd.DataFrame.replace(df, '?', value=None)
df = pd.DataFrame.replace(df, 9, 2)
print(df.head())

# ВЫВОДЫ
print(df.describe(include='int'))
# 1. Более 75% лошадей составляют лошади возрастной категории 1, то есть старше 6 мес
# 2. До 50% лошадей встречается паталогия
print(df['1:  surgery?'].describe())
# 3. В более чем 50% случаев, лошади подвергались хирургическому вмешательству.