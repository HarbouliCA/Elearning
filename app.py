from flask import Flask
from extensions import db
from models.user import User
from models.category import Category
from models.course import Course
from models.session import Session
from models.enrollment import Enrollment
from models.purchase import Purchase
from models.rewardpoint import RewardPoint
from routes.auth import auth as auth_blueprint
from routes.main import main as main_blueprint
from routes import course
import io
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'Mysecretkey'

# Specify the absolute path to the database file
app.root_path = os.path.dirname(os.path.abspath(__file__))
database_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'elearning.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elearning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(course)

first_request = True
@app.after_request
def after_request_function(response):
        global first_request
        if first_request:
            create_tables()
            first_request = False
        return response


def create_tables():
     db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
