from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.controllers.users_controllers import EmployeeController

employee_bp = Blueprint('employees', __name__)

@employee_bp.route('/employees', methods=['GET'])
@jwt_required()
def get_employees():
    return jsonify(EmployeeController.get_all_employees())

@employee_bp.route('/employees', methods=['POST'])
@jwt_required()
def add_employee():
    data = request.get_json()
    return jsonify(EmployeeController.add_employee(data['name'], data['position'], data['salary']))

@employee_bp.route('/employees/<int:employee_id>', methods=['DELETE'])
@jwt_required()
def delete_employee(employee_id):
    return jsonify(EmployeeController.delete_employee(employee_id))
