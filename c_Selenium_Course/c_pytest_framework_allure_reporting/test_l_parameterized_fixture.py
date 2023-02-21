# Pytest is unit testing framework for python users

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)


# run before each testcase in this file
def setup_function(function):
    global driver
    driver = webdriver.Chrome()  # launching browser
    driver.get("https://www.facebook.com/")
    driver.maximize_window()


# run after each testcase in this file
def teardown_function(function):
    driver.quit()


def get_data():
    # list of tuples
    return [
        ("trainer@way2automation.com", "value_1"),
        ("java@way2automation.com", "value_2"),
        ("python@way2automation.com", "value_3")
    ]

# testcase in this file
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.smoke
def test_loans_section():  # function continue execution even an assertion is failed
    assert "asdf" == "qwer"
    assert "zxcv" == "zxcv"

# testcase in this file , this executes for all dataset present in above function
@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username,password", get_data())
def test_login_form(username, password):
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)

