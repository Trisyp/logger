@echo off
cd %~dp0
echo %*
python pack_pyc.py %*
pause
