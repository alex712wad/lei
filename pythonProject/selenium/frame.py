from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.service import Service
url='http://mail.qq.com'
path=Service('chromedriver.exe')
browser=webdriver.Chrome(service=path)
browser.get(url)
#切换到下级frame中
browser.switch_to.frame('login_frame')
browser.find_element(By.id,'u').send_keys("128683827")
browser.find_element(By.id,'pwArea').send_keys("128683827")
#切换到上级frame中
browser.switch_to.parent_frame()
sleep(1)
browser.quit()