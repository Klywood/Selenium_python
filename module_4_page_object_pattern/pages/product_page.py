from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def product_name_should_match_the_message(self):
        actual_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print(actual_name)
        name_in_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE).text
        print(name_in_message)
        assert actual_name == name_in_message

    def product_price_should_match_the_message(self):
        actual_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text
        assert actual_price == price_in_message

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message still present, but should disappear"
