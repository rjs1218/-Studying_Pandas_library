'''
주식 현재가 크롤링 했던 데이터를
아래 양식의 엑셀을 불러와서 B2, B3, B4에 저장해보자.
'''

import requests
from bs4 import BeautifulSoup
import openpyxl

# 엑셀 경로
path = '/Users/gungo/Documents/Python/Crawling/naver_stockPrice/주식_수익률.xlsx'

# 엑셀열기
wb = openpyxl.load_workbook(path)

# 현재 활성화 되어있는 시트 오브젝트 지정
sheet = wb.active

# 종목 코드 리스트
codes = [
    '005930',     # 삼성전자
    '035720',     # 카카오
    '035420'      # 네이버
]

row = 2     # 행 시작점

# 종목 현재가 크롤링
for code in codes:
    url = rf"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    price = soup.select_one("#_nowVal").text
    price = price.replace(',', '')

    # 엑셀 데이터 수정하기
    sheet[f'B{row}'] = int(price)
    row += 1

# 엑셀 저장
wb.save(path)