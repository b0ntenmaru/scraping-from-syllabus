# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv


# rootのページからdetailページのhrefを取り出してlistに保存する
url = requests.get("http://review-movie.herokuapp.com/")
soup = BeautifulSoup(url.content, 'html.parser')
title_atags = soup.select('.entry-title a')

# リストlinksにtitleのhrefをappendする
links = []
for i in title_atags:
    links.append(i['href'])

# 各titleのhref属性をスクレイピング
# for a in title_atags:
#     print(a['href'])
