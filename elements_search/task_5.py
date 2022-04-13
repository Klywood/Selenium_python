"""
https://stepik.org/lesson/138920/step/11?unit=196194
"""
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
    links = ["http://suninjuly.github.io/registration1.html",
             "http://suninjuly.github.io/registration2.html"]

    for link in links:
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
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
