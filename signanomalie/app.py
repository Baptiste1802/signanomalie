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

print(os.environ.get("URL"), os.environ.get("APP_TOKEN"), os.environ.get("API_TOKEN") )

try:
    glpi = None
except GLPIError as err:
    print("Error", str(err))