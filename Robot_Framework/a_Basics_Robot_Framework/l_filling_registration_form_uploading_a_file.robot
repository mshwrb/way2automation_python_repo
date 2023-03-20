*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***
${url}    https://www.way2automation.com
${registration_form_url}    https://www.way2automation.com/way2auto_jquery/index.php

*** Test Cases ***
First Test Case
    launching url    ${registration_form_url}    chrome
    filling Registration form
    got to Registration form page
    fill new page registration form
    sleep    5s
    close window
    quiting url


#Second Test Case
#    launching url    ${registration_form_url}    firefox
#    quiting url


