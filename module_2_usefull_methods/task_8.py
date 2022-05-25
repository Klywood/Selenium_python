"""
https://stepik.org/lesson/181384/step/8?unit=156009
"""

import time
from math import log, sin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def fun(x):
    return log(abs(12 * sin(float(x))))


with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button = browser.find_element(By.ID, "book")
    #  scroll to button
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #  wait for target price
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button.click()
    # get 'x' value
    x = browser.find_element(By.ID, 'input_value').text
    #  send answer
    browser.find_element(By.ID, 'answer').send_keys(fun(x))
    #  click 'submit'
    browser.find_element(By.ID, 'solve').click()
    time.sleep(5)
