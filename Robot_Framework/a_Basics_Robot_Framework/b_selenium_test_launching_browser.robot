*** Settings ***
Library    SeleniumLibrary
*** Keywords ***
*** Variables ***
*** Test Cases ***
First Test Case
    log    This is my First Test Case
    open browser    https://www.way2automation.com    chrome
    log title
    close browser
Second Test Case
    log    This is my Second test Case
