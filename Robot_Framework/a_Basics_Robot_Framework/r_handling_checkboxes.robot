*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py
Suite Teardown    Ending the Test

*** Variables ***

*** Keywords ***
Ending the Test
    close browser

*** Test Cases ***
Handling CheckBoxes List
    launching url    http://www.tizag.com/htmlT/htmlcheckboxes.php    chrome
    page should contain checkbox    (//input[@name='sports'])[4]
    select checkbox    (//input[@name='sports'])[4]
    unselect checkbox    (//input[@name='sports'])[2]
    sleep    2
    select checkbox    (//input[@name='sports'])[2]
    checkbox should not be selected    (//input[@name='sports'])[2]
    sleep    2

Handling CheckBoxes from particular section
    page should contain checkbox    (//input[@name='sports'])[4]
    @{checkboxes_list_1}    get webelements    //td//div[@class='display'][2]//input
    ${count_checkboxes_section_1}    get length    ${checkboxes_list_1}
    log to console    Total checkboxes in sectuion 1: ${count_checkboxes_section_1}

    FOR    ${checkboxe}  IN   @{checkboxes_list_1}
       select checkbox  ${checkboxe}
    END
    sleep    2


