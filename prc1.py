from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = "https://map.naver.com/v5/"
browser = webdriver.Chrome()
browser.get(url)

element = browser.find_element(By.CLASS_NAME, 'link_login')
element = browser.find_element(By.CLASS_NAME, 'input_box')
element.send_keys("한국공학대학교")
element.send_keys(Keys.ENTER)

element.click()