# seed.py

from datetime import date
from faker import Faker
from app import app
from database_models.db import db, User, Workout, Exercise, UserWorkout

# Initialize Faker
faker = Faker()

with app.app_context():
    # Create all tables
    db.create_all()

    # Generate fake users
    users = []
    for _ in range(10):  # Create 10 users
        user = User(username=faker.user_name(), email=faker.email(), password=faker.password())
        users.append(user)
        db.session.add(user)

    # Commit users to get their IDs
    db.session.commit()

    # Generate fake workouts
    workouts = []
    for _ in range(5):  # Create 5 workouts
        workout = Workout(
            name=faker.word(),
            date=faker.date_this_year(),
            duration=faker.random_int(min=20, max=90),
            type=faker.random_element(elements=('cardio', 'strength', 'flexibility', 'balance'))
        )
        workouts.append(workout)
        db.session.add(workout)

    # Commit workouts to get their IDs
    db.session.commit()

    # Generate fake exercises
    exercises = []
    for workout in workouts:
        for _ in range(3):  # Create 3 exercises per workout
            exercise = Exercise(
                workout_id=workout.id,
                name=faker.word(),
                sets=faker.random_int(min=1, max=5),
                reps=faker.random_int(min=5, max=20),
                weight=faker.random_int(min=0, max=100)
            )
            exercises.append(exercise)
            db.session.add(exercise)

    # Commit exercises to get their IDs
    db.session.commit()

    # Generate fake user workouts
    user_workouts = []
    for user in users:
        workout = faker.random_element(elements=workouts)
        user_workout = UserWorkout(user_id=user.id, workout_id=workout.id)
        user_workouts.append(user_workout)
        db.session.add(user_workout)

    # Commit all changes
    db.session.commit()

    print("Database seeded with Faker data!")
