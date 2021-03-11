# Обязательная часть
# Вам необходимо провести базовый EDA выбранного набора данных.
# Требования к анализу:
# построить не менее 4 визуализаций различных видов;
# каждая визуализация должным образом оформлена и читается даже в отрыве от контекста;
# по каждой визуализации необходимо написать вывод (какую гипотезу на ее основе можно выдвинуть?).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'country_vaccinations.csv'
df = pd.read_csv(file_path)

countries = list(df[['country', 'daily_vaccinations']].groupby('country').sum().sort_values('daily_vaccinations', ascending=False).head(10).index)
print(countries)
for country in countries:
    total_vaccinations = df[['date', 'country', 'daily_vaccinations']].query(f'country == \'{country}\'').groupby('date').sum()
    plt.plot(total_vaccinations.index, total_vaccinations['daily_vaccinations']/1000000)
plt.xlabel('Date')
plt.ylabel('Vaccinations, millions')
plt.title('Vaccination Dynamic')
plt.legend(countries)
plt.xticks()
plt.show()
#
# vaccine = df[['vaccines', 'daily_vaccinations']].groupby('vaccines').sum()
# print(vaccine.head())
# plt.hist(vaccine.index)
# plt.ylabel('Vaccinations')
# plt.xlabel('Vaccine')
# plt.title('Most Popular Vaccine')
# plt.show()
#
# query_string = 'country == \'Russia\' or country == \'England\''
# vaccine_country = df[['vaccines', 'country']].query(query_string).count()
# print(vaccine_country)
# plt.plot(vaccine_country.index, vaccine_country['country'])
# plt.xlabel('Vaccine')
# plt.ylabel('County Count')
# plt.title('Vaccines by Country')
# plt.show()

