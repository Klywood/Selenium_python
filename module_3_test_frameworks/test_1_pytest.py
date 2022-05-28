"""https://stepik.org/lesson/193188/step/3?unit=167629"""
import logging
import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#  disable webdriver-manager logs
logging.getLogger('WDM').setLevel(logging.NOTSET)


def registration(link):
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get(link)
        browser.implicitly_wait(1)
        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        first_name.send_keys("Homer")
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        last_name.send_keys("Simpson")
        email = browser.find_element(By.CSS_SELECTOR, ".third_class .third")
        email.send_keys("simpsons@mail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text


def test_link1():
    link = "http://suninjuly.github.io/registration1.html"
    assert registration(link) == "Congratulations! You have successfully registered!", "Error"


def test_link2():
    link = "http://suninjuly.github.io/registration2.html"
    assert registration(link) == "Congratulations! You have successfully registered!", "Error"


if __name__ == '__main__':
    pytest.main()
