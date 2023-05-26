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
    # 사이트 로딩을 위한 시간 10초
    
    element = driver.find_element(By.CLASS_NAME, 'input_box')
    element.send_keys("한국공학대학교")
    element.send_keys(Keys.ENTER)
    print(element)
    element=driver.find_element(By.CLASS_NAME, 'CHC5F')
    element.click()
    
    location_xpath = driver.find_element('//*[@id="app-root"]/div/div/div/div[6]/div/div[1]/div/div/div[1]/div/a/span[1]')
    location = location_xpath.text
    phone_xpath = driver.find_element('//*[@id="app-root"]/div/div/div/div[6]/div/div[1]/div/div/div[4]/div/span[1]')
    phone = phone_xpath.text
    explain_xpath = driver.find_element('//*[@id="app-root"]/div/div/div/div[6]/div/div[1]/div/div/div[8]/div/a/span[1]')
    explain = explain_xpath.text
    
    print(location+'\n')
    print(phone+'\n')
    print(explain)
        
    driver.quit()
