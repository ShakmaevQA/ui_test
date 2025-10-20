import playwright
import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture(scope='session')
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    input_email = page.get_by_test_id('registration-form-email-input').locator('input')
    input_email.fill('user.name@gmail.com')

    input_username = page.get_by_test_id('registration-form-username-input').locator('input')
    input_username.fill('username')

    input_password = page.get_by_test_id('registration-form-password-input').locator('input')
    input_password.fill('password')

    button_register = page.get_by_test_id('registration-page-registration-button')
    button_register.click()

    context.storage_state(path='byba.json')
    browser.close()


@pytest.fixture(scope='session')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='byba.json')
    page = context.new_page()
    yield page
    browser.close()