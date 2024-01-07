from WebProject.base import *
import time
from selenium.webdriver.common.keys import Keys
def book_Ticket(start,end,date,name,id):
    browser = get_Browser()
    url = 'https://www.qunar.com/'
    open_Web(url)
    byname("fromCity").send_keys(Keys.CONTROL,'a')
    byname("fromCity").send_keys(Keys.BACK_SPACE)
    byname("fromCity").send_keys(start)
    click(0,0)
    byname("toCity").send_keys(end)
    click(0,0)
    byname('fromDate').send_keys(Keys.CONTROL,'a')
    byname('fromDate').send_keys(Keys.BACK_SPACE)
    byname('fromDate').send_keys(daysAfterToday(date))
    click(0,0)
    byCss(".button-search").click()
    time.sleep(2)
    byid("QunarPopBoxClosePop").click()
    time.sleep(30)
    byXpath("//*[@id='content']/div/div[3]/div/div[2]/div/div/div[1]/div").click()
    byCss('.input-wrap.passenger-name.js-name > input').send_keys(name)
    byCss('.e_error.label-tip > input').send_keys(id)
    close()
if __name__ == '__main__':
    book_Ticket('北京','上海','21','张三','511604200003159201')