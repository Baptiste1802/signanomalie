from ..app import app, glpi
from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField, SubmitField
from wtforms import StringField, SelectField, PasswordField, BooleanField, TextAreaField, EmailField, RadioField
from wtforms.validators import DataRequired, InputRequired, Length, Email, URL, ValidationError
import qrcode
import os
from .generateurPDF import generationPDF


class SelectFieldNoValidation(SelectField):
    def pre_validate(self, form):
        pass

class SignalForm(FlaskForm):
    
    mail = StringField('Renseignez votre adresse mail', 
        validators=[
            InputRequired(message="L'email est obligatoire"),
            Email(message="Email invalide", check_deliverability=True),
        ], render_kw={"placeholder" : "-"})

    mailDeSuivi = BooleanField('Recevoir des mails de suivi')

    batiment = SelectFieldNoValidation('Bâtiment', choices=[(id, name) for id, name in glpi.batiments.items()],
        validators=[
            InputRequired(message="Veuillez sélectionner un bâtiment")
        ])

    salle = SelectFieldNoValidation('Salle', choices=[],
        validators=[
            InputRequired(message="Veuillez sélectionner une salle")
        ])

    materiel = SelectFieldNoValidation('Nom du matériel', choices=[])

    type_materiel = SelectField('Type de matériel', choices=[
        ("Monitor", "Écran"),
        ("Computer", "Ordinateur"),
        ("Printer", "Imprimante")
    ])

    probleme = SelectFieldNoValidation('Problème', choices=[])

    priorite = SelectField('Priorité', choices=[(id, name) for id, name in glpi.priorite.items()],
        validators=[InputRequired(message="Veuiller selectionner la priorité")
        ])

    desc = TextAreaField('Décrivez le problème succinctement', render_kw={"placeholder" : "-"})

    envoyer = SubmitField("Envoyer")
    reset = SubmitField("Reset")


class QrCodeForm(FlaskForm):
    batiment = SelectField('Bâtiment', choices= [(id, name) for id, name in glpi.batiments.items()])
    salle = SelectField('Salle',choices=[])
    materiel = SelectField('Matériel',choices=[])
    envoyer = SubmitField('Envoyer')

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
        return generationPDF(batiment_selectionne, salle_selectionnee, materiel_selectionne, "signanomalie/qrcode/newqr.png")

