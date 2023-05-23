from flask import Blueprint

main = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)
course = Blueprint('course', __name__)

from . import auth, main, course