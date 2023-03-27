*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***

*** Keywords ***

*** Test Cases ***
Handling Javascript Execution
    open browser    https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onclick   chrome    options=add_argument("--ignore-certificate-errors")
    set browser implicit wait    10
    maximize browser window
    select frame    xpath://iframe[@id='iframeResult']
    execute javascript    myFunction()
    sleep    2

Handling Javascript Execution Custom
    open browser    https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onclick   chrome    options=add_argument("--ignore-certificate-errors")
    set browser implicit wait    10
    maximize browser window
    select frame    xpath://iframe[@id='iframeResult']
    ${web_ele}    get webelement    //button[normalize-space()='Click me']
    execute javascript    arguments[0].style.border='1px solid green'    ARGUMENTS    ${web_ele}
    sleep    2






