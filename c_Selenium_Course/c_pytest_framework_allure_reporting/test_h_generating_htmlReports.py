# Pytest is unit testing framework for python users
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


"""
13. For Html reports generation
    https://pypi.org/project/pytest-html/
    pip install pytest-html
    [pytest --html=test_reports.html]
"""

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


# testcase in this file , this executes for all dataset present in above function
@pytest.mark.parametrize("username,password", get_data())
def test_termination_form(username, password):
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
