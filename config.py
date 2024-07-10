import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
