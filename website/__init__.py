# CYBER PROJECT - NETA ITSHAYEK

"""This module is responsible for:
        User Interface - Displaying the windows for the client
    The screens that are presented to the client are:
    1. Opening screen
    2. Sign Up
    3. Log In
    4. Upload Photo
    5. Show Profile
    6. Solve Equation
"""

# IMPORTS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

#CONSTANTS
db = SQLAlchemy()
DB_NAME = "cbdatabase.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .board import board
    from .learn import learn
    from .notes import notes
    from .auth import auth
    from .home import home
    from .userSettings import userSettings

    app.register_blueprint(board, url_prefix='/')
    app.register_blueprint(learn, url_prefix='/')
    app.register_blueprint(notes, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(userSettings, url_prefix='/')



    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')