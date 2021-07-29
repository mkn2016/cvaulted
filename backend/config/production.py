from pathlib import Path

from dotenv import load_dotenv


from config.base import Config

environment_path = Path(__file__).parents[1].joinpath("secrets/prod.env")

try:
    load_dotenv(environment_path)
except (Exception, SystemExit):
    raise("Failed to load environment variables")
else:
    pass

class ProductionConfig(Config):
    DEBUG=False
    TESTING=False
    FLASK_ENV="production"