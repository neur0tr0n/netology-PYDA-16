# Задание 5 (необязательное)
ticket_number = input('Введите номер вашего билета (6 цифр): ')
sum1 = 0
sum2 = 0
if len(ticket_number) != 6:
    print(f'Введенный номер билета {ticket_number} некоректен!')
else:
    cnt = 1
    for i in ticket_number:
        if cnt > len(ticket_number) / 2:
            sum2 = sum2 + int(i)
        else:
            sum1 = sum1 + int(i)
        cnt += 1
    if sum1 == sum2:
        print(f'Ваш билет {ticket_number} является счастливым!')
    else:
        print(f'Ваш билет {ticket_number} является несчастливым!')







