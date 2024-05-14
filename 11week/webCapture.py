import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 크롬 옵션 설정
options = Options()
options.add_argument('headless')

# chromedriver 경로 설정 (원시 문자열 사용)
chromedriver_path = r'C:\sjcu_jsh\sjcu-python\11week\chromedriver-win64\chromedriver.exe'
service = Service(chromedriver_path)

# WebDriver 초기화
driver = webdriver.Chrome(service=service, options=options)

url = "http://www.naver.com/"
driver.get(url)
driver.implicitly_wait(2)

# 스크린샷 저장
driver.get_screenshot_as_file("webCapture.png")

# WebDriver 종료
driver.quit()
