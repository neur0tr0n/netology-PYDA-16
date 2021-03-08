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

df = pd.read_csv(file_path, names=headers, usecols=col_show, na_values='?')
s = pd.Series
# print(df.head(10))
for col in col_show:
    s = pd.to_numeric(df[col])
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    print(col)
    print(s.min(), s.max())
    print(q1, q3)
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    print(lower_bound, upper_bound)
    remove_outliers = df[df[col].between(lower_bound, upper_bound, inclusive=True)]
    outliers = pd.concat([df, remove_outliers]).drop_duplicates(keep=False)
    print(outliers)


# Вывод: В выбранных полях исследуемой выборки обнаружены выбросы:
# 1. Поле 2: Age. Выброс объясняется некорректной интрепретацией значения поля либо ошибкой передачи данных.
# Например, результаты изменений заносились вручную от руки, в при сканировании результатов, система распознавания
# текста ошибочно интерпретировала 2 как 9.
# 2. Поле 4: rectal temperature.
