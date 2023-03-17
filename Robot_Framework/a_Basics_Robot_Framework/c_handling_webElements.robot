*** Settings ***
Library    SeleniumLibrary
*** Keywords ***
*** Variables ***
*** Test Cases ***
First Test Case
    log    This is my First Test Case
    open browser    https://app.quaapps.com    chrome    options=add_argument("--ignore-certificate-errors")
    log title
    input text    id:txtEmailid    keshav.sharma@logixshapers.biz
    input text    id:txtPassword    Pass@123
    click element    xpath://button[normalize-space()='Sign in']
    close browser
Second Test Case
    log    This is my First Test Case
    open browser    https://gmail.com    chrome
    log title
    input text    id:identifierId    keshav.sharma@logixshapers.biz
    close browser
