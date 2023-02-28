# Pytest is unit testing framework for python users
import pytest


# testcase in this file
@pytest.mark.smoke
def test_registration_form():
    print("Executing RegistrationForm test")


# testcase in this file
@pytest.mark.regression
def test_termination_form():
    print("Executing TerminationForm test")


# testcase in this file
@pytest.mark.smoke
def test_compose_email():
    print("Executing ComposeEmail test")


# testcase in this file
@pytest.mark.smoke
@pytest.mark.skip
def test_table_data():
    print("Executing tableData test")
