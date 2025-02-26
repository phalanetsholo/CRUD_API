from flask_bcrypt import Bcrypt #type: ignore
from flask_jwt_extended import create_access_token #type: ignore
from models.db_models import get_db_connection  # Importing the db connection function
from flask import jsonify

bcrypt = Bcrypt()

class User:
    def __init__(self, name, email, password=None):
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def signup(name, email, password):
        conn = get_db_connection()
        cursor = conn.cursor()

       
        cursor.execute("SELECT * FROM auth WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            cursor.close()
            conn.close()
            return False

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

      
        cursor.execute("INSERT INTO auth (name, email, password_hash) VALUES (%s, %s, %s)",
                       (name, email, password_hash))
        conn.commit()

        cursor.close()
        conn.close()

        return True

    @staticmethod
    def signin(email, password):
        conn = get_db_connection()
        cursor = conn.cursor()

        
        cursor.execute("SELECT * FROM auth WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user:
           
            if 'password_hash' in [desc[0] for desc in cursor.description]:
                stored_password_hash = user[2]  
                if bcrypt.check_password_hash(stored_password_hash, password):
                    
                    access_token = create_access_token(identity=user[0]) 
                    cursor.close()
                    conn.close()
                    return jsonify({'access_token': access_token}), 200

        cursor.close()
        conn.close()
        return jsonify({'message': 'Invalid credentials'}), 401
