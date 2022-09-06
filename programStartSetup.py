from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from constants import *

driver = webdriver.Chrome(DRIVER_PATH)
# driver.implicitly_wait(0)
driver.get(MAIN_PAGE_LINK)
wait = WebDriverWait(webdriver, 5)
actions = ActionChains(driver)
suc_auth = False
lowest_price = '0'
