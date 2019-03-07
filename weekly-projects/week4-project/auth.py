import json


USERS_FILE_PATH = 'data/users.json'

def get_all_users():
	users = []
	with open(USERS_FILE_PATH) as f:
		users = json.load(f)
	return users


def login(username, password):
    for user in get_all_users():
    	if user['username'] == username:
    		if user['password'] == password:
    			return True
    else:
    	return False
