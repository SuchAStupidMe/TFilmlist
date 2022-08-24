# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from config import formatedlist, header, s_url


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

        # with open(f'{search_param}.txt', 'w', encoding='utf-8') as f:
        #     for line in final_dict:
        #         f.write(line + ' : ' + final_dict[line] + '\n')

    else:
        print('Connection ERROR')


def fulllist_search():
    for name in formatedlist:
        look_file(name)


def get_caption_title(link):
    headers = header

    r = requests.get(link, headers=headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        caption_title = soup.find('div', {'class': 'b-sidecover'})
        caption_title = caption_title.find('a').get('href')

        return caption_title
