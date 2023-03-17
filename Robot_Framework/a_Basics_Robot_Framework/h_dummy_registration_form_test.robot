*** Settings ***
Resource    Resources/registration_form.robot

*** Variables ***
${url}    https://www.way2automation.com
${registration_form_url}    https://www.way2automation.com/way2auto_jquery/index.php

*** Test Cases ***
First Test Case
    launching url    ${registration_form_url}    chrome
    input text    xpath://input[@name='name']    Keshav Sharma
    input text    css:input[name='phone']    9810023432
    input text    name:email    keshavsharma.tu@gmail.com
    select from list by value    xpath://select[@name='country']    Germany
    quiting url


#Second Test Case
#    launching url    ${registration_form_url}    firefox
#    quiting url


