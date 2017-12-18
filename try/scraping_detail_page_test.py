# -*- coding: utf-8 -*-
import requests
import csv
from time import sleep
from bs4 import BeautifulSoup
import os, sys
sys.path.append('../modules')
from get_info import get_info


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
# linksの中に書く授業の詳細ページへのリンクが入ってる
links = []
for name in subject_name:
    href = name['href']
    data = href[24:]
    links.append(data)

# scraping_data関数でインスタンスを作る

department_list = []
unit_number_list = []
for link in links:
    department = get_info('https://www.meijo-u.ac.jp/academics/syllabus/find/' + link)
    print(department)

print('完了')
