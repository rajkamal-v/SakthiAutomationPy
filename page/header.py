from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.__header_userarea = By.CLASS_NAME, "oxd-topbar-header-userarea"
        self.__username = By.CLASS_NAME, "oxd-userdropdown-name"
        self.__logout_menu = By.CSS_SELECTOR, "a[href$='logout']"

    def verify_header_visible(self):
        return self.is_element_visible(self.__header_userarea)

    def view_header_menu(self):
        self.click(self.__username)

    def logout(self):
        self.view_header_menu()
        self.click(self.__logout_menu)
        self.wait_for_url(self.base_url+"/auth/login")