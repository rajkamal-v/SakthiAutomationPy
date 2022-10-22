import allure
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = "https://opensource-demo.orangehrmlive.com/web/index.php"


    def find_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))


    def click(self, locator):
        self.find_element(locator).click()


    def input(self, locator, text):
        self.find_element(locator).send_keys(text)


    def is_element_visible(self, locator):
        return self.find_element(locator).is_displayed()


    def get_text(self, locator):
        return self.find_element(locator).text


    def wait_for_url(self, url):
        self.wait.until(ec.url_to_be(url))
