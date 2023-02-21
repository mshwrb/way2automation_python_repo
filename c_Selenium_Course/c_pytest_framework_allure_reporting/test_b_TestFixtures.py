# Pytest is unit testing framework for python users


# run before all testcases in this file
def setup_module(module):
    print("open DB connection")


# run before each testcase in this file
def setup_function(function):
    print("launch browser")


# testcase in this file
def test_registration_form():
    print("Executing RegistrationForm test")


# testcase in this file
def test_termination_form():
    print("Executing TerminationForm test")


# run after each testcase in this file
def teardown_function(function):
    print("close browser")


# run after all testcases in this file
def teardown_module(module):
    print("close DB connection")
