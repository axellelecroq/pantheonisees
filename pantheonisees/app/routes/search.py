from flask import render_template, request
from sqlalchemy import and_

from ..app import *
from ..modeles.pantheonisees import *


@app.route("/recherche")
def recherche():
    """
    Route permettant d'effectuer une recherche dans la base de donnés
    avec un ou plusieurs mots clés.
    Les résultats sont affichés par ordre alphabétique.
    :return: template search.html
    :rtype: template
    """
    # Booléan qui permet de vérifier si
    # l'utilisateur.rice a entré au
    # moins un mot clé.
    no_search = True

    # Liste qui recevra les résultats de la recherche
    resultats = []

    # Liste qui permet de stocker les mots clés
    # entrés par l'utilisateur.rice
    search_list = [i for i in request.args.values()]

    for i in search_list:
        if i:
            no_search = False

            # Si la variable est le 3e élément de la liste
            # à savoir la date de panthéonisation qui est,
            # dans le formulaire enregistré comme str
            # alors on le parse en int. Cela
            # permet d'effectuer la recherche dans la base de données
            # dans laquelle les dates sont enregistrées en int et
            # non en text.
            if i == search_list[2]:
                search_list[2] = int(search_list[2])

            # Requête avec tous les mots clés, enregistrés
            # auparavant dans la liste search_list. Les résultats
            # sont directement stockés dans la liste instancié
            # avant la boucle for.
            resultats = (
                Pantheonises.query.filter(
                    and_(
                        Pantheonises.name.like(f"%{search_list[0]}%"),
                        Pantheonises.firstname.like(f"%{search_list[1]}%"),
                        Pantheonises.pantheonisation.like(f"%{search_list[2]}%"),
                        Pantheonises.status.like(f"%{search_list[3]}%"),
                    )
                )
                .order_by(Pantheonises.name, Pantheonises.firstname)
                .all()
            )

    return render_template("pages/search.html", search=no_search, results=resultats)
