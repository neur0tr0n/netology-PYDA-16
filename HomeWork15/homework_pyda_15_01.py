# Обязательная часть
# Вам необходимо провести базовый EDA выбранного набора данных.
# Требования к анализу:
# построить не менее 4 визуализаций различных видов;
# каждая визуализация должным образом оформлена и читается даже в отрыве от контекста;
# по каждой визуализации необходимо написать вывод (какую гипотезу на ее основе можно выдвинуть?).

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

file_path = 'country_vaccinations.csv'
df = pd.read_csv(file_path)

date_min = datetime.strptime(df['date'].min(), '%Y-%m-%d')
date_max = datetime.strptime(df['date'].max(), '%Y-%m-%d')

# Рисуем динамику вакцинации по всем странам
# Спад динамики связан со спадом числа вакцинаций в Китае (см. следующий график),
# скорее всего это связано с празднованием Китайского Нового Года

# vaccine = df[['date', 'daily_vaccinations']].groupby('date').sum()
# plt.plot(vaccine.index, vaccine['daily_vaccinations'] / 1000000)
# plt.xlabel('Date')
# plt.ylabel('Vaccinations, millions')
# plt.title('Vaccination Dynamic')
# plt.xticks(np.arange(1, (date_max - date_min).days + 1, (date_max - date_min).days / 8))
# plt.xticks(rotation=20)
# plt.show()

# # Рисуем динамику вакцинации по первым 10 странам с максимальным количеством вакцинируемых
# # В тройке лидеров по вакцинации: США, Китай, Великобритания
# # Россия на 9-м месте

# countries = list(df[['iso_code', 'daily_vaccinations']].groupby('iso_code').sum().sort_values('daily_vaccinations', ascending=False).head(10).index)
# for country in countries:
#     total_vaccinations = df[['date', 'iso_code', 'daily_vaccinations']].query(f'iso_code == \'{country}\'').groupby('date').sum()
#     plt.plot(total_vaccinations.index, total_vaccinations['daily_vaccinations']/1000000)
# plt.xlabel('Date')
# plt.ylabel('Vaccinations, millions')
# plt.title('Vaccination Dynamic by Countries')
# plt.legend(countries)
# plt.xticks(np.arange(1, (date_max - date_min).days + 1, (date_max - date_min).days / 8))
# plt.xticks(rotation=20)
# plt.show()

# Рисуем бары сравнения вакцинированных людей и полностью вакцинированных с группировкой по странам
# Что падавляющее первенствопо по обеим категориям за США

# countries_ppl_fully_vaccinated = df[['iso_code', 'people_fully_vaccinated', 'people_vaccinated']].groupby('iso_code').max().sort_values('people_fully_vaccinated', ascending=False)
# countries_ppl_fully_vaccinated = countries_ppl_fully_vaccinated.head(10)
# countries = countries_ppl_fully_vaccinated.index
# people_vaccinated = countries_ppl_fully_vaccinated['people_vaccinated'] / 1000000
# people_fully_vaccinated = countries_ppl_fully_vaccinated['people_fully_vaccinated'] / 1000000
# width = 0.5
# plt.bar(countries, people_fully_vaccinated, width, color='r')
# plt.bar(countries, people_vaccinated - people_fully_vaccinated, width, bottom=people_fully_vaccinated, color='b')
# plt.legend(labels=['Fully Vaccinated People', 'Vaccinated People'])
# plt.title('Vaccinated People / Fully Vaccinated People')
# plt.xlabel('Countries')
# plt.ylabel('Vaccinated, millions')
# plt.show()


# Рисуем бары по самым "популярным" вакцинам, числу привитых людей,
# а также числу людей, прошедших полный цикл вакцинации определенной вакциной

most_popular_vaccine = df[['vaccines', 'daily_vaccinations', 'people_fully_vaccinated']].groupby('vaccines')\
    .agg({'daily_vaccinations':np.sum, 'people_fully_vaccinated': np.max})\
    .sort_values('daily_vaccinations', ascending=False).head(10)
print(most_popular_vaccine)
most_popular_vaccine_list = most_popular_vaccine.index
people_vaccinated = most_popular_vaccine['daily_vaccinations'] / 1000000
people_fully_vaccinated = most_popular_vaccine['people_fully_vaccinated'] / 1000000
width = 0.35
plt.bar(most_popular_vaccine_list, people_vaccinated, width, color='b')
plt.bar(most_popular_vaccine_list, people_fully_vaccinated, width, color='r')
plt.legend(labels=['Fully Vaccinated People', 'Vaccinated People'])
plt.title('Most Popular Vaccine and Its Full Cycle Usage')
plt.xlabel('Vaccines')
plt.ylabel('Vaccinated, millions')
plt.xticks(rotation=90)
plt.show()

