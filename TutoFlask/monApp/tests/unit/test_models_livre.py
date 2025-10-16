from monApp.models import Livre, Auteur, db

def test_livre_init():
    # Test de création sans DB
    livre = Livre(9.99, "Test Book", "http://test", "image.jpg", 1)
    assert livre.Prix == 9.99
    assert livre.Titre == "Test Book"
    assert livre.Url == "http://test"
    assert livre.Img == "image.jpg"
    assert livre.auteur_id == 1

def test_livre_in_db(testapp):
    with testapp.app_context():
        # Créer un auteur et un livre pour ce test
        auteur = Auteur(Nom="Victor Hugo")
        db.session.add(auteur)
        db.session.commit()
        
        livre = Livre(Prix=15.99, Titre="Les Misérables", Url="", Img="lesmiserables.jpg", auteur_id=auteur.idA)
        db.session.add(livre)
        db.session.commit()
        
        # Récupérer le livre
        livre_from_db = Livre.query.get(livre.idL)
        assert livre_from_db is not None
        assert livre_from_db.Titre == "Les Misérables"
        assert livre_from_db.auteur.Nom == "Victor Hugo"

def test_livre_repr(testapp):
    with testapp.app_context():
        # Créer un auteur et un livre pour ce test
        auteur = Auteur(Nom="Victor Hugo")
        db.session.add(auteur)
        db.session.commit()
        
        livre = Livre(Prix=15.99, Titre="Les Misérables", Url="", Img="lesmiserables.jpg", auteur_id=auteur.idA)
        db.session.add(livre)
        db.session.commit()
        
        # Tester le repr
        livre_from_db = Livre.query.get(livre.idL)
        assert repr(livre_from_db) == f"<Livre ({livre.idL}) Les Misérables>"
