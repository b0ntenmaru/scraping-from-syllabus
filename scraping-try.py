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

url = requests.get('https://www.meijo-u.ac.jp/academics/syllabus/find/details/112105')
soup = BeautifulSoup(url.content, 'html.parser')
tbody = soup.select('tr')
class_work_name = tbody[0]
print(class_work_name.td.text)
