from crypt import methods
import email
from click import password_option
from flask import Blueprint, flash, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_required, login_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/signin')
def sign_in():
    return render_template("signin.html")

@auth.route('/signin', methods = ['POST'])
def sign_in_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    # query data from database, filter by email
    user = User.query.filter_by(email=email).first()

    # check if user exist in database and if password was correct
    if not user or not check_password_hash(user.password, password):
        flash('Please check your credentials and try again')
        return redirect(url_for('auth.sigh_in'), code=400) # if user doesn`t exist or password was incorrect - return error and redirect to m
    else:
        login_user(user, remember=remember)
        return redirect(url_for('main.index')) # if user exists redirect to homepage

@auth.route('/signup')
def sign_up():
    return render_template("signup.html")

@auth.route('/signup', methods = ["POST"])
def sign_up_post():
    # validation of inputs
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")
    passwordConfirmation = request.form.get("confirmation")

    user = User.query.filter_by(email=email).first() # check if inputted email already exists
    if user:
        flash("Email adress already exists.")
        return redirect(url_for('auth.sign_up'), code= 403) # redirect user if email was found in database
    elif not email:
        flash("Please input email adress.")
        return redirect(url_for('auth.sign_up')) # redirect if email field is empty
    elif not password:
        flash("Please input password.")
        return redirect(url_for('auth.sign_up')) # redirect if password field is empty
    elif not passwordConfirmation:
        flash("Please confirm password.")
        return redirect(url_for('auth.sign_up')) # redirect if password confirmation field is empty
    elif not password==passwordConfirmation:
        flash("Passwords don`t match! Please try again.")
        return redirect(url_for('auth.sign_up')) # redirect if passwords don`t match

    # Check passed. Create a new user with form data
    else:
        new_user = User(email=email, name = name, password = generate_password_hash(password, method='sha256')) 

    # Add a new user to the database
    db.session.add(new_user)
    db.session.commit()

    # redirect user to a homepage
    return redirect(url_for('main.index'))

@auth.route('/signout')
@login_required
def sign_out():
    logout_user()
    return redirect(url_for('main.index'))






