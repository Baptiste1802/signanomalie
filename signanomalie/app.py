from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)

import os.path

def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__), p
        )
    )

load_dotenv(dotenv_path="config")