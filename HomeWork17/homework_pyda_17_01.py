# 2 Задача - ответить на вопрос есть ли связь между жёсткостью воды и средней годовой смертностью?
# Построить точечный график
# Рассчитать коэффициенты корреляции Пирсона и Спирмена
# Построить модель линейной регрессии
# Рассчитать коэффициент детерминации
# Вывести график остатков
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('water.csv')
df.corr()
print(df.info())
df.plot(kind='scatter', x='mortality', y='hardness')
plt.show()

corr = df[['mortality', 'hardness']].corr()['hardness']['mortality']
print(f'Корреляция (Пирсон): {corr:.2}')
corr_spearman = corr = df[['mortality', 'hardness']].corr(method='spearman')['hardness']['mortality']
print(f'Корреляция (Спирмен): {corr_spearman:.2}')

