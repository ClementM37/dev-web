import pytest
from monApp import app,db
from monApp.models import *
from hashlib import *
@pytest.fixture
def testapp():
    app.config.update({"TESTING":True,"SQLALCHEMY_DATABASE_URI":
    "sqlite:///:memory:","WTF_CSRF_ENABLED": False})
    with app.app_context():
        db.create_all()

        # --- INSERTIONS AUTEURS ---
        auteur1 = Auteur(Nom="Victor Hugo")
        auteur2 = Auteur(Nom="Jules Verne")
        auteur3 = Auteur(Nom="Hugo Boss")
        db.session.add_all([auteur1, auteur2, auteur3])
        db.session.commit()

        # --- INSERTIONS LIVRES ---
        livre1 = Livre(Prix=15.99, Titre="Les Misérables", Url="", Img="lesmiserables.jpg", auteur_id=auteur1.idA)
        livre2 = Livre(Prix=12.50, Titre="Notre-Dame de Paris", Url="",Img="notredame.jpg", auteur_id=auteur1.idA)
        livre3 = Livre(Prix=10.00, Titre="Vingt mille lieues sous les mers",Url="", Img="20000lieues.jpg", auteur_id=auteur2.idA)
        livre4 = Livre(Prix=8.99, Titre="Collection Hiver", Url="",Img="hiver.jpg", auteur_id=auteur3.idA)
        
        db.session.add_all([livre1, livre2, livre3, livre4])
        db.session.commit()

        # --- INSERTIONS USERS ---
        m = sha256()
        m.update("azerty".encode())
        hashed_password = m.hexdigest()
        user1 = User(Login="clement", Password=hashed_password)
        db.session.add(user1)
        db.session.commit()

    yield app

    # Cleanup après les tests
    with app.app_context():
        db.drop_all()
    
@pytest.fixture
def client(testapp):
    return testapp.test_client()