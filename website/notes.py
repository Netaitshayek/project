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
from .models import Note, text_to_speech
from . import db
import json

notes = Blueprint('notes', __name__)


@notes.route('/notes', methods=['GET', 'POST'])
@login_required
def create_note():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            text_to_speech(note)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("notes.html", user=current_user)
