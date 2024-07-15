import pytest
from models import User
from services.user_service import UserService


    assert len(users) > 0

def test_update_user(session):
    data = {'username': 'janedoe', 'email': 'janedoe@example.com', 'password': 'password123'}
    user = UserService.create_user(data)
    update_data = {'username': 'janedoe', 'email': 'jane.doe@example.com'}
    updated_user = UserService.update_user(user.id, update_data)
    assert updated_user.email == 'jane.doe@example.com'

def test_delete_user(session):
    data = {'username': 'markdoe', 'email': 'markdoe@example.com', 'password': 'password123'}
    user = UserService.create_user(data)
    deleted_user = UserService.delete_user(user.id)
    assert deleted_user is not None
    assert UserService.get_user_by_id(user.id) is None
