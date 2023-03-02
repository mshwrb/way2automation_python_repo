from behave import *
from behave import use_step_matcher
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


use_step_matcher('parse')

@given("I navigate to google.com")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.get("https://www.google.com/")
    print("I navigate to google.com")



@when("I Validate the Page title")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    title = context.driver.title
    assert title == "Google"
    print(title)
    print("I Validate the Page title")


@step("I click the search button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)
    print("And I click the search button")


@then('I enter the text as "{search_text}"')
def step_impl(context, search_text):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element(By.NAME, "q").send_keys(search_text)
    print(f"The entered text is {search_text}")




