import requests
from bs4 import BeautifulSoup

# 서버에서 막을 때 쓰기
header = {'User-agent' : 'Mozila/2.0'}

# 서버에서 막을 때 옵션 추가 : headers = ...
response = requests.get("https://news.naver.com/", headers = header)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

# 결과 값은 리스트임
# select_one은 한 개만 가져오기
title = soup.select_one('.cjs_t')

# title의 텍스트 값만 가져오고, strip() 함수는 공백을 제거해줌
print(title.text.strip())