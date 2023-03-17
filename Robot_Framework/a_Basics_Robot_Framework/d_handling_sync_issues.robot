*** Settings ***
Library    SeleniumLibrary
*** Keywords ***
*** Variables ***
*** Test Cases ***
First Test Case
    log    This is my First Test Case
    open browser    https://app.quaapps.com    chrome    options=add_argument("--ignore-certificate-errors")
    set selenium implicit wait    10 seconds
    log title
    wait until element is visible  txtEmailid
    input text    id:txtEmailid    keshav.sharma@logixshapers.biz
    wait until keyword succeeds  5x    2s    input text    id:txtPassword    Pass@123
    click element    xpath://button[normalize-space()='Sign in']
    ${dashboard_text}=  get text    //h1[normalize-space()='WELCOME TO DASHBOARD']
    close browser
Second Test Case
    log    This is my First Test Case
    open browser    https://gmail.com    firefox
    set selenium implicit wait    10 seconds
    log title
    input text    id:identifierId    keshav.sharma@gmail.com
    click element    //*[@id="identifierNext"]/div/button/span
    close browser
