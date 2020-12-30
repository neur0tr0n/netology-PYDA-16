# Задание 3 (бонусное)
import pandas as pd
import re


def production_year(row):
    '''
    Функция вовращает год выпсука фильма из названия, если он присутсвует.
    В противном случае возвразет 1900
    '''
    year = '1900'
    reg_exp = re.compile(r'\((\d{4})\-?(\d{4})?\)')
    if reg_exp.search(row['title']):
        year = reg_exp.search(row['title']).group(1)
    return year


path = '/Users/neur0tr0n/Downloads/ml-latest-small-3/'
movies_file = 'movies.csv'
rating_file = 'ratings.csv'
movies = pd.read_csv(path + movies_file)
ratings = pd.read_csv(path + rating_file)
movie_rating = movies.merge(ratings, how='left', on='movieId')
movie_rating['year'] = movie_rating.apply(production_year, axis=1)
print(movie_rating.groupby('year').mean().sort_values('rating', ascending=False)[['rating']].head(10))

