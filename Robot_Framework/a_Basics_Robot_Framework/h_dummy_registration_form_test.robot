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
    input text    xpath://input[@name='city']    Delhi
    input text    xpath://div[@id='load_box']//input[@name='username']    Keshav Sharma
    input text    xpath://div[@id='load_box']//input[@name='password']    asdfgghjhj
    click button    xpath://div[@id='load_box']//input[@value='Submit']
    sleep    2s
    quiting url


#Second Test Case
#    launching url    ${registration_form_url}    firefox
#    quiting url


