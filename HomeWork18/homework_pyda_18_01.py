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

cmap = colors.LinearSegmentedColormap(
    'red_blue_classes',
    {'red': [(0, 1, 1), (1, 0.7, 0.7)],
     'green': [(0, 0.7, 0.7), (1, 0.7, 0.7)],
     'blue': [(0, 0.7, 0.7), (1, 1, 1)]})

plt.cm.register_cmap(cmap=cmap)
iris = load_iris()
variety = iris.target
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=variety)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title('Распределение классов')
plt.show()


x_train, x_test, y_train, y_test = train_test_split(df, variety, test_size=0.33, random_state=42)
lda = LinearDiscriminantAnalysis()
lda.fit(x_train, y_train)
y_predict = lda.predict(x_test)
result = pd.DataFrame([y_test, y_predict]).T
print(result)
accuracy = accuracy_score(y_test, y_predict)
print(accuracy)
print(lda.coef_)
plt.scatter(x_test['sepal length (cm)'], x_test['sepal width (cm)'], c=y_predict)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Классификация модели. (Точность: {accuracy})')
plt.show()
plt.title(f'Ошибка предсказания.(Точность: {accuracy})')
plt.scatter(x_test['sepal length (cm)'], x_test['sepal width (cm)'], c=y_test)
plt.scatter(x_test['sepal length (cm)'], x_test['sepal width (cm)'], c=abs(y_predict - y_test))
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()

plt.scatter(x_test['sepal length (cm)'], x_test['sepal width (cm)'], c=y_predict)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.title(f'Классификация модели. Центроиды')
centers = lda.means_
plt.scatter(centers[:, 0], centers[:, 1], c='r', s=150, marker='*')

nx, ny = 200, 100
x_min, x_max = plt.xlim()
y_min, y_max = plt.ylim()
xx, yy = np.meshgrid(np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny))

Z = lda.predict_proba(np.c_[xx.ravel(), yy.ravel()])
Z = Z[:, 1].reshape(xx.shape)

#plt.pcolormesh(xx, yy, Z, cmap='red_blue_classes', norm=colors.Normalize(0., 1.), zorder=-1)
#plt.contour(xx, yy, Z, [0.5], linewidths=2., colors='white')
plt.contour(centers[:, 0], centers[:, 1], Z, [0.5], linewidth=2, colors='green')
print(y_predict.shape)
plt.show()

