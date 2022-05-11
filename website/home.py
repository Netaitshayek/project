# CYBER PROJECT - NETA ITSHAYEK

"""This module is responsible for:
    User Interface - Displaying the window for the client
    1. Opening screen
"""

# IMPORTS
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User

home = Blueprint('home', __name__)

@home.route('/', methods=['GET', 'POST'])
@login_required
def homepage():
    """ This function redire
    """
    child_name = current_user.child_name
    return render_template("home.html", user=current_user, child_name=child_name)