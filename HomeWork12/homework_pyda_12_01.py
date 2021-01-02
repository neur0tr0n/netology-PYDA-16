# Задание 1
# Для датафрейма log из материалов занятия создайте столбец source_type по следующим правилам:
# если источник traffic_source равен yandex или google, то в source_type ставится organic
# для источников paid и email из России - ставим ad
# для источников paid и email не из России - ставим other
# все остальные варианты берем из traffic_source без изменений
import pandas as pd


def get_source_type(row):
    source_type = ''
    if row['traffic_source'] == 'yandex' or row['traffic_source'] == 'google':
        source_type = 'organic'
    elif (row['traffic_source'] == 'paid' or row['traffic_source'] == 'email') and row['region'] == 'Russia':
        source_type = 'ad'
    elif (row['traffic_source'] == 'paid' or row['traffic_source'] == 'email') and row['region'] != 'Russia':
        source_type = 'other'
    else:
        source_type = row['traffic_source']
    return source_type


path = '/Users/neur0tr0n/Downloads/доп_материалы_к_пандас_1_и_2/'
file = 'visit_log.csv'
log_df = pd.read_csv(path + file, sep=';')
log_df['source_type'] = log_df.apply(get_source_type, axis=1)
print(log_df.head(10))
