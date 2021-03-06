from flask import render_template, jsonify, request, send_file
from .models.forms import SignalForm, QrCodeForm
from .app import app, glpi


@app.route("/", methods =("GET","POST"))
def home():
    """
    Route à la racine du site internet qui contient le formulaire de signalement et qui gère son traitement
    """

    form = SignalForm()
    success = False

    if form.validate_on_submit():
        notification = form.mailDeSuivi.data
        id_salle = form.salle.data
        materiel = form.materiel.data
        mail = form.mail.data
        priorite = form.priorite.data
        probleme = form.probleme.data
        desc = form.desc.data
        glpi.create_ticket(probleme, desc, mail, priorite, id_salle, materiel, notification)
        success = True
        form.desc.data = ""

    return render_template(
        "home.html",
        form=form,
        success = success
    )


@app.route("/qrcode/", methods =("GET","POST"))
def qrcode():
    """
    Route qui permet d'afficher un formulaire qui une fois complété génère un QRCode associé
    """
    form=QrCodeForm()
    afficherButton = False
    name=None

    if form.is_submitted():
        name=form.generateQRCode()
        afficherButton = True

    return render_template(
        "qrcode.html",
        form=form,
        afficherButton = afficherButton,
        path='signanomalie/static/pdf/',
        name=name
    )

@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    """
    Route qui permet de télécharger un fichier nommé <filename> contenu dans /static/pdf
    """
    file_path = 'static/pdf/' + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')