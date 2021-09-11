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
    return find_available_fules


def look_for_gas_prices():
    '''
    1.check prices of fuels on the websites
    2.save it to vars
    3.print for test
    '''
    find_available_pricing = DRIVER.find_elements_by_css_selector(".price")
    return find_available_pricing


def join_gas_with_price(find_available_fuels, find_available_pricing):
    '''
    1.take values from above functions
    2.iterate over them
    3.find list and save them to vars
    4. join them together
    '''
    for found_fuels in find_available_fuels:
        for found_pricing in find_available_pricing:
            print(found_pricing.text, found_fuels.text)

if __name__ == "__main__":
    accept_cookies()
    find_available_fuels = look_for_gas()
    find_available_pricing = look_for_gas_prices()
    join_gas_with_price(find_available_fuels, find_available_pricing)
    exit()
