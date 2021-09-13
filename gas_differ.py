import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.firefox.options import Options

options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
options.add_argument('window-size=1920x1080')
options.headless = True
DRIVER = webdriver.Firefox(options=options, executable_path=r'gecko/geckodriver')
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
    find_available_fuels = DRIVER.find_elements_by_css_selector(".fuel-header")
    list_of_fuels_found = []
    for found_fuels in find_available_fuels:
        list_of_fuels_found.append(found_fuels.text)
    return list_of_fuels_found


def look_for_gas_prices():
    '''
    1.check prices of fuels on the websites
    2.save it to vars
    3.print for test
    '''
    find_available_pricing = DRIVER.find_elements_by_css_selector(".price")
    list_of_pricing_found = []
    for found_pricing in find_available_pricing:
        list_of_pricing_found.append(found_pricing.text)
    return list_of_pricing_found


def join_gas_with_price(list_of_fuels_found, list_of_pricing_found):
    '''
    1.take values from above functions
    2.iterate over them
    3.find list and save them to vars
    4. join them together
    '''
    for fuel, pricing in zip(list_of_fuels_found, list_of_pricing_found):
        print(fuel + " - " + pricing)


if __name__ == "__main__":
    accept_cookies()
    list_of_fuels_found = look_for_gas()
    list_of_pricing_found = look_for_gas_prices()
    join_gas_with_price(list_of_fuels_found, list_of_pricing_found)
    DRIVER.close()
