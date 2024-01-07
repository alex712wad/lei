from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.service import Service
url='http://www.baidu.com'
path=Service('chromedriver.exe')
browser=webdriver.Chrome(service=path)
browser.get(url)
# 获得警告框
browser.switch_to.alert
#获得警告框并关闭
browser.switch_to.alert.dismiss()
#获得警告框的文字
print(browser.switch_to.alert.text)
#确认警告框
browser.switch_to.alert.accept()
sleep(1)
browser.quit()