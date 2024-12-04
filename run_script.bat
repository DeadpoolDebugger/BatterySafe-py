@echo off
REM Navigate to the virtual environment directory
cd D:\Development\Python\BatterySafe\.venv\

REM Activate the virtual environment
call Scripts\activate.bat

REM Navigate to python script
cd D:\Development\Python\BatterySafe\

REM Run the python script
start pythonw battery_monitor.py

REM Deactivate the virtual environment
deactivate