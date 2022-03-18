from flask import render_template, jsonify
from .models.forms import SignalForm
from .app import app, glpi

"""
Toutes les routes de ce fichier renvoie un Json contenant les données demandées en fonction de l'id passé en paramètre
"""

@app.route("/api/get/locations/<int:id>",  methods=['GET', 'POST'])
def api_get_locations(id):
    '''
    id -> int : identifiant du lieu dans lequel rechercher
    retourne les sous lieux d'un lieu en utilisant le client GLPI
    '''
    return jsonify(glpi.get_sub_locations(id))

@app.route("/api/get/computers/<int:id>", methods=["GET", "POST"])
def api_get_computers(id):
    '''
    id -> int : identifiant du lieu dans lequel rechercher
    retourne les ordinateurs Computer d'un lieu en utilisant le client GLPI
    '''
    return jsonify(glpi.get_computers_per_location(id))

@app.route("/api/get/printers/<int:id>", methods=["GET", "POST"])
def api_get_printers(id):
    '''
    id -> int : identifiant du lieu dans lequel rechercher
    retourne les imprimantes Printer d'un lieu en utilisant le client GLPI
    '''
    return jsonify(glpi.get_printers_per_location(id))

@app.route("/api/get/monitors/<int:id>", methods=["GET", "POST"])
def api_get_monitors(id):
    '''
    id -> int : identifiant du lieu dans lequel rechercher
    retourne les écrans Monitor d'un lieu en utilisant le client GLPI
    '''
    return jsonify(glpi.get_monitors_per_location(id))
