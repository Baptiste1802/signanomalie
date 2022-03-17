from crypt import methods
from flask import render_template, jsonify, request
from .models.forms import SignalForm
from .app import app, glpi

@app.route("/", methods = ["GET", "POST"])
def home():

    form = SignalForm()

    if form.validate_on_submit():
        notification = form.mailDeSuivi.data
        print(notification)
        id_salle = form.salle.data
        materiel = form.materiel.data
        mail = form.mail.data
        priorite = form.priorite.data
        probleme = form.probleme.data
        desc = form.desc.data

        print(materiel)
    
        glpi.create_ticket(probleme, desc, mail, priorite, id_salle, materiel, notification)
        
    return render_template(
        "home.html",
        title = "SignAnomalie",
        form=form,
    )