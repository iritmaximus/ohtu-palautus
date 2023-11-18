*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Create New User  martti  Unsecure1  Unsecure1
    Title Should Be  Welcome to Ohtu Application!



Register With Too Short Username And Valid Password
    Create New User  mö  Unsecure1  Unsecure1
    Title Should Be  Register
    Page Should Contain  Username too short


Register With Valid Username And Invalid Password
    Create New User  martti  unsecure  unsecure
    Title Should Be  Register
    Page Should Contain  Password contains only letters

Register With Nonmatching Password And Password Confirmation
    Create New User  martti  Unsecure1  Unsecure2
    Title Should Be  Register
    Page Should Contain  Password and confirmation don't match

Login After Successful Registration
    Create New User  martti  Unsecure1  Unsecure1
    Go To Login Page
    Login  martti  Unsecure1
    Main Page Should Be Open

Login After Failed Registration
    Create New User  martti  unsecure  unsecure
    Go To Login Page
    Login  martti  unsecure
    Login Page Should Be Open
    Page Should Contain  Invalid username or password

*** Keywords ***
Create New User
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password_confirmation}
    Submit New Registration

Login
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Submit Login
    

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Submit Login
    Click Button  Login

Submit New Registration
    Click Button  Register
