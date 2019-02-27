#!/usr/bin/bash

echo "Creating virtual environment..."
virtualenv env
source env/bin/activate
pip install flask
