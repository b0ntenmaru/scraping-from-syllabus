# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# detailページに入って授業名と成績評価方法をとってくる関数
def get_info(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'html.parser')

    # # 授業名を取得する
    # tbody = soup.select('tr')
    # subject_name = tbody[0].td.text
    #
    # # 担当教員の名前を取得する
    # teacher_name = tbody[2].td.text


    # 学科を取得する
    tbody = soup.select('tr')
    department = tbody[1].td.text
    # 単位数を取得する
    # tbody = soup.select('tr')
    # unit = tbody[6].td.text
    return(department)
