# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv

# 引数でlinkを渡す
# detailページに入って、映画情報pをとってくる
def scraping_message(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'html.parser')
    message = soup.select('.entry-content p')
    return message

# rootのページからdetailページのhrefを取り出してlistに保存する
url = requests.get('http://review-movie.herokuapp.com/')
soup = BeautifulSoup(url.content, 'html.parser')
title_atags = soup.select('.entry-title a')

# リストlinksにtitleのhrefをappendする
links = []
for i in title_atags:
    links.append(i['href'])

# forでlinksリスト回してscraping_messageでリンク先のmessageのurl取ってくる
for link in links:
    # print(type(link))
    print(scraping_message('http://review-movie.herokuapp.com/' + link + '\n'))
