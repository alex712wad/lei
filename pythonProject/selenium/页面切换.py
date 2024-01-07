from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.webdriver.chrome.service import Service
url='http://mail.qq.com'
path=Service('chromedriver.exe')
browser=webdriver.Chrome(service=path)
browser.get(url)
#handler为页面的标签
#获取所有handle
print(browser.window_handles)
#获取当前handler
print(browser.current_window_handle)
#切换到某个handler中
browser.switch_to.window(browser.window_handles[1])
#截图操作
browser.get_screenshot_as_file('1.jpg')
sleep(1)
browser.quit()