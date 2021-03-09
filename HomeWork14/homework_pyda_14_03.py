# Задание 3. Работа с пропусками
# Рассчитать количество пропусков для всех выбранных столбцов. Принять и обосновать решение о методе
# работы с пропусками по каждому столбцу, сформировать датафрейм, в котором пропуски будут отсутствовать.
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
print(df.head(10))
print(df.isnull().sum())
df_withoutna = pd.DataFrame()

# ВЫВОДЫ
# Меняем категориальные и дискретные значения на моду, а непрерывные значения на медиану
# 1:  surgery?  1 - заменяем на модальное значение
df_withoutna['1:  surgery?'] = df['1:  surgery?'].fillna(df['1:  surgery?'].mode()[0])

df_withoutna['2:  Age'] = df['2:  Age']

# 4:  rectal temperature 60 - заменяем на медианное значение по столбцу
df_withoutna['4:  rectal temperature'] = df['4:  rectal temperature'].fillna(df['4:  rectal temperature'].median())

# 5:  pulse 24 - заменяем на модальное значение
df_withoutna['5:  pulse'] = df['5:  pulse'].fillna(df['5:  pulse'].mode()[0])

# 6:  respiratory rate 58 - заменяем на модальное значение
df_withoutna['6:  respiratory rate'] = df['6:  respiratory rate'].fillna(df['6:  respiratory rate'].mode()[0])

# 7:  temperature of extremities 56 - заменяем на медианное значение по столбцу
df_withoutna['7:  temperature of extremities'] = df['7:  temperature of extremities'].fillna(df['7:  temperature of extremities'].median())

# 8:  peripheral pulse 69 - заменяем на модальное значение
df_withoutna['8:  peripheral pulse'] = df['8:  peripheral pulse'].fillna(df['8:  peripheral pulse'].mode()[0])

# 9:  mucous membranes 47 - заменяем на модальное значение
df_withoutna['9:  mucous membranes'] = df['9:  mucous membranes'].fillna(df['9:  mucous membranes'].mode()[0])

# 10: capillary refill time 32 - заменяем на модальное значение
df_withoutna['10: capillary refill time'] = df['10: capillary refill time'].fillna(df['10: capillary refill time'].mode()[0])

# 23: outcome 1 - заменить на модальное значение
df_withoutna['23: outcome'] = df['23: outcome'].fillna(df['23: outcome'].mode()[0])

df_withoutna['24: surgical lesion?'] = df['24: surgical lesion?']
# Показываем, что в результирующем датафрейме отсутсвуют пропуски
print(df_withoutna.isnull().sum())
# Выводим результитурующий датафрейм
print(df_withoutna.head(10))