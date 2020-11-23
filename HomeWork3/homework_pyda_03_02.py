# Задание 2
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
stat = {}
total_query_count = len(queries)
for query in queries:
    words = query.split(' ')
    if len(words) not in stat.keys():
        stat[len(words)] = 1
    else:
        stat[len(words)] += 1
for line in stat.keys():
    print(f'Поисковых запросов, содержащих {line} слов(а): {round(stat[line] / total_query_count * 100, 2)} %')
