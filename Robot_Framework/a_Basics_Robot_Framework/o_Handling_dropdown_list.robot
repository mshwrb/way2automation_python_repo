*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***

*** Test Cases ***
Handling Dropdown List
    launching url    https://www.wikipedia.org/    chrome
    select from list by label    name:language    Беларуская
    select from list by index    language    2
    select from list by value    language    hi
    @{elements}=    get webelements    //select[@id='searchLanguage']//option
    ${count}=    get length    ${elements}
    log to console    Total values are: ${count}
    FOR    ${element}    IN    @{elements}
#       ${text}=  get text    ${element}
       ${text}=  get element attribute    ${element}    lang
       log to console    ${text}
    END