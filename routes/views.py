from . import main
from extensions import db  # Importing from extensions module
from flask import Flask, render_template


@main.route('/')
def index():
    return "Welcome to E-learning App"
