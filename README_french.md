## Le projet
### À propos
Cette application web a été développée par [Axelle Lecroq](https://github.com/axellelecroq) dans le cadre du Master TNAH de l'[École nationale des chartes](http://www.chartes.psl.eu/fr/cursus/master-technologies-numeriques-appliquees-histoire).

Les données exploitées sur le site sont issues d'un set de données publique et accessible sur
[data.gouv](https://www.data.gouv.fr/fr/datasets/pantheonises/). Malgré tout, les dernières personnes inhumées au Panthéon ont été ajoutées par mes soins, ainsi que les liens vers les pages wikipédia et quelques photographies.
Ce site a été dévéloppé avec Flask, framework open-source de développement web en Python. Néanmoins les languages CSS et HTML ont été largement utilisés pour le front-end du site ainsi que JavaScript pour les visualisations de données avec notamment la librairie Plotly. De nombreux éléments proviennent également de la collection d'outils Bootstrap. La base de données a été constituée à partir de SQLite et est gérée, au sein de la programmation, grâce à l'ORM SQLAlchemy.

En cas de problème avec l'utilisation de la base ou pour toute information supplémentaire, n’hésitez pas à me contacter.

### La structure
```
pantheonisees
    ├── app
    │   ├── modeles
    │   │       ├── data.py
    │   │       └── user.py
    │   ├── routes
    │   │       ├── crud_person.py
    │   │       ├── errors.py
    │   │       ├── generic.py
    │   │       ├── search.py
    │   │       └── user.py
    │   ├── static
    │   │       ├── css/...
    │   │       ├── images/...
    │   │       └── js
    │   │           ├── graph_pantheonisation_date.js
    │   │           ├── graph_per_status.js
    │   │           ├── select_gender.js
    │   │           └── select_status.js
    │   ├── templates
    │   │       ├── errors/...
    │   │       ├── layout/default.html
    │   │       ├── pages
    │   │       │      ├── about.html
    │   │       │      ├── connexion.html
    │   │       │      ├── dataviz.html
    │   │       │      ├── home.html
    │   │       │      ├── login.html
    │   │       │      ├── person_create.html
    │   │       │      ├── person_update.html
    │   │       │      ├── person.html
    │   │       │      ├── search.html
    │   │       │      └── toutes.html
    │   │       ├── partials
    │   │       │       ├── css.html
    │   │       │       └── metadata.html
    │   │       └── conteneur.html
    │   ├── constantes.py
    │   └── app.py
    ├── db_pantheonises.db
    ├── db_test.db
    ├── run.py
    └── tests.py
```

### Les fonctionnalités
Accessibles à tou·te·s :
- effectuer une recherche dans la base de données des personnes panthéonisées
- découvrir les visualisations de données

Disponibles seulement pour les personnes ayant crée un compte :
- ajouter et supprimer un·e Panthéonisé·e
- modifier les informations actuelles enregistrées d'un·e Panthéonisé·e
- ajouter des photographies à un·e Panthéonisé·e

:film_strip: Vous pouvez visionner une vidéo de 2min présentant les fonctionnalités en cliquant sur la capture d'écran ci-dessous.

:information_source: L'enregistrement n'est pas optimal puisque le contraste est un peu fort et ne permet pas de reconnaître parfaitement les différents liens sur l'application. Aussi, les menus déroulants du formulaire de recherche n'apparaissent pas dans l'enregistrement. Néanmoins, cette vidéo permet d'avoir un bel aperçu des fonctionnalités de l'application et du front-end de celle-ci.
[![plot](./documentation/site_presentation.png)](https://user-images.githubusercontent.com/60888306/114012668-ec17c900-9866-11eb-9589-ee42c555e45d.mp4)

## Installer et lancer l'application
### Premier lancement

Pré-requis : python3  
*Vous pouvez l'installer via ce [site](https://www.python.org/downloads/). Pour rappel : la plupart des systèmes Linux intègrent déjà Python.*

1. Cloner ce dépôt git : `git clone https://github.com/axellelecroq/pantheonisees.git` et rentrer dedans
2. Installer un environnement virtuel : `virtualenv -p python3 env` 
3. Activer l'environnement virtuel via `source env/bin/activate`
4. Installer requirements.txt : rentrer dans le dossier `pantheonisees` et effectuer la commande `pip install -r requirements.txt`
5. Lancer l'application : aller au niveau du fichier `run.py` et lancer `python3 run.py`

### Lancement 
1. Aller dans le dossier de l'application
2. Activez le virtualenv : `source env/bin/activate`
3. Lancer l'application : aller au niveau du fichier `run.py` et lancer `python3 run.py`

### Les tests 
Pour lancer les tests de l'application:
1. Se situer au niveau des fichiers `README.md` et `requirements.txt`
2. Lancer cette commande : `python -m unittest discover`
