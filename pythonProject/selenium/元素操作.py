from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
url = 'http://www.baidu.com'
path = Service('chromedriver.exe')
browser = webdriver.Chrome(service=path)
browser.get(url)
print(browser.find_element(By.CSS_SELECTOR, '.bg.s_btn_wr > input').size)
print(browser.find_element(By.LINK_TEXT,'hao123').text)
print(browser.find_element(By.LINK_TEXT,'hao123').get_attribute("href"))
print(browser.find_element(By.LINK_TEXT,'hao123').is_enabled())
print(browser.find_element(By.LINK_TEXT,'hao123').is_displayed())
sleep(1)
browser.quit()