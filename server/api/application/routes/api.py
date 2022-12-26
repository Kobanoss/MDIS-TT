from flask import Blueprint, abort, jsonify, make_response, request

from application.routes.__imports__ import *

api = Blueprint('api', __name__)


@App.errorhandler(404)
def not_found(*args, **kwargs):
    return make_response(jsonify({'error': 'Not found'}), 404)


@api.route("/api/v1.0/user-contacts/<int:contact_id>", methods=['GET'])
async def get_contact(contact_id):
    # TODO: Add GET-REST later
    return abort(404)


@api.route("/api/v1.0/user-contacts<int:contact_id>", methods=['PUT'])
async def change_contact(contact_id):
    # TODO: Add PUT-REST later
    return abort(404)


@api.route("/api/v1.0/user-contacts", methods=['GET'])
def get_last_contact():
    contact = UserContacts.query.order_by(UserContacts.id.desc()).first()
    return make_response(contact.jsonsify(), 200)


@api.route("/api/v1.0/user-contacts", methods=['POST'])
def add_contact():
    req = request.get_json()
    if not req:
        abort(400)
    Db.session.add(UserContacts(full_name=req['full_name'],
                                birth_date=req['birth_date'],
                                address=req['address'],
                                phone=req['phone']))
    Db.session.commit()
    return make_response(jsonify({'status': 'created'}), 201)
