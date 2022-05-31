r"""
https://stepik.org/lesson/237240/step/9?unit=209628

To RUN test:
    pytest --language=fr test_items.py

Проверь, что находишься в текущей директории, если найходишься
в корне можно перейти в каталог с заданием с помощью команды:
    cd .\module_3_test_frameworks\tasks\

или запустить тест из корня:
    pytest --language=es .\module_3_test_frameworks\tasks\test_items.py """

import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_basket_button_exists(browser):
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form > button")
    #  проверяем, что кнопка есть
    assert len(button) == 1, 'Button does not exist'
    # Раскоменти, чтобы проверить с language=fr
    # time.sleep(30)
