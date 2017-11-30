# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

# detailページに入って書く
def scraping_data(link):
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'html.parser')
    table= soup.select('table')
    # return tr[13].text #[13] [16]
    table = table[1]
    tr = table.select('tr')
    print(tr[7].td.text)
