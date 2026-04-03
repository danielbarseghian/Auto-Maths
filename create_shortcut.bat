@echo off
:: Set the name of the shortcut
set "SHORTCUT_NAME=MyPythonSetup"

:: Get the full path of the current folder and the target file
set "TARGET_FILE=%~dp0setup_windows.bat"
set "DESTINATION=%USERPROFILE%\Desktop\%SHORTCUT_NAME%.lnk"

echo Creating shortcut for: %TARGET_FILE%
echo Placing it on: %DESTINATION%

:: Create the symbolic link
mklink "%DESTINATION%" "%TARGET_FILE%"

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to create shortcut. 
    echo Did you forget to Right-Click and "Run as Administrator"?
) else (
    echo [SUCCESS] Shortcut created on your Desktop!
)

pause
