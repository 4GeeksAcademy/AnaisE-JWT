"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
@api.route('/user' , methods=['POST'])
def handle_user():
    user = User()
    user.email = request.json.get("email")
    user.password = request.json.get("password")
    user.is_active = request.json.get("is_active")
    db.session.add(user)
    db.session.commit() 

    response_body = {
        "message": "Usuario creado"
    }

    return jsonify(response_body), 200
