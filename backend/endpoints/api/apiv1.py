from sys import path
from flask import Blueprint
from flask_restx import Api

from endpoints.auth.views import auth_namespace
from endpoints.roles.views import role_namespace
from endpoints.users.views import user_namespace

api_v1_blueprint = Blueprint("api", __name__, url_prefix='/api/v1')
apiv1 = Api(api_v1_blueprint, version="1.0", title="APIv1", description="API V1 Blueprints")


try:
    apiv1.add_namespace(auth_namespace)
    apiv1.add_namespace(role_namespace)
    apiv1.add_namespace(user_namespace)
except:
    print("Error occured when adding namespaces")
else:
    print("Successfully added namespaces")
