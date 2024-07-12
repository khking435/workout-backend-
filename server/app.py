from flask import Flask
from flask_migrate import Migrate
from database_models.db import db
from database_models.db import User
from database_models.db import Workout
from database_models.db import UserWorkout

print("DB module imported:", db)
print("User model imported:", User)
print("UserWorkout model imported:", UserWorkout)
print("Workout model imported:", Workout)

# Debug print statement to ensure the db module is imported correctly
#print("DB module imported:", db)

# Initializing Flask application
app = Flask(__name__)

# Debug print statement to ensure the app is created correctly
#print("Flask app created:", app)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Debug print statement to ensure the database URI is set correctly
#print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

# Initializing the migrate
migrate = Migrate(app, db)

# Debug print statement before initializing the app with the db
#print("Initializing the app with the db")

# Initializing the app with the db
db.init_app(app)

# Debug print statement after initializing the app with the db
#print("App initialized with the db")

@app.route('/')
def fit_fusion():
    return 'Hello, Fitness World!'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
