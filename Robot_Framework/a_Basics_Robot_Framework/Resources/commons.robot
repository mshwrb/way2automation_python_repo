*** Settings ***
Library     SeleniumLibrary

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