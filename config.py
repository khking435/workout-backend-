# config.py
import os

class Config:
    DEBUG = True
    # Add other configuration variables here


SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database_name.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
