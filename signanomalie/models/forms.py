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

    batiment = SelectFieldNoValidation('Bâtiment', choices=[(id, name) for id, name in glpi.get_batiments().items()],
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

class QrCodeForm(FlaskForm):
    batiment = SelectFieldNoValidation('Bâtiment', choices=[(id, name) for id, name in glpi.get_batiments().items()],
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
    envoyer = SubmitField('Envoyer')

    def generateQRCode(self):
        link = os.environ.get("URL") + "?"
        batiment_selectionne = self.batiment.data
        salle_selectionnee = self.salle.data
        materiel_selectionne = self.materiel.data
        type_materiel_selectionne = self.type_materiel.data
        print(type_materiel_selectionne)
        name_batiment = dict(self.batiment.choices).get(int(batiment_selectionne))
        name_salle = dict([(id, name) for id, name in glpi.locations.items()]).get(int(salle_selectionnee))
        if (batiment_selectionne != ""):
            link += "batiment="+batiment_selectionne+"&"
        if (salle_selectionnee != ""):
            link += "salle=" + salle_selectionnee+"&"
        if (type_materiel_selectionne != "" and materiel_selectionne != ""):
            link += "type="+type_materiel_selectionne+"&"
            link += "materiel=" + materiel_selectionne
        
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
        img.save("signanomalie/static/newqr.png")
        return generationPDF(name_batiment, name_salle, materiel_selectionne, "signanomalie/static/newqr.png")

