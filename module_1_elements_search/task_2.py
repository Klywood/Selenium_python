"""
https://stepik.org/lesson/138920/step/5?unit=196194
"""
import time
import math

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
    link_1 = 'http://suninjuly.github.io/find_link_text'
    browser.get(link_1)

    l_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    link_2 = browser.find_element(By.LINK_TEXT, l_text)
    time.sleep(5)
    link_2.click()

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(60)
