import pytest

from fixtures.pages import dashboard_page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

class TestSuccessfulRegistration:
    @pytest.mark.regression
    @pytest.mark.registration
    def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.open('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
        registration_page.fill_register_form(email='user.name@gmail.com',
                                                 username='username',
                                                 password='password'
                                                 )
        registration_page.click_register_button()

        dashboard_page.check_visible_title()
        