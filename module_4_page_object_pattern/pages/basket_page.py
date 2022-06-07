from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_text_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
            'No text that basket is empty!'

    def should_basket_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), \
            'Basket is not empty!'
