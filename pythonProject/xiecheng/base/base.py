from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date, datetime, timedelta
import openpyxl

# import xlrd
path = Service('../chromedriver.exe')
browser = webdriver.Chrome(service=path)


def open_Web(url):
    browser.get(url)
    browser.maximize_window()


def byid(element):
    return browser.find_element(By.ID, element)


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


def daysAfterToday(n):
    return str(date.today() + timedelta(days=int(n)))
