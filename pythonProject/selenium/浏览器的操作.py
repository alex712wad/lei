from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
url='https://www.baidu.com'
path=Service('chromedriver.exe')
browser=webdriver.Chrome(service=path)
browser.get(url)
#最大化浏览器
# browser.maximize_window()
#设置浏览器宽高
# browser.set_window_size(300,300)
#后退操作
# browser.find_element(By.ID,'kw').send_keys("王秋越")
# browser.find_element(By.ID,'su').click()
# sleep(1)
# browser.back()
#前进操作
# sleep(1)
# browser.forward()
# sleep(1)
# browser.refresh()
#close页面操作
# browser.find_element(By.LINK_TEXT,'hao123').click()
# print(browser.title)
# print(browser.current_url)
# sleep(1)
# browser.close()
#等待操作
browser.find_element(By.ID,'kw').send_keys('LOL')
browser.find_element(By.ID,'su').click()
#代码执行速度快于页面刷新
#强制等待(固定等待时间不一定可以与网速有关可能会多可能会少)
# sleep(2)
#显式等待
#           等待对象  最大等待时间           等待某个元素加载完成（每隔0.5秒检查一次）
# WebDriverWait(browser,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.c-title.t.t.tts-title > a')))
#隐式等待
browser.implicitly_wait(5)
browser.find_element(By.CSS_SELECTOR,'.c-title.t.t.tts-title > a').click()
sleep(3)
browser.quit()