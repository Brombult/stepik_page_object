import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

MAIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/'


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.ensure_basket_is_empty()
    basket.ensure_no_products_in_basket()


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_link(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, MAIN_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_link()
