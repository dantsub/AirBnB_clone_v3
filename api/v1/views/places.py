#!/usr/bin/python3
""" module places view """
from api.v1.views import app_views, get, delete, post, put
from flask import jsonify, request, abort
from models import storage


@app_views.route('/places/<place_id>', strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
@app_views.route('/cities/<city_id>/places', strict_slashes=False,
                 methods=['GET', 'POST'])
def crud_places(city_id=None, place_id=None):
    """ Crud for places
    Return request mothods
    """
    data = {
        'id': place_id,  # id for place
        'class': 'Place',  # Name class
        'f_id': city_id,  # foreign key value
        'table': 'places',  # table name for GET request
        'exists': ['name'],  # attr that must exist
        'r_class': 'City',  # class with which it's related
        'r_field': 'city_id',  # relation field
    }
    # All methods
    req_methods = {
        'GET': get,
        'DELETE': delete,
        'POST': post,
        'PUT': put
    }
    return req_methods[request.method](data)
