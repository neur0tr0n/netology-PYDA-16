# Задание 3. Работа с пропусками
# Рассчитать количество пропусков для всех выбранных столбцов. Принять и обосновать решение о методе
# работы с пропусками по каждому столбцу, сформировать датафрейм, в котором пропуски будут отсутствовать.
import pandas as pd

df = pd.read_csv('/Users/neur0tr0n/Downloads/homework_14/horse_data.csv', header=None)
df =pd.DataFrame.replace(df, '?', value=None)
print(df.head(10))
print(df[[0, 1, 3]].head(10))
print(df[[0, 1, 3]].describe(include='all'))