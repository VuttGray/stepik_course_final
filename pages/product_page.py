from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_title(self):
        return self.get_element_text(*ProductPageLocators.PRODUCT_TITLE)

    def get_product_price(self):
        return self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)

    def add_product(self):
        self.click_element(*ProductPageLocators.ADD_PRODUCT_BUTTON)

    def should_be_product_added_to_basket(self, title: str):
        self.should_be_success_message_after_adding_product_to_basket()
        added_product_message = self.get_element_text(*ProductPageLocators.ADDED_PRODUCT_TITLE)
        assert title == added_product_message, 'Basket message does not contain the product title'

    def should_be_basket_price(self, price):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), \
            'Basket total price is not presented, but should be'
        basket_price = self.get_element_text(*ProductPageLocators.BASKET_PRICE)
        assert price == basket_price, 'Basket total price is not equal to the added product price'

    def should_be_success_message_after_adding_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_TITLE), \
            'Success message is not presented, but should be'

    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_TITLE), \
            'Success message is presented, but should not be'

    def should_be_disappeared_success_message_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_TITLE), \
            'Success message is still presented, but should be disappeared'
