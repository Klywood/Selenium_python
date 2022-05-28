
"""https://stepik.org/lesson/36285/step/13?unit=162401"""
import logging
import unittest
import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#  disable webdriver-manager logs
logging.getLogger('WDM').setLevel(logging.NOTSET)

def get_result(link):
    with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
        browser.get(link)
        # name
        f_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]')
        f_name.send_keys("Name")
        # surname
        surname = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        surname.send_keys("Surname")
        # e-mail
        mail = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        mail.send_keys("my@mail.ru")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # возвращаем текст элемента
        return welcome_text_elt.text


class TestAbs(unittest.TestCase):

    def test_abs1(self):
        res = get_result("http://suninjuly.github.io/registration1.html")
        self.assertEqual("Congratulations! You have successfully registered!", res)

    def test_abs2(self):
        res = get_result("http://suninjuly.github.io/registration2.html")
        self.assertEqual("Congratulations! You have successfully registered!", res)


if __name__ == "__main__":
    # unittest.main()
    pytest.main()
