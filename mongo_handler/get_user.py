from . import client
import bcrypt

def get_user(email, password):
    db = client.ttmik
    users = db.users
    selected_user = users.find_one({"email": email})

    checked_pw = bcrypt.checkpw(password.encode(), selected_user['password'])
    

    try:
        if checked_pw:
            selected_user.pop('_id')
            selected_user.pop('password')
            return selected_user
        else:
            return "Sorry the email or password you provideded does not match anything in our database"
    except Exception:
        return "Unable to connect to the server."