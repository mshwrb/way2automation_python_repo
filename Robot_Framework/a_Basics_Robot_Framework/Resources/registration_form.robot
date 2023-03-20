*** Settings ***
Library     SeleniumLibrary
Variables   locators.py


*** Keywords ***
# Argumented Keyword
launching url
    [Arguments]    ${url}    ${browserName}
    open browser    ${url}    ${browserName}
    set selenium implicit wait    10 seconds
    maximize browser window
    log title

filling Registration form
    input text    ${name}    Keshav Sharma
    input text    ${phone}    9810023432
    ${random}=    evaluate    random.randint(5000,99999)
    ${emailnew}=    catenate    ${random}    __2_ @way2automation.com
    ${email_id}=    evaluate    '${emailnew}'.replace(' ','_')
    input text    ${email}    ${email_id}
    select from list by value    ${country}    Germany
    input text    ${city}    Delhi
    input text    ${username}    Keshav Sharma
    input text    ${password}    asdfgghjhj
    click button    ${submit_btn}

got to Registration form page
    click element    xpath://div[@id='load_box']//a[@class='fancybox'][normalize-space()='ENTER TO THE TESTING WEBSITE']
    scroll element into view    xpath://img[@alt='registration']
    click element    xpath://h2[normalize-space()='Registration']
    @{window_handles}=    get window handles
    log to console    ${window_handles}
    switch window    ${window_handles}[1]


fill new page registration form
    input text    xpath://fieldset[@class='fieldset']//input[@name='name']    Keshav
    input text    xpath:(//input[@type='text'])[2]    Sharma
    click element    xpath://label[normalize-space()='Single']
    click element    xpath://label[normalize-space()='Cricket']
    select from list by value    xpath://form[@id='register_form']/fieldset/select[1]    India
    select from list by label    xpath:(//select)[2]    1
    select from list by index    xpath:(//select)[3]    1
    select from list by value    xpath:(//select)[4]    2014
    input text    xpath://fieldset[@class='fieldset']//input[@name='phone']    12335425232
    input text    xpath://fieldset[@class='fieldset']//input[@name='username']    Keshav
    input text    xpath://fieldset[@class='fieldset']//input[@name='email']    keshavsharma@gmail.com
    choose file   xpath://input[@type='file']    C:/Users/User/Desktop/responsive_issue.png


quiting url
    close browser