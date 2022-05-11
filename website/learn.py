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
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user

from website import board

from .icon import icon
import json
from .models import text_to_speech

learn = Blueprint('learn', __name__)

@learn.route('/board', methods=['GET', 'POST'])
@login_required
def learning_board(board):
    if board not in icon.keys():
        board=get_key(board)
    title = board
    item_to_ittr = [(x, y) for x,y in icon[board].items()]
    items = [item_to_ittr[i:i+3] for i in range(0, len(item_to_ittr), 3)]
    if request.method == 'POST':
        text = request.form.get('id')
        text_to_speech(text)
    return render_template("board_learn.html", user=current_user, items=items, title=title)

@learn.route('/learn', methods=['GET', 'POST'])
@login_required
def display_boards():
    title = "Choose board"
    item_to_ittr = [(x, y) for x,y in icon["boards"].items()]
    items = [item_to_ittr[i:i+3] for i in range(0, len(item_to_ittr), 3)]
    if request.method == 'POST':
        board = request.form.get('id')
        text_to_speech(board)
        return learning_board(board)
    return render_template("boards.html", user=current_user, items=items, title=title)

def get_key(value):
    for name in icon["boards"].values():
        for value2 in icon[name].values():
            if value2 == value:
                return name
    else:
        return "shit"