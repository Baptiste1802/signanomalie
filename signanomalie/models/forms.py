from sqlalchemy import null
from ..app import app, glpi
from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField, SubmitField
from wtforms import StringField, SelectField, PasswordField, BooleanField, TextAreaField, EmailField, RadioField, FileField
from wtforms.validators import DataRequired, InputRequired, Length, Email, URL, ValidationError
import qrcode
import os
from markupsafe import Markup


class SignalForm(FlaskForm):
    mail = StringField('Renseignez votre adresse mail', validators=[DataRequired(),Email()], render_kw={"placeholder" : ""})
    mailDeSuivi = BooleanField('Recevoir des mails de suivi')
    batiment = SelectField('Bâtiment', choices= [(id, name) for id, name in glpi.batiments.items()])
    salle = SelectField('Salle',choices=[])
    materiel = SelectField('Matériel',choices=[])
    probleme = StringField('Résumez le problème', render_kw={"placeholder" : ""})
    priorite = SelectField('Priorité',choices=[(id, name) for id, name in glpi.priorite.items()])
    desc = TextAreaField('Décrivez le problème succinctement', render_kw={"placeholder" : ""})
    envoyer = SubmitField("Envoyer")
    reset = SubmitField("Reset")

        

        


class QrCodeForm(FlaskForm):
    batiment = SelectField('Bâtiment', choices= [(id, name) for id, name in glpi.batiments.items()])
    salle = SelectField('Salle',choices=[])
    materiel = SelectField('Matériel',choices=[])
    envoyer = SubmitField('Envoyer')
    reset = SubmitField("Reset")

    def generateQRCode(self):
        link = os.environ.get("URL") + "?"
        batiment_selectionne = self.batiment.data
        salle_selectionnee = self.salle.data
        materiel_selectionne = self.materiel.data
        if (batiment_selectionne != None):
            link += "batiment="+batiment_selectionne+"&"
        if (salle_selectionnee != None):
            link += "salle=" + salle_selectionnee+"&"
        if (materiel_selectionne != None and materiel_selectionne != "Aucun"):
            link += "materiel=" + materiel_selectionne
        print(link)
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        print(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("signanomalie/qrcode/newqr.png")

