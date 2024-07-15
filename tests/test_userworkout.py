import pytest
from models import UserWorkout
from services.userworkout_service import UserWorkoutService

    assert len(userworkouts) > 0

def test_update_userworkout(session):
    data = {'user_id': 1, 'workout_id': 1, 'start_date': '2024-07-01', 'completion_date': '2024-07-02', 'feedback': 'Good workout!'}
    userworkout = UserWorkoutService.create_userworkout(data)
    update_data = {'feedback': 'Excellent workout!'}
    updated_userworkout = UserWorkoutService.update_userworkout(userworkout.id, update_data)
    assert updated_userworkout.feedback == 'Excellent workout!'

def test_delete_userworkout(session):
    data = {'user_id': 1, 'workout_id': 1, 'start_date': '2024-07-01', 'completion_date': '2024-07-02', 'feedback': 'Challenging workout!'}
    userworkout = UserWorkoutService.create_userworkout(data)
    deleted_userworkout = UserWorkoutService.delete_userworkout(userworkout.id)
    assert deleted_userworkout is not None
    assert UserWorkoutService.get_userworkout_by_id(userworkout.id) is None
