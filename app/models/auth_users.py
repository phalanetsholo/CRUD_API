from app.models.db_models import get_db_connection
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User:
    @staticmethod
    def get_user_by_email(email):
        conn = get_db_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

    @staticmethod
    def create_admin(name, email, password):
        conn = get_db_connection()
        if not conn:
            return False
        
        cursor = conn.cursor()
        try:
            password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
            cursor.execute(
                "INSERT INTO users (name, email, password_hash, is_admin) VALUES (%s, %s, %s, %s)",
                (name, email, password_hash, True)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error creating admin: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
