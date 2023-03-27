*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***

*** Keywords ***

*** Test Cases ***
Handling Resizable Elements
    launching url    https://jqueryui.com/resources/demos/resizable/default.html   chrome
    wait until element is visible    //div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']
    drag and drop by offset    //div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']    400    400






