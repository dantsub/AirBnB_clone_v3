#!/usr/bin/python3
""" index of the api """
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    """ Return status ok """
    return jsonify({"status": "OK"})
