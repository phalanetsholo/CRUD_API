class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Ntsako@2000@localhost:5432/users'
    DEBUG = True


