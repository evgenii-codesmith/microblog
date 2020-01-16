import os
import pathlib
from dotenv import load_dotenv
load_dotenv('.env')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'youWontGuess'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + str(pathlib.Path('app.db').resolve())

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['email@example.com']
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'tr']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
