# Задание 2
# Добавьте в класс Rate параметр diff (со значениями True или False),
# который в случае значения True в методах курсов валют (eur, usd итд)
# будет возвращать не курс валюты, а изменение по сравнению в прошлым
# значением. Считайте, self.diff будет принимать значение True только при возврате
# значения курса. При отображении всей информации о валюте он не используется.
import requests


class Rate:
    diff = False

    def __init__(self, diff=False):
        self.diff = diff

    def get_quotes(self, currency=''):
        quotes = {}
        currs = {}
        currs = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']
        if currency == '':
            for cur in currs.values():
                if self.diff:
                    quotes[cur['CharCode']] = round(cur['Previous'] - cur['Value'], 4)
                else:
                    quotes[cur['CharCode']] = cur['Value']
        else:
            cur = currs[currency]
            if self.diff:
                quotes[cur['CharCode']] = round(cur['Previous'] - cur['Value'], 4)
            else:
                quotes[cur['CharCode']] = cur['Value']
        return quotes


quotes = Rate()
#quotes.diff = True
print(quotes.get_quotes('USD'))
