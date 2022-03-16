from flask import render_template
from .models.forms import SignalForm, QrCodeForm
from .app import app, glpi
from flask import request

@app.route("/", methods =("GET","POST"))
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


@app.route("/qrcode/", methods =("GET","POST"))
def qrcode():
    form=QrCodeForm()
    form.batiment.choices = [("auto","Choisissez un département"),("info","Informatique")]
    form.batiment.default = "auto"
    form.batiment(option_attr={"customselect-0": {"disabled": "auto"} })
    form.salle.choices = [("auto","Choisissez une salle"),("i01","I01"),("i02","I02"),("i03","I03"),("i04","I04"),("i05","I05"),("i06","I06"),("i07","I07")]
    form.salle(option_attr={"customselect-0": {"disabled": "auto"} })
    form.materiel.choices = [("auto","Choisissez un matériel"),("clavier","Clavier"),("souris","Souris"),("ecran","Ecran"),("unitecentrale","Unité centrale"),("videoproj","Vidéo Projecteur")]
    form.materiel(option_attr={"customselect-0": {"disabled": "auto"} })
    if form.validate_on_submit():
        form.generateQRCode()
    return render_template(
        "qrcode.html",
        title = "SignAnomalie",
        form=form
        # locations = glpi.get_locations()
    
    )

app.config['SECRET_KEY'] = "f2ef2834-7d1c-47a4-b35c-f48547b6c6dc"
