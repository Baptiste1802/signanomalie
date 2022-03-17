from ..app import app, glpi
from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField, SubmitField
from wtforms import StringField, SelectField, PasswordField, BooleanField, TextAreaField, EmailField, RadioField
from wtforms.validators import DataRequired, InputRequired, Length, Email, URL, ValidationError

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
            InputRequired(message="Veuillez selectionner un bâtiment")
        ])

    salle = SelectFieldNoValidation('Salle', choices=[],
        validators=[
            InputRequired(message="Veuillez selectionner une salle")
        ])

    materiel = SelectFieldNoValidation('Matériel', choices=[])

    probleme = StringField('Résumez le problème', render_kw={"placeholder" : "-"},
        validators=[InputRequired(message="Veuillez indiquer le problème")
        ])

    priorite = SelectField('Priorité', choices=[(id, name) for id, name in glpi.priorite.items()],
        validators=[InputRequired(message="Veuiller selectionner la priorité")
        ])

    desc = TextAreaField('Décrivez le problème succinctement', render_kw={"placeholder" : "-"})

    envoyer = SubmitField("Envoyer")
    
    reset = SubmitField("Reset")