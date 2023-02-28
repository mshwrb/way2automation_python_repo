# Pytest is unit testing framework for python users
import pytest
from assertpy.assertpy import assert_that

# testcase in this file
@pytest.mark.smoke
def test_registration_form():
    assert False, "forcefully failing the test"


# testcase in this file
@pytest.mark.smoke
def test_shares_section():  # function stopped execution once an assertion is failed
    assert "asdf" == "asdf"
    assert "zxcv" == "zhcv"
    assert_that("asdf").is_equal_to("asdef")
    assert_that("asdf").is_equal_to("asdf")


# testcase in this file
@pytest.mark.smoke
def test_loans_section():  # function continue execution even an assertion is failed
    assert "asdf" == "qwer"
    assert "zxcv" == "zxcv"


# testcase in this file
@pytest.mark.regression
def test_title_verification():
    expected_title = "gmail.com"
    actual_title = "gmail.com"
    assert actual_title == expected_title


# testcase in this file
@pytest.mark.smoke
def test_composeEmail():
    expected_email_name = "gurru"
    actual_email_name = "google"
    assert expected_email_name == actual_email_name, "window names are not matching"


# testcase in this file
@pytest.mark.smoke
def test_tableData():
    tableData = "Data in table Keshav Rahul Dimpy listed"
    expected_data_1 = "Rahul"
    expected_data_2 = "Jonny"
    assert expected_data_1 in tableData, "Rahul not exist in tableData"
    assert expected_data_2 in tableData, "Jonny not exist in tableData"
