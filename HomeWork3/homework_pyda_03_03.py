# Задание 3
results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24}
}
for line in results.values():
    roi = float(line['revenue'] / line['cost'] - 1) * 100
    line['ROI'] = round(roi, 2)
print(results)
