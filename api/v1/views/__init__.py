""" views """
# Import packages
from flask import Blueprint
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review

# Blueprint app_views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


# Requests methods
def get(data):
    """ Return json for HTTP GET request """
    # return the objs' dict which have a foreign key
    if data['f_id']:
        f_obj = storage.get(data['r_class'], data['f_id'])
        if f_obj is None:
            abort(404)
        return jsonify([f.to_dict() for f in getattr(f_obj, data['table'])])
    # return obj's dict if parameter id was passed
    if data['id']:
        obj = storage.get(data['class'], data['id'])
        if obj is None:
            abort(404)
        return jsonify(obj.to_dict()), 200
    # return dict of all objects type data['class']
    objs = [o.to_dict() for o in storage.all(data['class']).values()]
    return jsonify(objs), 200


def delete(data):
    """Deletes an object"""
    obj = storage.get(data['class'], data['id'])
    if obj:
        storage.delete(obj)
        storage.save()
        return jsonify({}), 200
    abort(404)


def post(data):
    """ Return dict for POST request """
    req = request.get_json()
    if req is None:
        return jsonify({'error': 'Not a JSON'}), 400
    for attr in data['exists']:
        if attr not in req:
            return jsonify({'error': 'Missing {}'.format(attr)}), 400
    # if obj has relation with other
    if data['f_id']:
        # ==== Next block code is necesary for place obj ====
        if 'user_id' in data['exists']:
            if not storage.get('User', req['user_id']):
                abort(404)
        # ===================================================
        f_obj = storage.get(data['r_class'], data['f_id'])
        if f_obj:
            # add relationship field and it's value
            req[data['r_field']] = data['f_id']
        else:
            abort(404)
    new_obj = eval(data['class'])(**req)
    new_obj.save()
    return jsonify(new_obj.to_dict()), 201


def put(data):
    """ Return dict for PUT request """
    ignore = ['id', 'user_id', 'city_id', 'place_id',
              'email', 'created_at', 'updated_at']
    req = request.get_json()
    if req is None:
        return jsonify({'error': 'Not a JSON'}), 400
    obj = storage.get(data['class'], data['id'])
    if obj is None:
        abort(404)
    for key, val in req.items():
        if key not in ignore:
            setattr(obj, key, val)
    storage.save()
    return jsonify(obj.to_dict()), 200

# import for views
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
