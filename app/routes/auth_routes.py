from flask import Blueprint
from app.controllers.employee_controller import signup_controller, signin_controller

auth_bp = Blueprint('auth_bp', __name__)

auth_bp.route('/signup', methods=['POST'])(signup_controller)
auth_bp.route('/signin', methods=['POST'])(signin_controller)
