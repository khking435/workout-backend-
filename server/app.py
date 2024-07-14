from flask import Flask, jsonify, request
from flask_migrate import Migrate
from database_models.db import db
from database_models.db import User
from database_models.db import Workout
from database_models.db import UserWorkout

# Initializing Flask application
app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing the migrate
migrate = Migrate(app, db)

# Initializing the app with the db
db.init_app(app)

@app.route('/')
def index():
    """Route to welcome message"""
    return 'Hello, Fitness World!'

# Routes for Users
@app.route('/users', methods=['GET'])
def get_all_users():
    """Route to get all users"""
    users = User.query.all()
    users_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify(users_list), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Route to get a specific user by ID"""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    user_data = {'id': user.id, 'username': user.username, 'email': user.email}
    return jsonify(user_data), 200

@app.route('/users', methods=['POST'])
def create_user():
    """Route to create a new user"""
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing username, email, or password'}), 400

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Route to update an existing user"""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)

    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Route to delete a user"""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200

# Code to print all registered routes
with app.test_request_context():
    print([str(rule) for rule in app.url_map.iter_rules()])

if __name__ == '__main__':
    app.run(port=5555, debug=True)
