from monApp import app

def test_auteurs_liste(client): #client est la fixture définie dans conftest.py
    response = client.get('/auteurs/')
    assert response.status_code == 200
    assert b'Victor Hugo' in response.data
    
def test_auteur_update_before_login(client):
    response = client.get('/auteurs/1/update/', follow_redirects=True)
    assert b"Login" in response.data # vérifier redirection vers page Login
    
def login(client, username, password, next_path):
    return client.post( "/login/",data={"Login": username,"Password": password, "next":next_path} 
                       ,follow_redirects=True)
    
def test_auteur_update_after_login(client,testapp):
    with testapp.app_context():
        # user non connecté
        response=client.get('/auteurs/1/update/', follow_redirects=False)
        # Redirection vers la page de login
        assert response.status_code == 302
        # vérification redirection vers page Login
        assert "/login/?next=%2Fauteurs%2F1%2Fupdate%2F" in response.headers["Location"]
        # simulation connexion user
        response=login(client, "clement", "azerty", "/auteurs/1/update/")  # <-- juste cette ligne modifiée
        # Page update après connexion
        assert response.status_code == 200
        assert b"Modification de l'auteur Victor Hugo" in response.data

# --- Vue /auteurs/<id>/view/ : pas besoin de login ---
def test_auteur_view(client):
    response = client.get('/auteurs/1/view/')
    assert response.status_code == 200
    assert b'Victor Hugo' in response.data

# --- Vue /auteurs/<id>/delete : avant login ---
def test_auteur_delete_before_login(client):
    response = client.get('/auteurs/1/delete', follow_redirects=False)
    # devrait rediriger vers login (302 ou 308 selon Flask)
    assert response.status_code in [302, 308]
    assert "/login/" in response.headers["Location"]

# --- Vue /auteurs/<id>/delete : après login ---
def test_auteur_delete_after_login(client,testapp):
    with testapp.app_context():
        response=login(client, "clement", "azerty", "/auteurs/1/delete")
        assert response.status_code == 200
        # vérifier présence d'un texte de confirmation
        assert b"Suppression de l'auteur" in response.data or b"confirmation" in response.data

# --- Vue /auteurs/ : création (avant login) ---
def test_auteur_create_before_login(client):
    response = client.get('/auteurs/', follow_redirects=False)
    # selon ton code, création sans login peut rediriger
    assert response.status_code == 200 

# --- Vue /auteurs/ : création (après login) ---
def test_auteur_create_after_login(client,testapp):
    with testapp.app_context():
        response=login(client, "clement", "azerty", "/auteurs/")
        assert response.status_code == 200
        # vérifier que le formulaire de création est présent
        assert b"Ajouter" in response.data or b"Nom" in response.data