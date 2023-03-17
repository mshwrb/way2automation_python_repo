*** Settings ***
Library    SeleniumLibrary
*** Keywords ***
# Scaler variables or Simple variables with global scope
*** Variables ***
${value_1}    100
${value_2}    200
${name}    Keshav
${floatValue}    10.092
${browser}    chrome
${options}    options=add_argument("--ignore-certificate-errors")
${env}    qa

# List variables    @{list_vars}=    10    20    Keshav    12.434
@{list_vars}=    10    20    Keshav    12.434    Delhi    Goa

# Dictionary Variables &{dictionary_vars}=    key=value    key=value
&{url_dictionary}=    qa=https://www.way2automation.com    quaps=https://app.quaapps.com    gmail=https://gmail.com

*** Test Cases ***
First Test Case
    log    ${value_1}
    log    ${name}
    log    ${floatValue}
    log    ${browser}
    log    ${options}
    log    ${${value_1} + ${value_2}}
    log    ${value_1} ${value_2} ${name}
    log    ${list_vars}[0] ${list_vars}[4]
    log    ${url_dictionary.qa} ${url_dictionary.quaps} ${url_dictionary.gmail}
    open browser    ${url_dictionary.${env}}    ${browser}
