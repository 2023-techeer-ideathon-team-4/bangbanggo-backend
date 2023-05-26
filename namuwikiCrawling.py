##from time import sleep
##import chromedriver_autoinstaller

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
    
    element = driver.find_element(By.CLASS_NAME, 'input_box')
    element.send_keys("한국공학대학교")
    element.send_keys(Keys.ENTER)
    element=driver.find_element(By.CLASS_NAME, 'CHC5F')
    element.click()
    
    location_class = driver.find_element(By.CLASS_NAME, 'O8qbU tQY7D')
    location = location_class.text
    phone_xpath = driver.find_element(By.CLASS_NAME, 'O8qbU nbXkr')
    phone = phone_xpath.text
    explain_xpath = driver.find_element(By.CLASS_NAME, 'O8qbU dRAr1')
    explain = explain_xpath.text
    
    print(location+'\n')
    print(phone+'\n')
    print(explain)
        
    driver.quit()


