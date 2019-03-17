#!/usr/bin/bash

virtualenv env
source env/bin/activate
pip3 install flask
sqlite3 data/data.db < data/seed.sql