# 2 Задача - ответить на вопрос есть ли связь между жёсткостью воды и средней годовой смертностью?
# Построить точечный график
# Рассчитать коэффициенты корреляции Пирсона и Спирмена
# Построить модель линейной регрессии
# Рассчитать коэффициент детерминации
# Вывести график остатков
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('water.csv')

# Построение точечного графика
plt.scatter(df['hardness'], df['mortality'])
plt.xlabel('mortality')
plt.ylabel('hardness')
plt.show()

# Расчет коэффициентов корреляции
corr = df[['mortality', 'hardness']].corr()['hardness']['mortality']
print(f'Корреляция (Пирсон): {corr:.2}')
corr_spearman = corr = df[['mortality', 'hardness']].corr(method='spearman')['hardness']['mortality']
print(f'Корреляция (Спирмен): {corr_spearman:.2}')

# Построение линейной регрессионной модели и вычисление коэффициента детерминации
x = df[['hardness']]
y = df['mortality']
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
