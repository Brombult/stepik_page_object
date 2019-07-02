from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    SUCCESS_MESSAGE_TEXT = (By.CSS_SELECTOR, '.alert:nth-of-type(1) > .alertinner > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-of-type(1) > .alertinner ')
