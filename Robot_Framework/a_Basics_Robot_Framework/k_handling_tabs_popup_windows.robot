*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***
${url}    https://www.way2automation.com
${registration_form_url}    https://www.way2automation.com/way2auto_jquery/index.php

*** Test Cases ***
First Test Case
    launching url    ${registration_form_url}    chrome
    filling Registration form
    click element    xpath://div[@id='load_box']//a[@class='fancybox'][normalize-space()='ENTER TO THE TESTING WEBSITE']
    scroll element into view    xpath://img[@alt='registration']
    click element    xpath://h2[normalize-space()='Registration']
    @{window_handles}=    get window handles
    log to console    ${window_handles}
    switch window    ${window_handles}[1]
    input text    xpath://fieldset[@class='fieldset']//input[@name='name']    Testing
    sleep    2s
    close window
    switch window    ${window_handles}[0]
    close window
    quiting url


#Second Test Case
#    launching url    ${registration_form_url}    firefox
#    quiting url


