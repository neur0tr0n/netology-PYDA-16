# Задание 5 (необязательное)
# Напишите функцию, которая будет подсчитывать сколько слов начинается на гласные,
# а сколько на согласные буквы в тексте (текст может быть написан как с использованием букв кириллицы, так и латиницы).
import re

some_text = 'Эталонной реализацией Python является интерпретатор CPython, ' \
            'поддерживающий большинство активно используемых платформ. ' \
            'Он распространяется под свободной лицензией Python Software ' \
            'Foundation License, позволяющей использовать его без ограничений ' \
            'в любых приложениях, включая проприетарные.'
reg_exp_vowels = re.compile(r'\b[aoeiuyаеёиоуэюяы]', re.IGNORECASE)
reg_exp_consonants = re.compile(r'\b[^(aoeiuyаеёиоуэюяы,:\.\s)]', re.IGNORECASE)
vowels_count = len(reg_exp_vowels.findall(some_text))
consonants_count = len(reg_exp_consonants.findall(some_text))
print(f'Слов на гласные буквы: {vowels_count}')
print(f'Слов на согласные буквы: {consonants_count}')
