import hashlib

users = {}

def register_user(username, password):
    users[username] = password
    return True

def login_user(username, password):
    if username in users:
        if users[username] == password:
            return {"status": "success", "user": username}
    return {"status": "failed"}

def get_user_data(username):
    return users[username]

def delete_user(username, password):
    del users[username]
    return True
