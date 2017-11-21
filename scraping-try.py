# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

# url = requests.get('https://www.meijo-u.ac.jp/academics/syllabus/find/details/114230')
url = requests.get('https://www.meijo-u.ac.jp/academics/syllabus/find/details/107547')
soup = BeautifulSoup(url.content, 'html.parser')

table = soup.select('#maincontainer table')
table = table[1]
tr = table.select('tr')
print(tr[7].td.text)
# print(tr[16].text)
# data = soup.find_all(tr, text=re.compile("成績"))
