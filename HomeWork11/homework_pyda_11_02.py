# Задание 2
# Используем файл keywords.csv.
# Необходимо написать гео-классификатор, который каждой строке сможет выставить географическую
# принадлежность определенному региону. Т. е. если поисковый запрос содержит название города региона,
# то в столбце ‘region’ пишется название этого региона. Если поисковый запрос не содержит названия города,
# то ставим ‘undefined’
import pandas as pd


def get_region(row):
    region = 'undefined'
    geo_data = {
        'Центр': ['москва', 'тула', 'ярославль'],
        'Северо-Запад': ['петербург', 'псков', 'мурманск'],
        'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
    }
    for key, cities in geo_data.items():
        split_keywords = [x.lower() for x in row['keyword'].split()]
        if set(split_keywords).intersection(cities):
            region = key
    return region


path = '/Users/neur0tr0n/Downloads/ml-latest-small-3/'
file = 'keywords.csv'
keywords = pd.read_csv(path + file)
keywords['region'] = keywords.apply(get_region, axis=1)
print(keywords.query('region != \'undefined\'').head(10))
