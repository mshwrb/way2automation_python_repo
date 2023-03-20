*** Settings ***
Resource    Resources/registration_form.robot
Variables    Resources/locators.py

*** Variables ***

*** Keywords ***

*** Test Cases ***
Handling Sliders
    launching url    https://jqueryui.com/resources/demos/slider/default.html   chrome
    wait until element is visible    //span[@class='ui-slider-handle ui-corner-all ui-state-default']
    drag and drop by offset    //span[@class='ui-slider-handle ui-corner-all ui-state-default']    200    0
    sleep    1
    close browser

Handling Sliders By Length
    launching url    https://jqueryui.com/resources/demos/slider/default.html   chrome
    wait until element is visible    //span[@class='ui-slider-handle ui-corner-all ui-state-default']
    @{slide_bar_size}    get element size    //div[@id='slider']
    log to console    ${slide_bar_size}[0]
    drag and drop by offset    //span[@class='ui-slider-handle ui-corner-all ui-state-default']    ${${${slide_bar_size}[0] - 1}/2}    0
    sleep    1
    close browser




