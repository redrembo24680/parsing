import requests
from bs4 import BeautifulSoup as bs

base_url = requests.get('https://knu.ua/ua/departments')


if base_url.status_code == 200:
    soup = bs(base_url.content, features="html.parser")
    f_selector = 'div.b-references'
    list_ = []
    for tag_a in soup.select(f_selector):
        list_.append(f'{tag_a.text} -> {tag_a.get("href")}')
    print(list_)


