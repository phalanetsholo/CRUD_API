import os

class Config:
    SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or '1017'
    DB_HOST = "localhost"
    DB_NAME = "testapi"
    DB_USER = "postgres"
    DB_PASSWORD = "1017"
