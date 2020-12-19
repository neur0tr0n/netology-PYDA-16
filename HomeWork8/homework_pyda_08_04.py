# Задание 4
# Напишите функцию, которая будет принимать на вход список
# email-адресов и выводить их распределение по доменным зонам.
import re

emails = 'test@gmail.com, xyz@test.in, test@ya.ru, xyz@mail.ru, xyz@ya.ru, xyz@gmail.com'
reg_exp = re.compile(r'(?:@)(\w+\.\w{2,3})')
domains = reg_exp.findall(emails)
domain_entry = {}
for domain in domains:
    if domain in domain_entry.keys():
        domain_entry[domain] += 1
    else:
        domain_entry[domain] = 1
for dom, count in domain_entry.items():
    print(f'{dom} : {count}')




