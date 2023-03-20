*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***
${options}=

*** Test Cases ***
Handling Dropdown List
    launching url    https://www.wikipedia.org/    chrome
    @{links}    get webelements    //a
    ${link_count}    get length    ${links}
    log to console    Total link count: ${link_count}
    @{child_elements}    get webelements    //div[@class='other-projects']//a/div[@class='other-project-text']/span[1]
    ${chile_links_count}    get length    ${child_elements}
    log to console    Total links in the section are: ${chile_links_count}
    FOR    ${link}    IN    @{child_elements}
       ${text}=  get text    ${link}
       log to console    ${text}
    END


