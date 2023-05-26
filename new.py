from time import sleep
import chromedriver_autoinstaller

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver



def crawling():
    # chrome driver를 자동으로 설치함
    # chromedriver_autoinstaller.install()

    # 크롤링 할 URL
    url = 'https://map.naver.com/v5/'
    driver = webdriver.Chrome()
    driver.get(url)
    # 사이트 로딩을 위한 시간 10초
    
    Search = driver.find_element(By.CLASS_NAME, 'input_box')
    Search.send_keys("피자헛")
    Search.send_keys(Keys.ENTER)
    
    star = driver.find_element(By.div.span.CLASS_NAME, "PXMot LXIwF")
    
    print(star.text)
        
    driver.quit()
