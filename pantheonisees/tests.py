from .app.app import *
from .app.modeles.user import User
from .app.modeles.data import Pantheonises

from unittest import TestCase


# pour lancer les tests : python -m unittest discover 


class Base(TestCase):
    # Configuration de la base de données :
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./db_test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    pantheonises = [
        Pantheonises(
            id = 101,
            name = "Riqueti de Mirabeau",
            firstname = "Honoré-Gabriel",
            status = "diplomate, journaliste et homme politique français",
            pantheonisation = 1792,
            birth = 1749,
            death = 1791,
            sex = "homme",
            wiki_link = "https://fr.wikipedia.org/wiki/Honor%C3%A9-Gabriel_Riqueti_de_Mirabeau",
        ), 
        Pantheonises(
            id =102,
            name = "Marat",
            firstname = "Jean-Paul",
            status = "dmédecin, physicien, journaliste et homme politique français, révolutionnaire",
            pantheonisation = 1793,
            birth = 1743,
            death = 1793,
            sex = "homme",
            wiki_link = "https://fr.wikipedia.org/wiki/Jean-Paul_Marat",
        )]

    def setUp(self):
        self.app = app
        self.client = app.test_client()
        self.db = db
        self.db.create_all(app=self.app)

    def tearDown(self):
        self.db.drop_all(app=self.app)

    def insert_all(self, pantheonises):
        # On donne à notre DB le contexte d'exécution
        with self.app.app_context():
            if pantheonises:
                for fixture in self.pantheonises:
                    self.db.session.add(fixture)
            self.db.session.commit()


class TestUser(Base):
    """ Unit tests for Users """
    def test_registration(self):
        with self.app.app_context():
            statut = User.inscription(
                identifiant="helloworld",
                motdepasse="helloworld1",
                mail="hello.world@chartes.psl.eu",
            )
                      
            user = User.query.filter(User.email == "hello.world@chartes.psl.eu").first()
        self.assertEqual(user.username, "helloworld")
        self.assertNotEqual(user.password, "helloworld1")
        self.assertTrue(statut)

    def test_registration_login(self):
        with self.app.app_context():
            statut = User.inscription(
                identifiant="helloworld",
                motdepasse="helloworld1",
                mail="hello.world@chartes.psl.eu",
            )

            user_connected = User.connexion("helloworld", "helloworld1")
            
        self.assertTrue(user_connected)
        self.assertTrue(statut)