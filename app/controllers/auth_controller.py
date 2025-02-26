from flask import request, jsonify
from models.user_model import User

def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    user = User(name=name, email=email, password=password)
    created_user = user.signup()

    if created_user:
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'message': 'User already exists'}), 400

def signin():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    user = User.signin(email, password)

    if user:
        return jsonify({'message': 'Login successful', 'user': user}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
