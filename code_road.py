# 종목 코드 가져오기
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os
import re
import requests

BaseUrl = 'http://finance.naver.com/sise/entryJongmok.nhn?&page='

if os.path.exists('KOSPI200.csv'):
    os.remove('KOSPI200.csv')
else:
    print("Sorry, I can not remove {} file.".format('KOSPI200.csv'))

for i in range(1, 22, 1):
    try:
        url = BaseUrl + str(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        items = soup.find_all('td', {'class': 'ctg'})

        with open('KOSPI200.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            for item in items:
                txt = item.a.get('href')
                k = re.search('[\d]+', txt)
                if k:
                    code = k.group()
                    name = item.text
                    data = code, name
                    writer.writerow(data)

    except Exception as e:
        print("Error:", e)
        continue
# 파일 열어서 개행 문자 제거
with open('KOSPI200.csv', 'r') as file:
    lines = [line.strip() for line in file]

df = pd.DataFrame([x.split(',') for x in lines], columns = ['종목코드','종목명'])
def find_stock_code(stock_name):
    stock_name = stock_name.lower()
    return df[df['종목명'].str.lower() == stock_name]['종목코드'].values
