from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.PARTIAL_LINK_TEXT, "basket")


class BasketLocators:
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    SUCCESS_MESSAGE_TEXT = (By.CSS_SELECTOR, '.alert:nth-of-type(1) > .alertinner > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert:nth-of-type(1) > .alertinner ')
