import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
#크롬 에러 수정
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enavle-logging'])
driver = webdriver.Chrome(options=options)


#설정된 Driver Web 주소 불러오기
#주소 설정
URL = 'https://nid.naver.com/nidlogin.login?url=http%3A%2F%2Fmail.naver.com%2F'
#드라이버 로드(chromedriver)
driver = webdriver.Chrome(executable_path='chromedriver')
#담아준 주소를 브라우저에서 띄움
driver.get(url=URL)

# 현재 url 얻기
print(driver.current_url)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,'btn_text'))
    )
finally:
    driver.quit()
    print(EC.presence_of_element_located((By.CLASS_NAME,'btn_text')))

#브라우저 닫기
#driver.close()