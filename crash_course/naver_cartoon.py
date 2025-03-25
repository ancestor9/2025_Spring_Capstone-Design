import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
# print(res.status_code)  # 응답 상태 확인
# print(res.raise_for_status())  # 에러 발생시 에러코드 출력
# print(res.text)  # HTML 코드 출력

soup = BeautifulSoup(res.text, "lxml")  # HTML 파싱
print(soup.title.text)  # 제목 출력
print(soup.title.get_text())  # 같은 결과 출력

# --------------------dynamic web----------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 웹드라이버 실행 (Chrome)
driver = webdriver.Chrome()

# 네이버 웹툰 페이지 열기
driver.get("https://comic.naver.com/webtoon/weekday")

# 페이지 HTML 가져오기
soup = BeautifulSoup(driver.page_source, "lxml")

# 제목 출력
print('selenium')
print(soup.title.text)

# 페이지 로딩 대기
time.sleep(5) # 3초 대기 대기안하면 None 출력

# F12에서 Copy selector를 하고 chat에게 #container > div.ListSpot__spot_wrap--Iko15 > div.content > div > ul
# 대상 요소 선택 (ul 아래의 모든 li 요소 가져오기)
elements = driver.find_elements(By.CSS_SELECTOR, "#container > div.ListSpot__spot_wrap--Iko15 > div.content > div > ul > li")

# 가져온 데이터 출력
# for index, element in enumerate(elements, start=1):
#     print(f"{index}. {element.text}")


# 브라우저 종료
driver.quit()


