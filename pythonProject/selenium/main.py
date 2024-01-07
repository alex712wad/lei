from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service

#准备一个网址
url = "http://www.baidu.com/"
#定义chrome驱动去地址
path = Service('chromedriver.exe')
#  获取浏览器对象
browser = webdriver.Chrome(service=path)
browser.get(url)
sleep(5)
browser.quit()
