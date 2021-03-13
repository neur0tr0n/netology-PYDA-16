# 3 Задание.
# Сохраняется ли аналогичная зависимость для северных и южных городов по отдельности?
# Разделить данные на 2 группы
# Повторить аналогичные шаги из пункта 1 для каждой группы по отдельности

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def build_regg_model(df_):
    # Расчет коэффициентов корреляции
    corr = df_[['mortality', 'hardness']].corr()['hardness']['mortality']
    print(f'Корреляция (Пирсон): {corr:.2}')
    corr_spearman = corr = df_[['mortality', 'hardness']].corr(method='spearman')['hardness']['mortality']
    print(f'Корреляция (Спирмен): {corr_spearman:.2}')
    # Построение линейной регрессионной модели и вычисление коэффициента детерминации
    x = df_[['hardness']]
    y = df_['mortality']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    model = LinearRegression()
    model.fit(x_train, y_train)
    print(f'Параметры модели: a = {model.coef_}, b = {model.intercept_}')
    y_pedict = model.predict(x_test)
    determinantion = model.score(x_test, y_test)
    print(f'Коэффициент детерминации: {determinantion}')
    plt.scatter(x_test, y_test)
    plt.plot(x_test, y_pedict, color='r')
    plt.xlabel('hardness')
    plt.ylabel('mortality')
    plt.show()
    # График остатков
    plt.scatter(x_test, y_pedict - y_test)
    plt.xlabel('hardness')
    plt.ylabel('mortality')
    plt.show()


df = pd.read_csv('water.csv')
df_north = df.query('location == \'North\'')
df_south = df.query('location == \'South\'')

# Построение точечного графика
plt.scatter(df_north['hardness'], df_north['mortality'], color='b')
plt.scatter(df_south['hardness'], df_south['mortality'], color='r')
plt.xlabel('mortality')
plt.ylabel('hardness')
plt.legend(labels=['North', 'South'])
plt.show()

print('Северные города')
build_regg_model(df_north)
print('\nЮжные города')
build_regg_model(df_south)





