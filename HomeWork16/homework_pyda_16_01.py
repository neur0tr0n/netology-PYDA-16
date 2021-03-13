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
# Число попыток игрока
user_trials = 10
# Банк игрока
user_bank = 100
# Колесо автомата с числами
AUTOMATE_PIN = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Количество одновременно выпадающих чисел автомата
AUTOMATE_PATTERN = 3

def make_trial():
    pattern = ''
    for p in range(AUTOMATE_PATTERN):
        pattern = pattern + AUTOMATE_PIN[random.randint(0, len(AUTOMATE_PIN) - 1)]
    return pattern

for i in range(user_trials):
    print(make_trial())


