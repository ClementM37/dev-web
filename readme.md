# Clément Moisan Projet Flask
## TP1
J'ai oublié de mettre a jour mon readme pour cette séance
## TP2 
- Mise en place d’une base de données SQLite dans un projet Flask.

- Installation et configuration de SQLAlchemy pour gérer la communication entre Flask et la base de données.

- Définition de modèles Python (Auteur, Livre) correspondant aux tables de la base.

- Ajout d’une commande personnalisée loaddb permettant de créer les tables et de les peupler à partir d’un fichier YAML grâce à PyYAML.

- Découverte et utilisation du shell Flask pour interagir directement avec les modèles : requêtes de sélection, filtres, récupération par identifiant, relations entre tables.

- Manipulation des données avec SQLAlchemy : ajout, modification et suppression d’enregistrements, validation avec session.commit().
## TP3
- Compréhension de l’architecture MVT (Modèle – Vue – Template) et de son rôle dans l’organisation d’un projet Flask.

- Mise en place de premiers templates HTML (index.html) permettant d’afficher des variables Python passées par les vues (ex. title et name).

- Création et modification de vues dans views.py à l’aide du décorateur @app.route, avec gestion de plusieurs URL pour une même fonction.

- Ajout d’un fichier CSS statique (style.css) dans le répertoire static/ et utilisation de url_for('static', filename='style.css') dans les templates pour lier les styles.

- Définition de nouvelles routes et templates (about.html, contact.html) afin de séparer les différentes pages du site.

- Mise en pratique des concepts :
    - Une vue génère la réponse HTTP (contenu renvoyé).

    - Un template affiche dynamiquement des variables Python.

## TP4
- Mise en place de l’héritage de templates avec base.html

- Utilisation du moteur de templates Jinja2

- Affichage de données issues de la base avec SQLAlchemy

- Création d’une vue listant les auteurs (/auteurs/)

- Ajout et stylisation de tableaux HTML

- Installation et configuration de Bootstrap (Flask-Bootstrap5)

- Ajout d’une barre de navigation et adaptation du design avec Bootstrap

## TP5

- Création du fichier forms.py avec la classe FormAuteur

- Mise en place d’un formulaire sécurisé avec clé secrète et token CSRF

- Implémentation complète du CRUD sur les auteurs :

    - Création d’un auteur (create/insert), Lecture/consultation d’un auteur (view), Modification d’un auteur (update/save) et Suppression d’un auteur (delete/erase)

- Ajout de la gestion et de l’affichage des erreurs de validation

- Ajout des liens de navigation entre les différentes actions CRUD

- Application du même principe pour les livres (modification du prix uniquement)

## TP6

- Installation et configuration de Flask-Login pour gérer l'authentification des utilisateurs

- Création du modèle User avec Login et Password (crypté en SHA256) héritant de UserMixin

- Ajout de commandes CLI personnalisées :
    - `syncdb` pour créer les tables manquantes dans la base de données
    - `newuser` pour ajouter un utilisateur avec mot de passe hashé
    - `newpasswrd` pour modifier le mot de passe d'un utilisateur existant

- Mise en place du LoginManager et du callback user_loader dans models.py

- Création du formulaire LoginForm avec méthode get_authenticated_user() pour vérifier les identifiants

- Implémentation des vues d'authentification :
    - Vue /login/ (GET et POST) avec formulaire de connexion
    - Vue /logout/ pour déconnecter l'utilisateur

- Ajout du template login.html pour afficher le formulaire de connexion

- Modification de base.html pour afficher l'utilisateur connecté et les liens de connexion/déconnexion

- Protection des vues sensibles avec le décorateur @login_required

- Mise en place de la redirection automatique :
    - Configuration de login_manager.login_view
    - Ajout du champ HiddenField next dans LoginForm
    - Redirection vers la page initialement demandée après authentification réussie

- Restriction de l'accès : consultation libre pour tous, modification/suppression réservées aux utilisateurs authentifiés

## TP7

- Installation des outils de test : pytest, pytest-flask et coverage

- Configuration des tests avec création du fichier conftest.py :
    - Fixture testapp pour créer une application de test avec base SQLite en mémoire
    - Désactivation de la protection CSRF pour les tests
    - Création d'un jeu de données de test (auteur, livre, user)
    - Fixture client pour simuler les requêtes HTTP

- Tests unitaires du modèle dans tests/unit/ :
    - test_models_auteur.py : test de l'initialisation et de la représentation
    - test_models_livre.py : test du modèle Livre
    - test_models_user.py : test du modèle User et de la fonction load_user()

- Tests fonctionnels des vues GET dans tests/functional/test_routes_auteur.py :
    - Test des vues publiques (liste, consultation)
    - Test de la redirection vers login pour les vues protégées
    - Création d'une fonction login() pour simuler l'authentification
    - Test des vues après authentification

- Tests fonctionnels des formulaires POST dans tests/functional/test_forms_auteur.py :
    - Test de la soumission du formulaire de Capture d’écran_2025-10-16_15-15-30modification (/auteur/save/)
    - Test de la création d'auteur (/auteur/insert/)
    - Test de la suppression d'auteur (/auteur/erase/)
    - Vérification des redirections et de la mise à jour en base de données

- Application des tests aux livres pour atteindre plus de 90% de couverture

- Configuration de .coveragerc pour exclure certains fichiers du calcul de couverture

- Utilisation des commandes coverage :
    - `coverage run -m pytest` pour exécuter les tests avec mesure de couverture
    - `coverage report -m` pour afficher le rapport dans le terminal
    - `coverage html` pour générer un rapport HTML détaillé

## Travail Bonus
- Ajout de la recherche de livre avec le nom d'un auteur.

## Image des testes 

![Image du coverage](/TutoFlask/Poucentage_teste.png)
