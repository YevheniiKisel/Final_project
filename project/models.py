from enum import unique
from unicodedata import name
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String (100), unique = True)
    password = db.Column(db.String (100))
    name = db.Column(db.String(1000))

class Subscription(db.Model):
    __tablename__= 'subscription' 
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    delivery_PerWeek = db.Column(db.Integer)
    subscription_Period = db.Column(db.Integer)
    delivery_Date = db.Column(db.DateTime)
    delivery_Time = db.Column(db.String(10))
    starter_Pack = db.Column(db.String(10))

class Delivery_address(db.Model):
    __tablename__='delivery_address'
    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    street = db.Column(db.String(100))
    block = db.Column(db.String(10))
    apartment = db.Column(db.String(10))
    contact_Number = db.Column(db.String(20))