# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# セッション関数でselect入力を保持する
s = requests.Session()
r = s.post(
    'https://www.meijo-u.ac.jp/academics/syllabus/find/',
    data = {
        'data[find][fiscal_year]': ['2017'],
        'data[find][faculty_id]': ['119']
    }
)

# rootのページからdetailページのhrefを取り出してlistに保存する
soup = BeautifulSoup(r.content, 'html.parser')
# subject_nameにaタグ１行が入ってる
subject_name = soup.select('.normal td a')

# リストlinksにsubject_nameのhrefを格納する
links = []
for name in subject_name:
    href = name['href']
    data = href[24:]
    links.append(data)
