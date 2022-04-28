*** Settings ***
Resource  resource.robot
Test Setup  Create First User

*** Test Cases ***
Register With Valid Username And Password
    Create User  second  second
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  jaakko  jaakko123
    Output Should Contain  User with username jaakko already exists


*** Keywords ***
Create First User
    Create User  jakke  jakke123
    Create New Command
