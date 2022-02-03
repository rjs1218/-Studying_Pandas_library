import requests
from bs4 import BeautifulSoup


header = {'User-agent' : 'Mozila/2.0'}

response = requests.get("https://news.naver.com/", headers = header)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

# select는 여러개 가져오기
titles = soup.select('.cjs_t')

for title in titles:
    print(title.text.strip())