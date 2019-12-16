import os
import pathlib


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'youWontGuess'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + str(pathlib.Path('app.db').resolve())

    SQLALCHEMY_TRACK_MODIFICATION = False
