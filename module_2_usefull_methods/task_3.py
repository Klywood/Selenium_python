
"""
https://stepik.org/lesson/228249/step/3?unit=200781
"""

import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
    browser.get("http://suninjuly.github.io/selects2.html")
    #  count sum
    res = int(browser.find_element(By.ID, 'num1').text) + int(browser.find_element(By.ID, 'num2').text)
    #  select element with counted sum
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))
    #  click submit button
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(5)
