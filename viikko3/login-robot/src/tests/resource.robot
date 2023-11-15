*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input New Command  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Input New Command
    [Arguments]  ${command}
    Input  ${command}

Input New Command And Create New User
    [Arguments]  ${username}  ${password}
    Input New Command  new
    Input Credentials  ${username}  ${password}
