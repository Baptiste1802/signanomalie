from flask import url_for
from ..app import app
from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField, SubmitField
from wtforms import StringField, SelectField, PasswordField, BooleanField, TextAreaField, EmailField, RadioField, FileField
from wtforms.validators import DataRequired, InputRequired, Length, Email, URL, ValidationError
import qrcode
import os

class SignalForm(FlaskForm):
    mail = EmailField('Renseignez votre adresse mail',[DataRequired(),Email()])
    mailDeSuivi = BooleanField('Recevoir des mails de suivi')
    batiment = SelectField('Bâtiment',choices=[])
    salle = SelectField('Salle',choices=[])
    materiel = SelectField('Matériel',choices=[])
    probleme = StringField('Résumez le problème')
    priorite = SelectField('Priorité',choices=[])
    desc = TextAreaField('Décrivez le problème succinctement')
    envoyer = SubmitField("Envoyer")
    reset = SubmitField("Reset")


class QrCodeForm(FlaskForm):
    batiment=SelectField('Bâtiment', choices=[])
    salle = SelectField('Salle', choices=[])
    materiel = SelectField('Matériel', choices=[])
    envoyer = SubmitField('Envoyer')
    reset = SubmitField("Reset")

    def generateQRCode(this):
        link = os.environ.get("URL") + "/?"
        if (this.batiment.data != None):
            link += this.batiment.data
        if (this.salle.data != None):
            link += this.salle.data
        if (this.materiel.data != None):
            link += this.materiel.data
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("signanomalie/qrcode/newqr.png")
