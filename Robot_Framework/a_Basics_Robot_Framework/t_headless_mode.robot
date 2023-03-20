*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py
Suite Teardown    Ending the Test

*** Variables ***

*** Keywords ***
Ending the Test
    close browser

*** Test Cases ***
Handling Alerts In Headless Mode in Chrome
    launching url    https://www.way2automation.com/way2auto_jquery/alert.php#load_box    headlesschrome
    select frame    //iframe[@src='alert/simple-alert.html']
    wait until element is enabled    //button[normalize-space()='Click the button to display an alert box:']
    click element    //button[normalize-space()='Click the button to display an alert box:']
    ${alert_message}    handle alert
    log to console    ${alert_message}
    unselect frame
    click element    //a[normalize-space()='Input Alert']
    select frame    //iframe[@src='alert/input-alert.html']
    wait until element is enabled    //button[normalize-space()='Click the button to demonstrate the Input box.']
    click element    //button[normalize-space()='Click the button to demonstrate the Input box.']
    input text into alert    Keshav Sharma
    ${messages_changed}    get text    //p[@id='demo']
    log to console    ${messages_changed}
    sleep    3

Handling Alerts In Headless Mode in Firefox
    launching url    https://www.way2automation.com/way2auto_jquery/alert.php#load_box    headlessfirefox
    select frame    //iframe[@src='alert/simple-alert.html']
    wait until element is enabled    //button[normalize-space()='Click the button to display an alert box:']
    click element    //button[normalize-space()='Click the button to display an alert box:']
    ${alert_message}    handle alert
    log to console    ${alert_message}
    unselect frame
    click element    //a[normalize-space()='Input Alert']
    select frame    //iframe[@src='alert/input-alert.html']
    wait until element is enabled    //button[normalize-space()='Click the button to demonstrate the Input box.']
    click element    //button[normalize-space()='Click the button to demonstrate the Input box.']
    input text into alert    Keshav Sharma
    ${messages_changed}    get text    //p[@id='demo']
    log to console    ${messages_changed}
    sleep    3


