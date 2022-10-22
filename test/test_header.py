import allure
import pytest

from page.login_page import LoginPage
from utils.wrapper import screenshot_wrapper


@pytest.mark.usefixtures("driver_init")
class TestHeader:

    @pytest.fixture(autouse=True)
    def go_to_header(self, driver_init):
        self.header = LoginPage(self.driver).load().using("Admin", "admin123")


    @allure.description("Test Logout is working")
    @allure.severity(allure.severity_level.CRITICAL)
    @screenshot_wrapper
    def test_logout(self):
        self.header.logout()
        assert "/auth/login" in self.driver.current_url



