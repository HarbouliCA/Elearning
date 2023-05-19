from flask import Blueprint, render_template
from extensions import db  # Importing from extensions module

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
