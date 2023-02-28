import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

"""
For this file before and after testfunctions certain functions,modules,session
execute which is not in this file but in conftest.py file
"""


def get_data():
    # list of tuples
    return [
        ("trainer@way2automation.com", "value_1"),
        ("java@way2automation.com", "value_2"),
        ("python@way2automation.com", "value_3")
    ]


# testcase in this file , this executes for all dataset present in above function
@pytest.mark.parametrize("username,password", get_data())
def test_login_form(username, password, get_browser):
    driver = get_browser
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    allure.attach(driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)
