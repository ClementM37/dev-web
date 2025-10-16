from monApp.models import Auteur, db

def test_auteur_init():
    auteur = Auteur(Nom="Cricri DAL")
    assert auteur.Nom == "Cricri DAL"

def test_auteur_repr(testapp):
    with testapp.app_context():
        # Ajouter un auteur pour ce test
        auteur = Auteur(Nom="Victor Hugo")
        db.session.add(auteur)
        db.session.commit()

        # Récupérer l'auteur depuis la base
        auteur_from_db = Auteur.query.get(auteur.idA)
        assert repr(auteur_from_db) == f"<Auteur ({auteur.idA}) Victor Hugo>"
