from monApp.models import *

def test_user_init():
    user = User(Login="testuser", Password="pwd")
    assert user.Login == "testuser"
    assert user.Password == "pwd"

def test_user_get_id(testapp):
    with testapp.app_context():
        user = User.query.get("clement")
        assert user.get_id() == "clement"
