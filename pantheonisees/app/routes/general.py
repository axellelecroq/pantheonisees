from flask import render_template
from ..app import *
from ..modeles.pantheonisees import *


"""
/
/toutes
/a_propos
/chiffres 

"""


@app.route("/")
def accueil():
    """
    Route permettant l'affichage de la page d'accueil
    :return: template home.html de la page d'accueil
    :rtype: template
    """
    return render_template("pages/home.html")


@app.route("/toutes")
def toutes():
    """
    Route permettant l'affichage de toutes les personnes
    panthéonisées enregistrées dans la base de données
    :return: template toutes.html
    :rtype: template
    """

    # Requête permettant de récupérer toutes les personnes
    # dans la base de donnée. Elles sont ordonnées par leur nom.
    all_person = Pantheonises.query.order_by(Pantheonises.name).all()

    return render_template("pages/toutes.html", toutes=all_person)


# ROUTES DES PAGES ANNEXES
# Route vers la page à propos
@app.route("/a_propos")
def a_propos():
    """
    Route permettant l'affichage de la page à propos
    :return: template about.html
    :rtype: template
    """
    return render_template("pages/about.html")


@app.route("/chiffres")
def chiffres():
    """
    Route permettant l'affichage de la page "en chiffre"
    :return: template dataviz.html
    :rtype: template
    """
    return render_template("pages/dataviz.html")
