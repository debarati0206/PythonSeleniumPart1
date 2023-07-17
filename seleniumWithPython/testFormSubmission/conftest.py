
from selenium import webdriver

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        obj = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=obj)
    elif browser_name == "edge":
        obj = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=obj)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    # return driver
    # yield
    # driver.close() ---this will not work ->return before yield
    request.cls.driver = driver
    yield
    driver.close()
