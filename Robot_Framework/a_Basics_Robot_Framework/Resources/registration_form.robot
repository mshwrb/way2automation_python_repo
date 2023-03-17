*** Settings ***
Library     SeleniumLibrary


*** Keywords ***
# Argumented Keyword
launching url
    [Arguments]    ${url}    ${browserName}
    open browser    ${url}    ${browserName}
    set selenium implicit wait    10 seconds
    maximize browser window
    log title

quiting url
    close browser