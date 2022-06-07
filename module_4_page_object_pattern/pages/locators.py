from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, '.basket-mini .btn-group > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name=registration-email]")
    REGISTER_PASSW = (By.CSS_SELECTOR, "[name=registration-password1]")
    REGISTER_PASSW_CONFIRM = (By.CSS_SELECTOR, "[name=registration-password2]")
    REG_BUTTON = (By.CSS_SELECTOR, '[value=Register]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(3) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
