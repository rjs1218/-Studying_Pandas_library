'''
프로그램을 실행하면 검색어를 입력받게 해서, 해당 검색어로 크롤링 되게 만들어보자.

조건 1. 내가 원하는 페이지까지 크롤링 해보자
ex) 10 페이지까지
'''

# 네이버 키워드와 관련된 연관검색어 크롤링하기
import requests
from bs4 import BeautifulSoup

print("사람 이름, 제3자의 명예훼손 검색어 제외 요청 등 이러한 키워드의 연관검색어는 없습니다.")

# 키워드 입력
keyword_txt = input('키워드를 입력하세요 : ')

# 연관검색어 개수
keyword_num = int(input('연관검색어를 몇 개 가져올까요?(1 ~ 10) : '))

# 네이버 검색 링크
link = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='

# 키워드로 검색
response = requests.get(link + keyword_txt)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
words = soup.select(".keyword")     # 결과는 리스트값

# 연관검색어 개수만큼 반복
for word in words[:keyword_num]:
    keyword = word.text             # 텍스트 요소만 가져옴 
    print(keyword.strip())          # 공백 제거