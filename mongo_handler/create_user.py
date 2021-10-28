from . import client
import bcrypt


def create_user(email, password, first_name, last_name, profile_picture_path):
    db = client.ttmik
    users = db.users

    hashed_pw = bcrypt.hashpw(str.encode(password), bcrypt.gensalt(12))
    created_user = users.insert_one({"email": email, "password": hashed_pw, "first_name": first_name, "last_name": last_name, "profile_picture_path": profile_picture_path})


    try:
        return f"successful creation of new user \n\n {created_user}"
    except Exception:
        return "Unable to connect to the server."