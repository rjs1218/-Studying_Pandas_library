from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

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

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    # key end를 누르면 사이트 맨 아래로 이동함
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    # 부하가 생기지 않도록 스크롤 사이 페이지 로딩 시간을 줌
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 파일 생성
# 'w' 쓰기 모드, newline='' 줄바꿈 없애기
f = open(r"/Users/gungo/Documents/Python/Crawling/naver_shopping/data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)


# 상품 정보 div
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")

for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text
    
    try:
        price = item.find_element_by_css_selector(".price_num__2WUXn").text
    except:
        print("판매중단")

    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')

    print(name, price, link)
    
    # 데이터 쓰기
    csvWriter.writerow([name, price, link])

# 파일 닫기
f.close()
    