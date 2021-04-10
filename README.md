# Projet 13 devops

- Description générale du système ou du projet

Corrections de bugs, Refonte modulaire du projet, écriture de tests avec pytest,
pipepline CI/CD avec deploiement sur Heroku et ajout de sentry au projet.

- Statut du projet

Le projet est terminé

- Installation

2. créer le virtual env : python -m venv venv (à la racine du projet)
3. switcher sur le virtual env : source venv/bin/activate pour linux ou venv\Scripts\activate pour windows(à la racine du projet)
4. récupérer les modules du fichier requirements.txt sur votre venv : pip install -r requirements.txt(à la racine du projet)

- Démarrage

1. lancer le serveur :python manage.py runserver (à la racine du projet)
. Rendez-vous dans votre navigateur web à l'url indiquée par la ligne de commande, http://127.0.0.1:8000/

- Comment lancer les tests

Taper : pytest -vvv à la racine du projet

- Linting

. Taper : flake8 à la racine du projet
. On peut changer la config de flake8 dans le fichier setup.cfg

- Déploiement

Configuration requise : CirclCI , Heroku
1. Installer les CLI d'heroku.
2. Aller sur Heroku: https://dashboard.heroku.com/apps et créer une app.
3. Lier votre repo github du projet à CircleCI sur leur site web à cette adresse:https://app.circleci.com
4. Selectionner le projet et demarrer un build deja existant grace au fichier config.yml dans le dossier .circleci
5. Une fois fait aller dans l'onglet  organisation settings de votre projet dans circle ci 
 et crée un context appelé: projet13
Passer les Variables d'environnemnt au context projet13 :
1. HEROKU_TOKEN(pour obtenir le token: heroku authorizations:create dans votre terminal)
2. DEBUG: False
3. SECRET_KEY: de votre projet django(vous pouvez en générer,
 regarder sur le net si besoin comment générer un secret key django)
. Il reste plus qu'à commit sur la branche master de votre projet pour lancer  les tests et le deploiement via circleci.
. Pour voir le deploiement rendez sur votre app heroku dans settings pour récuperer l'adresse web.

- Docker

Un conteneur est crée  automatiquement pour le deploiement grace au fichier Dockerfile.
1. Vous pouvez crée une image grace à la commande :docker build -t ImageName
2. Pour run l'image: docker run -d -p 8000:8000 ImageName
3. Rendez vous en local à l' adresse: 127.0.0.1:8000

- Sentry

Sentry à été ajouter au projet pour la correction de bug
1. Aller sur le site web sentry: https://sentry.io/ créer une app avec django et récuperait votre dsn
2. Passer votre dsn à l' application local:set DSN= votre dsn 
Si vous voulez passer sentry au projet déployé:
1. Passer la varibale d'environnement DSN à circleCI ou  setter directement à heroku la variable d'env:
heroku config:set DSN=votre dsn 


Fabriqué avec:

Pycharm

Auteurs :

Florent Peyre alias Alucard