"""
https://stepik.org/lesson/184253/step/6?unit=158843
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
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    #  click on button
    browser.find_element(By.TAG_NAME, 'button').click()
    #  switch to new window
    browser.switch_to.window(browser.window_handles[1])
    # get 'x' value
    x = browser.find_element(By.ID, 'input_value').text
    #  send answer
    browser.find_element(By.ID, 'answer').send_keys(fun(x))
    #  click 'submit'
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(5)
