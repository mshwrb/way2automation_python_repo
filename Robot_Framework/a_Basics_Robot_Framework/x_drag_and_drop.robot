*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***

*** Keywords ***

*** Test Cases ***
Handling Drag and Drop Elements
    launching url    https://jqueryui.com/resources/demos/droppable/default.html   chrome
    wait until element is visible    id:draggable
    drag and drop    id:draggable    id:droppable
    sleep    1






