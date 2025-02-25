from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from app.models.auth_users import User

bcrypt = Bcrypt()

class AuthController:
    @staticmethod
    def signup(name, email, password):
        existing_user = User.get_user_by_email(email)
        if existing_user:
            return {'message': 'User already exists'}, 400
        
        success = User.create_admin(name, email, password)
        if success:
            return {'message': 'Admin user created successfully'}, 201
        return {'message': 'Error creating user'}, 500

    @staticmethod
    def signin(email, password):
        user = User.get_user_by_email(email)
        if user and bcrypt.check_password_hash(user[3], password):  # Assuming user[3] is password_hash
            if not user[4]:  # Assuming user[4] is is_admin field
                return {'message': 'You are not authorized'}, 403
            
            access_token = create_access_token(identity=str(user[0]))  # user[0] is user_id
            return {'access_token': access_token}, 200
        return {'message': 'Invalid credentials'}, 401
