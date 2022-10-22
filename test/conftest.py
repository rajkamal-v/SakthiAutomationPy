import os

import allure
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    """
    can pass --browser=browser_name as command line argument
    @browser_name: chrome, firefox, edge
    """
    parser.addoption("--browser", action="store", default="chrome")

@allure.step("driver init and close")
@pytest.fixture(scope="session")
def driver_init(request, pytestconfig):
    """
    initiates the driver at the start of the session and
    destroys the driver at the end of the session
    """
    driver = get_browser_driver(pytestconfig.getoption('browser'))
    a = 10
    driver.maximize_window()


    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
        setattr(cls.obj, "x", a)

    yield driver

    driver.close()
    if driver is not None:
        driver.quit()


def get_browser_driver(browser):
    """
    @returns the driver object as per the browser
              returns chrome if given browser name not matches
    @params browser - chrome, edge, firefox
    """

    if browser == "edge":
        from selenium.webdriver.edge.service import Service
        return webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        return webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        from selenium.webdriver.chrome.service import Service
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))