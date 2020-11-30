# Задание 2
from datetime import datetime

stream = ['2018-04-02', '2018-02-29', '2018-19-02']


def check_date(dat):
    try:
        date_time = datetime.strptime(dat, '%Y-%m-%d')
        if date_time != '':
            return True
        else:
            return False
    except:
        return False


for date_ in stream:
    print(date_, ' - ', check_date(date_))
