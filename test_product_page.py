import pytest

from pages.product_page import ProductPage

PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


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


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_login_page()
