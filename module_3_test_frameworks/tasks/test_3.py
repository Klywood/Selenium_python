

"""https://stepik.org/lesson/237240/step/2?unit=209628"""

import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
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
    print(res)
    browser.quit()


class TestLinks:
    global res

    lessons = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']

    @pytest.mark.parametrize('lesson', lessons)
    def test_link(self, browser, lesson):
        global res
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.get(link)
        browser.implicitly_wait(5)
        #  send result
        result_form = browser.find_element(By.TAG_NAME, "textarea")
        result_form.send_keys(str(math.log(int(time.time()))))
        #  click submit
        submit = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
        submit.click()

        answer = WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'smart-hints__hint')))
        ans_text = answer.text

        if ans_text != 'Correct!':
            res += ans_text
        assert ans_text == 'Correct!'


if __name__ == '__main__':
    pytest.main()
