from flask import Flask
from dotenv import load_dotenv
from .models.glpi_api import GLPIError
from .models.glpi_client import GLPI_CLIENT
import os

app = Flask(__name__)

import os.path

def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__), p
        )
    )

print(os.getenv("URL"), os.getenv("APP_TOKEN"), os.getenv("API_TOKEN") )

try:
    glpi = GLPI_CLIENT(
        url = os.getenv("URL"),
        apptoken = os.getenv("APP_TOKEN"),
        auth = os.getenv("API_TOKEN")
    )
except GLPIError as err:
    print("Error", str(err))