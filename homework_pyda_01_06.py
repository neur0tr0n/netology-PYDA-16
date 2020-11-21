# Задание 6 (необязательное)
import math
side_a = 0
side_b = 0
side_c = 0
radius = 0
area = 0
print('Расчет площади фигуры.')
figure_type = int(input('Введите тип фигуры: 1 - круг, 2 - треугольник, 3 - прямоугольник: '))
if figure_type == 1:
    print('Вы выбрали рачет плащади круга.')
    radius = float(input('Введите значение радиуса круга: '))
    area = math.pi * pow(radius, 2)
    print(f'Площадь круга равна: {area}')
elif figure_type == 2:
    print('Вы выбрали рачет плащади треугольника.')
    side_a = float(input('Введите зачение длины 1 стороны: '))
    side_b = float(input('Введите зачение длины 2 стороны: '))
    side_c = float(input('Введите зачение длины 3 стороны: '))
    area = (side_a + side_b + side_c) / 2
    print(f'Площадь треугольника равна: {area}')
else:
    print('Вы выбрали рачет плащади прямоугольника.')
    side_a = float(input('Введите зачение длины 1 стороны: '))
    side_b = float(input('Введите зачение длины 2 стороны: '))
    area = side_a * side_b
    print(f'Площадь прямоугольника равна: {area}')

