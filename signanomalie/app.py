from flask import Flask
from dotenv import load_dotenv
from .models.glpi_api import GLPI, GLPIError
from .models.glpi_client import GLPI_CLIENT
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = "f2ef2834-7d1c-47a4-b35c-f48547b6c6dc"

import os.path

def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__), p
        )
    )

# Permet de vérifier si les variables d'environnement sont bien initialiées
# print(os.environ.get("URL"), os.environ.get("APP_TOKEN"), os.environ.get("API_TOKEN") )

try:
    # création de l'objet glpi qui servira de client pour communiquer avec l'instance de GLPI
    glpi = GLPI_CLIENT(os.environ.get("URL"), os.environ.get("APP_TOKEN"), os.environ.get("API_TOKEN"))
except GLPIError as err:
    print("Error", str(err))