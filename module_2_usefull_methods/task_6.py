"""
https://stepik.org/lesson/184253/step/4?unit=158843
"""

import time
from math import log, sin

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def fun(x):
    return log(abs(12 * sin(float(x))))


with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    #  click on first button
    browser.find_element(By.TAG_NAME, 'button').click()
    #  click 'ok' in alert-confirm window
    browser.switch_to.alert.accept()
    time.sleep(1)
    # get 'x' value
    x = browser.find_element(By.ID, 'input_value').text
    #  send answer
    browser.find_element(By.ID, 'answer').send_keys(fun(x))
    #  click 'submit'
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(5)
