# Import des libraires standards
import os

# Import des libraires tierces
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from .contants import CONFIG


# Déclarations liées au module os :
chemin_actuel = os.path.dirname(os.path.abspath(__file__))

# Stockage des différents chemin dans des variables
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")
img = os.path.join(statics, "images")

app = Flask("pantheonisees", template_folder=templates, static_folder=statics)


login = LoginManager(app)

# la base de donnée est stockée dans une variable db
db = SQLAlchemy(app)

# Imports locaux
from .modeles.data import *
from .modeles.user import *
from .routes import general, search, errors, user, crud_person


def config_app(config_name="test"):
    """ Create the application """

    app.config.from_object(CONFIG[config_name])

    # Set up extensions
    db.init_app(app)
    login.init_app(app)

    return app
