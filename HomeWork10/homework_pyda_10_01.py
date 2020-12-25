# Задание 1
# Скачайте с сайта https://grouplens.org/datasets/movielens/ датасет любого размера.
# Определите какому фильму было выставлено больше всего оценок 5.0.
import pandas as pd
rating_path = '/Users/neur0tr0n/Downloads/ml-latest-small/ratings.csv'
films_path = '/Users/neur0tr0n/Downloads/ml-latest-small/movies.csv'

ratings = pd.read_csv(rating_path)
films = pd.read_csv(films_path)
rating = '5.0'
most_popular_film = ratings[['movieId', 'rating']].query('rating == 5.0').value_counts().head(1)
id_most_popular_film = most_popular_film.index[0][0]
print(films[['title', 'movieId']].query('movieId == {}'.format(id_most_popular_film))['title'])



