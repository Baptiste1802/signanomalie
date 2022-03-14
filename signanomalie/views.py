from flask import render_template
from .models.forms import SignalForm
from .app import app, glpi

@app.route("/")
def home():
    form=SignalForm()
    choicesbat = form.batiment.choices = ["Informatique","Chimie","QLIO","GTE","GEA","GMP","Autres"]
    choicesSalleInfo = form.salle.choices = ["I01","I02","I03","I04","I05","I06","I07"]
    choicesMateriel = form.materiel.choices = ["Clavier","Souris","Ecran","Unité centrale","Vidéo Projecteur"]
    choicesProbleme = form.probleme.choices = ["Pertes des droits","Connexion à ma session impossible"]
    choicesPriorite = form.priorite.choices = ["Maximale","Urgente","Moyenne","Peu attendre","Minimale"]

    return render_template(
        "home.html",
        title = "SignAnomalie",
        form=form,
        choicesbat=choicesbat,
        choicesSalleInfo=choicesSalleInfo,
        choicesMateriel=choicesMateriel,
        choicesProbleme=choicesProbleme,
        choicesPriorite=choicesPriorite
        # locations = glpi.get_locations()
    
    )
app.config['SECRET_KEY'] = "f2ef2834-7d1c-47a4-b35c-f48547b6c6dc"
