# Задание 1
from datetime import datetime
dates = {'The Moscow Times': 'Wednesday, October 2, 2002',
         'The Guardian': 'Friday, 11.10.13',
         'Daily News': 'Thursday, 18 August 1977'
}
date_time = datetime.strptime(dates['The Moscow Times'], '%A, %B %d, %Y')
print(date_time)
date_time = datetime.strptime(dates['The Guardian'], '%A, %d.%m.%y')
print(date_time)
date_time = datetime.strptime(dates['Daily News'], '%A, %d %B %Y')
print(date_time)

