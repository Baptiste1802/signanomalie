from flask import render_template, jsonify
from .models.forms import SignalForm
from .app import app, glpi

@app.route("/api/get/locations/<int:id>",  methods=['GET', 'POST'])
def api_get_locations(id):
    '''return sub locations of a location'''
    return jsonify(glpi.get_sub_locations(id))

@app.route("/api/get/computers/<int:id>", methods=["GET", "POST"])
def api_get_computers(id):
    '''return sub items of a location'''
    return jsonify(glpi.get_computers_per_location(id))
