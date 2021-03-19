# Домашнее задание
# Возьмите датасет с цветками iris’а (функция load_iris из библиотеки sklearn)
# Оставьте два признака - sepal_length и sepal_width и целевую переменную - variety
# Разделите данные на выборку для обучения и тестирования
# Постройте модель LDA
# Визуализируйте предсказания для тестовой выборки и центры классов
# Отбросьте целевую переменную и оставьте только два признака - sepal_length и sepal_width
# Подберите оптимальное число кластеров для алгоритма kmeans и визуализируйте полученную кластеризацию

import  matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from matplotlib import colors
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

cmap = colors.LinearSegmentedColormap(
    'red_blue_classes',
    {'red': [(0, 1, 1), (1, 0.7, 0.7)],
     'green': [(0, 0.7, 0.7), (1, 0.7, 0.7)],
     'blue': [(0, 0.7, 0.7), (1, 1, 1)]})

# Отображение классификации объектов
plt.cm.register_cmap(cmap=cmap)
iris = load_iris()
variety = iris.target
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=variety)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title('Распределение классов')
plt.show()

# Строим модель линейно-дискриминантного анализа
x_train, x_test, y_train, y_test = train_test_split(df, variety, test_size=0.33, random_state=42)
lda = LinearDiscriminantAnalysis()
lda.fit(x_train, y_train)
y_predict = lda.predict(x_test)
# Результат предсказания модели
result = pd.DataFrame([y_test, y_predict]).T
print(result)
# Точность предсказания
accuracy = accuracy_score(y_test, y_predict)
print(accuracy)
# Коэффициенты дискриминантных линий
print(lda.coef_)
# Визуализация результатов предсказания
plt.scatter(x_test['sepal length (cm)'], x_test['sepal width (cm)'], c=y_predict)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Классификация модели. (Точность: {accuracy})')
plt.show()
# Визуализация ошибки предсказания
plt.title(f'Ошибка предсказания.(Точность: {accuracy})')
plt.scatter(x_test['sepal length (cm)'], x_test['sepal width (cm)'], c=y_test)
plt.scatter(x_test['sepal length (cm)'], x_test['sepal width (cm)'], c=abs(y_predict - y_test))
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()
# Визуализация центроидов
plt.scatter(x_test['sepal length (cm)'], x_test['sepal width (cm)'], c=y_predict)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Классификация модели. Центроиды')
centers = lda.means_
plt.scatter(centers[:, 0], centers[:, 1], c='r', s=150, marker='*')
plt.show()

sx_train = x_train[(y_train == 0) | (y_train == 2)]
sx_train = sx_train[['sepal length (cm)', 'sepal width (cm)']]
sy_train = y_train[(y_train == 0) | (y_train == 2)]
sx_test = x_test[(y_test == 0) | (y_test == 2)]
sx_test = sx_test[['sepal length (cm)', 'sepal width (cm)']]
sy_test = y_test[(y_test == 0) | (y_test == 2)]
plt.scatter(sx_train['sepal length (cm)'], sx_train['sepal width (cm)'], c=sy_train)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Классификация модели. Два класса')
plt.show()
# Строим визуализацию с центроидами и окрашиванием областей
slda = LinearDiscriminantAnalysis()
slda.fit(sx_train, sy_train)
scentroids = slda.means_
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Классификация модели. Два класса. Центроиды')
plt.scatter(sx_train['sepal length (cm)'], sx_train['sepal width (cm)'], c=sy_train)
plt.scatter(scentroids[:, 0], scentroids[:, 1], s=150, c='r', marker='*')
nx, ny = 200, 100
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
xx, yy = np.meshgrid(np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny))
Z = slda.predict_proba(np.c_[xx.ravel(), yy.ravel()])
Z = Z[:, 1].reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap='red_blue_classes', shading='auto', zorder=-1)
plt.contour(xx, yy, Z, [0.5], linewidths=2., colors='white')
plt.show()
# Кластеризация
x = df[['sepal length (cm)', 'sepal width (cm)']]
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Кластеризация')
plt.scatter(x['sepal length (cm)'], x['sepal width (cm)'], s=100, cmap='autumn')
plt.show()
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Кластеризация. Нормализация')
plt.scatter(x_scaled[:, 0], x_scaled[:, 1], s=100, cmap='autumn')
plt.show()
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(x_scaled)
plt.scatter(x_scaled[:, 0], x_scaled[:, 1], cmap='autumn', c=clusters, s=60)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Кластеризаци. Разбиение')
plt.show()
# Строим график локтя
inertias_list = []
ks = range(1, 20)
for i in ks:
    kmean = KMeans(n_clusters=i)
    cluster = kmean.fit_predict(x_scaled)
    inertias_list.append(kmean.inertia_)
plt.plot(ks, inertias_list)
plt.plot(ks, inertias_list, 'ro')
plt.show()
# Строим кластеризацию на основе например 5 кластеров
kmeans = KMeans(n_clusters=5)
clusters = kmeans.fit_predict(x_scaled)
plt.scatter(x_scaled[:, 0], x_scaled[:, 1], cmap='autumn', c=clusters, s=60)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Кластеризаци. Разбиение на 5 кластеров')
plt.show()
# Но самым оптимальным будет разбиение на 2 кластера
kmeans = KMeans(n_clusters=2)
clusters = kmeans.fit_predict(x_scaled)
plt.scatter(x_scaled[:, 0], x_scaled[:, 1], cmap='autumn', c=clusters, s=60)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Кластеризаци. Разбиение на 2 кластера')
plt.show()