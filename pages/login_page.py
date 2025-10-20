from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.register_link = page.get_by_test_id('login-page-registration-link')
        self.allert_message = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    
    def fill_login_form(self, email=None, password=None):
        if email is not None:

            self.email_input.fill(email)
            expect(self.email_input).to_have_value(email)

        if password is not None:
            self.password_input.fill(password)
            expect(self.password_input).to_have_value(password)


    def click_login_button(self):
        self.login_button.click()

    def click_register_link(self):
        self.register_link.click()

    def check_allert_message(self):
        expect(self.allert_message).to_be_visible()
        expect(self.allert_message).to_have_text('Wrong email or password')


