import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import logging

#  disable webdriver-manager logs
logging.getLogger('WDM').setLevel(logging.NOTSET)
res = ''


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print("\nquit browser..")
    browser.quit()
