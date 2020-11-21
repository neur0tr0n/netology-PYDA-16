# Задание 4
width = 70
length = 204
height = 70

if width < 15 and length < 15 and height < 15:
    print('Коробка №1')
elif (width >= 15 and width < 50) or (length >= 15 and length < 50) or (height >= 15 and height < 50):
    print('Коробка № 2')
elif length > 200:
    print('Упаковка для лыж')
else:
    print('Стандартная упаковка')