from random import choices
from tkinter.tix import Select
from ..app import app
from flask_wtf import FlaskForm
from wtforms.fields.simple import HiddenField, SubmitField
from wtforms import StringField, SelectField, PasswordField, BooleanField, TextAreaField, EmailField, RadioField, FileField
from wtforms.validators import DataRequired, InputRequired, Length, Email, URL, ValidationError

class SignalForm(FlaskForm):
    mail = EmailField('Renseignez votre adresse mail',[DataRequired(),Email()])
    mailDeSuivi = BooleanField('Recevoir des mails de suivi')
    batiment = SelectField('Bâtiment',choices=[])
    salle = SelectField('Salle',choices=[])
    materiel = SelectField('Matériel',choices=[])
    probleme = SelectField('Problème',choices=[])
    priorite = SelectField('Priorité',choices=[])
    desc = TextAreaField('Décrivez le problème succinctement')
    envoyer = SubmitField("Envoyer")
    reset = SubmitField("Reset")