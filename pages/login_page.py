from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, f'Not a login page, got {self.browser.current_url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), 'No login username'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), 'No login password'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_USERNAME), 'No register username'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), 'No register password'
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), 'No register confirm password'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_USERNAME).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()


