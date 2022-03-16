from flask import render_template, jsonify
from .models.forms import QrCodeForm, SignalForm
from .app import app, glpi
from flask import request

@app.route("/", methods =("GET","POST"))
def home():
    form=SignalForm()

    return render_template(
        "home.html",
        title = "SignAnomalie",
        form=form,
    )


@app.route("/qrcode", methods =("GET","POST"))
def home():
    form=QrCodeForm()

    return render_template(
        "qrcode.html",
        title = "SignAnomalie",
        form=form,
    )
