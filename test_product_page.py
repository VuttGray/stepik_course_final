from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.urls import Urls
import pytest
import random
import string


def string_generator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, Urls.LOGIN_LINK)
        login_page.open()

        email = 'test_user_' + string_generator(6) + "@test-mail.org"
        password = string_generator(12)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        yield
        login_page.logout()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, Urls.get_product_link(Urls.PRODUCT_207))
        page.open()
        product_title = page.get_product_title()
        product_price = page.get_product_price()

        page.add_product()
        page.should_be_product_added_to_basket(product_title)
        page.should_be_basket_price(product_price)

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, Urls.get_product_link(Urls.PRODUCT_207), timeout=0)
        page.open()
        page.should_not_be_success_message_after_adding_product_to_basket()


@pytest.mark.parametrize('link', [Urls.get_product_link(Urls.PRODUCT_207, "offer0"),
                                  Urls.get_product_link(Urls.PRODUCT_207, "offer1"),
                                  Urls.get_product_link(Urls.PRODUCT_207, "offer2"),
                                  Urls.get_product_link(Urls.PRODUCT_207, "offer3"),
                                  Urls.get_product_link(Urls.PRODUCT_207, "offer4"),
                                  Urls.get_product_link(Urls.PRODUCT_207, "offer5"),
                                  Urls.get_product_link(Urls.PRODUCT_207, "offer6"),
                                  pytest.param(Urls.get_product_link(Urls.PRODUCT_207, "offer7"),
                                               marks=pytest.mark.xfail),
                                  Urls.get_product_link(Urls.PRODUCT_207, "offer8"),
                                  Urls.get_product_link(Urls.PRODUCT_207, "offer9")])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    product_title = page.get_product_title()
    product_price = page.get_product_price()

    page.add_product()
    page.solve_quiz_and_get_code()
    page.should_be_product_added_to_basket(product_title)
    page.should_be_basket_price(product_price)


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, Urls.get_product_link(Urls.PRODUCT_95))
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Urls.get_product_link(Urls.PRODUCT_207), timeout=0)
    page.open()
    page.should_not_be_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Urls.get_product_link(Urls.PRODUCT_207), timeout=0)
    page.open()
    page.add_product()
    page.should_not_be_success_message_after_adding_product_to_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, Urls.get_product_link(Urls.PRODUCT_207), timeout=0)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_message_about_empty_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Urls.get_product_link(Urls.PRODUCT_95))
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Urls.get_product_link(Urls.PRODUCT_207), timeout=0)
    page.open()
    page.add_product()
    page.should_be_disappeared_success_message_after_adding_product_to_basket()
