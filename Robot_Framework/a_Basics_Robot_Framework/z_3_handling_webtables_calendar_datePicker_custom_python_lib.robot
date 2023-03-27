*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***

*** Keywords ***

*** Test Cases ***
Handling Webtables Calendar DatePicker CustomPythonLibrary
    open browser    https://www.espncricinfo.com/series/sa20-2022-23-1335268/points-table-standings   chrome
    set browser implicit wait    10
    maximize browser window
    wait until element is not visible    xpath://div[contains(@id,'ad-overlay')]
    @{row_count}    get webelements    //tbody/tr[@class='ds-text-tight-s']
    ${total_rows}    get length    ${row_count}
    @{column_count}    get webelements    //tbody/tr[@class='ds-text-tight-s'][1]/td
    ${total_columns}    get length    ${column_count}
    log to console  Total rows are: ${total_rows} and Total columns are: ${total_columns}
    # Printing the table data :
    FOR    ${i}    IN    @{row_count}
         ${text}    get text    ${i}
         log to console   ${text}
    END

