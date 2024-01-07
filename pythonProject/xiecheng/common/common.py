from selenium.webdriver.common.action_chains import ActionChains
def click(a, b, browser):
    action = ActionChains(browser)
    action.move_by_offset(a, b)
    action.click()
    action.perform()
