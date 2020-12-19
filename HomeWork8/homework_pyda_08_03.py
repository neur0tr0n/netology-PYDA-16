# Задание 3
# Напишите функцию, которая будет возвращать акроним по переданной в нее строке со словами.
import re

some_words = 'Информационные технологии'
#some_words = 'Near Field Communication'
reg_exp = re.compile(r'(\b\w)+')
list_ = reg_exp.findall(some_words)
new_word = ''
for letter in list_:
    new_word = new_word + letter
new_word = new_word.upper()
print(new_word)