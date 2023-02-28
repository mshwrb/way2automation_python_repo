# Pytest is unit testing framework for python users
import pytest


# testcase in this file
def test_registration_form():
    print("Executing RegistrationForm test")


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
    print(username + "\n" + password + "\nExecuting TerminationForm test")


# testcase in this file
def test_compose_email():
    print("Executing ComposeEmail test")


# testcase in this file
def test_table_data():
    print("Executing tableData test")
