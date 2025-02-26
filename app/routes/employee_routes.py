from flask import Blueprint
from app.controllers.employee_controller import get_employees_controller, add_employee_controller, update_employee_controller, delete_employee_controller

employee_bp = Blueprint('employee_bp', __name__)

# Route to get all employees
employee_bp.route('/employees', methods=['GET'])(get_employees_controller)

# Route to add a new employee
employee_bp.route('/employees', methods=['POST'])(add_employee_controller)

# Route to update an existing employee by ID
employee_bp.route('/employees/<int:employee_id>', methods=['PUT'])(update_employee_controller)

# Route to delete an employee by ID
employee_bp.route('/employees/<int:employee_id>', methods=['DELETE'])(delete_employee_controller)
