
"""
https://stepik.org/lesson/237240/step/6?unit=209628
https://stepik.org/lesson/237240/step/7?unit=209628
"""

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")

#  pytest -s -v --browser_name=firefox test_parser.py
'''With reruns'''
# pytest -v --tb=line --reruns 1 --browser_name=chrome test_parser.py
