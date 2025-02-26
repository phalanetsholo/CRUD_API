from app.models.employee_model import Employee
from flask import jsonify, request

def signup_controller():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    if Employee.signup(name, email, password):
        return jsonify({'message': 'User registered successfully'}), 201

    return jsonify({'message': 'Email already registered'}), 400

def signin_controller():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Missing required fields'}), 400

    response = Employee.signin(email, password)
    if response:
        return jsonify(response), 200

    return jsonify({'message': 'Invalid credentials'}), 401

def get_users_controller():
    users = Employee.get_users()
    return jsonify(users), 200
