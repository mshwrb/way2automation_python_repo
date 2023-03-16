*** Settings ***
Library    SeleniumLibrary
*** Variables ***
# Scaler varibale
${URl}    https://www.way2automation.com/way2auto_jquery/index.php
${a}    12
# Dictionary variable
&{d}    key1=value1    key2=value2    key3=value3
# List variables
@{list}     value1    value2    value3    value4

*** Keywords ***
*** Test Cases ***
    open browser    ${URL}    chrome




