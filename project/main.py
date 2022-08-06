from ast import Sub
from crypt import methods
from unicodedata import name
from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Subscription, Delivery_address
from . import db
from sqlalchemy import func
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.dialects import postgresql


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/profile', methods=["GET"])
@login_required
def profile():
    user = current_user.id
    user_name = current_user.name
    User.query.filter_by(email=email).first()
    User.query.filter_by(email=email).first()
    subscriptions = db.execute("SELECT delivery_Date, delivery_Time, starter_Pack FROM subscription WHERE user = ?", user)
    deliveries = db.execute("SELECT street, block, apartment WHERE user=?", user)

    return render_template("profile.html", subscriptions, deliveries,)

@main.route('/subscription')
def subscription():
    return render_template("subscription1.html")

@main.route('/subscription', methods = ["POST"])
@login_required
def subscription_post():
    #data for Subscribtion table in database
    deliveryPerWeek = request.form.get('perWeek')
    subscriptionPeriod = request.form.get('durationMonth')
    deliveryDate = request.form.get('deliveryDate')
    deliveryTime = request.form.get('deliveryTime')
    starterPack = request.form.get('starterPack')

    #data for Delivery table in database
    str = request.form.get('steet')
    blck = request.form.get('block')
    apart = request.form.get('apartment')
    contactNumber = request.form.get('contactNumber')
    
    #add data to subscription table
    new_subscription = Subscription(user=current_user.id, 
        delivery_PerWeek=deliveryPerWeek, 
        subscription_Period=subscriptionPeriod, 
        delivery_Date=deliveryDate, 
        delivery_Time=deliveryTime, 
        starter_Pack=starterPack
    )
    db.session.add(new_subscription)
    db.session.commit()

    #add data to delivery table
    new_delivery = Delivery_address(user=current_user.id, 
        street=str, 
        block=blck, 
        apartment=apart, 
        contact_Number=contactNumber
    )

    db.session.add(new_delivery)
    db.session.commit()

    #Find out name of current user
    name = current_user.name

    #pass flash, that said, that purchase was successful 
    flash("Purchase was successful!")

    return render_template("profile.html", deliveryTime=deliveryTime, deliveryDate=deliveryDate, street=str, block=blck, apartment=apart, name=name, starterPack=starterPack)


@main.route('/bouquet')
def bouquet():
    return "This is bouquet. TODO"

@main.route('/event')
def event():
    return "This is event. TODO"

@main.route('/contact')
def contact():
    return "This is contact. TODO"
