from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from .config import DevelopmentConfig
from App.routes.user_routes import user_bp 


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    
    app.register_blueprint(user_bp, url_prefix='/users')
    

    return app


    







