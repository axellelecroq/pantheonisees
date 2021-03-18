from ..app import *

from flask import flash
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import requests


class Pantheonises(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    firstname = db.Column(db.Text)
    status = db.Column(db.Text)
    pantheonisation = db.Column(db.Integer)
    birth = db.Column(db.Integer)
    death = db.Column(db.Integer)
    sex = db.Column(db.Text)
    wiki_link = db.Column(db.Text)

    image_id = db.relationship("Images", backref="pantheonises", uselist=False)

    def __init__(
        self,
        id,
        name,
        firstname,
        status,
        pantheonisation,
        birth,
        death,
        sex,
        wiki_link,
    ):
        self.id = id
        self.name = name
        self.firstname = firstname
        self.status = status
        self.pantheonisation = pantheonisation
        self.birth = birth
        self.death = death
        self.sex = sex
        self.wiki_link = wiki_link

    @staticmethod
    def add_new_person(infos: dict):
        """
        Méthode permettant d'ajouter une personne panthéonisée
        dans la base de données.
        :param infos : list
        """
        count = Pantheonises.query.filter(Pantheonises.id).count()

        person = Pantheonises(
            id=count + 1,
            name=infos["name"],
            firstname=infos["firstname"],
            status=infos["status"],
            pantheonisation=infos["pantheonisation"],
            birth=infos["birth_date"],
            death=infos["death_date"],
            sex=infos["sex"],
            wiki_link=infos["wikipedia"],
        )

        try:
            db.session.add(person)
            db.session.commit()
            return True
        except Exception as E:
            print(E)
            return False

    @staticmethod
    def add_required_info(id: int, infos: dict):
        """
        Méthode permettant d'ajouter les données obligatoires
        d'une personne panthéonisées dans la base de données.
        :param person_id : int
        :param infos : list
        """

        p = Pantheonises.query.filter(Pantheonises.id == id).first()
        p.birth = int(infos["birth_date"])
        p.death = int(infos["death_date"])
        p.pantheonisation = int(infos["pantheonisation"])
        p.status = infos["status"]
        p.wiki_link = infos["wikipedia"]

        db.session.commit()

    @staticmethod
    def is_date(date: str):
        """
        Méthode permettant de verifier qu'une chaîne de
        caractère ne comprend que des chiffres.
        :param date : str
        :rtype: booléen
        """
        for i in date:
            if i.isalpha() == True:
                return False
        return True

    @staticmethod
    def is_valid_url(url: str):
        """
        Méthode permettant de verifier qu'une chaîne
        de caractère est un lien valide.
        :param url : str
        :rtype: booléen
        """
        try:
            requests.get(url)
            return True
        except Exception as E:
            print(E)
            return False


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pers_id = db.Column(db.Integer, db.ForeignKey("pantheonises.id"))
    portrait_path = db.Column(db.Text)
    portrait_desc = db.Column(db.Text)
    date = db.Column(db.Text)
    tomb_path = db.Column(db.Text)

    def __init__(
        self,
        id,
        pers_id,
        portrait_path,
        portrait_desc,
        date,
        tomb_path,
    ):
        self.id = id
        self.pers_id = pers_id
        self.portrait_path = portrait_path
        self.portrait_desc = portrait_desc
        self.date = date
        self.tomb_path = tomb_path

    @staticmethod
    def upload_image(file):
        """
        Méthode permettant de télécharger un fichier
        dans le dossier prévu pour les images de l'application.
        :param file : file
        """
        try:
            file.save(os.path.join(img, secure_filename(file.filename)))
        except Exception as E:
            print(E)
            flash(
                "Une erreur est survenue lors de l'enregistrement de l'image.",
                category="error",
            )

    @staticmethod
    def add_data_images(id: int, infos: dict):
        """
        Méthode permettant d'ajouter les données concernant
        les images dans la base de données
        :param id : int
        :param infos : dict
        """
        p = Pantheonises.query.filter(Pantheonises.id == id).first()
        count = Images.query.filter(Images.id).count()

        if p.image_id:
            p.image_id.portrait_path = infos["p_path"]
            p.image_id.portrait_desc = infos["p_desc"]
            p.image_id.date = infos["p_date"]
            p.image_id.tomb_path = infos["t_path"]

            db.session.commit()

        else:
            img = Images(
                id=count + 1,
                pers_id=id,
                portrait_path=infos["p_path"],
                portrait_desc=infos["p_desc"],
                date=infos["p_date"],
                tomb_path=infos["t_path"],
            )

            try:
                db.session.add(img)
                db.session.commit()
                return True
            except Exception as E:
                print(E)
                return False


class User(UserMixin, db.Model):
    id = db.Column(
        db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True
    )
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    @staticmethod
    def connexion(identifiant: str, motdepasse: str):
        """
        Méthode permettant de connecter l'utilisateur.rice
        :param identifiant : str
        :param motdepasse : str
        """
        user = User.query.filter(User.username == identifiant).first()
        if user and check_password_hash(user.password, motdepasse):
            return user

    @staticmethod
    def inscription(identifiant: str, motdepasse: str, mail: str) -> bool:
        """
        Méthode permettant d'inscrire un.e l'utilisateur.rice
        :param identifiant : str
        :param motdepasse : str
        """

        user_count = User.query.filter(User.id).count()

        user = User(
            id=user_count + 1,
            username=identifiant,
            password=generate_password_hash(motdepasse),
            email=mail,
        )

        try:
            db.session.add(user)
            db.session.commit()
            return True
        except Exception as E:
            print(E)
            return False

    @staticmethod
    def is_unique(identifiant: str):
        user = User.query.filter(User.username == identifiant).count()
        # email = User.query.filter(User.email = mail).count()
        # if email:
        #     flash(
        #         "Cet email a déjà un compte.",
        #         category="error",
        #     )
        #     return False
        if user:
            return False
        else:
            return True

    def get_id(self) -> int:
        return self.id


@login.user_loader
def charger_utilisateur(identifiant: int):
    return User.query.get(identifiant)


# Enfin on indique à l'ORM via la méthode .commit()
# de faire les requêtes nécéssaires pour finaliser les
# opérations d'ajouts dans la table.

# db.session.commit()
db.create_all()
