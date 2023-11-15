*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create New User  martti  Unsecure1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create New User  martti  Unsecure1
    Input New Command And Create New User  martti  asontehu1
    Output Should Contain  User with username martti already exists

Register With Too Short Username And Valid Password
    Input New Command And Create New User  mö  natohseu13
    Output Should Contain  Username mö too short

Register With Enough Long But Invalid Username And Valid Password
    Input New Command ANd Create New User  MArtti  asonehusnoa1
    Output Should Contain  Username MArtti can only contain characters a-z

Register With Valid Username And Too Short Password
    Input New Command ANd Create New User  martti  aoeu1
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command ANd Create New User  martti  aoeuaoeu
    Output Should Contain  Password contains only letters
