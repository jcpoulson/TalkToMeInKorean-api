from flask import request
from . import api

@api.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return "Hey whats up bro you made a GET Request dude"
    elif request.method == "POST":
        data = request.data
        return "Hey whats up you made a POST request to this method. The data you sent is: " + str(data)