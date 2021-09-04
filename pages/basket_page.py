from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    pass

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_GRID), \
            'Products are presented, but should not be'

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), \
            'Message about empty basket is not presented, but should be'
