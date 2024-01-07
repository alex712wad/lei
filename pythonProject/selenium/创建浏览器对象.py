from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.webdriver import Service
url = "http://www.baidu.com"
path = Service('chromedriver.exe')
browser = webdriver.Chrome(service=path)
browser.get(url)
sleep(3)
browser.quit()