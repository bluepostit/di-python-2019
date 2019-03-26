#!/usr/bin/bash

virtualenv env
source env/bin/activate
pip3 install flask
sqlite3 data/crm.db < data/seed.sql