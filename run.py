from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from app.routes.auth_routes import auth_bp
from app.routes.users_routes import employee_bp

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = Config.SECRET_KEY
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(employee_bp)

if __name__ == '__main__':
    app.run(debug=True)
