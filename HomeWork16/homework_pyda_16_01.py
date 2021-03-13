# Задание
# Смоделировать игру против лотерейного автомата типа “777”. Игрок платит 1 руб.,
# после чего выпадает случайное целое число, равномерно распределенное от 0 до 999.
# При некоторых значениях числа игрок получает выигрыш (см. справа)
# Выгодна ли игра игроку?
import numpy as np
import random
prizes = {
    r'777': 200,
    r'999': 100,
    r'555': 50,
    r'333': 15,
    r'111': 10,
    r'\d77': 5,
    r'\d{2}7': 3,
    r'\d00': 2,
    r'\d{2}0': 1
}
# СИло попыток
trials = 10
# Банк игрока
bank = 100
num = 9
pattern_len = 3
pattern = ''
for i in range(trials):
    pattern = ''
    for p in range(pattern_len):
        pattern = pattern + str(random.randint(0, num))
    print(pattern)

