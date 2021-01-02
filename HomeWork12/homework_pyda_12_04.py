# Задание 4
# Дана статистика услуг перевозок клиентов компании по типам (см. файл с кодом занятия).
# Необходимо сформировать две таблицы:
# таблицу с тремя типами выручки для каждого client_id без указания адреса клиента
# аналогичную таблицу по типам выручки с указанием адреса клиента
import pandas as pd

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)
auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)
air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)
client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)
joined_df = rzd.merge(auto, how='outer', on='client_id').merge(air, how='outer', on='client_id').fillna(0)
print(joined_df)
joined_df_addr = joined_df.merge(client_base, how='outer', on='client_id')
print(joined_df_addr)
