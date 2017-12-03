# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# detailページに入って書く
def scraping_data(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'html.parser')

    # 授業名を取得する
    # tbody = soup.select('tr')
    # class_work_name = tbody[0].td.text
    # class_work_name = class_work_name.td.text

    # 成績評価方法を取得
    table= soup.select('table')
    table = table[1]

    try:
        subject_eval = table.select('tr')[7].td.text
        return (subject_eval)
    except:
        print('エラー')
