from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_link')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCTS_GRID = (By.CSS_SELECTOR, '.basket_summary')
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, 'div#content_inner > p > a')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-lg.btn-primary.btn-add-to-basket')
    ADDED_PRODUCT_TITLE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages > div.alert-info strong')
