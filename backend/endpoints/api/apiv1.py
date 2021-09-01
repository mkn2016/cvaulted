from sys import path
from flask import Blueprint
from flask_restx import Api

from endpoints.auth.views import auth_namespace
from endpoints.roles.views import role_namespace
from endpoints.users.views import user_namespace
from endpoints.statistics.views import statistics_namespace

api_v1_blueprint = Blueprint("api", __name__, url_prefix='/api/v1')

apiv1 = Api(
    api_v1_blueprint,
    doc="/docs",
    version="1.0",
    title="APIv1",
    description="API V1 Endpoints",
    contact_url="m.k.ndirangu@gmail.com",
)


try:
    apiv1.add_namespace(auth_namespace)
    apiv1.add_namespace(role_namespace)
    apiv1.add_namespace(user_namespace)
    apiv1.add_namespace(statistics_namespace)
except:
    print("Error occured when adding namespaces")
else:
    print("Successfully added namespaces")
