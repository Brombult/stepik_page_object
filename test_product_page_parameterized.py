import pytest

from pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{number}" for number in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_cart(browser, link):
    prod_page = ProductPage(browser, link, timeout=10)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.ensure_message_about_adding_is_present()
    prod_page.ensure_product_price_is_equal_to_basket_total()
