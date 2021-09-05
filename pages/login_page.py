from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.send_keys_in_element(*LoginPageLocators.REGISTRATION_EMAIL, email)
        self.send_keys_in_element(*LoginPageLocators.REGISTRATION_PASSWORD1, password)
        self.send_keys_in_element(*LoginPageLocators.REGISTRATION_PASSWORD2, password)
        self.click_element(*LoginPageLocators.REGISTRATION_BUTTON)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'URL does not contain "login"'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'
