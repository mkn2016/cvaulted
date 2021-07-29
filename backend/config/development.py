from os import getenv, environ

from pathlib import Path

from dotenv import load_dotenv


from config.base import Config

environment_path = Path(__file__).parents[1].joinpath("secrets/dev.env")

try:
    load_dotenv(environment_path)
except (Exception, SystemExit):
    raise("Failed to load environment variables")
else:
    pass


class DevelopmentConfig(Config):
    TESTING=True
    FLASK_ENV="development"
    # SQLALCHEMY_ECHO = True
    PROPAGATE_EXCEPTIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY=environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI=environ.get("SQLALCHEMY_DATABASE_URI")
    JWT_ACCESS_LIFESPAN = {'days': 1}
    JWT_REFRESH_LIFESPAN = {'days': 1}
