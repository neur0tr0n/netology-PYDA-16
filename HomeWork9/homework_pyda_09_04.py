# Задание 4
# Найдите самого похожего пользователя. Т. е. посчитайте косинусное сходство между этим пользователем и
# всеми пользователями из массива user_stats
import numpy as np
from numpy import linalg as la

users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ],
    np.int32
)
next_user_stats = np.array([0, 1, 2, 0, 0, 0])


def get_cos(user_a, user_b):
    a_length = la.norm(user_a)
    b_length = la.norm(user_b)
    return round(np.dot(user_a, user_b) / (a_length * b_length), 3)


max_cos = -1
for user in users_stats:
    cos = get_cos(next_user_stats, user)
    if max_cos < cos:
        max_cos = cos
        match_user = user
print(next_user_stats)
print(match_user)
print(max_cos)
