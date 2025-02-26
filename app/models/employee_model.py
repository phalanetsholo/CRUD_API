from app.models.db_models import get_db_connection
from flask_bcrypt import Bcrypt # type: ignore
from flask_jwt_extended import create_access_token # type: ignore

bcrypt = Bcrypt()

class Employee:
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
            stored_password_hash = user[2]  # Assuming password_hash is at index 2
            if bcrypt.check_password_hash(stored_password_hash, password):
                access_token = create_access_token(identity=user[0])  # Assuming user ID is at index 0
                cursor.close()
                conn.close()
                return {'access_token': access_token}

        cursor.close()
        conn.close()
        return None

    @staticmethod
    def get_users():
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, email FROM auth")
        users = cursor.fetchall()

        cursor.close()
        conn.close()

        return [{'id': user[0], 'name': user[1], 'email': user[2]} for user in users]
