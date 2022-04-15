
"""
https://stepik.org/lesson/228249/step/8?unit=200781
"""

import time
import os

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'to_send.txt')


with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    #  inputs
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']").send_keys('Name')
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter last name']").send_keys('Name')
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter email']").send_keys('e@mail.com')
    #  attaching the file
    browser.find_element(By.ID, "file").send_keys(file_path)
    #  click submit
    browser.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)

