import pytest
from xiecheng.base.base import *
from xiecheng.common.common import *
from selenium.webdriver.common.keys import Keys
from time import sleep
def book_Ticket(start,end,time):
    browser = get_Browser()
    url = 'https://flights.ctrip.com/online/channel/domestic'
    browser.get(url)
    sleep(3)
    byXpath('//input[@name="owDCity"]').send_keys(Keys.CONTROL,'a')
    byXpath('//input[@name="owDCity"]').send_keys(Keys.BACK_SPACE)
    byXpath('//input[@name="owDCity"]').send_keys(start)
    click(0,0,browser)
    byXpath('//input[@name="owACity"]').send_keys(Keys.CONTROL, 'a')
    byXpath('//input[@name="owACity"]').send_keys(Keys.BACK_SPACE)
    byXpath('//input[@name="owACity"]').send_keys(end)
    click(0, 0,browser)
    byXpath('//input[@placeholder="yyyy-mm-dd"]').send_keys(Keys.CONTROL, 'a')
    byXpath('//input[@placeholder="yyyy-mm-dd"]').send_keys(Keys.BACK_SPACE)
    byXpath('//input[@placeholder="yyyy-mm-dd"]').send_keys(time)
    click(0, 0,browser)
    byXpath('//button[@class="search-btn"]').click()
if __name__ == '__main__':
    book_Ticket('重庆','上海','2');