# Import the Flask class to create a Flask application
from flask import Flask

# Import SQLAlchemy for database handling
from flask_sqlalchemy import SQLAlchemy

# Import Migrate for handling database migrations
from flask_migrate import Migrate

 # Create an instance of the Flask class
app = Flask(__name__) 

# Set the URI for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workout.db'  

# Create a SQLAlchemy object and link it to the Flask app
db = SQLAlchemy(app)  

# Create a Migrate object to handle migrations
migrate = Migrate(app, db)  

# Define the Exercise model
class Exercise(db.Model):
    # Primary key column
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # Foreign key to the Workout model
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'), nullable=False)
    # Name of the exercise
    name = db.Column(db.String, nullable=False)
    # Number of sets
    sets = db.Column(db.Integer, nullable=False)
    # Number of repetitions
    reps = db.Column(db.Integer, nullable=False)
    # Weight used in the exercise
    weight = db.Column(db.Integer, nullable=False)
