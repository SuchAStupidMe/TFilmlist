# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from config import header, s_url


def look_file(param):
    headers = header
    search_url = s_url
    search_param = param
    url = search_url + search_param

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        divs = soup.find_all('div', {'class': 'b-content__inline_item'})

        ref_list = []
        for div in divs:
            div = div.find('a').get('href')
            ref_list.append(div)

        title_list = []
        for title in divs:
            title = title.find('div', {'class': 'b-content__inline_item-link'}).find('a').string
            title_list.append(title)

        final_dict = dict(zip(title_list, ref_list))
        return final_dict

    else:
        print('Connection ERROR')


def get_caption_title_and_description(link):
    r = requests.get(link, headers=header)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        caption_title = soup.find('div', {'class': 'b-sidecover'})
        caption_title = caption_title.find('img')
        url = caption_title['src']
        with open('caption_title.png', 'wb') as handle:
            response = requests.get(url)
            handle.write(response.content)

        description = soup.find('div', {'class': 'b-post__description_text'}).text
        return description

    else:
        pass


def format_list():
    f = open('list.txt', 'rt')  # File open
    filmlist = [line.strip() for line in f]

    formatedlist = []  # Getting actual names without numeration
    for i in filmlist:
        i = i.split('.')
        formatedlist.append(i[1])
    return formatedlist
