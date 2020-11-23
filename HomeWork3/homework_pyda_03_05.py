# Задание 5 (необязательно)
my_list = ['2018-01-01', 'yandex', 'cpc', 100]
my_list_ = ['a', 'b', 'c', 'd', 'e', 'f']
test_dict = {}
tmp_dict = {}
i = 0
for m in range(len(my_list) - 2, -1, -1):
    if i == 0:
        test_dict[my_list[m]] = my_list[m + 1]
    else:
        test_dict.clear()
        test_dict[my_list[m]] = tmp_dict
    tmp_dict = test_dict.copy()
    i += 1
print(test_dict)
