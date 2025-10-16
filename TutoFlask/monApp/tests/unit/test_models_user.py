from monApp.models import User, db

def test_user_init():
    user = User(Login="testuser", Password="pwd")
    assert user.Login == "testuser"
    assert user.Password == "pwd"

def test_user_get_id(testapp):
    with testapp.app_context():
        # Créer un user pour ce test
        user = User(Login="clement", Password="testpassword")
        db.session.add(user)
        db.session.commit()
        
        # Récupérer le user
        user_from_db = User.query.get("clement")
        assert user_from_db is not None
        assert user_from_db.get_id() == "clement"
