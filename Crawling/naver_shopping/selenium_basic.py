from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 생성
browser = webdriver.Chrome('/Users/gungo/Documents/chromedriver')

# 웹 사이트 열기
browser.get('https://www.naver.com/')
# 네이버 -> 네이버 쇼핑으로 넘어오는 대기 시간이 길어지면 css를 못 받아서 오류가 생길 때가 종종있음.
# 그래서 로딩이 끝날 때까지 10초까지는 기다려줌.
browser.implicitly_wait(10)

# 쇼핑 메뉴 클릭
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)   # 페이지가 넘어가기도 전에 다음 명령어인 검색창 클릭이 실행될 수도 있기 때문에 기다려주는 명령어를 넣어줌.

# 검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input')
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)