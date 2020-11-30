import json

directory = 'C:\\Users\\boris\\Downloads\\Downloads\\'
log_file = open(directory + 'visit_log.csv', 'r')
purchase_file = open(directory + 'purchase_log.txt', 'r')
funnel_file = open(directory + 'funnel_2.csv', 'w')
purchases = {}
purchase = {}
purchases_len = 0
for line in purchase_file:
    purchase = json.loads(line)
    purchases[purchase['user_id']] = purchase['category']
purchase_file.close()
count = 0
for i in log_file:
    count += 1
log_len = count
log_file.seek(0)
quantization = round(log_len / 1000)
count = 0
for line in log_file:
    item = line.strip().split(',')
    for uid, cat in purchases.items():
        if uid == item[0]:
            funnel_file.write(f'{item[0]},{item[1]},{cat}\n')
            break
    if count % quantization == 0:
        print(f'Выполнено: {round(count / log_len * 100, 2)} %')
    count += 1
funnel_file.close()
