# Задание 3
# Напишите класс Designer, который учитывает количество международных премий.
# Подсказки в коде занятия в разделе “Домашнее задание задача 3”.
class Designer:
    grants = {'LOC_GRNT': 0, 'ITL_GRNT': 0}
    first_name = ''
    last_name = ''
    points = 0
    grade = 0

    def __init__(self, first_name, last_name, points=0, grade=0):
        self.first_name = first_name
        self.last_name = last_name
        self.points = points
        self.grade = grade

    def put_grant(self, grant='LOC_GRNT'):
        if grant in self.grants.keys():
            if grant == 'LOC_GRNT':
                self.grants['LOC_GRNT'] += 1
            elif grant == 'ITL_GRNT':
                self.grants['ITL_GRNT'] += 1
        else:
            print('Unknown type of grant!')
        self.points_upgrade(grant)

    def points_upgrade(self, grant):
        if grant == 'LOC_GRNT':
            self.points += 1
        elif grant == 'ITL_GRNT':
            self.points += 2
        self.grade_up()

    def grade_up(self):
        if self.points % 7 == 0:
            self.grade += 1
            self.get_info()

    def get_info(self):
        print(f'Desiner {self.first_name, self.last_name} has {self.grade} grade with {self.points} points')
        print(f'His grants: {self.grants}')


# Создаем экземпляр класса
alex = Designer('Alex', 'Ivanov')
alex.put_grant('')
alex.put_grant('ITL_GRNT')
# Дизайнер Алекс уже имеет две премии: одну государственную, вторую - международную
alex.get_info()
# Добавляем ему еще 10 гос. премий
for i in range(10):
    alex.put_grant()
alex.get_info()
# А затем 5 международных
for i in range(5):
    alex.put_grant('ITL_GRNT')
alex.get_info()
