# Задание 3
# Напишите класс Designer, который учитывает количество международных премий.
# Подсказки в коде занятия в разделе “Домашнее задание задача 3”.
class Designer:
    itl_grant_count = 0

    def __init__(self, first_name, last_name, grade = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

    def grade_up(self):
