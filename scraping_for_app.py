# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from get_selector_data import scraping_data
import csv
from time import sleep

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

name_list = []
eval_list = []
for link in links:
    name, subject_eval = scraping_data('https://www.meijo-u.ac.jp/academics/syllabus/find/' + link)

    # nameとsubject_evalをリストに格納する
    name_list.append(name)
    eval_list.append(subject_eval)
    sleep(3)
    print(name + '完了')
with open('economics.csv', 'a') as f:
    length = len(name_list)
    for i in range(length):
        f.write(name_list[i] + ',' + str(eval_list[i]) + '\n')

print('完了')
print(len(name_list))
print(len(eval_list))
