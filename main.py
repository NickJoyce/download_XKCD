#! python3
# Загружает все комиксы с https://xkcd.com/
import os
import requests
from bs4 import BeautifulSoup

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print(f'Загружается страница: {url}')
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    comic_elem = soup.find('div', id='comic').find('img')
    if comic_elem == None:
        print('Не удалось найти изображение комикса')
    else:
        img_url = comic_elem.get('src')
        print(f'Загружается изображение: {img_url}')
        res = requests.get('https:' + img_url)
        res.raise_for_status()
        img_file = open(os.path.join('xkcd', os.path.basename(img_url)), 'wb')
        img_file.write(res.content)
        img_file.close()
    prev_link = soup.find('a', rel='prev')
    url = f"https://xkcd.com{prev_link.get('href')}"
print('Готово')
