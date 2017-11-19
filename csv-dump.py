# -*- coding: utf-8 -*-
"""
経済学部の授業スクレイピングした
"""
import requests
from bs4 import BeautifulSoup
import csv

s = requests.Session()
r = s.post(
    'https://www.meijo-u.ac.jp/academics/syllabus/find',
    data = {
        'data[find][fiscal_year]': ['2017'],
        # 'data[find][faculty_id]': ['119']
    }
)
soup = BeautifulSoup(r.text, 'html.parser')
# items = soup.select('td a')
a = soup.select('.normal td a')
# 授業名を１つずつinfoに格納した
list = []
for i in a:
    info = i.string
    list.append(info.rstrip())

with open('web.csv', 'a') as f:
    length = len(list)
    for i in range(length):
        f.write(list[i] + ',' + '\n')

print('完了')
