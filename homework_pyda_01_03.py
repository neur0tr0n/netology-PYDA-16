# Задание 3
months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
astrology_signs = ['Козерог', 'Водолей', 'Рыбы', 'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец']
month = input('Введите месяц своего рождения: ')
if month in months:
    day = int(input('Ведите день своего рождения: '))
    mindx = months.index(month)
    if (mindx % 2 == 0 and mindx <= 6 and day <= 31) or (mindx % 2 == 0 and mindx > 7 and day <= 30):
        print('Все правильно ввели')
    else:
        print('Дата рождения введена некорректно')
else:
    print('Такого месяца не существует!')