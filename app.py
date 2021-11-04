from flask import Blueprint
from flask_restful import Api
from resources.registration import RegistrationAPI

# Route initialization for API

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(RegistrationAPI, '/register')
