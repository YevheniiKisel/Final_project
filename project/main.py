from unicodedata import name
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name = current_user.name)

@main.route('/subscription')
def subscription():
    return render_template("subscription1.html")

@main.route('/bouquet')
def bouquet():
    return "This is bouquet. TODO"

@main.route('/event')
def event():
    return "This is event. TODO"

@main.route('/contact')
def contact():
    return "This is contact. TODO"
