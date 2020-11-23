# Задание 1
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]
       }
set_ids = set()
for line in ids.values():
    for num in line:
        set_ids.add(num)
print(set_ids)
