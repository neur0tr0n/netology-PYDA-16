# Задание 3
#boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
#girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()
if len(boys) == len(girls):
    print('Идеальные пары:')
    for i in range(len(boys)):
        print(f'{boys[i]} и {girls[i]}')
else:
    print('Внимание, кто-то может остаться без пары!')