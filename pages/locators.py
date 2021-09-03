from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    ADDED_PRODUCT_TITLE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages > div.alert-info strong')
