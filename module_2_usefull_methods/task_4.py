"""
https://stepik.org/lesson/228249/step/6?unit=200781
"""

import time
from math import log, sin

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


def calc(x):
    return log(abs(12 * sin(x)))


with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    #  get x
    x = int(browser.find_element(By.ID, "input_value").text)

    #  input answer (with scrolling)
    ans_field = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", ans_field)
    ans_field.send_keys(calc(x))
    #  radiobutton and checkbox
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.ID, 'robotCheckbox').click()
    #  click submit
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    time.sleep(5)
