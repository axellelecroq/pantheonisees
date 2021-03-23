from flask import render_template, request, flash, redirect, url_for
import requests
import unidecode

from ..app import *
from ..modeles.data import *
from .general import toutes


"""
/person/<id>
/person/create
/person/<id>/modification
/person/<id>/delete

"""


@app.route("/person/<int:person_id>")
def person(person_id):
    """
    Route permettant l'affichage d'une personne panthéonisée
    précise. Cette page apparaît une fois que l'utilisateur.rice
    a cliqué sur le nom de cette personne soit dans la page toutes.html
    ou bien lors d'une recherche effectuée par lui ou elle-même.
    :param person_id : int
    :return: template person.html
    :rtype: template
    """
    if person_id:
        # Éxecution de la requête en fonction de l'ID de la personne
        person = Pantheonises.query.filter(Pantheonises.id == person_id).first()

        # Récupération de l'url afin de créer un lien vers la page
        # des résultats une fois la personne panthéonisée consultée
        referrer = request.referrer

        return render_template("pages/person.html", result=person, back_page=referrer)

    else:
        return render_template("errors/404.html"), 404


@app.route("/person/create", methods=["GET", "POST"])
def create_person():
    """
    Route permettant l'ajout d'une personne panthéonisée
    dans la base de données.
    :return: template person.html si l'ajout a été effectué
    avec succès, sinon template person_create.html
    :rtype: template
    """
    if request.method.lower() == "post":

        form_infos = {
            "name": request.form.get("name"),
            "firstname": request.form.get("firstname"),
            "birth_date": request.form.get("birthDate"),
            "death_date": request.form.get("deathDate"),
            "pantheonisation": request.form.get("pantheonisationDate"),
            "status": request.form.get("status"),
            "wikipedia": request.form.get("wikiLink"),
            "sex": request.form.get("sex"),
        }

        ## LES INFOS OBLIGATOIRES ##
        # Si un champ obligatoire est vide, alors un message d'erreur
        # est envoyé à l'utilisateur·rice
        if (
            not form_infos["name"]
            or not form_infos["firstname"]
            or not form_infos["birth_date"]
            or not form_infos["death_date"]
            or not form_infos["pantheonisation"]
            or not form_infos["status"]
            or not form_infos["wikipedia"]
        ):
            flash(
                "Tous les champs obligatoires doivent être renseignés.",
                category="error",
            )
            return render_template("pages/create.html")

        # Vérification qu'il y ait bien que des chiffres dans les dates
        # Si il y a une lettre, alors un message d'erreur est envoyé à l'utilisateur·rice
        if (
            Pantheonises.is_date(form_infos["birth_date"]) == False
            and Pantheonises.is_date(form_infos["death_date"]) == False
            and Pantheonises.is_date(form_infos["pantheonisation"]) == False
        ):
            flash(
                "Une des dates obligatoires entrées n'est pas valide.", category="error"
            )
            return render_template("pages/create.html")
        # Si non, les informations sont enregistrées dans la base de données.
        else:
            Pantheonises.add_new_person(form_infos)

        flash(
            "Une nouvelle personne a été ajoutée à la base de donnée.",
            category="success",
        )
        return redirect(url_for("toutes"))

    else:
        return render_template("pages/person_create.html")


@app.route("/person/<int:person_id>/modification", methods=["GET", "POST"])
def update_person(person_id):
    """
    Route permettant d'actualiser les informations d'une personne panthéonisée.
    :param person_id : int
    :return: template person.html
    :rtype: template
    """

    # Si l'utilisateur·rice a cliqué sur le bouton "valider" du formulaire
    if request.method.lower() == "post":
        # Récupération de la personne panthéonisée par son id
        # afin de pouvoir mettre à jour les informations
        person = Pantheonises.query.filter(Pantheonises.id == person_id).first()

        # Enregistrement des champs du formulaire au sein d'un dictionnaire
        form_infos = {
            "birth_date": request.form.get("birthDate"),
            "death_date": request.form.get("deathDate"),
            "pantheonisation": request.form.get("pantheonisationDate"),
            "status": request.form.get("status"),
            "wikipedia": request.form.get("wikiLink"),
            "p_path": "",
            "p_desc": request.form.get("descPortrait"),
            "p_date": request.form.get("portraitDate"),
            "t_path": "",
        }

        ## LES INFOS OBLIGATOIRES ##
        # Si un champ obligatoire est vide, alors un message d'erreur
        # est envoyé à l'utilisateur·rice
        if (
            not form_infos["birth_date"]
            or not form_infos["death_date"]
            or not form_infos["pantheonisation"]
            or not form_infos["status"]
            or not form_infos["wikipedia"]
        ):
            flash(
                "Tous les champs obligatoires doivent être renseignés.",
                category="error",
            )
            return render_template("pages/person_update.html", result=person)

        # Vérification qu'il y ait bien que des chiffres dans les dates
        # Si il y a une lettre, alors un message d'erreur est envoyé à l'utilisateur·rice
        if (
            Pantheonises.is_date(form_infos["birth_date"]) == False
            and Pantheonises.is_date(form_infos["death_date"]) == False
            and Pantheonises.is_date(form_infos["pantheonisation"]) == False
        ):
            flash(
                "Une des dates obligatoires entrées n'est pas valide.", category="error"
            )
            return render_template("pages/person_update.html", result=person)
        # Si non, les informations sont enregistrées dans la base de données.
        else:
            Pantheonises.add_required_info(person_id, form_infos)

            ## LES IMAGES ##
        ## Pour le portrait :
        if request.files["portraitFile"]:
            # Récuperation du fichier
            portrait_file = request.files["portraitFile"]

            # Renommage du fichier
            # Les espaces dans le(s) prénom(s) et nom(s) sont remplacés
            # par des tirets.
            name = unidecode.unidecode(person.name.replace(" ", "-").lower())
            firstname = unidecode.unidecode(person.firstname.replace(" ", "-").lower())
            # Le(s) prénom(s) et nom(s) sont séparés par un underscore.
            portrait_file.filename = "{}_{}.jpg".format(name, firstname)

            # Enregistrement du fichier  dans l'application
            Images.upload_image(portrait_file)

        # Création de la chaîne de charactère pour le chemin vers l'image
        if person.image_id:
            if person.image_id.portrait_path:
                form_infos["p_path"] = person.image_id.portrait_path
            else:
                form_infos["p_path"] = "/static/images/" + portrait_file.filename
        else:
            form_infos["p_path"] = "/static/images/" + portrait_file.filename

        if request.files["tombFile"]:
            ## Mêmes étapes pour la tombe que précédemment à savoir :
            # 1. Renommage du nom du fichier afin qu'il soit enregistré dans la base
            # 2. Enregistrement du fichier dans l'application
            # 3. Création du nom du chemin vers l'image
            # 4. Enregistrement des données vers la base

            # 1.
            tomb_file = request.files["tombFile"]
            name = unidecode.unidecode(person.name.replace(" ", "-").lower())
            firstname = unidecode.unidecode(person.firstname.replace(" ", "-").lower())
            tomb_file.filename = "{}_{}_tomb.jpg".format(name, firstname)

            # 2.
            Images.upload_image(tomb_file)

        # 3.
        if person.image_id:
            if person.image_id.tomb_path:
                form_infos["t_path"] = person.image_id.tomb_path
            else:
                form_infos["t_path"] = "/static/images/" + tomb_file.filename
        else:
            form_infos["t_path"] = "/static/images/" + tomb_file.filename

        # 4.
        Images.add_data_images(person_id, form_infos)

        # L'opération a été effectuée avec succès.
        flash("Les modifications ont bien été ajoutées.", category="success")
        return render_template("pages/person.html", result=person)

    # Si aucune requête "post" n'est faite, il s'agit alors que l'affichage
    # des données de la personne panthéonisée :
    elif person_id:
        # Récupération des données
        person = Pantheonises.query.filter(Pantheonises.id == person_id).first()
        # Envoi des données à la template
        return render_template("pages/person_update.html", result=person)
    else:
        return render_template("errors/404.html"), 404


@app.route("/person/<int:person_id>/delete", methods=["GET", "POST"])
def delete_person(person_id):
    """
    Route permettant de supprimer une personne panthéonisée de la base de données
    :param person_id : int
    :return: template toutes.html
    :rtype: template
    """
    p = Pantheonises.query.filter(Pantheonises.id == person_id).first()
    name = p.name + " " + p.firstname

    Pantheonises.delete_person(person_id)

    flash(name + " a bien été supprimé·e de la base.", category="success")
    return toutes()
