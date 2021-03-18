# Import des libraires standards
import os

# Import des libraires tierces
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# Déclarations liées au module os :
chemin_actuel = os.path.dirname(os.path.abspath(__file__))

# on stocke le chemin du fichier courant

templates = os.path.join(chemin_actuel, "templates")

# on stocke le chemin vers les template\s

statics = os.path.join(chemin_actuel, "static")

# on stocke le chemin vers les pages éléments de "statics"

img = os.path.join(statics, "images")


# Instanciation de l'application, il n'est pas utile
# de donner un nom particulier à l'application,
# mais par soucis de clarté et dans le cadre de dévellopements ultérieurs,
# le choix a été fait de conserver un nom personalisé.

# Ajout des paramètres, liens vers les dossiers déclarés par le module os


app = Flask("pantheonisees", template_folder=templates, static_folder=statics)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# Configuration de la base de données :

# Lien avec la base de données sqlite

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./db_pantheonises.db"
app.config["SECRET_KEY"] = "JeSuisUnSecret"


# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login = LoginManager(app)

# On initie l'extension SQLAlchemy à l'application Flask;
# la BDD est stocké dans une variable db

db = SQLAlchemy(app)

# On relie les routes à l'application.
# Elles sont situées à la fin, car il faut d'abord déclarer
# la variable app pour que l'import des routes
# soit opérationnel

#  db.create_all()


# Imports locaux
from .modeles import *
from .routes import general, search, errors, connexion, crud_person
