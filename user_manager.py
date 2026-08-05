import json

def load_users(filepath):
    f = open(filepath)
    data = json.load(f)
    return data

def update_user(users, user_id, new_email):
    for user in users:
        if user['id'] == user_id:
            user['email'] = new_email
    return users

def delete_user(users, user_id):
    users = [u for u in users if u['id'] != user_id]
    return users
