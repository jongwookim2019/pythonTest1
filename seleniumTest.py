import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


#설정된 Driver Web 주소 불러오기
#주소 설정
URL = 'https://www.naver.com'
#드라이버 로드(chromedriver)
driver = webdriver.Chrome(executable_path='chromedriver')
#담아준 주소를 브라우저에서 띄움
driver.get(url=URL)

# 현재 url 얻기
print(driver.current_url)

#브라우저 닫기
driver.close()