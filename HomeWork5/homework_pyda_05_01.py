import json
purchase = {}
dict_purchase = {}
file_purchase = input('Введите путь и имя файла: ')
if file_purchase == '':
    file_purchase = open('/Users/neur0tr0n/Downloads/Downloads/purchase_log.txt', 'r')
else:
    file_purchase = open(file_purchase, 'r')
for line in file_purchase:
    purchase = json.loads(line)
    dict_purchase[purchase['user_id']] = purchase['category']
file_purchase.close()

print(dict_purchase)
