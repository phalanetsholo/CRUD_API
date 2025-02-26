import psycopg2
import os

def get_db_connection():
    """
    Establishes and returns a connection to the database.
    """
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME', 'users'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'your_password'),
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432')
    )
    return conn
