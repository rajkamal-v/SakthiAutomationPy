from page.base_page import BasePage


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = self.base_url+"/auth/requestPasswordResetCode"

    def wait_for_forgot_password_page(self):
        self.wait_for_url(self.page_url)