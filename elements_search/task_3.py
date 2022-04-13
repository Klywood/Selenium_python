"""
https://stepik.org/lesson/138920/step/7?unit=196194
"""
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')
    for element in elements:
        element.send_keys("1")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)
