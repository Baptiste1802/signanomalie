from ..app import app, glpi
from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField, SubmitField
from wtforms import StringField, SelectField, PasswordField, BooleanField, TextAreaField, EmailField, RadioField, FileField
from wtforms.validators import DataRequired, InputRequired, Length, Email, URL, ValidationError

class SignalForm(FlaskForm):
    mail = StringField('Renseignez votre adresse mail', validators=[DataRequired(),Email()], render_kw={"placeholder" : "-"})
    mailDeSuivi = BooleanField('Recevoir des mails de suivi')
    batiment = SelectField('Bâtiment', choices= [(id, name) for id, name in glpi.batiments.items()])
    salle = SelectField('Salle',choices=[])
    materiel = SelectField('Matériel',choices=[])
    probleme = StringField('Résumez le problème', render_kw={"placeholder" : "-"})
    priorite = SelectField('Priorité',choices=[(id, name) for id, name in glpi.priorite.items()])
    desc = TextAreaField('Décrivez le problème succinctement', render_kw={"placeholder" : "-"})
    envoyer = SubmitField("Envoyer")
    reset = SubmitField("Reset")