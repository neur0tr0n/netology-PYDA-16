# Задание 3
# Используйте файл с оценками фильмов ml-latest-small/ratings.csv. Посчитайте среднее время жизни пользователей,
# которые выставили более 100 оценок. Под временем жизни понимается разница между максимальным и минимальным
# значением столбца timestamp для данного значения userId.
import pandas as pd

path = '/Users/neur0tr0n/Downloads/Python_13_join/ml-latest-small/'
file = 'ratings.csv'
ratings_df = pd.read_csv(path + file)
print(ratings_df.head(10))

