from app.app import db, login
from app.modeles.user import *
from app.modeles.data import *


from unittest import TestCase


class Base(TestCase):
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
        self.app = config_app("test")
        self.db = db
        self.client = self.app.test_client()
        self.db.create_all(app=self.app)

    def tearDown(self):
        self.db.drop_all(app=self.app)

    def insert_all(self, person=True):
        # On donne à notre DB le contexte d'exécution
        with self.app.app_context():
            if person:
                for fixture in self.person:
                    self.db.session.add(fixture)
            self.db.session.commit()


class TestUser(Base):
    """ Unit tests for Users """
    def test_registration(self):
        with self.app.app_context():
            statut, user = User.inscription(
                username="helloworld",
                password="helloworld1",
                email="hello.world@chartes.psl.eu",
            )
                      
            query = User.query.filter(User.user_email == "hello.world@chartes.psl.eu").first()
        self.assertEqual(query.username, "helloworld")
        self.assertNotEqual(query.user_password, "helloworld1")
        self.assertTrue(statut)

    def test_login_et_creation(self):
        with self.app.app_context():
            statut, user = User.inscription(
                username="helloworld",
                password="helloworld1",
                email="hello.world@chartes.psl.eu",
            )

            connected = User.connexion("helloworld", "helloworld1")

        self.assertEqual(user, connected)
        self.assertTrue(statut)