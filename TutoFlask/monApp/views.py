from .app import app
from flask import render_template, request
from monApp.models import *
from monApp.forms import *
from flask import url_for , redirect
from .app import db
from flask_login import *
from flask import flash
from sqlalchemy.exc import IntegrityError

@app.route('/')
@app.route('/index/')
def index():
    # si pas de paramètres
    if len(request.args)==0:
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name="Cricri")
    else :
        param_name = request.args.get('name')
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name=param_name)

@app.route('/contact')
def contact():
    return render_template("contact.html",title ="R3.01 Dev Web avec Flask",name="Lechop")

@app.route('/about')
def about():
    return render_template("about.html",title ="R3.01 Dev Web avec Flask",name="Arsouze")

@app.route('/auteurs/')
def getAuteurs():
    lesAuteurs = Auteur.query.all()
    return render_template('auteurs_list.html', title="R3.01 Dev Web avec Flask", auteurs=lesAuteurs)

@app.route('/livres/')
def getLivres():
    lesLivres = Livre.query.all()
    print(Livre.query.count())
    return render_template('livre_list.html', title="R3.01 Dev Web avec Flask", livres=lesLivres)

@app.route('/auteurs/<idA>/update/')
@login_required
def updateAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_update.html",selectedAuteur=unAuteur, updateForm=unForm)

@app.route('/auteur/save/', methods=("POST",))
@login_required
def saveAuteur():
    unForm = FormAuteur()
    updatedAuteur = None
    if unForm.validate_on_submit():
        idA = int(unForm.idA.data)
        updatedAuteur = Auteur.query.get(idA)
        
        # Vérifie si un autre auteur a déjà ce nom
        if Auteur.query.filter(Auteur.Nom == unForm.Nom.data, Auteur.idA != idA).first():
            flash("Un auteur avec ce nom existe déjà.", "warning")
            return render_template("auteur_update.html", selectedAuteur=updatedAuteur, updateForm=unForm)
        
        # Mise à jour si tout est ok
        updatedAuteur.Nom = unForm.Nom.data
        try:
            db.session.commit()
            flash("Auteur mis à jour avec succès !", "success")
            return redirect(url_for('viewAuteur', idA=updatedAuteur.idA))
        except IntegrityError:
            db.session.rollback()
            flash("Ce nom d'auteur existe déjà.", "danger")
            return render_template("auteur_update.html", selectedAuteur=updatedAuteur, updateForm=unForm)
    
    return render_template("auteur_update.html", selectedAuteur=updatedAuteur, updateForm=unForm)


@app.route('/auteurs/<idA>/view/')
def viewAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur (idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_view.html",selectedAuteur=unAuteur, viewForm=unForm)

@app.route('/auteur/')
@login_required
def createAuteur():
    unForm = FormAuteur()
    return render_template("auteur_create.html", createForm=unForm)

@app.route('/auteur/insert/', methods=("POST",))
@login_required
def insertAuteur():
    unForm = FormAuteur()
    if unForm.validate_on_submit():
        # Vérifie si le nom existe déjà
        if Auteur.query.filter_by(Nom=unForm.Nom.data).first():
            flash("Ce nom d'auteur existe déjà. Veuillez en choisir un autre.", "danger")
            return render_template("auteur_create.html", createForm=unForm)

        insertedAuteur = Auteur(Nom=unForm.Nom.data)
        db.session.add(insertedAuteur)
        try:
            db.session.commit()
            flash("Auteur créé avec succès !", "success")
            return redirect(url_for('viewAuteur', idA=insertedAuteur.idA))
        except IntegrityError:
            db.session.rollback()
            flash("Ce nom d'auteur existe déjà. Veuillez en choisir un autre.", "danger")
            return render_template("auteur_create.html", createForm=unForm)
    
    return render_template("auteur_create.html", createForm=unForm)


@app.route('/auteurs/<idA>/delete/')
@login_required
def deleteAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA, Nom=unAuteur.Nom)
    return render_template("auteur_delete.html",selectedAuteur=unAuteur, deleteForm=unForm)

@app.route ('/auteur/erase/', methods =("POST" ,))
@login_required
def eraseAuteur():
    deletedAuteur = None
    unForm = FormAuteur()
    #recherche de l'auteur à supprimer
    idA = int(unForm.idA.data)
    deletedAuteur = Auteur.query.get(idA)
    #suppression
    db.session.delete(deletedAuteur)
    db.session.commit()
    return redirect(url_for('getAuteurs'))

@app.route('/livres/<idL>/update/')
@login_required
def updateLivre(idL):
    unLivre = Livre.query.get(idL)
    unForm = FormLivre(idL=unLivre.idL , Prix=unLivre.Prix)
    return render_template("livre_update.html",selectedLivre=unLivre, updateForm=unForm)

@app.route('/livre/save/', methods=("POST",))
@login_required
def saveLivre():
    updatedLivre = None
    unForm = FormLivre()
    # recherche du livre à modifier
    print(unForm.idL.data)
    idL = int(unForm.idL.data)
    updatedLivre = Livre.query.get(idL)
    # si les données saisies sont valides pour la mise à jour
    if unForm.validate_on_submit():
        print("je passe")
        updatedLivre.Prix = unForm.Prix.data
        db.session.commit()
        return redirect(url_for('viewLivre', idL=updatedLivre.idL))
    return render_template("livre_update.html", selectedLivre=updatedLivre, updateForm=unForm)


@app.route('/livres/<idL>/view/')
def viewLivre(idL):
    unLivre = Livre.query.get(idL)
    unForm = FormLivre(idL=unLivre.idL, Titre=unLivre.Titre)
    return render_template("livre_view.html", selectedLivre=unLivre, viewForm=unForm)

@app.route ("/login/", methods =("GET","POST" ,))
def login():
    unForm = LoginForm()
    unUser=None
    if not unForm.is_submitted():
        unForm.next.data = request.args.get('next')
    elif unForm.validate_on_submit():
        unUser = unForm.get_authenticated_user()
        if unUser:
            login_user(unUser)
            next = unForm.next.data or url_for("index",name=unUser.Login)
            return redirect (next)
    return render_template ("login.html",form=unForm)


@app.route ("/logout/")
def logout():
    logout_user()
    return redirect ( url_for ('index'))

@app.route('/livres/auteur', methods=['GET'])
def livresParAuteur():
    nom = request.args.get('nomAuteur', '').strip()

    if nom == '':
        return render_template('livres_par_auteur.html', livres=None)

    livres = Livre.query.join(Auteur).filter(Auteur.Nom.ilike(f"%{nom}%")).all()

    return render_template('livres_par_auteur.html', livres=livres)


if __name__ == "__main__":
    app.run()
