"""
https://stepik.org/lesson/165493/step/7?unit=140087
"""

import math
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
    link = "http://suninjuly.github.io/get_attribute.html"

    browser.get(link)
    # get number
    number = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    # calc result
    result = calc(number)
    # input answer
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(result)

    #  click on checkbox and radiobutton
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    #  click submit
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    time.sleep(5)
