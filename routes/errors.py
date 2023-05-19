from flask import render_template
from . import main
from extensions import db  # Importing from extensions module

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
