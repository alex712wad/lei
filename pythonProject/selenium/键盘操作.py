import keyword

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep
url ='https://www.baidu.com'
path = Service('chromedriver.exe')
browser = webdriver.Chrome(service=path)
browser.get(url)
demo=browser.find_element(By.id,'1')
#模拟输入删除键
# demo.send_keys(Keys.BACK_SPACE)
#模拟输入ctrl+a全选操作
# browser.find_element(By.ID,'1').send_keys(Keys.CONTROL,'a')
#模拟粘贴操作
# browser.find_element(By.CSS_SELECTOR,'.bg1.bg2>imput').send_keys(Keys.CONTROL,'v')
sleep(1)
browser.quit()