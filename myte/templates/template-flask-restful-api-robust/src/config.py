# config.py

"""
This module defines...
"""

# imports

import os

from dotenv import load_dotenv

# configurations

load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
DATABASE_NAME_TEST = os.getenv('DATABASE_NAME_TEST')

DEBUG = True

# databases
# delete any database you don't want to use

# postgreSQL - default (pip install psycopg2 (windows users) or psycopg2-binary (linux and mac users))  # noqa

SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'  # noqa

# # mySQL (pip install mysql-connector-python)
# uncomment line 35 to use MySQL DB and comment line 30

# SQLALCHEMY_DATABASE_URI = f'mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'  # noqa

# # SQLite (goto https://www.sqlite.org/download.html, download and install, if you've not)  # noqa
# uncomment line 40 to use SQLite DB and comment line 30

SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_NAME}.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.getenv('SECRETKEY')

# test database (PostgreSQl)

test_db_url = f'{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME_TEST}'  # noqa

# server

SECRET_KEY = os.getenv("SECRET_KEY")
ENVIRONMENT = os.getenv("ENVIRONMENT") == "DEV"
APPLICATION_ROOT = os.getenv("API_APPLICATION_ROOT", "/v1/api")
HOST = os.getenv("APPLICATION_HOST")
PORT = int(os.getenv("APPLICATION_PORT", "3000"))
