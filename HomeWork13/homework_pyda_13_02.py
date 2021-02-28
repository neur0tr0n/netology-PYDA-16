# Задание 2.
# Обязательная часть
# Написать скрипт, который будет проверять список e-mail адресов на утечку при помощи сервиса Avast Hack Ckeck.
# Список email-ов задаем переменной в начале кода:
# EMAIL = [xxx@x.ru, yyy@y.com]
# В итоге должен формироваться датафрейм со столбцами: <почта> - <дата утечки> - <источник утечки> - <описание утечки>
# Подсказка: сервис работает при помощи "скрытого" API. Внимательно изучите post-запросы.
import requests
from bs4 import BeautifulSoup as bs
email_list = ['bstrygin@bk.ru', 'neur0tr0n@me.com', 'boris.srygin@gmail.com']
url = 'https://www.avast.com/hackcheck/'
params = {}
resp = requests.get(url, params=params)
soup = bs(resp.text, 'html.parser')
print(soup)


