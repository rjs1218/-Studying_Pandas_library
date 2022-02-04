import requests
from bs4 import BeautifulSoup

# 종목 코드 리스트
codes = [
    '005930',     # 삼성전자
    '035720',     # 카카오
    '035420'      # 네이버
]

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    respones = requests.get(url)
    html = respones.text
    soup = BeautifulSoup(html, 'html.parser')

    price = soup.select_one("#_nowVal").text
    price = price.replace(',', '')  # 함수 replace()는 문자열을 바꿔준다.
    print(price)