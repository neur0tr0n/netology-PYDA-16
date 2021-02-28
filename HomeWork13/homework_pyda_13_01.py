# Задание 1.
# Обязательная часть
# Будем парсить страницу со свежеми новостям на habr.com/ru/all/.
# Вам необходимо собирать только те статьи, в которых встречается хотя бы одно требуемое ключевое слово.
# Эти слова определяем в начале кода в переменной, например:
# KEYWORDS = ['python', 'парсинг']
# Поиск вести по всей доступной preview-информации (это информация, доступная непосредственно с текущей страницы).
# В итоге должен формироваться датафрейм вида: <дата> - <заголовок> - <ссылка>
# Дополнительная часть (необязательная)
# Улучшить скрипт так, чтобы он анализировал не только preview-информацию статьи, но и весь текст статьи целиком.
# Для этого потребуется получать страницы статей и искать по тексту внутри этой страницы.
# Итоговый датафрейм формировать со столбцами: <дата> - <заголовок> - <ссылка> - <текст_статьи>
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import time

URL = 'https://habr.com/ru/all/'
KEYWORDS = ['python', 'парсинг']
params = {}


def get_pages_count():
    """
    Функция определения количества страниц ресурса по URL
    :return:
    """
    reg_exp = re.compile(r'(\d{1,})')
    res = requests.get(URL, params=params)
    soup = bs(res.text, 'html.parser')
    last_page_url = soup.find('a', class_='toggle-menu__item-link toggle-menu__item-link_pagination toggle-menu__item-link_bordered').get('href')
    return reg_exp.search(last_page_url)[0]


def get_articles(url_, keywords_, full_search=False):
    """
    Функция возвращающая DataFrame cо спсиком статей, найденных по словам из словаря поиска
    :type full_search: object
    :param url_:
    :param keywords_:
    :return:
    """
    articles = pd.DataFrame()
    for i in range(1, pages_count):
        page_url = url_ + 'page' + str(i)
        resp = requests.get(page_url, params=params)
        time.sleep(0.3)
        soup = bs(resp.text, 'html.parser')
        # Получаем превью каждой статьи на странице
        post_previews = soup.find_all('article', class_='post post_preview')
        # Парсим каждую превью
        for post_preview in post_previews:
            # Получем дату
            date = post_preview.find('span', class_='post__time').text
            title = post_preview.find('h2', class_='post__title')
            # Название статьи
            article_title = title.text
            # Линк на статью
            link = title.find('a').get('href')
            # Текст превью
            preview_text = post_preview.find('div', class_='post__body post__body_crop').text
            # Поиск по ключевым слеовам в превью
            if if_keywords_found(keywords_, preview_text) and full_search == False:
                row = {'date': date, 'article_title': article_title, 'link': link}
                articles = pd.concat([articles, pd.DataFrame([row])])
            # Поиск по ключевым словам в полном тексте статьи
            elif full_search:
                full_text = get_full_article_text(link)
                if if_keywords_found(keywords_, full_text):
                    row = {'date': date, 'article_title': article_title, 'link': link, 'full_text': full_text}
                    articles = pd.concat([articles, pd.DataFrame([row])])
    return articles


def get_full_article_text(url_):
    """
    Функция определяющая вхождение ключевых слов словаря поиска в полном тексте статьи
    :param url_:
    :return:
    """
    resp = requests.get(url_)
    soup = bs(resp.text, 'html.parser')
    article_full_text = soup.find('div', class_='post__body post__body_full').text
    return  article_full_text


def if_keywords_found(keywords_, text_):
    """
    Функция определяющая вхождение слов из словаря поиска в исследуемом тексте
    :param keywords_:
    :param text_:
    :return:
    """
    ret_val = False
    if set(keywords_) & set(text_.split()):
        ret_val = True
    else:
        for keyword in keywords_:
            if keyword in text_:
                ret_val = True
                break
    return ret_val


pages_count = int(get_pages_count())
article_list = get_articles(URL, KEYWORDS)
print('Поиск по превьюшкам статей.')
print(article_list)
# Расширеный поиск по текстам статей
#article_list = get_articles(URL, KEYWORDS, full_search=True)
#print('Поиск по полному тексту статьи.')
print(article_list)
