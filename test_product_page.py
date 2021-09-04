import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
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


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK, timeout=0)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_message_about_empty_basket()
