import os
import re
import json
import datetime
from flask import request
from flask_restful import Resource
from model import db, Registration, RegistrationSchema

registration_schema = RegistrationSchema(many=True)

# This is the script where we defined what operation would we like to execute with our API

class RegistrationAPI(Resource):

    # This is the GET method to retrieve all registration objects
    def get(self):
        registration = Registration.query.all()
        registration = registration_schema.dump(registration).data
        return {'status': 'success', 'data': registration}, 200

    # This is the POST method to save registration objects that was sent to the API
    def post(self):
        # This is a prerequisite to process the request as First Name, Last Name, Email and Mobile No is a mandatory field
        if 'first_name' in request.form and 'last_name' in request.form and 'email' in request.form and 'mobile_no' in request.form:
            # This is a regular expression used to validate that the mobile number processed is indeed Indonesian number, if not then we will return error
            reg = re.search("(\+62 ((\d{3}([ -]\d{3,})([- ]\d{4,})?)|(\d+)))|(\(\d+\) \d+)|\d{3}( \d+)+|(\d+[ -]\d+)|\d+", request.form['mobile_no'])
            if reg:
                try:
                    registration = Registration(
                    first_name = request.form['first_name'],
                    last_name = request.form['last_name'],
                    email = request.form['email'],
                    gender = request.form.get('gender', ""),
                    mobile_no = request.form['mobile_no'],
                    date_of_birth = request.form['date_of_birth']
                    )
                    db.session.add(registration)
                    db.session.commit()
                except:
                    # This response is used for the Vue application to give an alert that the user already exists in the database
                    return {"status": 'failed', 'message': "User already exists"}, 201

                # This response is used for the Vue application as a signal that the process is a successful one
                return { "status": 'success'}, 201
            else:
                # This response is used for the Vue application to give an alert that the mobile number is not a valid Indonesian number
                return {"status": 'failed', 'message': "Mobile Number is not valid"}, 201
        else:
            return { "status": 'failed', 'message': 'form not complete' }, 400
    