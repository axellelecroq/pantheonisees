# Import librairies installées via PIP
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

# Import de mes propres modules
from app.app import app, login
from app.modeles import *
from ..modeles.data import *


@app.route("/connexion", methods=["GET", "POST"])
def connexion():
    """
    Route permettant la connexion de l'utilisateur.rice
    :return: redirection vers la page home.html si la connexion a été effectuée avec succès
             sinon templace connexion.html
    :rtype: template
    """
    if request.method.lower() == "post":
        # Récupérations des données du formulaire
        ident = request.form.get("login")
        pw = request.form.get("password")
        user = User.connexion(ident, pw)
        # Si l'utilisateur·rice est bien dans la base de données
        # et que les données envoyées correspondent avec celles stockées
        if user:
            # alors la connexion réussie
            login_user(user)
            flash("Vous êtes connecté·e", category="success")
            return redirect(url_for("accueil"))
        else:
            # sinon envoi d'un message d'erreur sous forme de flashed message.
            flash("Connexion infructueuse", category="error")

    return render_template("pages/connexion.html")


@app.route("/deconnexion")
def deconnexion():
    """
    Route permettant la déconnexion de l'utilisateur.rice
    :return: redirection vers la page d'accueil
    :rtype: template
    """

    # Vérification si l'utilisateur.rice est connectée
    if current_user.is_authenticated:
        # afin de pouvoir le·la déconnecter
        logout_user()
        flash("Vous êtes déconnecté·e", category="success")
    else:
        flash("Non connecté·e", category="error")
    return redirect(url_for("accueil"))


@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    """
    Route permettant l'inscription d'un.e nouvel.le utilisateur.rice
    :return: template login.html si erreur lors de l'inscription
             ou redirection vers la page home.html si l'inscription a été effectuée avec succès.
    :rtype: template
    """

    if request.method.lower() == "post":
        # Inscription de l'utilisateur-rice
        ident = request.form.get("login")
        pw = request.form.get("password")
        email = request.form.get("email")
        errors = []

        # Vérification si le nom d'utilisateur.rice est disponible
        is_unique = User.is_unique(identifiant=ident, mail=email)
        if is_unique is False:
            return render_template("pages/login.html")

        # Vérifications validité de l'identifiant
        elif not ident:
            errors.append("Aucun identifiant renseigné")
        elif len(ident) < 8:
            errors.append(
                "Votre identifiant est trop court. Veuillez entrer un identifiant avec au moins 8 caractères."
            )

        # Vérifications validité du mot de passe
        elif not pw:
            errors.append("Mot de passe non renseigné")
        elif len(pw) < 8:
            errors.append(
                "Votre mot de passe trop court. Veuillez entrer un mot de passe avec au moins 8 caractères."
            )

        # Inscription si aucune erreur n'a été rencontrée
        if not errors:
            User.inscription(ident, pw, email)
            flash("Vous êtes inscrit·e", category="success")
            return redirect(url_for("accueil"))
        # Sinon envoi de toutes les erreurs sous forme de flashed messages
        else:
            for error in errors:
                flash(error, category="error")

    return render_template("pages/login.html")


# Définit la page où l'utilisateur·rice est redirigé·e quand iel n'est pas connecté·e
login.login_view = connexion
