#!/usr/bin/python3
""" module reviews view """
from api.v1.views import app_views, get, delete, post, put
from flask import jsonify, request, abort
from models import storage


@app_views.route('/reviews/<review_id>', strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
@app_views.route('/places/<place_id>/reviews', strict_slashes=False,
                 methods=['GET', 'POST'])
def crud_reviews(place_id=None, review_id=None):
    """ Crud for reviews
    Return request mothods
    """
    data = {
        'id': review_id,  # id for review
        'class': 'Review',  # Name class
        'f_id': place_id,  # foreign key value
        'table': 'reviews',  # table name for GET request
        'exists': ['user_id', 'text'],  # attr that must exist
        'r_class': 'Place',  # class with which it's related
        'r_field': 'place_id',  # relation field
    }
    # All methods
    req_methods = {
        'GET': get,
        'DELETE': delete,
        'POST': post,
        'PUT': put
    }
    return req_methods[request.method](data)
