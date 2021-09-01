from flask import jsonify, request
from flask_praetorian.exceptions import (
    AuthenticationError,
    ExpiredAccessError,
    MissingRoleError
)
from flask_restx import Resource, Namespace
from flask_praetorian.decorators import auth_required, roles_accepted, roles_required

from endpoints.roles.models import Role
from endpoints.users.models import User
from endpoints.users.models import Account

statistics_namespace = Namespace("statistics", description="Statistics Operations", path="/statistics")

@statistics_namespace.errorhandler(MissingRoleError)
def handle_error(e):
    return {"message": str(e)}

@statistics_namespace.errorhandler(AuthenticationError)
def handle_error(e):
    return {"message": str(e)}

@statistics_namespace.errorhandler(ExpiredAccessError)
def handle_error(e):
    return {"message": str(e)}


class StatisticsResource(Resource):
    @statistics_namespace.doc("Get Statistics")
    @statistics_namespace.response(200, 'Success')
    @statistics_namespace.response(500, 'MissingRoleError')
    @statistics_namespace.response(500, 'AuthenticationError')
    @statistics_namespace.response(500, 'ExpiredAccessError')
    @auth_required
    @roles_accepted("superuser", "admin", "moderator", "manager")
    def get(self):
        print(User.count())
        
        return {
            "data": {
                "users_count": User.count(),
                "roles_count": Role.count(),
                "accounts_count": Account.count()
            }
        }

statistics_namespace.add_resource(StatisticsResource, "/")