# Задание 2
numbers = list()
summa = 0
while True:
    num = int(input('Ведите число: '))
    if num != 0:
        numbers.append(num)
    else:
        break
for num in numbers:
    summa += num
print(summa)