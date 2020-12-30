# Задание 1**
# Напишите функцию, которая классифицирует фильмы из материалов занятия по следующим правилам:
# - оценка 2 и меньше - низкий рейтинг
# - оценка 4 и меньше - средний рейтинг
# - оценка 4.5 и 5 - высокий рейтинг
# Результат классификации запишите в столбец class
import pandas as pd


def movie_classify(row):
    '''
    Функция классификации фильма по значению поля rating из dataframe ratings
    '''
    rating = ''
    if row['rating'] <= 2:
        rating = 'низкий рейтинг'
    elif 2 < row['rating'] <= 4:
        rating = 'средний рейтинг'
    elif 4 < row['rating'] <= 5:
        rating = 'высокий рейтинг'
    else:
        rating = 'рейтинг не определен'
    return rating


movies_file = '/Users/neur0tr0n/Downloads/ml-latest-small-3/movies.csv'
rating_file = '/Users/neur0tr0n/Downloads/ml-latest-small-3/ratings.csv'
movies = pd.read_csv(movies_file)
ratings = pd.read_csv(rating_file)
movie_rating = pd.merge(movies, ratings, how='left', on='movieId')
movie_rating['class'] = movie_rating.apply(movie_classify, axis=1)
print(movie_rating.head(10))
