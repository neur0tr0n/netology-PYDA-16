# Задание 4
stats = {
    'facebook': 55,
    'yandex': 115,
    'vk': 120,
    'google': 99,
    'email': 42,
    'ok': 98
}
max_num = 0
channel = ''
for line in stats.items():
    if max_num < line[1]:
        max_num = line[1]
        channel = line[0]
print(f'Максимальный объем продаж на рекламном канале: {channel}')