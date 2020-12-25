# Задание 2
# По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония)
# категорий 4, 12 и 21 за период с 2005 по 2010 года. Не учитывайте в расчетах отрицательные значения quantity.
import pandas as pd

countries = pd.read_csv('/Users/neur0tr0n/Downloads/10/power.csv')
filtered_countries = countries[['country', 'quantity', 'category', 'year']]\
    .query('(country == \'Estonia\' or country == \'Lithuania\' or country == \'Lithuania\')  '
             'and (category == 4 or category == 12 or category == 21) and quantity > 0 '
             'and year > 2005 and year < 2010')
print('Суммарное потребление стран Прибалтики (Латвия, Литва и Эстония): {}'.format(filtered_countries['quantity'].sum()))
