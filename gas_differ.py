import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import ActionChains

DRIVER = webdriver.Firefox(executable_path=r'gecko/geckodriver')
wait = WebDriverWait(DRIVER, 5)

DRIVER.get("https://www.autocentrum.pl/stacje-paliw/pkn-orlen/pkn-orlen-tadeusza-kosciuszki-35-zory")

#SEARCH = DRIVER.find_element_by_class_name("fuel-header")
#SEARCH.send_keys("95")
#SEARCH.send_keys(Keys.RETURN)

def accept_cookies():
    '''
    1.wait till page is loaded
    2.look for button class name
    3.click button
    '''
    button_xpath = '//button[text()="AKCEPTUJĘ I PRZECHODZĘ DO SERWISU"]'
    wait.until(presence_of_element_located((By.XPATH, button_xpath)))
    find_accept_button = DRIVER.find_element_by_xpath(button_xpath)
    find_accept_button.click()


def look_for_gas():
    '''
    1.check availalble fuels on the websites
    2.save it to vars
    3.print for test
    '''
    find_available_fules = DRIVER.find_elements_by_css_selector(".fuel-header")
    for cos in find_available_fules:
        fuels = cos.text
    return fuels


def look_for_gas_prices(tak):
    '''
    1.check prices of fuels on the websites
    2.save it to vars
    3.print for test
    '''
    find_available_fules = DRIVER.find_elements_by_css_selector(".price")
    for cos in find_available_fules:
        fuels_cost = cos.text
    return fuels_cost


def join_gas_with_price():
    print("ok")


if __name__ == "__main__":
    accept_cookies()
    look_for_gas()
    look_for_gas_prices()
    join_gas_with_price()

