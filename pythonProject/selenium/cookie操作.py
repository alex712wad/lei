from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
url='https://www.baidu.com'
path=Service('chromedriver.exe')
browser=webdriver.Chrome(service=path)
browser.get(url)
time.sleep(1)
browser.add_cookie({"name":'BDUSS',"value":'rtnhjjrgrb'})
browser.add_cookie({"name":'BAIDUID',"value":'111111111'})
browser.refresh()
time.sleep(30)
browser.quit()