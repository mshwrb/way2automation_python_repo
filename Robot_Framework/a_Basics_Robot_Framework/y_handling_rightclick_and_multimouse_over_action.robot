*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***

*** Keywords ***

*** Test Cases ***
Handling Drag and Drop Elements
    launching url    https://deluxe-menu.com/popup-mode-sample.html   chrome
    wait until element is visible    xpath://img[@src='data-samples/images/popup_pic.gif']
    open context menu    //img[@src='data-samples/images/popup_pic.gif']
    mouse over    id:dm2m1i1tdT
    mouse over    id:dm2m2i1tdT
    click element    id:dm2m3i0tdT
    sleep    5






