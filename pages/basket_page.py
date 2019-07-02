from pages.base_page import BasePage
from pages.locators import BasketLocators


class BasketPage(BasePage):

    def ensure_basket_is_empty(self):
        basket_is_empty_message = self.browser.find_element(*BasketLocators.BASKET_IS_EMPTY_MESSAGE).text
        assert 'Your basket is empty' in basket_is_empty_message, \
            f'expected "Your basket is empty", got {basket_is_empty_message}'

    def ensure_no_products_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_ITEMS)