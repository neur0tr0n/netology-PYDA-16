# Дополнительное задание повышенной сложности. Теоретически рассчитать средний выигрыш (проигрыш)
# и сравнить с результатами моделирования
import numpy as np
import re
PRIZES = {
    r'777': [0, 200],
    r'999': [0, 100],
    r'555': [0, 50],
    r'333': [0, 15],
    r'111': [0, 10],
    r'\d77': [0, 5],
    r'\d{2}7': [0, 3],
    r'\d00': [0, 2],
    r'\d{2}0': [0, 1]
}


def check_if_exists(str_):
    ret_val = 0
    for key, val in PRIZES.items():
        reg_exp = re.compile(key)
        if reg_exp.findall(str_):
            lst = PRIZES[key]
            lst[0] += 1
            PRIZES[key] = lst
            ret_val = 1
            break
    return ret_val


count = 0
bet_number = 1000
bet = 1
for i in range(0, bet_number):
    count += check_if_exists(str(i).zfill(3))

print('Выводы:')
print(f'Число выигрышных случаев: {count}\nПри этом для комбинации:')
total_prize = 0
for key, val in PRIZES.items():
    prize = val[0] * val[1]
    print(f'\t- \'{key}\'\t - число выигрышных случаев: {val[0]}, '
          f'вероятность выпадения комбинации: {val[0] / bet_number * 100:.2}%, '
          f'а сумма всех выигрышей составит: {prize}')
    total_prize += prize
print(f'Общая сумма \'возможного\' выигрыша составит: {total_prize} при потраченных: {bet * bet_number}')
print(f'Математическое ожидание выигрыша составит: {total_prize / (bet * bet_number)} на каждую ставку,\n'
      f'что не является выигрышной стратегией, и подтверждается экспериментально в первом задании ДР.')

