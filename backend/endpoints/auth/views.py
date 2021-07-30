from flask import Blueprint, jsonify, request
from flask.json import dump, dumps
from flask_restx import Api, Resource
from flask_praetorian.exceptions import AuthenticationError

from extensions import security

auth_blueprint = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)
auth_api = Api(auth_blueprint)


@auth_api.errorhandler(AuthenticationError)
def handle_error(e):
    return {"message": str(e)}


@auth_api.route("/login")
class AuthResource(Resource):
    @auth_api.doc("Login")
    @auth_api.response(200, 'Success')
    @auth_api.response(500, 'AuthenticationError')
    def post(self):
        data = request.get_json(force=True)

        username = data.get("username", None)
        password = data.get("password", None)

        user = security.authenticate(
            username,
            password
        )

        token = {
            "access_token": security.encode_jwt_token(
                user,
                first_name=user.profile.first_name,
                surname=user.profile.surname,
                member_since=user.created.strftime("%d-%m-%Y %X"),
                roles=[user_role.name for user_role in user.roles.all()]
            )
        }

        return jsonify(token, 200)