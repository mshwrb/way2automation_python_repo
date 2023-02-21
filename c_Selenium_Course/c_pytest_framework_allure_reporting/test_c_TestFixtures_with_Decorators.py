# Pytest is unit testing framework for python users
import pytest


@pytest.fixture(scope='module')  # run before all test cases in this file
def Module():
    print("open DB connection")

    yield  # run after all test cases in this file
    print("close DB connection")


@pytest.fixture(scope='function')  # run before each test case in this file
def Function():
    print("launch browser")

    yield  # run after each test case in this file
    print("close browser")


# testcase in this file
def test_registration_form(Module, Function):
    print("Executing RegistrationForm test")


# testcase in this file
@pytest.mark.usefixtures("Module", "Function")
def test_termination_form():
    print("Executing TerminationForm test")
