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
# de notre suite de tests.
# L'article en question :
# https://freecontent.manning.com/making-better-unit-tests-part-1-the-aaa-pattern/

# Pour lancer les tests :
# 1. Être au  niveau du fichier requirements.txt
# 2. Lancer : python -m unittest discover


class Base(TestCase):
    # Les données tests, appelées aussi fixtures sont enregistrées
    # dans un dictionnaire, eux-mêmes enregistrés dans une liste.
    pantheonises = [
        {
            "name": "Marat",
            "firstname": "Jean-Paul",
            "birth_date": "1743",
            "death_date": "1793",
            "pantheonisation": "1793",
            "status": "médecin, physicien, journaliste et homme politique français, révolutionnaire",
            "wikipedia": "https://fr.wikipedia.org/wiki/Jean-Paul_Marat",
            "sex": "homme",
        },
        {
            "name": "Riqueti de Mirabeau",
            "firstname": "Honoré-Gabriel",
            "birth_date": "1749",
            "death_date": "1791",
            "pantheonisation": "1792",
            "status": "diplomate, journaliste et homme politique français",
            "wikipedia": "https://fr.wikipedia.org/wiki/Honor%C3%A9-Gabriel_Riqueti_de_Mirabeau",
            "sex": "homme",
        },
    ]

    # D'après la documentation, il est généralement conseillé
    # de créer et de supprimer les fixtures à chaque
    # exécution de test, afin de garantir des tests propres.
    # Lire la partie "Testing with SQLAlchemy" : https://pythonhosted.org/Flask-Testing/
    def setUp(self):
        # Configuration de la base de données-test
        self.app = config_app("test")
        self.db = db
        self.client = self.app.test_client()
        self.db.create_all(app=self.app)

    def tearDown(self):
        # Les fixtures sont supprimés de la base de données-test
        # une fois que tous les tests ont été effectué.
        self.db.drop_all(app=self.app)

    def insert_pantheonises(self, pantheonises):
        # Contexte d'exécution donné à la DB
        with self.app.app_context():
            for person in pantheonises:
                Pantheonises.add_new_person(person)


class TestUser(Base):
    """ Unit tests for Users """

    # Test d'inscription d'un·e utilisateur·rice
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

    # Test de connexion d'un·e utilisateur·rice
    def test_login(self):
        with self.app.app_context():
            statut = User.inscription(
                "helloworld", "helloworld1", "hello.world@chartes.psl.eu"
            )

            user_connected = User.connexion("helloworld", "helloworld1")

        self.assertTrue(user_connected)


class TestPantheonises(Base):
    """ Unit tests for Pantheonises """

    # Test de l'ajout des Panthéonisés-tests
    # dans la base de données
    def test_pantheonise_is_added(self):
        with self.app.app_context():
            self.insert_pantheonises(self.pantheonises)

            person = Pantheonises.query.filter(Pantheonises.id == 1).first()

        self.assertEqual(person.name, "Marat")
        self.assertEqual(person.birth, 1743)

    # Test d'une réponse HTTP pour un·e panthéonisé·e
    # enregistrée dans la base de données
    def test_response_for_pantheonise(self):
        with self.app.app_context():
            self.insert_pantheonises(self.pantheonises)

        r = self.client.get("/person/1")

        self.assertEqual(r.status_code, 200)

    # Test si le nombre de panthéonisé·e·s diminue
    # une fois qu'un·e panthéonisé·e ait été supprimé·e
    # de la base de données
    def test_count_decreasing_when_pers_deleted(self):
        with self.app.app_context():
            self.insert_pantheonises(self.pantheonises)

            Pantheonises.delete_person(1)
            count = Pantheonises.query.filter(Pantheonises.id).count()

        self.assertEqual(count, 1)

    # Test de l'id de la première personne panthéonisée enregistrée
    # une fois que le·la panthéonisé·e ayant l'id 1 ait été supprimé·e
    def test_left_pers_when_pers_deleted(self):
        with self.app.app_context():
            self.insert_pantheonises(self.pantheonises)

            Pantheonises.delete_person(1)
            left_person = Pantheonises.query.filter(Pantheonises.id).first()

        self.assertEqual(left_person.id, 2)

    # Test d'une mise à jour des informations d'un·e panthéonisé·e
    # dans la base de données
    def test_update_infos_pantheonises(self):
        with self.app.app_context():
            self.insert_pantheonises(self.pantheonises)
            new_infos = {
                "birth_date": "1750",  # Élément modifié, initialement : 1749
                "death_date": "1791",
                "pantheonisation": "1792",
                "status": "Homme politique",  # Élement modifié, initialement : "diplomate, journaliste et homme politique français"
                "wikipedia": "https://fr.wikipedia.org/wiki/Honor%C3%A9-Gabriel_Riqueti_de_Mirabeau",
                "sex": "homme",
            }

            Pantheonises.add_required_info(2, new_infos)
            p = Pantheonises.query.filter(Pantheonises.id == 2).first()

        self.assertEqual(p.id, 2)
        self.assertEqual(p.pantheonisation, 1792)
        self.assertEqual(p.status, "Homme politique")
        self.assertNotEqual(p.birth, 1749)
