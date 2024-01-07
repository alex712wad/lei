from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
url ='https://www.baidu.com'
path = Service('chromedriver.exe')
browser = webdriver.Chrome(service=path)
browser.get(url)
mouse = ActionChains(browser)
#拖动操作
# mouse.drag_and_drop(browser.find_element(By.CSS_SELECTOR,'XXX'),browser.find_element(By.CSS_SELECTOR,'XXX '))
# mouse.perform()
# sleep(1)
#移动鼠标
# mouse.move_to_element(browser.find_element(By.CSS_SELECTOR,'XXX'))
# mouse.perform()
#双机鼠标
# mouse.double_click(browser.find_element(By.ID,'X'))
# mouse.perform()

sleep(1)
browser.quit()