from flask import Blueprint, render_template
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/profile')
def profile():
    return render_template("profile.html")

@main.route('/subscription')
def subscription():
    return "This is subscription. TODO"

@main.route('/bouquet')
def bouquet():
    return "This is bouquet. TODO"

@main.route('/event')
def event():
    return "This is event. TODO"

@main.route('/contact')
def contact():
    return "This is contact. TODO"
    