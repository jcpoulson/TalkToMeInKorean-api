from flask import Blueprint

api = Blueprint('api', '__name__')

from .index import *
from .lessons import *
from .users import *

# This functionality is needed to replace current firebase production backend
# getLevels (done), signIn (done), signUp (done), updateUser, uploadImage