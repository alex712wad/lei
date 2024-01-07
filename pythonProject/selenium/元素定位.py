from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from time import sleep
from selenium.webdriver.common.by import By
url = "http://www.baidu.com"
path = Service('chromedriver.exe')
browser = webdriver.Chrome(service=path)
browser.get(url)
#老式写法 browser.find_element_by_id("kw")
#新写法 通过id查找元素
# browser.find_element(By.ID,'kw').send_keys("LOL")
# browser.find_element(By.ID,'su').click()
#通过name查找元素
# browser.find_element(By.CLASS_NAME,'s_ipt').send_keys("LOL")
# browser.find_element(By.id,'su').click()
#定位a标签  hao123是<a>hao123</a>标签里面的内容
# browser.find_element(By.LINK_TEXT,'hao123').click()
#使用css选择器定位 #代表id选择器  [name= wd]名字选择器
# browser.find_element(By.CSS_SELECTOR,'[name=wd]').send_keys("LOL")
# browser.find_element(By.CSS_SELECTOR,'#kw').send_keys("LOL")
# browser.find_element(By.CSS_SELECTOR,'#su').click()
# browser.find_element(By.CSS_SELECTOR,'[value=百度一下]').click()
# browser.find_element(By.XPATH,'//*[@id="kw"]').send_keys("LOL")
# browser.find_element(By.XPATH,"//*[@id='su']").click()
browser.find_element(By.ID,'kw').send_keys("王秋越")
browser.find_element(By.ID,'su').click()
sleep(3)
browser.quit()