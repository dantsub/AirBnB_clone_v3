#!/usr/bin/python3
""" module cities view """
from api.v1.views import app_views, get, delete, post, put
from flask import jsonify, request, abort
from models import storage


@app_views.route('/cities/<city_id>', strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
@app_views.route('/states/<state_id>/cities', strict_slashes=False,
                 methods=['GET', 'POST'])
def crud_cities(state_id=None, city_id=None):
    """ Crud for cities
    Return request mothods
    """
    data = {
        'id': city_id,  # id for state
        'class': 'City',  # Name class
        'f_id': state_id,  # foreign key value
        'table': 'cities',  # table name for GET request
        'exists': ['name'],  # attr that must exist
        'r_class': 'State',  # class with which it's related
        'r_field': 'state_id',  # relation field
    }
    # All methods
    req_methods = {
        'GET': get,
        'DELETE': delete,
        'POST': post,
        'PUT': put
    }
    return req_methods[request.method](data)
