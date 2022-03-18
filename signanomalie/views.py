from crypt import methods
from flask import render_template, jsonify, send_file
from .models.forms import QrCodeForm, SignalForm
from .app import app


@app.route("/", methods =("GET","POST"))
def home():
    form=SignalForm()
    return render_template(
        "home.html",
        title = "SignAnomalie",
        form=form,
    )


@app.route("/qrcode/", methods =("GET","POST"))
def qrcode():
    form=QrCodeForm()
    afficherButton = False
    name=None

    if form.is_submitted():
        name=form.generateQRCode()
        afficherButton = True


    return render_template(
        "qrcode.html",
        title = "SignAnomalie",
        form=form,
        afficherButton = afficherButton,
        path='signanomalie/static/pdf/',
        name=name
    )

@app.route("/downloadfile/<filename>", methods = ['GET'])
def download_file(filename):
    file_path = 'static/pdf/' + filename
    return send_file(file_path, as_attachment=True, attachment_filename='')