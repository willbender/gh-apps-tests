@echo off
REM Startup script for the weather service on Windows

REM Change to the project root directory
cd /d "%~dp0\.."

REM Run the weather service from the src directory
set PYTHONPATH=%PYTHONPATH%;%cd%\src
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --log-level info
