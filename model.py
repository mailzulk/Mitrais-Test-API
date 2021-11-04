from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

# This is the model definition for our object which we want to work with

class Registration(db.Model):
    registration_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True)
    gender = db.Column(db.String(50))
    mobile_no = db.Column(db.String(50))
    date_of_birth = db.Column(db.DateTime, nullable=True)

    def __init__(self, first_name, last_name, email, gender, mobile_no, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.mobile_no = mobile_no
        self.date_of_birth = date_of_birth

class RegistrationSchema(ma.Schema):
    registration_id = fields.Integer()
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    gender = fields.String()
    mobile_no = fields.String(required=True)
    date_of_birth = fields.DateTime()