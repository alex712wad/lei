from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
url='http://www.baidu.com'
path=Service('chromedriver.exe')
browser=webdriver.Chrome(service=path)
select=Select(browser.find_element(By.id,'X'))
#根据下拉框的索引选择
select.select_by_index(1)
#根据下拉框的value选择
select.select_by_value('bj')
#根据下拉框的可以看见的前端文字选择
select.select_by_visible_text('知乎')
browser.get(url)
time.sleep(1)

browser.quit()