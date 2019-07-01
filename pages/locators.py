from selenium.webdriver.common.by import By


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    PRODUCT_HAS_BEEN_ADDED_ALERT = (By.CSS_SELECTOR, '.alert:nth-of-type(1) > .alertinner > strong')