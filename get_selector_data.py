# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# detailページに入って書く
def scraping_data(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'html.parser')

    # 授業名を取得する
    tbody = soup.select('tr')
    class_work_name = tbody[0]
    class_work_name = class_work_name.td.text
    # 成績評価方法を取得
    table= soup.select('table')
    table = table[1]
    class_work_evaluation = table.select('tr')
    class_work_evaluation = class_work_evaluation[7].td.text

    # 授業名と成績評価方法を返す
    # class_work_name => 授業名
    # class_work_evaluation => 成績評価方法
    return (class_work_name, class_work_evaluation)
