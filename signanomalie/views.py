from flask import render_template
from .app import app, glpi

@app.route("/")
def home():
    return render_template(
        "home.html",
        title = "SignAnomalie",
    )

app.config['SECRET_KEY'] = "f2ef2834-7d1c-47a4-b35c-f48547b6c6dc"
