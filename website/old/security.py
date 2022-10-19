from website.user import User

users = [
    User(1, 'Alia', 'Abdelmoty')
]
 
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

#userid_mapping[1] we will be able to find a user using an ID 

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return user_id_mapping.get(user_id,)
