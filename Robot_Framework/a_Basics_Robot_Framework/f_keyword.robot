*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${options}    add_argument("--ignore-certificate-errors")
&{url_dictionary}=    qa=https://www.way2automation.com    quapps=https://app.quaapps.com    gmail=https://gmail.com

*** Keywords ***
# Argumented Keyword
launching browser
    [Arguments]    ${browserName}
    open browser    ${url_dictionary.quapps}    ${browserName}    options=${options}
    set selenium implicit wait    10 seconds
    log title


# Normal Keyword
perform login
    input text    id:txtEmailid    keshav.sharma@logixshapers.biz
    input text    id:txtPassword    Pass@123
    click element    xpath://button[normalize-space()='Sign in']
    close browser

*** Test Cases ***
First Test Case
    launching browser    chrome
    perform login

Second Test Case
    launching browser    firefox
    perform login


