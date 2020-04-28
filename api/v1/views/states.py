#!/usr/bin/python3
""" module states view """
from api.v1.views import app_views, get, delete, post, put
from flask import jsonify, request, abort
from models import storage


@app_views.route('/states', strict_slashes=False, methods=['GET', 'POST'])
@app_views.route('/states/<state_id>', strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
def crud_states(state_id=None):
    """ Crud for states
    Return request mothods
    """
    data = {
        'class': 'State',  # Name class
        'id': state_id,  # id for state
        'f_id': None,  # foreign key
        'exists': ['name']  # attr that must exist
    }
    # All methods
    req_methods = {
        'GET': get,
        'DELETE': delete,
        'POST': post,
        'PUT': put
    }
    return req_methods[request.method](data)
