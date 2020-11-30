# Задание 3
from datetime import datetime
from datetime import timedelta


def check_date(dat):
    try:
        date_time = datetime.strptime(dat, '%Y-%m-%d')
        if date_time != '':
            return True
        else:
            return False
    except:
        return False


def check_date_btlt(s_date, e_date):
    if s_date > e_date:
        return False
    else:
        return True


def get_date_list(s_date, e_date):
    dt_list = []
    s_date_dt = datetime.strptime(s_date, '%Y-%m-%d')
    e_date_dt = datetime.strptime(e_date, '%Y-%m-%d')
    cur_date = s_date_dt
    while cur_date <= e_date_dt:
        dt_list.append(cur_date)
        cur_date += timedelta(days=1)
    return dt_list


start_date = input('Введите начальную дату диапазона в формате \'YYYY-MM-DD\': ')
end_date = input('Введите конечную дату диапазона в формате \'YYYY-MM-DD\': ')
date_list = []
if check_date_btlt(start_date, end_date) and check_date(start_date) and check_date(end_date):
    date_list = get_date_list(start_date, end_date)
else:
    date_list = []
for item in date_list:
    print(item.strftime('%Y-%m-%d'))
