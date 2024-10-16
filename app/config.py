import os


class ConfigClass:
    SECRET_KEY = os.environ.get('SECRET_KEY')