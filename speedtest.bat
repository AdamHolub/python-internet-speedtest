@echo off
cd /d "%~dp0"
call .venv\Scripts\activate
python speedtest_console.py
pause