import pytest
from selenium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# run before each testcase in this file
@pytest.fixture(scope="session")  # function/class/session/module
def chrome_browser():
    global driver
    driver = webdriver.Chrome()  # launching browser
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


# run before each testcase in this file
@pytest.fixture(params=["chrome","firefox"],scope="function")
def get_browser(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()  # launching browser
    if request.param == "firefox":
        driver = webdriver.Firefox()

    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    yield driver
    driver.quit()