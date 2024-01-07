from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date, datetime, timedelta
import pandas
import openpyxl

# import xlrd
path = Service('chromedriver.exe')
browser = webdriver.Chrome(service=path)


def open_Web(url):
    browser.get(url)
    browser.maximize_window()

def byid(element):
    return browser.find_element(By.ID,element)
def byname(element):
    return browser.find_element(By.NAME, element)


def byXpath(element):
    return browser.find_element(By.XPATH, element)


def byCss(element):
    return browser.find_element(By.CSS_SELECTOR, element)


def get_Browser():
    return browser


def close():
    browser.quit()


def click(a, b):
    action = ActionChains(browser)
    action.move_by_offset(a, b)
    action.click()
    action.perform()


def daysAfterToday(n):
    return str(date.today() + timedelta(days=int(n)))


def readExcel(filename):
    data = pandas.read_excel(filename).values
    return data


# if __name__ == '__main__':
    # data = readExcel('data.xlsx')
    # print(data)
