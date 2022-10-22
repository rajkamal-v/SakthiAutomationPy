import time

import allure
import pytest

from page.header import Header
from page.login_page import LoginPage
from utils.reader import get_excel_data as GET
from utils.wrapper import screenshot_wrapper


@pytest.mark.usefixtures("driver_init")
class TestLoginPage:

    @pytest.fixture(autouse=True)
    def load_login(self, driver_init):
        self.login = LoginPage(self.driver).load()
        yield
        self.driver.delete_all_cookies()


    @allure.severity(allure.severity_level.BLOCKER)
    @screenshot_wrapper
    def test_valid_login(self):
        self.login.using("Admin", "admin123")
        assert Header(self.driver).verify_header_visible()

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.parametrize("data", GET("test_data.xlsx","login_fail"))
    @screenshot_wrapper
    def test_for_empty_field(self, data):
        self.login.using(data['username'], data['password'])
        assert self.login.get_required_field_error_text() == data['error']

    @pytest.mark.my_tag
    @allure.description("Test Login with Invalid Credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    @screenshot_wrapper
    def test_invalid_credentials(self):
            self.login.using("apple", "apple")
            assert self.login.get_error_text() == "Invalid credential"


    @allure.description("Test Forgot password link is working")
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.skip("skipping due to link not working")
    @screenshot_wrapper
    def test_forgot_password_link_is_working(self):
        self.login.click_forgot_password().wait_for_forgot_password_page()
        assert "/auth/requestPasswordResetCode" in self.driver.current_url



