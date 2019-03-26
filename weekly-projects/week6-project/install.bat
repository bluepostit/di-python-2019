@echo off

echo Creating virtual environment...
virtualenv env
call env\Scripts\activate.bat
pip install flask
