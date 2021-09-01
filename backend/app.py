from flask import Flask, config
from flask_restx import resource

from extensions import *
from endpoints.users.models import User
from endpoints.api.apiv1 import api_v1_blueprint as api


class MainApp(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(__name__)
        self.args = args
        self.kwargs = kwargs
    
    def initialize_extensions(self):
        db.init_app(self)
        ma.init_app(self)
        security.init_app(self, User)
        api_v1_config = {
            "origins": [
                "*"
            ],
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Authorization", "Content-Type"]
        }
        cors.init_app(self,
            resources={
                r"/api/v1/*": api_v1_config
            },
            supports_credentials=True
        )
        limiter.init_app(self)
    
    def initialize_configurations(self):
        if self.kwargs.get("environment") == "development":
            self.config.from_object("config.development.DevelopmentConfig")
        elif self.kwargs.get("environment") == "staging":
            self.config.from_object("config.staging.StagingConfig")
        elif self.kwargs.get("environment") == "production":
            self.config.from_object("config.production.ProductionConfig")
        else:
            self.config.from_object("config.development.DevelopmentConfig")
    
    def initalize_blueprints(self):
        try:
            self.register_blueprint(api)
        except:
            print("could not register blueprints")
        else:
            print("successfully registered blueprints")

    def setup(self):
        self.initialize_configurations()
        self.initialize_extensions()
        self.initalize_blueprints()
