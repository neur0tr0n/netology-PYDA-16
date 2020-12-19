# Задание 2
# Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму ее значений на диагонали.
import numpy as np

number = 10
matrix = np.diag(np.arange(number - 1, -1, -1), k=0)
sum = 0
for i in range(number):
    sum += matrix[i, i]
print(sum)
