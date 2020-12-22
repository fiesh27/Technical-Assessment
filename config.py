import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/divvy'
    SQLALCHEMY_TRACK_MODIFICATIONS = False