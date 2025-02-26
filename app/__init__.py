from flask import Flask
from app.routes.auth_routes import auth_bp
from app.routes.employee_routes import employee_bp  # type: ignore

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(employee_bp, url_prefix='/employees')

    return app
