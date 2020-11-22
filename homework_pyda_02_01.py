# Задание 1
word = 'test'
word_len = len(word)
if word_len % 2 == 0:
    print(word[int(word_len / 2 - 1):int(word_len / 2 + 1)])
else:
    print(word[int(word_len / 2)])