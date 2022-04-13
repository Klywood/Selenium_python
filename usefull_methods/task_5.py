
"""
https://stepik.org/lesson/228249/step/8?unit=200781
"""

import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select



with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as browser:
    link = "https://yandex.ru/images/search?from=tabbar&text=%D0%B0%D0%B2%D0%B8%D1%82%D0%BE"
    browser.get(link)

