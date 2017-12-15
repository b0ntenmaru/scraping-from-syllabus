# -*- coding: utf-8 -*-
import requests
import csv
from time import sleep
from bs4 import BeautifulSoup
import os, sys
sys.path.append('../../modules')
from get_selector_data import scraping_data


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

subject_name_list = [] # 教科名
teachers_name_list = [] # 教員
eval_list = [] # 成績評価方法
for link in links:
    subject_name, teacher_name, subject_eval = scraping_data('https://www.meijo-u.ac.jp/academics/syllabus/find/' + link)

    # subject_nameとteachers_nameとevalをリストに格納する
    subject_name_list.append(subject_name)
    teachers_name_list.append(teacher_name)
    eval_list.append(subject_eval)
    # sleep(1)
    print(subject_name + '完了')


with open('economics.csv', 'a') as f:
    length = len(subject_name_list)
    for i in range(length):
        f.write('経済,' + '"' + subject_name_list[i] + '"' + ',' + '"' + teachers_name_list[i] + '"' + ',' + '"' + str(eval_list[i]) + '"' + '\n')

print('完了')
print(len(subject_name_list))
print(len(teachers_name_list))
print(len(eval_list))
