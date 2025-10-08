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
