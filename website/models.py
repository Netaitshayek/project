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
from multiprocessing.dummy import current_process
from . import db
from flask_login import UserMixin, current_user
from sqlalchemy.sql import func
import pyttsx3
import time
import smtplib

#CONSTANTS
SUBJECT="Hey, your child has sent you a message"
EMAIL= "communicationboard1@gmail.com"
EMAIL_PASSWORD="CB123456789"


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    parent_name = db.Column(db.String(150))
    child_name = db.Column(db.String(150))
    notes = db.relationship('Note')



def text_to_speech(text):
    """ 
    Function to convert text to speech
    """
    engine = pyttsx3.init()
    while(engine._inLoop):
        time.sleep(0.01)
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 0.8)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    if engine._inLoop:
        engine.endLoop()


def sendEmail(receiver_email, content):

    sent_from = EMAIL
    subject = 'communication board: your child needs something'
    body = 'Hello! This Message was sent by the communication board\n" + "your child needs ' + content

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(receiver_email), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(EMAIL, EMAIL_PASSWORD)
        smtp_server.sendmail(sent_from, receiver_email, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)