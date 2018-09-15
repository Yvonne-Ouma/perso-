from flask import Flask
from . import main
from flask import render_template
# ,redirect, request, url_for,abort,flash
from flask_login import login_required, current_user
from ..models import User
# from .forms import MinutePitchForm,UpdateProfile,CommentForm
from .. import db


app = Flask(__name__)


# views
@main.route("/")
def index():
    '''
    title = "Welcome to my personal blog"
    '''
    title = 'Welcome to my personal blog'
    # pitches = Pitch.query.all()

    return render_template('index.html', title= title)