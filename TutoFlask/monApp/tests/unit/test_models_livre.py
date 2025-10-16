from monApp.models import Livre

def test_livre_init(testapp):
    # Test de création sans DB
    livre = Livre(9.99, "Test Book", "http://test", "image.jpg", 1)
    assert livre.Prix == 9.99
    assert livre.Titre == "Test Book"
    assert livre.Url == "http://test"
    assert livre.Img == "image.jpg"
    assert livre.auteur_id == 1

def test_livre_in_db(testapp):
    with testapp.app_context():
        livre = Livre.query.get(1)
        assert livre is not None
        assert livre.Titre == "Les Misérables"
        assert livre.auteur.Nom == "Victor Hugo"

def test_livre_repr(testapp):
    with testapp.app_context():
        livre = Livre.query.get(1)
        assert repr(livre) == "<Livre (1) Les Misérables>"
