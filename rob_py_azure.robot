*** Settings ***
Documentation     Example Test Suite
Library           SeleniumLibrary
Library           OperatingSystem
Library           BuiltIn

*** Variables ***
${AzureDevOpsURL}    https://dev.azure.com/miguelmduarte
${PAT}    fa6karjl6lufcj6ovtkvubjkif4rwpqyxofegqsdadadu76wggnma
${Project}    Testezao
${BROWSER}    chrome
${URL}    https://www.saucedemo.com/
${object}    //span[@class='title' and text()='Products']

*** Test Cases ***
Primeiro
    [Tags]    Vai Funcionar
    [Setup]    Open Browser    ${URL}    ${BROWSER}
    Input Text    //*[@id="user-name"]    standard_user
    Input Text    //*[@id="password"]    secret_sauce
    Capture Page Screenshot    MyScreenshot1.png
    Click Element    //*[@id="login-button"]
    Wait Until Page Contains    Swag Labs
    Page Should Contain Element    ${object}
    Capture Page Screenshot    MyScreenshot2.png

    OperatingSystem.Run    python C:\Users\a\Desktop\IW\PythonAzure\pythonazure.py


    Close Browser
