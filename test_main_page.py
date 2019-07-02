from pages.main_page import MainPage
from pages.basket_page import BasketPage

MAIN_PAGE_LINK = 'http://selenium1py.pythonanywhere.com/en-gb/'


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.ensure_basket_is_empty()
    basket.ensure_no_products_in_basket()
