@echo off

echo Creating virtual environment...
virtualenv env
call env\Scripts\activate.bat
pip install -r requirements.txt
python seed.py
