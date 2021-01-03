# Задание 3
# Используйте файл с оценками фильмов ml-latest-small/ratings.csv. Посчитайте среднее время жизни пользователей,
# которые выставили более 100 оценок. Под временем жизни понимается разница между максимальным и минимальным
# значением столбца timestamp для данного значения userId.
import pandas as pd

path = '/Users/neur0tr0n/Downloads/Python_13_join/ml-latest-small/'
file = 'ratings.csv'
ratings = pd.read_csv(path + file)
ratings_max = ratings.groupby('userId').max()
ratings_min = ratings.groupby('userId').min()
ratings_count = ratings.groupby('userId').count()
ratings_count['max'] = ratings_max['timestamp']
ratings_count['min'] = ratings_min['timestamp']
ratings_count['diff'] = ratings_count['max'] - ratings_count['min']
mean_user_life = ratings_count.query('movieId > 100')['diff'].mean()
print(mean_user_life)

