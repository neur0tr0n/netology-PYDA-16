# Задание 4 (бонусное)
DEFAULT_USER_COUNT = 3


def delete_and_return_last_user(region, default_list=['A100', 'A101', 'A102']):
    """
    Удаляет из списка default_list последнего пользователя
    и возвращает ID нового последнего пользователя.
    """
    last_elem = ''
    try:
        element_to_delete = default_list[-1]
        default_list.remove(element_to_delete)
        last_elem = default_list[-1]
        return last_elem
    except IndexError:
        return 'В списке более нет элементов!'
    #return default_list[DEFAULT_USER_COUNT - 2]
# Ответ: проблема в некорретном обращении к элементу списка с использованием глобальной переменной DEFAULT_USER_COUNT.
# На второй иттерации функция пытается вернуть уже удаленный элемент списка с индексом 1, что вызывает вызов EXCEPTION.
# Испоьзоварние временной переменной и обработки исключений поможет решить проблему


print(delete_and_return_last_user(1))
print(delete_and_return_last_user(1))
print(delete_and_return_last_user(1))
# Удалены все элементы списка.
# Попробуем удалить еще "несколько"
print(delete_and_return_last_user(1))
print(delete_and_return_last_user(1))