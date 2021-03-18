from ..app import *
from . import user, pantheonisees

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