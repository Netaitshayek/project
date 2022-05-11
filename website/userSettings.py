# CYBER PROJECT - NETA ITSHAYEK

"""This module is responsible for:
    User Interface - Displaying the window for the client:
    1. Show Profile

"""

# IMPORTS
from flask import Blueprint, render_template
from flask_login import login_required, current_user

userSettings = Blueprint('userSettings', __name__)


@userSettings.route('/userSettings', methods=['GET', 'POST'])
@login_required
def settings():
    """ This function redirects the user to the profile and settings page
    """
    child_name = current_user.child_name
    parent_name = current_user.parent_name
    email = current_user.email
    profile_picture = "../commboard.png"

    return render_template("profile.html", user=current_user, parent_name=parent_name, child_name=child_name, email=email, profile_picture=profile_picture)