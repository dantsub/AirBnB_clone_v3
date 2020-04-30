#!/usr/bin/python3
""" module users view """
from api.v1.views import app_views, get, delete, post, put
from flask import jsonify, request, abort
from models import storage


@app_views.route('/users/<user_id>', strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])
@app_views.route('/users', strict_slashes=False,
                 methods=['GET', 'POST'])
def crud_users(user_id=None):
    """ Crud for users
    Return request mothods
    """
    data = {
        'id': user_id,  # id for user
        'class': 'User',  # Name class
        'f_id': None,  # foreign key value
        'exists': ['email', 'password'],  # attr that must exist
    }
    # All methods
    req_methods = {
        'GET': get,
        'DELETE': delete,
        'POST': post,
        'PUT': put
    }
    return req_methods[request.method](data)
