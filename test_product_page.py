import time

import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    prod_page = ProductPage(browser, PRODUCT_LINK)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.ensure_success_message_is_present()
    prod_page.ensure_product_price_is_equal_to_basket_total()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    prod_page = ProductPage(browser, PRODUCT_LINK)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.ensure_success_message_is_not_present()


def test_guest_cant_see_success_message(browser):
    prod_page = ProductPage(browser, PRODUCT_LINK)
    prod_page.open()
    prod_page.ensure_success_message_is_not_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_cart(browser):
    prod_page = ProductPage(browser, PRODUCT_LINK)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.ensure_success_message_has_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.ensure_basket_is_empty()
    basket.ensure_no_products_in_basket()


class TestUserAddToCartFromProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "pass"
        page = LoginPage(self.browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        prod_page = ProductPage(self.browser, PRODUCT_LINK)
        prod_page.open()
        prod_page.ensure_success_message_is_not_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self):
        prod_page = ProductPage(self.browser, PRODUCT_LINK)
        prod_page.open()
        prod_page.add_product_to_basket()
        prod_page.solve_quiz_and_get_code()
        prod_page.ensure_success_message_is_present()
        prod_page.ensure_product_price_is_equal_to_basket_total()
