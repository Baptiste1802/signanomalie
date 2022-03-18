# Signanomalie
## Le système de signalement d'anomalies 

Sign'anomalie est un système de signalement d'anomalies permettant d'effectuer efficacement un signalement
au Gestionnaire Libre de Parc Informatique (GLPI) en ayant la possibilité d'utiliser un QR Code pour préremplir le questionnaire

## Fonctionnalitées

- Formulaire efficace et communiquant directement avec la base de données GLPI
- Remplissage automatique des champs en fonction des paramètres passés dans l'URL
- Formulaire produisant un QRCode permettant de pré-remplir des champs du formulaire principal
- Génération d'un PDF à imprimer avec le QRCode et les informations requises

## Technologies

Sign'anomalie utilise plusieurs technologies :

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Framework de développement web en Python
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/) - Extension dépendante de Flask afin de créer des formulaires
- [GLPI](https://glpi-project.org/fr/) - Logiciel open-source permettant la gestion de parc informatique

Sign'anomalie est aussi un logiciel open-source possédant son dépôt Git ici : [Sign'anomalie](https://gitlab.com/blambert1802/signalement_anomalie_2a12).

## Installation sur Linux

Sign'anomalie nécessite [Python3](https://www.python.org/downloads/) ainsi que [pip](https://pypi.org/project/pip/) pour fonctionner.

**Autorisation GLPI**

Il faut aussi posséder un jeton d'API ainsi qu'un jeton d'Application de son instance de GLPI.

**Cloner le dépôt**

```sh
git clone https://gitlab.com/blambert1802/signalement_anomalie_2a12.git
cd signalement_anomalie_2a12
```

**Créer le fichier .flaskenv**

Le fichier .flaskenv contient des variables d'environnement qui seront chargées à chaque lancement de l'application

Il se place à la racine du projet : /signalement_anomalie_2a12/.flaskenv

```sh
nano .flaskenv
```

```txt
FLASK_APP=signanomalie
FLASK_ENV=development
FLASK_DEBUG=0
APP_TOKEN=peyK4XPibwSJ8LK0NfN1bHm5C1yUskCubfMXh77l
API_TOKEN=lLEfZ7w8jjjsVwunTg0Ctx1ZojicD4wnKBVrEAl8
URL=https://glpi.iut45.univ-orleans.fr/glpi-sidev/apirest.php
URL_APP=http://localhost:5000/
```

Un peu d'explications : 

- FLASK_APP - contient le nom du dossier dans lequel est située l'application
- FLASK_ENV - indique que le serveur est un serveur de développement
- FLASK_DEBUG - 0 ou 1 : désactive ou active le débogage dans le terminal
- APP_TOKEN - le token d'application lié à l'instance de GLPI
- API_TOKEN - le token d'api lié à votre compte sur l'instance de GLPI
- URL - l'url vers l'api de votre instance de GLPI
- URL_APP - l'url vers la racine de votre site internet

**Créer l'environnement virtuel et lancer l'application**

```sh
./build.sh
y
source/venv/bin/activate
flask run
```

Le script build.sh créer un environnement virtualenv et installe les dépendances requises spécifiées dans requirements.txt dans votre nouvel environnement

Pour installer virtualenv :

```sh
pip3 install virtualenv
```
