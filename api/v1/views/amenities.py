#!/usr/bin/python3
""" module amenities view """
from api.v1.views import app_views, get, delete, post, put
from flask import jsonify, request, abort
from models import storage


@app_views.route('/amenities', strict_slashes=False, methods=['GET', 'POST'])
@app_views.route('/amenities/<amenity_id>', strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
def crud_amenities(amenity_id=None):
    """ Crud for amenities
    Return request mothods
    """
    data = {
        'id': amenity_id,  # id for amenity
        'class': 'Amenity',  # Name class
        'f_id': None,  # foreign key value
        'exists': ['name'],  # attr that must exist
    }
    # All methods
    req_methods = {
        'GET': get,
        'DELETE': delete,
        'POST': post,
        'PUT': put
    }
    return req_methods[request.method](data)
