#!/usr/bin/bash

virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
python3 seed.py