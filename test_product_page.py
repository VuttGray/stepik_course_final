from .pages.product_page import ProductPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    product_title = page.get_product_title()
    product_price = page.get_product_price()

    page.add_product()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket(product_title)
    page.should_be_basket_price(product_price)
