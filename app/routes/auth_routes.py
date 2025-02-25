from flask import Blueprint, request, jsonify
from app.controllers.auth_controllers import AuthController

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    return jsonify(AuthController.signup(data['name'], data['email'], data['password']))

@auth_bp.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    return jsonify(AuthController.signin(data['email'], data['password']))
