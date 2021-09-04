import pytest
from .pages.product_page import ProductPage

PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
# 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


@pytest.mark.skip
@pytest.mark.parametrize('link', [PRODUCT_LINK + "?promo=offer0",
                                  PRODUCT_LINK + "?promo=offer1",
                                  PRODUCT_LINK + "?promo=offer2",
                                  PRODUCT_LINK + "?promo=offer3",
                                  PRODUCT_LINK + "?promo=offer4",
                                  PRODUCT_LINK + "?promo=offer5",
                                  PRODUCT_LINK + "?promo=offer6",
                                  pytest.param(PRODUCT_LINK + "?promo=offer7",  marks=pytest.mark.xfail),
                                  PRODUCT_LINK + "?promo=offer8",
                                  PRODUCT_LINK + "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_title = page.get_product_title()
    product_price = page.get_product_price()

    page.add_product()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket(product_title)
    page.should_be_basket_price(product_price)


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK, timeout=0)
    page.open()
    page.add_product()
    page.should_not_be_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_LINK, timeout=0)
    page.open()
    page.should_not_be_success_message_after_adding_product_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK, timeout=0)
    page.open()
    page.add_product()
    page.should_be_disappeared_success_message_after_adding_product_to_basket()
