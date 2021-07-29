from json import dumps

from flask import Flask
from werkzeug.exceptions import HTTPException
from flask.json import jsonify

from extensions import *
from endpoints.users.models import User
from endpoints.users.views import users_blueprint
from endpoints.roles.views import roles_blueprint
from endpoints.auth.views import auth


class MainApp(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(__name__)
        self.args = args
        self.kwargs = kwargs
    
    def initialize_extensions(self):
        db.init_app(self)
        ma.init_app(self)
        security.init_app(self, User)
    
    def initialize_configurations(self):
        if self.kwargs.get("environment") == "development":
            self.config.from_object('config.development.DevelopmentConfig')
        elif self.kwargs.get("environment") == "staging":
            self.config.from_object('config.staging.StagingConfig')
        elif self.kwargs.get("environment") == "production":
            self.config.from_object('config.production.ProductionConfig')
        else:
            self.config.from_object('config.development.DevelopmentConfig')
    
    def initalize_blueprints(self):
        self.register_blueprint(auth)
        self.register_blueprint(users_blueprint)
        self.register_blueprint(roles_blueprint)

    def setup(self):
        self.initialize_configurations()
        self.initialize_extensions()
        self.initalize_blueprints()
