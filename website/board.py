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
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .icon import icon
from .models import sendEmail, text_to_speech

board = Blueprint('board', __name__)

@board.route('/board', methods=['GET', 'POST'])
@login_required
def display_board():
    item_to_ittr = [(x, y) for x,y in icon["Necessities"].items()]
    items = [item_to_ittr[i:i+3] for i in range(0, len(item_to_ittr), 3)]
    if request.method == 'POST':
        text = request.form.get('id')
        print(text)
        text_to_speech("I need To" + text)
        sendEmail(current_user.email, text)
    return render_template("board_push.html", user=current_user, items=items)
