from monApp.models import Auteur
from monApp import db
from monApp.tests.functional.test_routes_auteur import login

def test_auteur_save_success(client, testapp):
    with testapp.app_context():
        # Créer un auteur dans la base de données avec un nom unique
        auteur = Auteur(Nom="Ancien Nom Test Unique")
        db.session.add(auteur)
        db.session.commit()
        idA = auteur.idA
    
    # simulation connexion user (en dehors du contexte)
    login(client, "clement", "azerty", "/auteur/save/")
    
    # soumission du formulaire pour modifier l'auteur
    response = client.post("/auteur/save/",
        data={"idA": idA, "Nom": "Alexandre Dumas"},
        follow_redirects=True)
    
    # Vérifier le statut de la réponse
    assert response.status_code == 200
    
    # Vérifier que l'auteur apparaît quelque part dans la réponse
    assert b"Alexandre Dumas" in response.data or b"auteur" in response.data.lower()
    
    # Vérifier que la base a été mise à jour
    with testapp.app_context():
        auteur_updated = Auteur.query.get(idA)
        assert auteur_updated is not None
        assert auteur_updated.Nom == "Alexandre Dumas"
