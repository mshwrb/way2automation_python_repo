*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***
${options}=

*** Test Cases ***
Handling Dropdown List
    open browser    https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_submit    chrome    options=add_argument("--ignore-certificate-errors")
    set browser implicit wait    10
    maximize browser window
    wait until element is enabled   //iframe
    ${frames}    get webelements    //iframe
    ${count}=    get length    ${frames}
    log to console    ${count}

    select frame    //iframe[@id='iframeResult']
    wait until element is visible  //input[@value='Submit']
    click element    //input[@value='Submit']
    sleep    1
    ${message}    get text  //p[contains(text(),'The server has processed your input and returned t')]
    unselect frame
    log to console    ${message}
