import os
from flask import Flask
from flask_cors import CORS
from model import db, Registration

# This is the initialization of our app along with its database and CORS rule

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object('config')

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    db.init_app(app)

    CORS(app)

    return app

if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
