
## Présentation

## Installation de l'application 

1. Installer pantheonisees à partir de la branche master du dépôt pantheonisees Github :
`$ git clone  `

2. Installer Python via le [site](https://www.python.org/downloads/). Pour rappel : la plupart des systèmes Linux, intègre déjà Python.

3. Créer un environnement virtuel à l'aide de VirtualEnv. Dans votre terminal, taper la commande : `$ pip install virtualenv` pour installer VirtualEnv puis `$ virtualenv -p python3 env` ou sous windows : `$ virtualenv -p` puis `$ env:python3 env`

4. Activer l'environnement virtuel via `$ source env/bin/activate`. Pour quitter l'environnement taper simplement `$ deactivate`.

5. Dans le terminal, se placer au niveau du fichier `requirements.txt`, puis installer les différents packages nécéssaires avec la commande suivante : `$ pip install -r requirements.txt`.

6. Dans le terminal, rentrer la commande `$ cd /`, Une fois dans le dossier lancer l'application avec la commande `$ python run.py` ou `$ python3 run.py` via le serveur local et selon votre version de python (`$ python --version ou -V`).

