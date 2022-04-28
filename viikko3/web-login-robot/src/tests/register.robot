*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application And Go To Register Page


*** Test Cases ***
Register New User With Valid Username And Password
    Set Username  qwertyui
    Set Password  kalle123
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  q
    Set Password  kalle123
    Submit Register
    Register Should Succeed
    

Register With Valid Username And Too Short Password
    Set Username  q12345678
    Set Password  k
    Submit Register
    Register Should Succeed

Register With Nonmatching Password And Password Confirmation
    Set Username  q12345555
    Set Password  kkkkkkkkk
    Create Failed User  uusiuusi  eitoimi
    Submit Register
    Register Should Succeed


*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Register Page Should Be Open
    Title Should Be  Register

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Click Register Link
    Click Link  Register new user
    Register Page Should Be Open

Submit Register
    Click Button  Register

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirmation Password
    [Arguments]  ${password}
    Set Password Confirmation  password  ${password_confirmation}

Reset Application And Go To Register Page
    Reset Application
    Go To Register Page






