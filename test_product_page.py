from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.ensure_message_about_adding_is_present()
    prod_page.ensure_product_price_is_equal_to_basket_total()
