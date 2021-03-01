# Задание 2.
# Обязательная часть
# Написать скрипт, который будет проверять список e-mail адресов на утечку при помощи сервиса Avast Hack Ckeck.
# Список email-ов задаем переменной в начале кода:
# EMAIL = [xxx@x.ru, yyy@y.com]
# В итоге должен формироваться датафрейм со столбцами: <почта> - <дата утечки> - <источник утечки> - <описание утечки>
# Подсказка: сервис работает при помощи "скрытого" API. Внимательно изучите post-запросы.
import requests
import json
import pandas as pd

response = {}
emails = ['neur0tr0n@me.com', 'boris.strygin@gmail.com', 'bstrygin@bk.ru']
url = 'https://identityprotection.avast.com/v1/web/query/site-breaches/unauthorized-data'
data = {'emailAddresses' : ['neur0tr0n@me.com', 'boris.strygin@gmail.com', 'bstrygin@bk.ru']}
headers = {
    'Content-Type': 'application/json;charset=utf-8',
    'Accept': 'text/plain',
    'Vaar-Header-App-Product-Name': 'hackcheck-web-avast',
    'Vaar-Version': '0',
    'Vaar-Header-App-Product': 'hackcheck-web-avast',
    'Vaar-Header-App-Build-Version': '1.0.0'
}
res = requests.post(url, headers=headers, data=json.dumps(data))

print(res.status_code)
if res.status_code == 200 and res.json():
    response = res.json()
    email_dictionary = response['summary']
    d_frame = pd.DataFrame()
    for email in emails:
        if email_dictionary[email]['breaches']:
            breaches = email_dictionary[email]['breaches']
            for breach in breaches:
                breach_dictionary = response['breaches'][str(breach)]
                publishDate = breach_dictionary['publishDate']
                site = breach_dictionary['site']
                description = breach_dictionary['description']
                row = {'email': email, 'publishDate': publishDate, 'site': site, 'description': description}
                d_frame = pd.concat([d_frame, pd.DataFrame([row])])
    print(d_frame)
else:
    print('Request has returned none!')

