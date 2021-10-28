import ast
from flask import request
from . import api
from mongo_handler.get_user import get_user
from mongo_handler.create_user import create_user

@api.route('/users', methods=["GET"])
def users():
    request_data = request.data.decode('UTF-8') # turns bytes into a string
    user_credentials = ast.literal_eval(request_data) # turns string into a dictionary
    user_email = user_credentials['email']
    user_password = user_credentials['password']
    user = get_user(user_email, user_password)
    return user


@api.route('/users', methods=["POST"])
def users_post():
    request_data = request.data.decode('UTF-8')
    user_form_data = ast.literal_eval(request_data)

    user_email = user_form_data['email']
    user_password = user_form_data['password']
    user_first_name = user_form_data['first_name']
    user_last_name = user_form_data['last_name']
    user_profile_picture_path = user_form_data['profile_picture_path']

    create_user(user_email, user_password, user_first_name, user_last_name, user_profile_picture_path)
    return f"Account creation successful for {user_first_name} {user_last_name}"