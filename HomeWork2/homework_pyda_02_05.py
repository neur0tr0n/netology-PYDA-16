# Задание 5 (необязательное)
stream1 = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',
    '2018-05-03,user4,9',
    '2018-05-11,user4,11'
]
stream2 = [
    '2018-01-01,user100,150',
    '2018-01-07,user99,205',
    '2018-03-29,user1001,81'
]
lookups = 0
users = list()
for strm in stream2:
    str_list = strm.split(',')
    users.append(str_list[1])
    lookups += int(str_list[2])
unique_users = set(users)
avg_lookup = round(lookups / len(unique_users), 2)
print(avg_lookup)
