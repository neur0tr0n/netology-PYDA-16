documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
command_list = {
    'h': 'Вывод справки',
    'p': 'Поиск владельца документа по номеру',
    's': 'Поиск полки размещения документа по номеру',
    'l': 'Вывод полного спика документов',
    'ls': 'Вывод полного спика полок',
    'lsd': 'Вывод полного спика полок и документов',
    'as': 'Добавление новой полки',
    'ds': 'Удаление существующей полки',
    'ad': 'Добавление нового документа',
    'd': 'Удаление существующего документа',
    'm': 'Перемещение документа с полки на полку',
    'q': 'Выход из приложения',
}


def get_name(number):
    owner_name = ''
    for line in documents:
        if line['number'] == number:
            owner_name = line['name']
            break
        else:
            owner_name = 'not found'
    return owner_name


def get_shelf(number):
    shelf = ''
    for key, values in directories.items():
        if number in values:
            shelf = key
            break
        else:
            folder = 'none'
    return shelf


def doc_full_list():
    for docs in documents:
        doc_num = docs['number']
        doc_typ = docs['type']
        doc_name = docs['name']
        print(f'№: {doc_num}, тип: {doc_typ}, владелец: {doc_name}, полка хранения: {get_shelf(doc_num)}')


def shelf_list():
    s_list = []
    for shelf in directories:
        s_list.append(shelf)
    return s_list


def shelf_full_list():
    s_list = []
    for shelf, doc_list in directories.items():
        str_ = format(f'Полка: {shelf}: Список документов: {doc_list}')
        s_list.append(str_)
    return s_list


def add_new_shelf(number):
    ret_val = False
    if number not in directories.keys():
        directories[str(number)] = []
        ret_val = True
    else:
        ret_val = False
    return ret_val


def add_new_doc(doc_num, doc_t, doc_own, doc_s):
    ret_val = False
    doc_list = []
    if if_exists(doc_s):
        doc_list.append(doc_num)
        directories[doc_s] = doc_list
        documents.append({'type': doc_t, 'number': doc_num, 'name': doc_own})
        ret_val = True
    else:
        ret_val = False
    return ret_val


def is_empty(number):
    rev_val = False
    docs = directories[number]
    if len(docs) != 0:
        rev_val = False
    else:
        rev_val = True
    return rev_val


def if_exists(number):
    rev_val = False
    if number in directories.keys():
        rev_val = True
    return rev_val


def if_doc_exists(number):
    rev_val = -1
    for line in documents:
        if number == line['number']:
            rev_val = documents.index(line)
            break
    return rev_val


def delete_shelf(number):
    ret_val = 0
    if not if_exists(number):
        ret_val = -1
    elif is_empty(number):
        del directories[number]
        ret_val = 1
    else:
        ret_val = 0
    return ret_val


def delete_doc_from_shelf(number):
    ret_val = False
    doc_list = []
    res = if_doc_exists(number)
    if res != -1:
        shelf_num = get_shelf(number)
        doc_list = directories[shelf_num]
        doc_list.remove(number)
        directories[shelf_num] = doc_list
        ret_val = True
    else:
        ret_val = False
    return ret_val


def delete_doc(number):
    ret_val = ''
    res = if_doc_exists(number)
    if res != -1 and delete_doc_from_shelf(number):
        ret_val = documents.pop(res)
    return ret_val


def move_doc(doc_num, shelf_num):
    ret_val = False
    doc_list = []
    res = if_doc_exists(doc_num)
    if res != -1 and if_exists(shelf_num):
        if delete_doc_from_shelf(doc_num):
            doc_list = directories[shelf_num]
            doc_list.append(doc_num)
            directories[shelf_num] = doc_list
            ret_val = True
        else:
            ret_val = False
    else:
        ret_val = False
    return ret_val


def get_help():
    print('Список команд приложения:')
    for key, value in command_list.items():
        print(f'{key} - {value}')


while True:
    command = input('Введите команду (для выхода введите \'q\', для помощи - \'h\'): ')
    if command == 'p':
        doc_number = input('Введите номер документа: ')
        name = get_name(doc_number)
        if name != 'not found':
            print(f'Владелец документа: {name}')
        else:
            print('Документ не найден в базе.')
    elif command == 's':
        doc_number = input('Введите номер документа: ')
        directory = get_shelf(doc_number)
        if directory != 'none':
            print(f'Документ хранится на полке: {directory}')
        else:
            print('Документ не найден в базе.')
    elif command == 'l':
        doc_full_list()
    elif command == 'ls':
        print(shelf_list())
    elif command == 'lsd':
        print(shelf_full_list())
    elif command == 'as':
        shelf_number = input('Введите номер полки: ')
        if add_new_shelf(shelf_number):
            print('Полка добавлена.')
        else:
            print('Такая полка уже существует.')
        print('Текущий перечень полок:')
        print(shelf_full_list())
    elif command == 'ds':
        shelf_number = input('Введите номер полки: ')
        result = delete_shelf(shelf_number)
        if result == 1:
            print('Полка удалена.')
        elif result == 0:
            print('На полке есть документ(ы), удалите их перед удалением полки.')
        elif result == -1:
            print('Такой полки не существует.')
        print('Текущий перечень полок:')
        print(shelf_list())
    elif command == 'ad':
        doc_number = input('Введите номер документа: ')
        doc_type = input('Введите тип документа: ')
        doc_owner = input('Введите имя владельца документа: ')
        doc_self = input('Введите полку для хранения: ')
        result = add_new_doc(doc_number, doc_type, doc_owner, doc_self)
        if result:
            print('Документ добавлен.')
        else:
            print('Такой полки не существует. Добавьте полку командой \'as\'.')
        print('Текущий список документов:')
        doc_full_list()
    elif command == 'd':
        doc_number = input('Введите номер документа: ')
        result = delete_doc(doc_number)
        if result != '':
            print('Документ удален.')
        else:
            print('Документ не найден в базе.')
        print('Текущий список документов:')
        doc_full_list()
    elif command == 'm':
        doc_number = input('Введите номер документа: ')
        shelf_number = input('Введите номер полки: ')
        result = move_doc(doc_number, shelf_number)
        if result:
            print('Документ перемещен.')
        else:
            print('Документ не найден в базе.')
        print('Текущий список документов:')
        doc_full_list()
    elif command == 'h':
        get_help()
    elif command == 'q':
        break
