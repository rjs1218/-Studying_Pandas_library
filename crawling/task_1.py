'''
프로그램을 실행하면 검색어를 입력받게 해서, 해당 검색어로 크롤링 되게 만들어보자.

조건 1. 내가 원하는 페이지까지 크롤링 해보자
ex) 10 페이지까지
'''

# 무신사스토어에서 리뷰와 별점 개수 크롤링하기
import requests
from bs4 import BeautifulSoup


# 무신사에서 반스 컴피쿠시원의 리뷰와 별점 개수를 크롤링 할 거임
response = requests.get("https://store.musinsa.com/app/goods/2233180?loc=goods_rank")
html = response.text

soup = BeautifulSoup(html, 'html.parser')
reviews = soup.select(".review-contents__text")


print(reviews)
# for review in reviews:
#     result = review.text
#     print(result)