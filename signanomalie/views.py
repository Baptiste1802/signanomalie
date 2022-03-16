from flask import render_template, jsonify
from .models.forms import SignalForm
from .app import app, glpi

@app.route("/")
def home():
    form=SignalForm()

    return render_template(
        "home.html",
        title = "SignAnomalie",
        form=form,
    )