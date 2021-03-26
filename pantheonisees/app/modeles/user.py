from ..app import *

from flask import flash
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from validate_email import validate_email


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
    def is_unique(identifiant: str, mail: str):
        """
        Méthode permettant de vérifier que le mail et l'identifiant
        proposés le.la nouveau.elle utilisateur.rice
        :param identifiant : str
        :param mail : str
        :rtype: bool
        """
        user = User.query.filter(User.username == identifiant).count()
        email = User.query.filter(User.email == mail).count()
        if email:
            flash(
                "Cet email a déjà un compte.",
                category="error",
            )
            return False
        elif user:
            flash(
                "Cet identifiant est déjà utilisé par un·e autre utilisateur·rice. Veuillez en proposer un nouveau.",
                category="error",
            )
            return False
        else:
            return True

    @staticmethod
    def is_valid_email(mail) -> bool:
        """
        Méthode permettant de vérifier que le mail proposé
        est valide ou non
        :param mail : str
        :rtype: bool
        """
        if validate_email(mail) == True:
            return True
        else:
            return False

    def get_id(self) -> int:
        return self.id


@login.user_loader
def charger_utilisateur(identifiant: int):
    return User.query.get(identifiant)


db.create_all()
