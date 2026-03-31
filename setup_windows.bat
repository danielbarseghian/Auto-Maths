@echo off

:: 1. Create venv if it doesn't exist
if exist venv\ (
    call venv\Scripts\activate
) else (
    python -m venv venv
    call venv\Scripts\activate
    
    :: Only create .env if it doesn't exist already
    if not exist .env (
        echo key="PAST YOUR KEY HERE" > .env
    )
    
    python -m pip install -r requirements.txt
)

:: 2. Run the application
python main.py

:: 3. Exit the virtual environment
call deactivate
