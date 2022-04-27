*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login
Create New Command
    Create User

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
