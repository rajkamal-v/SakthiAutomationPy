import allure
import pytest

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.forgot_password_page import ForgotPasswordPage
from page.header import Header



class LoginPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = self.base_url+"/auth/login"
        self.__username_tb = By.NAME, "username"
        self.__password_tb = By.NAME, "password"
        self.__login_btn = By.TAG_NAME, "button"
        self.__error_txt = By.CSS_SELECTOR, "[role='alert'] p"
        self.__empty_field_errors_txt = By.CLASS_NAME, "oxd-input-field-error-message"
        self.__forgot_password_link = By.CLASS_NAME, "orangehrm-login-forgot-header"


    def load(self):
        self.driver.get(self.base_url)
        return self

    def using(self, username, password):
        return self.input_username(username).input_password(password).click_login()

    @allure.step("Input username")
    def input_username(self, username):
        self.input(self.__username_tb, username)
        return self

    @allure.step("Input password")
    def input_password(self, password):
        self.input(self.__password_tb, password)
        return self

    def click_login(self):
        self.click(self.__login_btn)
        return Header(self.driver)


    def get_error_text(self):
        return self.get_text(self.__error_txt)

    def get_required_field_error_text(self):
        return self.get_text(self.__empty_field_errors_txt)

    def click_forgot_password(self):
        self.click(self.__forgot_password_link)
        return ForgotPasswordPage(self.driver)




