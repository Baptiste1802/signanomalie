from crypt import methods
from flask import render_template, jsonify, request
from .models.forms import SignalForm
from .app import app, glpi

@app.route("/", methods = ["GET", "POST"])
def home():
    form=SignalForm()

    if form.validate_on_submit():
        return "h1"

    return render_template(
        "home.html",
        title = "SignAnomalie",
        form=form,
    )