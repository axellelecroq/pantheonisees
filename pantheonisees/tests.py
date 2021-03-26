from .app.app import db, login
from .app.modeles.user import *
from .app.modeles.data import *

from unittest import TestCase


class Base(TestCase):
    pantheonises = [
        Pantheonises(
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
            user = User.inscription()
            statut, utilisateur = User.creer("joh", "johanna.johanna@enc-sorbonne.fr", "Johanna", "azerty")
            query = User.query.filter(User.user_email == "johanna.johanna@enc-sorbonne.fr").first()
        self.assertEqual(query.user_nom, "Johanna")
        self.assertEqual(query.user_login, "joh")
        self.assertNotEqual(query.user_password, "azerty")
        self.assertTrue(statut)

    def test_login_et_creation(self):
        with self.app.app_context():
            statut, cree = User.creer("joh", "johanna.johanna@enc-sorbonne.fr", "Johanna", "azerty")
            connecte = User.identification("joh", "azerty")

        self.assertEqual(cree, connecte)
        self.assertTrue(statut)