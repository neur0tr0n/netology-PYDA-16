# Домашнее задание
# Возьмите датасет с цветками iris’а (функция load_iris из библиотеки sklearn)
# Оставьте два признака - sepal_length и sepal_width и целевую переменную - variety
# Разделите данные на выборку для обучения и тестирования
# Постройте модель LDA
# Визуализируйте предсказания для тестовой выборки и центры классов
# Отбросьте целевую переменную и оставьте только два признака - sepal_length и sepal_width
# Подберите оптимальное число кластеров для алгоритма kmeans и визуализируйте полученную кластеризацию

import  matplotlib.pyplot as plt
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
plt.show()

x_train, x_test, y_train, y_test = train_test_split(df, variety, train_size=0.25)
lda = LinearDiscriminantAnalysis()
lda.fit(x_train, y_train)
y_predict = lda.predict(x_test)
result = pd.DataFrame([y_test, y_predict]).T
print(result)
print(accuracy_score(y_test, y_predict))
print(lda.coef_)
plt.scatter(x_train['sepal length (cm)'], x_train['sepal width (cm)'], c=y_train)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()

plt.title('Ошибка предсказания')
plt.scatter(x_test['sepal length (cm)'], x_test['sepal width (cm)'], c=y_test)
plt.scatter(x_test['sepal length (cm)'], x_test['sepal width (cm)'], c=abs(y_predict - y_test))
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()


