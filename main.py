import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import *
from programStartSetup import *


def fuel_page_navigate():
    # Vilnius selection
    city_dropdown = driver.find_element(By.XPATH, CITY_SELECT)
    city_dropdown.click()
    select = Select(city_dropdown)
    select.select_by_index(1)
    # sort btn click
    driver.find_element(By.XPATH, SORT_BTN).click()
    # sort by A95
    driver.find_element(By.XPATH, A95_COL).click()

    get_lowest_price()


def d_quit(): driver.quit()


def get_lowest_price():
    global lowest_price
    prices_arr = []
    table = driver.find_element(By.XPATH, DATA_TABLE)
    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')

        try:
            prices_arr.append(float(cols[4].text))
        except ValueError:
            continue

    prices_arr.sort()

    if len(prices_arr) > 0:
        lowest_price = str(prices_arr[0])


def fill_input_field(name, value):
    try:
        actions.send_keys_to_element(driver.find_element(By.XPATH, name), value).perform()
        actions.release()
    except NoSuchElementException:
        print('Cant\'t find element by XPATH: ' + name)


def perform_btn_click(xpath):
    actions.click(driver.find_element(By.XPATH, xpath)).perform()
    actions.release()


def perform_keyboard_press(key=Keys.ENTER):
    actions.send_keys(key).perform()
    actions.release()


def paste_text(text):
    actions.send_keys(Keys.CONTROL + text).perform()
    actions.release()


def auth_gmail():
    driver.get(GM_AUTH_ADDRESS)
    time.sleep(2)
    wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, SUBMIT_EMAIL_BTN)))
    paste_text(AUTH_EMAIL)
    time.sleep(2)
    perform_btn_click(SUBMIT_EMAIL_BTN)
    time.sleep(2)
    wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, SUBMIT_PASSWORD_BTN)))
    paste_text(AUTH_PASSWORD)
    time.sleep(2)
    perform_btn_click(SUBMIT_PASSWORD_BTN)
    time.sleep(2)


def send_mail():
    driver.get(SEND_NEW_MAIL_ADDRESS)

    wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, SENDING_MAIL_TO)))

    fill_input_field(SENDING_MAIL_TO, RECIPIENT_MAIL)
    perform_keyboard_press()
    perform_keyboard_press(Keys.TAB)
    paste_text(MSG_SUBJECT)
    perform_keyboard_press(Keys.TAB)
    paste_text(lowest_price)
    perform_keyboard_press(Keys.TAB)
    perform_keyboard_press()


fuel_page_navigate()
auth_gmail()
send_mail()
d_quit()
