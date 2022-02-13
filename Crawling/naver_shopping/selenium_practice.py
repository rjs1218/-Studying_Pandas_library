from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

# 브라우저 생성
browser = webdriver.Chrome('/Users/gungo/Documents/chromedriver')

# 웹 사이트 열기
browser.get(r"https://www.naver.com/")
browser.implicitly_wait(10)

# 쇼핑 메뉴 클릭
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

# 검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input')
search.click()

# 검색어 입력
search.send_keys('이클립스')
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    time.sleep(1)

    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break

    before_h = after_h

# 파일 생성
f = open(r"/Users/gungo/Documents/Python/Crawling/naver_shopping/eclips_data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)


item_num = 0    # 아이템 개수

# 상품 정보 div
items = browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")

for item in items:
    name = item.find_element_by_css_selector(".basicList_title__3P9Q7").text

    try:
        price = item.find_element_by_css_selector(".price_num__2WUXn").text
    except:
        print("판매중단")

    link = item.find_element_by_css_selector(".basicList_title__3P9Q7 > a").get_attribute('href')

    item_num += 1

    print(item_num, name, price, link)

    # 데이터 쓰기
    csvWriter.writerow([item_num ,name, price, link])
    
# 파일 닫기
f.close()