*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jaakko  jaakko123
    Output Should Contain  Logged in
Register With Already Taken Username And Valid Password
    Create User  jaakko  jaakko123
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Create User And Input Login Command
    Create User  jaakko  jaakko123
    Input Login Command
Input New Command And Create User
