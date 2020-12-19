# Задание 3
# Решите систему уравнений:
# 4x + 2y + z = 4
# x + 3y = 12
# 5y + 4z = -3
import numpy as np
from numpy import linalg as la

mat_a = np.array([[4, 2, 1], [1, 3, 0], [0, 5, 4]])
mat_b = np.array([4, 12, -3])
solv = la.solve(mat_a, mat_b)
print(solv)
print(np.allclose(np.dot(mat_a, solv), mat_b))