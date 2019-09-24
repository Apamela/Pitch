import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY ='ff73536b7f0e63d45fe4f61ecf8eb703'
    SECRET_KEY ='a rondom string'
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
