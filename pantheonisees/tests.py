from .app.app import config_app, login, db
from .app.modeles.data import Pantheonises
from .app.modeles.user import User

from unittest import TestCase

# Lors de la rédaction des tests, j'ai suivi le "3A pattern" :
# "arrange, act, assert". Suivre ce principe est considéré être
# une bonne pratique dans la rédaction des tests et permet
# d'uniformiser leur structure. Dans l'article mentionné
# ci-dessous, il est écrit que cette structure uniforme
# est l'un de ses plus grands avantages : une fois habitué·e à
# ce modèle, on peut lire et comprendre les tests plus facilement.
# Ce qui, à son tour, réduit le coût de maintenance de l'ensemble
# de notre suite de test.
# L'article en question :
# https://freecontent.manning.com/making-better-unit-tests-part-1-the-aaa-pattern/

# pour lancer les tests : python -m unittest discover


class Base(TestCase):
    # Configuration de la base de données :
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./db_test.db"
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    pantheonises = [
        Pantheonises(
            id=101,
            name="Riqueti de Mirabeau",
            firstname="Honoré-Gabriel",
            status="diplomate, journaliste et homme politique français",
            pantheonisation=1792,
            birth=1749,
            death=1791,
            sex="homme",
            wiki_link="https://fr.wikipedia.org/wiki/Honor%C3%A9-Gabriel_Riqueti_de_Mirabeau",
        ),
        Pantheonises(
            id=102,
            name="Marat",
            firstname="Jean-Paul",
            status="dmédecin, physicien, journaliste et homme politique français, révolutionnaire",
            pantheonisation=1793,
            birth=1743,
            death=1793,
            sex="homme",
            wiki_link="https://fr.wikipedia.org/wiki/Jean-Paul_Marat",
        ),
    ]

    def setUp(self):
        self.app = config_app("test")
        self.db = db
        self.client = self.app.test_client()
        self.db.create_all(app=self.app)

    def tearDown(self):
        self.db.drop_all(app=self.app)

    def insert_pantheonises(self, pantheonises):
        with self.app.app_context():
            for person in pantheonises:
                Pantheonises.add_new_person(person)


class TestUser(Base):
    """ Unit tests for Users """

    def test_registration(self):
        with self.app.app_context():
            # Afin d'illustrer ce qui a été mentionné plus haut,
            # ce test est accompagné de commentaires permettant
            # d'identifier chacune des parties du "3A pattern".
            # Dans les tests suivants, les parties seront séparées
            # par un saut de ligne.

            # Arrange
            statut = User.inscription(
                "helloworld", "helloworld1", "hello.world@chartes.psl.eu"
            )

            # Act
            db_user = User.query.filter(
                User.email == "hello.world@chartes.psl.eu"
            ).first()

        # Assert
        self.assertEqual(db_user.username, "helloworld")
        self.assertNotEqual(db_user.password, "helloworld1")
        self.assertTrue(statut)

    def test_login(self):
        with self.app.app_context():
            statut = User.inscription(
                "helloworld", "helloworld1", "hello.world@chartes.psl.eu"
            )

            user_connected = User.connexion("helloworld", "helloworld1")

        self.assertTrue(user_connected)


class TestPantheonises(Base):
    """ Unit tests for Pantheonises """

    pantheonises = [
        Pantheonises(
            id=101,
            name="Riqueti de Mirabeau",
            firstname="Honoré-Gabriel",
            status="diplomate, journaliste et homme politique français",
            pantheonisation=1792,
            birth=1749,
            death=1791,
            sex="homme",
            wiki_link="https://fr.wikipedia.org/wiki/Honor%C3%A9-Gabriel_Riqueti_de_Mirabeau",
        ),
        Pantheonises(
            id=102,
            name="Marat",
            firstname="Jean-Paul",
            status="médecin, physicien, journaliste et homme politique français, révolutionnaire",
            pantheonisation=1793,
            birth=1743,
            death=1793,
            sex="homme",
            wiki_link="https://fr.wikipedia.org/wiki/Jean-Paul_Marat",
        ),
    ]

    def test_pantheonises_is_added(self):
        with self.app.app_context():
            for fixture in self.pantheonises:
                self.db.session.add(fixture)
            self.db.session.commit()

            person = Pantheonises.query.filter(
                Pantheonises.id == 102
            ).first()

        self.assertEqual(person.name, "Marat")
        self.assertEqual(person.birth, 1743)
