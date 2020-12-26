# Задание 3
# Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas dataframe.
import pandas as pd
import requests
url = 'https://fortrader.org/quotes'
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

response = requests.get(url, headers=header)
data = pd.read_html(response.text)
print(data)
