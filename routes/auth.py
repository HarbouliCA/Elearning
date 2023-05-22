
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models.user import User
from flask import render_template, redirect, url_for
from extensions import db  # Importing from extensions module
from flask_login import current_user


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) 

    login_user(user, remember=remember)
    return redirect(url_for('auth.welcome'))  # redirect to the welcome page


@auth.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html', name=current_user.username, role=current_user.role)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        role = request.form.get('role')  # get role from form data

        if role not in ['Teacher', 'Student']:
            flash('Invalid role.')
            return redirect(url_for('auth.signup'))

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        new_user = User(email=email, username=name, password=generate_password_hash(password, method='sha256'), role=role)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    else: # If request is GET show signup page
        return render_template('signup.html')



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
