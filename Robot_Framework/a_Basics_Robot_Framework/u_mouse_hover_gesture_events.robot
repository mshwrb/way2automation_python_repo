*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py
Suite Teardown    Ending the Test

*** Variables ***

*** Keywords ***
Ending the Test
    close browser

*** Test Cases ***
Handling Mouse Hover Menues
    launching url    https://www.way2automation.com   chrome
    wait until element is visible    //li[@id='menu-item-27617']//span[@class='menu-text'][normalize-space()='Resources']
    mouse over    //li[@id='menu-item-27617']//span[@class='menu-text'][normalize-space()='Resources']
    click element    //li[@id='menu-item-27618']//span[@class='menu-text'][normalize-space()='Practice Site 1']
    sleep    3



