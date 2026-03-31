#!/bin/bash

# 1. Create venv if it doesn't exist
if [ -d "venv" ]; then
    source venv/bin/activate
else
    python3 -m venv venv
    source venv/bin/activate
    
    # Only create .env if it doesn't exist already
    if [ ! -f ".env" ]; then
        echo 'key="PAST YOUR KEY HERE"' > .env
    fi
    
    python3 -m pip install -r requirements.txt
fi

# 2. Run the application
python3 main.py

# 3. Exit the virtual environment
deactivate
