import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        obj = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=obj)  # when driver is declared global it'll not create any new driver object
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


# code to generate screenshot in case of test failure


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)  # to access driver after closing in line 35 , make driver global
