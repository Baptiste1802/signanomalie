from flask import render_template
from .models.forms import SignalForm, QrCodeForm
from .app import app, glpi
from flask import request

@app.route("/")
def home():
    form=SignalForm()
    choicesbat = form.batiment.choices = ["grrrr"]
    choicesSalleInfo = form.salle.choices = ["I01","I02","I03","I04","I05","I06","I07"]
    choicesMateriel = form.materiel.choices = ["Clavier","Souris","Ecran","Unité centrale","Vidéo Projecteur"]
    choicesProbleme = form.probleme.choices = ["Pertes des droits","Connexion à ma session impossible"]
    choicesPriorite = form.priorite.choices = ["Maximale","Urgente","Moyenne","Peu attendre","Minimale"]

    return render_template(
        "home.html",
        title = "SignAnomalie",
        form=form,
        prefillBat = request.args.get('batiment'),
        prefillSalle = request.args.get('salle'),
        prefillMateriel = request.args.get('materiel'),
        choicesbat=choicesbat,
        choicesSalleInfo=choicesSalleInfo,
        choicesMateriel=choicesMateriel,
        choicesProbleme=choicesProbleme,
        choicesPriorite=choicesPriorite
        # locations = glpi.get_locations()
    
    )


@app.route("/qrcode/")
def qrcode():
    form=QrCodeForm()
    choicesbat = form.batiment.choices = ["grrrr"]
    choicesSalleInfo = form.salle.choices = ["I01","I02","I03","I04","I05","I06","I07"]
    choicesMateriel = form.materiel.choices = ["Clavier","Souris","Ecran","Unité centrale","Vidéo Projecteur"]

    if form.validate_on_submit():
        user=form.generateQRCode()

    return render_template(
        "qrcode.html",
        title = "SignAnomalie",
        form=form,
        choicesbat=choicesbat,
        choicesSalleInfo=choicesSalleInfo,
        choicesMateriel=choicesMateriel,
        # locations = glpi.get_locations()
    
    )

app.config['SECRET_KEY'] = "f2ef2834-7d1c-47a4-b35c-f48547b6c6dc"
