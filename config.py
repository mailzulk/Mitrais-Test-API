import os
basedir = os.path.abspath(os.path.dirname(__file__))

# SQL params for SQLAlchemy

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
# your SQL Database and Credentials in the format: 'sql://user@password/db-name'
SQLALCHEMY_DATABASE_URI = '<your-database-credentials>'
