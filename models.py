from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Fake database (replace with real DB later)
users = []

def create_user(username, password):
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    users.append({"username": username, "password": hashed_pw})

def verify_user(username, password):
    for user in users:
        if user["username"] == username and bcrypt.check_password_hash(user["password"], password):
            return True
    return False