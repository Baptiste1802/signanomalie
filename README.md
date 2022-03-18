# Signanomalie
## Le système de signalement d'anomalies 

Signanomalie est un système de signalement d'anomalies permettant d'effectuer efficacement un signalement
au Gestionnaire Libre de Parc Informatique (GLPI) en ayant la possibilité d'utiliser un QR Code pour préremplir le questionnaire

## Fonctionnalitées

- Formulaire efficace et communiquant directement avec la base de données GLPI
- Remplissage automatique des champs en fonction des paramètres passés dans l'URL
- Formulaire produisant un QRCode permettant de pré-remplir des champs du formulaire principal
- Génération d'un PDF à imprimer avec le QRCode et les informations requises

## Technologies

Signanomalie utilise plusieurs technologies :

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Framework de développement web en Python
- [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/) - Extension dépendante de Flask afin de créer des formulaires
- [GLPI](https://glpi-project.org/fr/) - Logiciel open-source permettant la gestion de parc informatique

Signanomalie est aussi un logiciel open-source possédant son dépôt Git ici : [Signanomalie](https://gitlab.com/blambert1802/signalement_anomalie_2a12).

## Installation

Signanomalie nécessite [Python3](https://www.python.org/downloads/) ainsi que [pip](https://pypi.org/project/pip/) pour fonctionner.

**Installation sur Linux**

```sh
cd signanomalie
./build.sh
y
flask run
```

## Utilisation

