# Задание 2
# Добавьте в класс Rate параметр diff (со значениями True или False),
# который в случае значения True в методах курсов валют (eur, usd итд)
# будет возвращать не курс валюты, а изменение по сравнению в прошлым
# значением. Считайте, self.diff будет принимать значение True только при возврате
# значения курса. При отображении всей информации о валюте он не используется.
import requests


class Rate:
    def __init__(self, diff=False):
        self.diff = diff

    def get_quotes(self) -> None:
        quotes = {}
        currs = {}
        req = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        currs = req.json()['Valute']
        for curr, values in currs.items():
            if self.diff:
                quotes[values['CharCode']] = round(values['Previous'] - values['Value'], 4)
            else:
                quotes[values['CharCode']] = values['Value']
        return quotes


quotes = Rate()
quotes.diff = True
print(quotes.get_quotes())
