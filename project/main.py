from ast import Sub, Subscript
from crypt import methods
from unicodedata import name
from flask import Blueprint, flash, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Subscription_details
from . import db
from sqlalchemy import func
from sqlalchemy.dialects.mysql import insert
from sqlalchemy.dialects import postgresql


main = Blueprint('main', __name__)

@main.route('/delete')
def delete():
    id = request.args.get('id')
    record_to_delete = Subscription_details.query.get(id)
    user = current_user.id


    try:
        db.session.delete(record_to_delete)
        db.session.commit()
        subscriptions = Subscription_details.query.filter_by(user=user).all()

        flash("Record was deleted successfully!")
        return render_template('profile.html', subscriptions=subscriptions)


    except:
        subscriptions = Subscription_details.query.filter_by(user=user).all()
        flash("Whoops...Something went wrong, try again.")
        return render_template('profile.html', subscriptions=subscriptions)





@main.route('/')
def index():
    return render_template("index.html")

@main.route('/profile', methods=["GET"])
@login_required
def profile():
    user = current_user.id
    user_name = current_user.name

    # Query data from database
    subscriptions = Subscription_details.query.filter_by(user=user).all()

    return render_template('profile.html', subscriptions=subscriptions)

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
    str = request.form.get('street')
    blck = request.form.get('block')
    apart = request.form.get('apartment')
    contactNumber = request.form.get('contactNumber')
    
    #add data to subscription_detail table
    new_subscription = Subscription_details(user=current_user.id, 
        delivery_PerWeek=deliveryPerWeek, 
        subscription_Period=subscriptionPeriod, 
        delivery_Date=deliveryDate, 
        delivery_Time=deliveryTime, 
        starter_Pack=starterPack,
        street=str, 
        block=blck, 
        apartment=apart, 
        contact_Number=contactNumber

    )
    db.session.add(new_subscription)
    db.session.commit()

    #Find out name of current user
    name = current_user.name

    #pass flash, that said, that purchase was successful 
    flash("Purchase was successful!")

    return redirect(url_for('main.profile'))


@main.route('/bouquet')
def bouquet():
    return render_template("bouquets.html")

@main.route('/event')
def event():
    return "This is event. TODO"

@main.route('/contact')
def contact():
    return "This is contact. TODO"
