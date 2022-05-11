# CYBER PROJECT - NETA ITSHAYEK

"""This module is responsible for:
    The authentication procees:
    1. Log Out
    2. Sign Up
    3. Log In
"""

# IMPORTS
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ This function recieve the data from the form the user flls,
    if all the data meets the requirments it logs into the account and redirects the user to the homepage. 
    else, flashes error and the user need to insert new data
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('home.homepage'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    """ This function logs out of the users account and redirects to the login page
    """
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """ This function recieve the data from the form the user flls,
    if all the data meets the requirments it creates an account saves it to the database and redirects the user to the homepage. 
    else, flashes error and the user need to insert new data
    """
    if request.method == 'POST':
        email = request.form.get('email')
        parent_name = request.form.get('parentName')
        child_name = request.form.get('childName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(parent_name) < 2:
            flash('Parent name must be greater than 1 character.', category='error')
        elif len(child_name) < 2:
            flash('Child name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, parent_name=parent_name, child_name=child_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('home.homepage'))

    return render_template("sign_up.html", user=current_user)
