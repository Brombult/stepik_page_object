from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def ensure_message_about_adding_is_present(self):
        product_added_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_HAS_BEEN_ADDED_ALERT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text in product_added_alert.text, \
            f'expected "{product_name.text}" product name, got "{product_added_alert.text}"'

    def ensure_product_price_is_equal_to_basket_total(self):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text == basket_total.text, \
            f'expected {product_price.text} price, got {basket_total.text}'
