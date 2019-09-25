import os

class Config:

    SECRET_KEY = 'powerfulsecretkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # SECRET_KEY ='a rondom string'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:pamela@localhost/pitch'
    UPLOADED_PHOTOS_DEST='app/static/photos'
    
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:pamela@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:pamela@localhost/pitch_test'
