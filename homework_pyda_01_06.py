# Задание 6 (необязательное)
import math
print('Расчет площади фигуры.')
figure_type = int(input('Введите тип фигуры: 1 - круг, 2 - треугольник, 3 - прямоугольник: '))
if figure_type == 1:
    print('Вы выбрали рачет плащади круга.')
    radius = float(input('Введите значение радиуса круга: '))
    area = round(math.pi * pow(radius, 2), 2)
    print(f'Площадь круга равна: {area}')
elif figure_type == 2:
    print('Вы выбрали рачет плащади треугольника.')
    side_a = float(input('Введите зачение длины 1 стороны: '))
    side_b = float(input('Введите зачение длины 2 стороны: '))
    side_c = float(input('Введите зачение длины 3 стороны: '))
    area = round((side_a + side_b + side_c) / 2, 2)
    print(f'Площадь треугольника равна: {area}')
else:
    print('Вы выбрали рачет плащади прямоугольника.')
    side_a = float(input('Введите зачение длины 1 стороны: '))
    side_b = float(input('Введите зачение длины 2 стороны: '))
    area = round(side_a * side_b, 2)
    print(f'Площадь прямоугольника равна: {area}')

