*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***
${url}    https://www.way2automation.com
${registration_form_url}    https://www.way2automation.com/way2auto_jquery/index.php


*** Test Cases ***
First Test Case
    launching url    ${registration_form_url}    chrome
     input text    ${name}    Keshav Sharma
    input text    ${phone}    9810023432
    ${random}=    evaluate    random.randint(5000,99999)
    ${emailnew}=    catenate    ${random}    __2_ @way2automation.com
    ${email_id}=    evaluate    '${emailnew}'.replace(' ','_')
    input text    ${email}    ${email_id}
    select from list by value    ${country}    Germany
    input text    ${city}    Delhi
    input text    ${username}    Keshav Sharma
    input text    ${password}    asdfgghjhj
    click button    ${submit_btn}
    sleep    5s
    quiting url


#Second Test Case
#    launching url    ${registration_form_url}    firefox
#    quiting url


